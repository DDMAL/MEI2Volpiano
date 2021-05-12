# Skeleton Process
# 1. Get the MEI file into the script
# 2. Parse until the `body` section is reached
# 3. Parse each `sylabble` tag and put the words and neuemes in pairs (dict)
# 4. Match the words and the neumes at the end of the body loop
# 5. Convert output dict into string and export
# Process is one pass with O(x) for x = length of lines in body. Roughly

import argparse
import xml.etree.ElementTree as ET
from timeit import default_timer as timer

NAMESPACE = "{http://www.music-encoding.org/ns/mei}"  # namespace for MEI tags


class MEItoVolpiano:
    def get_mei_elements(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        mei_element_objects = root.findall(".//")
        elements = []
        for mei_element in mei_element_objects:
            elements.append(mei_element)  # append each to list
        return elements

    def find_clefs(self, elements):
        # Finds all clefs in a given file.
        clefs = []
        for element in elements:
            if element.tag == f"{NAMESPACE}staffDef":
                clefs.append(element.attrib["clef.shape"])
            elif element.tag == f"{NAMESPACE}clef":
                clefs.append(element.attrib["shape"])
        return clefs

    def find_notes(self, elements):
        notes = []
        for element in elements:
            if element.tag == f"{NAMESPACE}nc":
                notes.append(element.attrib["pname"])

        return notes

    # error in the code because the syl is not always considered first
    # it affect the final result
    def map_sylb(self, elements):
        syl_note = {"dummy": ""}
        dbase_bias = 0
        
        for element in elements:
            last = "dummy"

            if element.tag == f"{NAMESPACE}syl":
                key = self.get_syl_key(element, dbase_bias)
                syl_note[key] = syl_note[last]
                dbase_bias += 1
                syl_note["dummy"] = ""
                last = key
                

            if element.tag == f"{NAMESPACE}nc":
                note = element.attrib["pname"]
                ocv = element.attrib["oct"]
                volpiano = self.getVolpiano(note, ocv)
                syl_note[last] = f"{syl_note[last]}{volpiano}"
           
            if element.tag == f"{NAMESPACE}neume":
                syl_note[last] = f'{syl_note[last]}{"-"}'
      
            # may have errors
            if element.tag == f"{NAMESPACE}sb":
                if syl_note[last] != "":
                    syl_note[last] = f'{syl_note[last]}{"7"}'
                 

            if element.tag == f"{NAMESPACE}syllable":
                if syl_note[last] != "":
                    syl_note[last] = f'{syl_note[last]}{"---"}'
                  
                last = "dummy"

        return syl_note
    
    def get_syl_key(self, element, bias):
        key = -1
        if element.text:
            key = "".join(f"{bias}_")
            key = f"{key}{element.text}"
        else:
            key = "".join(f"{bias}")
        return key

    def getVolpiano(self, note, ocv):
        oct1 = {"g": "9", "a": "a", "b": "b"}
        oct2 = {"c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "a": "h", "b": "j"}
        oct3 = {"c": "k", "d": "l", "e": "m", "f": "n", "g": "o", "a": "p", "b": "q"}
        oct4 = {"c": "r", "d": "s"}

        if ocv == "1":
            if note in oct1:
                return oct1[note]
            else:
                return "NOTE_NOT_IN_OCTAVE"
        elif ocv == "2":
            if note in oct2:
                return oct2[note]
            else:
                return "NOTE_NOT_IN_OCTAVE"
        elif ocv == "3":
            if note in oct3:
                return oct3[note]
            else:
                return "NOTE_NOT_IN_OCTAVE"
        elif ocv == "4":
            if note in oct4:
                return oct4[note]
            else:
                return "NOTE_NOT_IN_OCTAVE"
        else:
            return "ERROR_OCTAVE"

    def export_volpiano(self, mapping_dictionary):
        values = list(mapping_dictionary.values())
        clef = "1---"
        vol_string = "".join(values)
        return f"{clef}{vol_string}"


def main():

    start = timer()
    parser = argparse.ArgumentParser()
    msg = "An MEI encoded music file"
    parser.add_argument("mei_files", type=str, nargs="+", help=msg)
    args = vars(parser.parse_args())  # stores each positional input in dict

    # TODO: set up argparse as follows:
    # mei2volpiano.py [filename of mei] will output volpiano to terminal
    # mei2volpiano.py [filename of mei] [filename of output] -e will output
    # to specified txt file

    for mei_file in args["mei_files"]:
        with open(mei_file, "r") as f:
            lib = MEItoVolpiano()
            elements = lib.get_mei_elements(f)
            mapped = lib.map_sylb(elements)
            print(lib.export_volpiano(mapped))
    elapsed_time = timer() - start
    print(f'Script took {elapsed_time} seconds to execute')


if __name__ == "__main__":
    main()
