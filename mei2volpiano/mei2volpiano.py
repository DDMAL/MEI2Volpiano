"""Converts MEI files to volpiano strings.

Takes in one or more MEI files and outputs their volpiano representation.
See README for flags and usage.
"""

import xml.etree.ElementTree as ET

# namespace for MEI tags
NAMESPACE = "{http://www.music-encoding.org/ns/mei}"


class MEItoVolpiano:
    """
    Class: MEItoVolpiano

    Methods:

        [Main]:
            get_mei_elements(file) -> list[MEI elements]
            sylb_volpiano_map(list[elements]) -> dict{string: string}
            get_syl_key(element, integer) -> string
            get_volpiano(char, char) -> char
            export_volpiano(dict{syllables: notes}) -> string
            convert_mei_volpiano(file) -> string 

            ^ convert_mei_volpiano handles all methods in main.
        
        [Debugging]:
            find_clefs(list[elements]) -> list[char]
            find_notes(list[elements]) -> list[char]
            find_syls(list[elements]) -> list[string]
            sylb_note_map(list[elements]) -> dict{string: string}

            ^ useful for MEI parsing and testing outputs.

    """
    def get_mei_elements(self, filename:str) -> list:
        """Returns a list of all elements in the MEI file.

        Args:
            filename (string): An open MEI file.

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

    def find_clefs(self, elements: list) -> list:
        """Finds all clefs in a given elements list

        Args:
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
        """Finds all notes in a given elements list

        Args:
            elements (list): List of elements

        Returns:
            notes (list): char list of all notes found, in order.
        """
        notes = []
        for element in elements:
            if element.tag == f"{NAMESPACE}nc":
                notes.append(element.attrib["pname"])

        return notes

    def find_syls(self, elements):
        """Finds all syllables in a given elements list

        Args:
            elements (list): List of elements

        Returns:
            syls (list): string list of all syllables found, in order.
        """
        syls = []
        for element in elements:
            if element.tag == f"{NAMESPACE}syl":
                if element.text:
                    syls.append(element.text)
        return syls

    def sylb_note_map(self, elements):
        """Creates a dictionary map of syllables and their notes (with octaves).

        Args:
            elements (list): List of elements

        Returns:
            syl_dict (dict): Dictionary {identifier: notes} of syllables and
            their unique data base numbers as keys and notes (with octaves) as values.
        """

        syl_dict = {"dummy": ""}
        dbase_bias = 0
        last = "dummy"

        for element in elements:

            if element.tag == f"{NAMESPACE}syl":
                key = self.get_syl_key(element, dbase_bias)
                syl_dict[key] = syl_dict[last]
                dbase_bias += 1
                syl_dict["dummy"] = ""
                last = key

            if element.tag == f"{NAMESPACE}nc":
                note = element.attrib["pname"]
                ocv = element.attrib["oct"]
                finNote = f"{note}{ocv}"
                syl_dict[last] = f"{syl_dict[last]}{finNote}"

            if element.tag == f"{NAMESPACE}neume":
                if syl_dict[last] != "":
                    syl_dict[last] = f'{syl_dict[last]}{"-"}'

            if element.tag == f"{NAMESPACE}syllable":
                last = "dummy"

        del syl_dict["dummy"]
        return syl_dict

    def sylb_volpiano_map(self, elements):
        """Creates a dictionary of syllables and their volpiano values.

        Args:
            elements (list): List of elements

        Returns:
            syl_note (dict): Dictionary {identifier: volpiano notes} of
            syllables and their unique data base numbers as keys and volpiano
            notes with correct octaves as values.
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
        """Finds the dictionary key of a syllable from their 'syl' and database
        identifier.

        Args:
            element (element): A single element representing a syllable (syl)
            bias (int): The database identifier.

        Returns:
            key (string): The dictionary key for the given syllable.
        """
        key = -1
        if element.text:
            key = "".join(f"{bias}_")
            key = f"{key}{element.text}"
        else:
            key = "".join(f"{bias}")
        return key

    def get_volpiano(self, note, ocv):
        """Finds the volpiano representation of a note given its value and octave.

        Args:
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

        error = "OCTAVE_ERROR"

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
        """Creates volpiano string with clef attached.

        Args:
            mapping_dictionary (dict): Dictionary of syllables and their
            corresponding volpiano notes.

        Returns:
            (string): Final, valid volpiano with the clef attached in a single line.
        """
        values = list(mapping_dictionary.values())
        clef = "1---"
        vol_string = "".join(values)
        return f"{clef}{vol_string}"

    def convert_mei_volpiano(self, filename):
        """All-in-one method for converting MEI file to valid volpiano string.

        Args:
            filename (file): Open MEI file you want the volpiano of.

        Returns:
            volpiano (string): Valid volpiano string representation of the input.
        """
        elements = self.get_mei_elements(filename)
        mapped_values = self.sylb_volpiano_map(elements)
        volpiano = self.export_volpiano(mapped_values)
        return volpiano