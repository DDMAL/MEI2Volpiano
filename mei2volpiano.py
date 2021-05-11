# Skeleton Process
# 1. Get the MEI file into the script
# 2. Parse until the `body` section is reached
# 3. Parse each `sylabble` tag and put the words and neuemes in pairs (dict)
# 4. Match the words and the neumes at the end of the body loop
# 5. Convert output dict into string and export
# Process is one pass with O(x) for x = length of lines in body. Roughly

# -- Needs to properly differentiate the words, syllables, neumes
# to determine the number of hyphens

'''
TODO:
- 
'''


import argparse
import xml.etree.ElementTree as ET

NAMESPACE = "{http://www.music-encoding.org/ns/mei}"  # namespace for MEI tags


class MEItoVolpiano:
    def get_mei_elements(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        a = root.findall(".//")
        elements = []
        for i in a:
            elements.append(i)  # append each to list
        return elements

    def find_clefs(elements):
        # Finds all clefs in a given file.
        clefs = []
        for element in elements:
            if element.tag == f"{NAMESPACE}staffDef":
                clefs.append(element.attrib["clef.shape"])
            elif element.tag == f"{NAMESPACE}clef":
                clefs.append(element.attrib["shape"])
        return clefs

    def find_notes(elements):
        notes = []
        for element in elements:
            if element.tag == f"{NAMESPACE}nc":
                notes.append(element.attrib["pname"])

        return notes

    def map_sylb(elements):
        syl_note = {"0": ""}
        dbase_bias = 0
        # currClef = [] #stack
        for element in elements:
            last = list(syl_note)[-1]
            if element.tag == f"{NAMESPACE}syl":
                key = MEItoVolpiano.get_syl_key(element, dbase_bias)
                syl_note[key] = ""
                dbase_bias += 1
                last = key
            if element.tag == f"{NAMESPACE}nc":
                offset = (int(element.attrib['oct']) - 1) * 8   # offset to calculate volpiano in higher octaves
                syl_note[last] = f'{syl_note[last]}{chr(ord(element.attrib["pname"]) + offset)}'
            if element.tag == f"{NAMESPACE}neume":
                if syl_note[last] != "":
                    syl_note[last] = f'{syl_note[last]}{"-"}'

        return syl_note

    def get_syl_key(element, bias):
        key = -1
        if element.text:
            key = "".join(f"{bias}_")
            key += element.text
        else:
            key = "".join(f"{bias}")
        return key

    def convertNote(clef, note, octave):
        # convert note to volpiano

        pass

    def export_volpiano(volpiano_dict):


def main():
    parser = argparse.ArgumentParser()
    error = "Please enter one or multiple MEI files"
    parser.add_argument("mei_files", type=str, nargs="+", help=f"{error}")
    args = vars(
        parser.parse_args()
    )  # stores each positional input in dict, may want to check file validity

    for mei_file in args["mei_files"]:
        with open(mei_file, "r") as f:
            # clean_mei = MEItoVolpiano.import_mei(f)
            # clef = MEItoVolpiano.find_clef(clean_mei)
            # print(clef)
            elements = MEItoVolpiano.get_mei_elements(f)
            # clefs = MEItoVolpiano.find_clefs(elements)
            # notes = MEItoVolpiano.find_notes(elements)
            mapped = MEItoVolpiano.map_sylb(elements)
            # print(clefs)
            # print(notes)
            print(mapped)


if __name__ == "__main__":
    main()
