# Skeleton Process
# 1. Get the MEI file into the script
# 2. Parse until the `body` section is reached
# 3. Parse each `sylabble` tag and put the words and neuemes in pairs (dict)
# 4. Match the words and the neumes at the end of the body loop
# 5. Convert output dict into string and export
# Process is one pass with O(x) for x = length of lines in body. Roughly
import sys


class MEItoVolpiano:
    def import_mei(mei_file):

        # The two flags find the start and end of the body tag, printing lines between them.

        bodyFlag = bodyEndFlag = False
        for line in mei_file:
            if "<body" in line:
                bodyFlag = True
            if "</body" in line:
                bodyEndFlag = True
            if bodyFlag and not bodyEndFlag:
                print(line.strip())

    def create_volpaino(parsed_mei):
        pass

    def export_volpiano(volpiano_file):
        pass


def main():
    f = open(sys.argv[1], "r")
    for line in f:
        if "<body" in line:
            bodyFlag = True
        if "</body" in line:
            bodyEndFlag = True
        if bodyFlag and not bodyEndFlag:
            print(line.strip())

    MEItoVolpiano.import_mei(f)


if __name__ == "__main__":
    main()
