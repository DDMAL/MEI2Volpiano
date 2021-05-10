# Skeleton Process
# 1. Get the MEI file into the script
# 2. Parse until the `body` section is reached
# 3. Parse each `sylabble` tag and put the words and neuemes in pairs (dict)
# 4. Match the words and the neumes at the end of the body loop
# 5. Convert output dict into string and export
# Process is one pass with O(x) for x = length of lines in body. Roughly
import sys
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

    def create_volpiano(parsed_mei):
        clef = []
        for line in parsed_mei:
            if "staffDef" in line:
                curr = line.split()
                clef.append(curr[-1])
                clef.append(curr[-2])
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
    f = open(sys.argv[1], "r")
    clean_mei = MEItoVolpiano.import_mei(f)

    # for line in clean_mei:
    #    print(line)

    volpiano = MEItoVolpiano.create_volpiano(clean_mei)
    print(volpiano)


if __name__ == "__main__":
    main()
