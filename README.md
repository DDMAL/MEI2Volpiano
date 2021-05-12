# MEI2Volpiano
MEI2Volpiano is a Python library developed for the purpose of converting Neume MEI files to a Volpiano string.

# Licence
MEI2Volpiano is released under the MIT license.

# Setup and Usage

MEI2Volpiano requires at least Python 3.
* Clone project `https://github.com/DDMAL/MEI2Volpiano.git`
* Enter the script directory (mei2volpiano.py)
* For ease of use with CLI, you can put your MEI files in the same directory as the script, otherwise you will have to specify the path to file in the next steps below

To output the MEI file's volpiano string to the terminal, run

`python mei2volpiano filename.mei`

Multiple files can be passed in at once

`python mei2volpiano filename1.mei filename2.mei`

To output the volpiano string(s) to a text file, use the `--e` flag as such

`python mei2volpiano filename1.mei --e output_file.txt`

If multiple MEI files are passed in and the `--e` flag is used, each volpiano string will be outputted to its own text file, with the file name being appended with an index representing the position in which its respective MEI file was passed into the program (ex. `1_output_file.txt`).

Currently, the program works as a CLI program, proper library usage will be added soon.
