# Skeleton Process
# 1. Get the MEI file into the script
# 2. Parse until the `body` section is reached
# 3. Parse each `sylabble` tag and put the words and neuemes in pairs (dict)
# 4. Match the words and the neumes at the end of the body loop
# 5. Convert output dict into string and export
# Process is one pass with O(x) for x = length of lines in body. Roughly

import re
import argparse
import xml.etree.ElementTree as ET


class MEItoVolpiano:
<<<<<<< HEAD
=======

>>>>>>> 344bff99832e9cc3dbd38c3191408018a6511007
    def get_mei_attrs(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        a = root.findall(".//")
        atribs = []
        for i in a:
            if "clef.shape" in i.keys() or "pname" in i.keys():
                atribs.append(i.attrib)
        return atribs

    def find_clef(parsed_mei):

        # Find the clef shape and line location from body
        clef = []
        for line in parsed_mei:
            if "staffDef" in line:  # This assumes exact information location

                # playing around with some regex
                # can be used for other lines as well
                mei_tag_attrs = dict(re.findall(r"(\w*)=(\".*?\"|\S*)", line))
                clef.append(mei_tag_attrs["shape"])
                clef.append(mei_tag_attrs["line"])
                break

        for char in clef[0]:
            if "A" <= char <= "Z":
                clef[0] = char
        for char in clef[1]:
            if char.isdigit():
                clef[1] = int(char)
        return clef

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
            print(MEItoVolpiano.get_mei_attrs(f))


if __name__ == "__main__":
    main()
