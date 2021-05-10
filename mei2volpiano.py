# Skeleton Process
# 1. Get the MEI file into the script 
# 2. Parse until the `body` section is reached 
# 3. Parse each `sylabble` tag and put the words and neuemes in pairs (dict)
# 4. Match the words and the neumes at the end of the body loop
# 5. Convert output dict into string and export
# Process is one pass with O(x) for x = length of lines in body. Roughly

class MEItoVolpiano:
    
    def import_mei(self, mei_file):
        print(mei_file)

    def parse_mei(self, mei_body):
        pass
    
    def create_volpaino(self, parsed_mei):
        pass

    def export_volpiano(self, volpiano_file):
        pass


def main():
    a = MEItoVolpiano()
    a.import_mei(2)

if __name__ == "__main__":
    main()