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

    usage: mei2vol [-h] (-N N [N ...] | -W W [W ...] | -txt [TXT]) [-export]
    mei2vol: error: one of the arguments -mei -txt is required
    """
    start = timer()
    parser = argparse.ArgumentParser()
    option = parser.add_mutually_exclusive_group(required=True)

    # check the validity of file(s) being passed into program
    def check_file_validity(fname, valid_ext):
        ext = os.path.splitext(fname)[1][1:]
        if ext != valid_ext:
            parser.error(
                f"Unexpected file type for the specified flag\nInput Type: {ext} \nExpected Type: {valid_ext}"
            )
        return fname

    option.add_argument(
        "-N",
        type=lambda fname: check_file_validity(fname, "mei"),
        nargs="+",
        help="An MEI neume encoded music file representing neume notation",
    )

    option.add_argument(
        "-W",
        nargs="+",
        type=lambda fname: check_file_validity(fname, "mei"),
        help="An MEI western encoded music file representing western notation",
    )

    option.add_argument(
        "-Ntxt",
        nargs="?",
        type=lambda fname: check_file_validity(fname, "txt"),
        help="A text file with each MEI file/path to be converted per line",
    )

    option.add_argument(
        "-Wtxt",
        nargs="?",
        type=lambda fname: check_file_validity(fname, "txt"),
        help="A text file with each MEI file/path to be converted per line",
    )

    parser.add_argument(
        "-export",
        action="store_true",
        help="flag output converted volpiano to a .txt file (name corresponding with input)",
    )

    args = vars(parser.parse_args())  # stores each positional input in dict

    lib = mei2volpiano.MEItoVolpiano()
    vol_strings = []
    f_names = []

    # if args["mei"] and args["txt"]:
    #     parser.error('Cannot use both "-mei" and "-txt" simultaneously')

    if args["Ntxt"] is not None:
        txt_file = open(args["Ntxt"])
        for mei_file in txt_file:
            f_names.append(mei_file.strip())
            vol_strings.append(lib.convert_mei_volpiano(mei_file.strip()))
    
    if args["Wtxt"] is not None:
        txt_file = open(args["Wtxt"])
        for mei_file in txt_file:
            f_names.append(mei_file.strip())
            vol_strings.append(lib.Wconvert_mei_volpiano(mei_file.strip()))

    if args["N"] is not None:
        for mei_file in args["N"]:
            with open(mei_file, "r") as f:
                f_names.append(mei_file)
                vol_strings.append(lib.convert_mei_volpiano(f))

    if args["W"] is not None:
        for mei_file in args["W"]:
            with open(mei_file, "r") as f:
                f_names.append(mei_file)
                vol_strings.append(lib.Wconvert_mei_volpiano(f))

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
