# Skeleton Process
# 1. Get the MEI file into the script
# 2. Parse until the `body` section is reached
# 3. Parse each `sylabble` tag and put the words and neuemes in pairs (dict)
# 4. Match the words and the neumes at the end of the body loop
# 5. Convert output dict into string and export
# Process is one pass with O(x) for x = length of lines in body. Roughly

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

    def find_clef(mei_atrrs):

        for element in mei_atrrs:
            print(element)

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
            MEItoVolpiano.find_clef(atr)


if __name__ == "__main__":
    main()
