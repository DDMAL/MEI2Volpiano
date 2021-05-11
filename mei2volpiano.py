# Skeleton Process
# 1. Get the MEI file into the script
# 2. Parse until the `body` section is reached
# 3. Parse each `sylabble` tag and put the words and neuemes in pairs (dict)
# 4. Match the words and the neumes at the end of the body loop
# 5. Convert output dict into string and export
# Process is one pass with O(x) for x = length of lines in body. Roughly

# -- Needs to properly differentiate the words, syllables, neumes
# to determine the number of hyphens

import argparse
import xml.etree.ElementTree as ET


class MEItoVolpiano:
    def get_mei_attrs(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        a = root.findall(".//")
        atribs = []
        for i in a:
            atribs.append(i)  # append each to list
        return atribs

    def find_clefs(mei_atrrs):
        # Finds all clefs in a given file.
        clefs = []
        for element in mei_atrrs:
            if element.tag == "{http://www.music-encoding.org/ns/mei}staffDef":
                clefs.append(element.attrib["clef.shape"])
            elif element.tag == "{http://www.music-encoding.org/ns/mei}clef":
                clefs.append(element.attrib["shape"])
        return clefs

    def export_volpiano(volpiano_file):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mei_files", type=str, nargs="+", help="Please enter one or multiple MEI files"
    )
    args = vars(
        parser.parse_args()
    )  # stores each positional input in dict, may want to check file validity

    for mei_file in args["mei_files"]:
        with open(mei_file, "r") as f:
            # clean_mei = MEItoVolpiano.import_mei(f)
            # clef = MEItoVolpiano.find_clef(clean_mei)
            # print(clef)
            atr = MEItoVolpiano.get_mei_attrs(f)
            clefs = MEItoVolpiano.find_clefs(atr)
            print(clefs)


if __name__ == "__main__":
    main()
