# Skeleton Process
# 1. Get the MEI file into the script
# 2. Parse until the `body` section is reached
# 3. Parse each `sylabble` tag and put the words and neuemes in pairs (dict)
# 4. Match the words and the neumes at the end of the body loop
# 5. Convert output dict into string and export
# Process is one pass with O(x) for x = length of lines in body. Roughly
import sys
import re
import argparse


class MEItoVolpiano:
    def import_mei(mei_file):

        # The two flags find the start and end of the body tag, printing lines between them.
        mei_line_array = []
        bodyFlag = bodyEndFlag = False
        for line in mei_file:
            if "<body" in line:
                bodyFlag = True
            if "</body" in line:
                bodyEndFlag = True
            if bodyFlag and not bodyEndFlag:
                # print(line.strip())
                mei_line_array.append(line.strip())

        return mei_line_array

    def find_clef(parsed_mei):

        # Find the clef shape and line location from body
        clef = []
        for line in parsed_mei:
            if "staffDef" in line: # This assumes exact information location 
                
                # playing around with some regex, may have found a good solution
                mei_tag_attrs = dict(re.findall(r'(\w*)=(\".*?\"|\S*)', line))  # may be slow
                clef.append(mei_tag_attrs['shape'])
                clef.append(mei_tag_attrs['line'])
                break

        for char in clef[0]:
            if char >= "A" and char <= "Z":
                clef[0] = char
        for char in clef[1]:
            if char.isdigit():
                clef[1] = int(char)
        return clef

    def export_volpiano(volpiano_file):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mei_files", type=str, nargs='+', help="Please enter one or multiple MEI files")
    args = vars(parser.parse_args())  # stores each positional input in dict, may want to check file validity

    for mei_file in args['mei_files']:
        with open(mei_file, 'r') as f:
            clean_mei = MEItoVolpiano.import_mei(f)
            clef = MEItoVolpiano.find_clef(clean_mei)
            print(clef)


if __name__ == "__main__":
    main()
