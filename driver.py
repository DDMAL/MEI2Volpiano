import os.path
import argparse
import mei2volpiano
from timeit import default_timer as timer

# driver code for CLI program
def main():
    start = timer()
    parser = argparse.ArgumentParser()

    # check the validity of file(s) being passed into program
    def check_file_validity(fname):
        ext = os.path.splitext(fname)[1][1:]
        if ext != "mei":
            parser.error('Must be a valid mei file with an ".mei" extension')
        return fname

    parser.add_argument(
        "mei_files",
        type=lambda fname: check_file_validity(fname),
        nargs="+",
        help="An MEI encoded music file",
    )

    parser.add_argument(
        "--e", type=str, nargs="?", help="A text file to hold output volpiano strings"
    )
    args = vars(parser.parse_args())  # stores each positional input in dict

    lib = mei2volpiano.MEItoVolpiano()
    ind = 1
    for mei_file in args["mei_files"]:
        with open(mei_file, "r") as f:
            print("\n" + f"The corresponding Volpiano string for {mei_file} is:")
            elements = lib.get_mei_elements(f)
            mapped = lib.map_sylb(elements)
            final_string = lib.export_volpiano(mapped)
            print("\n" + final_string + "\n")
        if args["e"] is not None:
            with open(f'{ind}_{args["e"]}', "a") as out:
                out.write(mei_file + "\n")
                out.write(final_string + "\n")
        ind += 1

    # testing time
    elapsed_time = timer() - start
    print(f"Script took {elapsed_time} seconds to execute" + "\n")


if __name__ == "__main__":
    main()