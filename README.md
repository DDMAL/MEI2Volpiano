# MEI2Volpiano
MEI2Volpiano is a Python library developed for the purpose of converting Neume MEI files to a Volpiano string.

# Licence
MEI2Volpiano is released under the MIT license.

# Setup and Usage

MEI2Volpiano requires at least Python 3.6.
* Clone project `https://github.com/DDMAL/MEI2Volpiano.git`
* Enter the script directory (src)
* For ease of use with CLI, you can put your MEI files in the same directory as the script, otherwise you will have to specify the path to file in the next steps below

To output the MEI file's volpiano string to the terminal, run

`python driver.py -mei filename1.mei`

Multiple files can be passed in at once

`python driver.py -mei filename1.mei filename2.mei`

To output the volpiano string(s) to a text file, use the `-export` flag as such

`python driver.py -mei filename1.mei -export`

and the program will output each mei file's volpiano to a similarly named file as its input.

To make it easier to pass in multiple MEI files, the `-txt` file can be used

`python driver.py -txt filename1.txt`

where the ".txt" file being passed in must hold the name/relative path of the required MEI files on distinct lines.



The `-export` tag can be used on any valid input to the program. `-mei` or `-txt` are required flags for the program to identify the file(s) you are attempting to input.

# Tests

To run the current test suite, `cd` into "/tests/" and run
`python3 test.py ../resources/016r_reviewed.mei ../resources/CDN-Hsmu_M2149.L4_003r.mei ../resources/CDN-Hsmu_M2149.L4_003v.mei` to compare the output to human generated
ground truth.
