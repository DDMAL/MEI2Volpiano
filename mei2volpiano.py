"""
MEI to volpiano converter.

Takes in one or more MEI files and outputs their volpiano representation.
See README for flags and usage. 


Class: MEItoVolpiano

Fucntions:

    get_mei_elements(file) -> list[MEI elements]
    find_clefs(list[elements]) -> list[char]
    find_notes(list[elements]) -> list[char]
    map_sylb(list[elements]) -> dict{syllable: notes}
    get_syl_key(element, integer) -> string
    get_volpiano(char, char) -> char
    export_volpiano(dict{syllables: notes}) -> string
"""

import argparse
import os.path
import xml.etree.ElementTree as ET
from timeit import default_timer as timer

# namespace for MEI tags
NAMESPACE = "{http://www.music-encoding.org/ns/mei}"


class MEItoVolpiano:
    def get_mei_elements(self, filename):
        """
        Return a list of all elements in the MEI file.

            Parameter:
                filename (file): An open file (see main)

            Returns:
                elements (list): List of all elements found.
        """
        tree = ET.parse(filename)
        root = tree.getroot()
        mei_element_objects = root.findall(".//")
        elements = []
        for mei_element in mei_element_objects:
            elements.append(mei_element)
        return elements

    def find_clefs(self, elements):
        """
        Finds all clefs in a given elements list (from an MEI file)

            Parameter:
                elements (list): List of elements

            Returns:
                clefs (list): char list of all clefs found, in order.
        """
        clefs = []
        for element in elements:
            if element.tag == f"{NAMESPACE}staffDef":
                clefs.append(element.attrib["clef.shape"])
            elif element.tag == f"{NAMESPACE}clef":
                clefs.append(element.attrib["shape"])
        return clefs

    def find_notes(self, elements):
        """
        Finds all notes in a given elements list (from an MEI file)

            Parameter:
                elements (list): List of elements

            Returns:
                notes (list): char list of all notes found, in order.
        """
        notes = []
        for element in elements:
            if element.tag == f"{NAMESPACE}nc":
                notes.append(element.attrib["pname"])

        return notes

    def map_sylb(self, elements):
        """
        Creates a dictionary of syllables and their respective neuemes.

            Parameter:
                elements (list): List of elements

            Returns:
                syl_note (dict): Dictionary {identifier: volpiano notes} of
                syllables and their unique data base numbers as keys and volpiano
                notes with correct octaves (output ready) as values.
        """
        syl_note = {"dummy": ""}
        dbase_bias = 0
        last = "dummy"
        for element in elements:

            if element.tag == f"{NAMESPACE}syl":
                key = self.get_syl_key(element, dbase_bias)
                syl_note[key] = syl_note[last]
                dbase_bias += 1
                syl_note["dummy"] = ""
                last = key

            if element.tag == f"{NAMESPACE}nc":
                note = element.attrib["pname"]
                ocv = element.attrib["oct"]
                volpiano = self.get_volpiano(note, ocv)
                syl_note[last] = f"{syl_note[last]}{volpiano}"

            if element.tag == f"{NAMESPACE}neume":
                if syl_note[last] != "":
                    syl_note[last] = f'{syl_note[last]}{"-"}'

            if element.tag == f"{NAMESPACE}sb":
                if syl_note[last] != "":
                    syl_note[last] = f'{syl_note[last]}{"7"}'

            if element.tag == f"{NAMESPACE}syllable":
                if syl_note[last] != "":
                    syl_note[last] = f'{syl_note[last]}{"---"}'
                last = "dummy"

        return syl_note

    def get_syl_key(self, element, bias):
        """
        Finds the dictionary key of a syllable from their 'syl' and database
        identifier.

            Parameters:
                element (element): A single element representing a syllable (syl)
                bias (int): The database identifier.

            Returns:
                key (int): The dictionary key for the given syllable.
        """
        key = -1
        if element.text:
            key = "".join(f"{bias}_")
            key = f"{key}{element.text}"
        else:
            key = "".join(f"{bias}")
        return key

    def get_volpiano(self, note, ocv):
        """
        Finds the volpiano representation of a note given its value and octave.

            Parameters:
                note (char): Note value taken from an element ('c', 'd', 'e' etc.)
                ocv (char): Octave of a given note ('1', '2', '3', or '4')

            Returns:
                oct{x}[note] (char): Volpiano character corresponding to
                input note and octave

                or

                error (string): Error if octave is out of range or note not in
                octave.

        """
        oct1 = {"g": "9", "a": "a", "b": "b"}
        oct2 = {"c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "a": "h", "b": "j"}
        oct3 = {"c": "k", "d": "l", "e": "m", "f": "n", "g": "o", "a": "p", "b": "q"}
        oct4 = {"c": "r", "d": "s"}

        error = "ERROR_OCTAVE"

        if ocv == "1":
            if note in oct1:
                return oct1[note]
            else:
                error = "NOTE_NOT_IN_OCTAVE"
                return error
        elif ocv == "2":
            if note in oct2:
                return oct2[note]
            else:
                error = "NOTE_NOT_IN_OCTAVE"
                return error
        elif ocv == "3":
            if note in oct3:
                return oct3[note]
            else:
                error = "NOTE_NOT_IN_OCTAVE"
                return error
        elif ocv == "4":
            if note in oct4:
                return oct4[note]
            else:
                error = "NOTE_NOT_IN_OCTAVE"
                return error
        else:
            return error

    def export_volpiano(self, mapping_dictionary):
        """
        Creates volpiano string with clef attached.

            Parameter:
                mapping_dictionary (dict): Dictionary of syllables and their
                corresponding volpiano notes.

            Returns:
                (string): Final, valid volpiano with the clef attached in a single line.
        """
        values = list(mapping_dictionary.values())
        clef = "1---"
        vol_string = "".join(values)
        return f"{clef}{vol_string}"


# driver code for CLI program
def main():
    start = timer()
    parser = argparse.ArgumentParser()

    # check the validity of file(s) being passed into program
    def check_file_validity(fname):
        ext = os.path.splitext(fname)[1][1:]
        if ext != "mei":
            parser.error('Must be a valid mei file with an ".mei" extension')
        return fname

    parser.add_argument(
        "mei_files",
        type=lambda fname: check_file_validity(fname),
        nargs="+",
        help="An MEI encoded music file",
    )

    parser.add_argument(
        "--e", type=str, nargs="?", help="A text file to hold output volpiano strings"
    )
    args = vars(parser.parse_args())  # stores each positional input in dict

    lib = MEItoVolpiano()
    ind = 1
    for mei_file in args["mei_files"]:
        with open(mei_file, "r") as f:
            print("\n" + f"The corresponding Volpiano string for {mei_file} is:")
            elements = lib.get_mei_elements(f)
            mapped = lib.map_sylb(elements)
            final_string = lib.export_volpiano(mapped)
            print("\n" + final_string + "\n")
        if args["e"] is not None:
            with open(f'{ind}_{args["e"]}', "a") as out:
                out.write(mei_file + "\n")
                out.write(final_string + "\n")
        ind += 1

    # testing time
    elapsed_time = timer() - start
    print(f"Script took {elapsed_time} seconds to execute" + "\n")


if __name__ == "__main__":
    main()
