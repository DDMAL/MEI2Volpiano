"""CLI program implementation of the MEI2Volpiano library  

    See README for details.
"""

import os.path
import argparse
import mei2volpiano
from timeit import default_timer as timer

# driver code for CLI program
def main():
    """
    This is the command line application MEI2Volpiano

    usage: driver.py [-h] (-N | -W) -t [T] [--export] mei [mei ...]

    positional arguments:
    mei         One or multiple MEI, or text file(s) with each relative MEI file/path to be converted per line

    optional arguments:
    -h, --help  show this help message and exit
    -N          An MEI neume encoded music file representing neume notation
    -W          An MEI western encoded music file representing western notation
    -t [T]      Flag indicating whether the inputs will be mei or txt files
    --export    flag indicating output to be sent to a .txt file (name corresponding with input mei)
    """
    start = timer()
    parser = argparse.ArgumentParser()
    option = parser.add_mutually_exclusive_group(required=True)

    # check the validity of file(s) being passed into program
    def check_file_validity(fname, valid_ext):

        if isinstance(valid_ext, list):
            if fname in valid_ext:
                return fname
            else:
                print(fname)
                parser.error(
                    "Invalid choice for type -t. Please choose from 'mei' or 'txt'"
                )
        else:
            ext = os.path.splitext(fname)[1][1:]
            if ext != valid_ext:
                parser.error(
                    f"Unexpected file type for the specified flag\nInput Type: {ext} \nExpected Type: {valid_ext}"
                )
            return fname

    # options for either neume or CWN
    option.add_argument(
        "-N",
        action="store_true",
        help="An MEI neume encoded music file representing neume notation",
    )

    option.add_argument(
        "-W",
        action="store_true",
        help="An MEI western encoded music file representing western notation",
    )

    parser.add_argument(
        "-t",
        nargs="?",
        required=True,
        type=lambda fname: check_file_validity(fname, ["txt", "mei"]),
        help="Flag indicating whether the inputs will be mei or txt files",
    )

    parser.add_argument(
        "mei",
        nargs="+",
        # type=lambda fname: check_file_validity(fname, "txt"),
        help="One or multiple MEI, or text file(s) with each relative MEI file/path to be converted per line",
    )

    parser.add_argument(
        "--export",
        action="store_true",
        help="flag indicating output to be sent to a .txt file (name corresponding with input mei)",
    )

    args = vars(parser.parse_args())  # stores each positional input in dict
    lib = mei2volpiano.MEItoVolpiano()
    vol_strings = []
    f_names = []

    # verify each file input matches (no mismatch extensions)
    ftype = None
    for pos_args in args["mei"]:
        if not ftype:
            ftype = os.path.splitext(pos_args)[1][1:]
        else:
            check_file_validity(pos_args, ftype)

    if args["W"]:
        if args["t"] == "mei":
            for mei_file in args["mei"]:
                with open(mei_file, "r") as f:
                    f_names.append(mei_file)
                    vol_strings.append(lib.Wconvert_mei_volpiano(f))
        if args["t"] == "txt":
            for txt_file in args["mei"]:
                txt_file = open(txt_file, "r")
                for mei_file in txt_file:
                    f_names.append(mei_file.strip())
                    vol_strings.append(lib.Wconvert_mei_volpiano(mei_file.strip()))

    if args["N"]:
        if args["t"] == "mei":
            for mei_file in args["mei"]:
                with open(mei_file, "r") as f:
                    f_names.append(mei_file)
                    vol_strings.append(lib.convert_mei_volpiano(f))
        if args["t"] == "txt":
            for txt_file in args["mei"]:
                txt_file = open(txt_file, "r")
                for mei_file in txt_file:
                    f_names.append(mei_file.strip())
                    vol_strings.append(lib.convert_mei_volpiano(mei_file.strip()))

    name_vol_pairs = list(zip(f_names, vol_strings))

    if args["export"]:
        for pair in name_vol_pairs:
            basename = os.path.basename(pair[0])
            out_name = os.path.splitext(basename)[0]
            with open(f"{out_name}.txt", "a") as out:
                out.write(out_name + "\n")
                out.write(pair[1])

    for pair in name_vol_pairs:
        print(f"\nThe corresponding Volpiano string for {pair[0]} is: \n{pair[1]}\n")

    # testing time
    elapsed_time = timer() - start
    print(f"Script took {elapsed_time} seconds to execute" + "\n")


if __name__ == "__main__":
    main()
