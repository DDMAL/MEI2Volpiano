# MEI2Volpiano
MEI2Volpiano is a Python library developed for the purpose of converting Neume MEI files to a Volpiano string.

## Licence
MEI2Volpiano is released under the MIT license.

## Installation

* `pip install mei2volpiano`

## Development Setup

MEI2Volpiano requires at least Python 3.6.
* Clone project `https://github.com/DDMAL/MEI2Volpiano.git`
* Enter the project checkout
* Execute `pip install .` or `poetry install` (this will install development dependencies)

## Usage

As long as you're in the python environment, you can execute `mei2volpiano` or the shorthand `mei2vol` while in your python virtual environment

### Standard Usage (Neume notation)

To output the MEI file's volpiano string to the terminal, run

`mei2vol -N filename1.mei`

Multiple files can be passed in at once

`mei2vol -N filename1.mei filename2.mei`

### Western

To convert MEI files written in Common Western Music Notation (CWMN), run

`mei2vol -W filename1.mei`

All of the CWMN files processed by this library (so far) come from [this collection](https://github.com/DDMAL/Andrew-Hughes-Chant/tree/master/file_structure_text_file_MEI_file). Thus, we followed the conventions of those files. Namely:

- Every neume is encoded as a quarter note
- Stemless notes


### Mutiple MEI File Runs

To make it easier to pass in multiple MEI files, the `-Ntxt` or `-Wtxt` flags can be used as so

`mei2vol -Ntxt filename1.txt`

where the ".txt" file being passed in must hold the name/relative path of the required MEI files on distinct lines.

**Note: If passing inputs through this method, the formats of the MEI files within the text file must be of the same type** (either neume for `-Ntxt` or western for `-Wtxt`)

### Exporting

The `-export` tag can be used on any valid input to the program. Simply tack it on to the end of your command like so

`mei2vol -N filename1.mei -export`

and the program will output each mei file's volpiano to a similarly named file as its input.




## Tests

To run the current test suite, execute `pytest`
