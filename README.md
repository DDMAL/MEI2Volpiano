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

To output the MEI file's volpiano string to the terminal, run

`mei2vol -mei filename1.mei`

Multiple files can be passed in at once

`mei2vol -mei filename1.mei filename2.mei`

To output the volpiano string(s) to a text file, use the `-export` flag as such

`mei2vol -mei filename1.mei -export`

and the program will output each mei file's volpiano to a similarly named file as its input.

To make it easier to pass in multiple MEI files, the `-txt` file can be used

`mei2vol -txt filename1.txt`

where the ".txt" file being passed in must hold the name/relative path of the required MEI files on distinct lines.

The `-export` tag can be used on any valid input to the program. `-mei` or `-txt` are required flags for the program to identify the file(s) you are attempting to input.

## Tests

To run the current test suite, execute `pytest`