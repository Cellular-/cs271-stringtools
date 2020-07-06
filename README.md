# cs271-stringtools

# Stringtools

Python script to perform analyses and operations on text files.

## Dependencies
Python

re (builtin)

os (builtin)

glob (builtin)

editdistance (external library)

## Installation
Move `base_script.py` and `output` folder into your working directory.

## Usage
Move `.txt` files into same location as `base_script.py` and `output` folder.
Move file named `words.txt` to base directory to perform edit distance analysis.

Windows:
Double-click `base_script.py` (assumes Python is in PATH)

Linux:
`python base_script.py`

Provide preference to write or print output to prompt.

Navigate to `output` folder and review program output.

## Limitations
Script will perform all operations on all `.txt` files in the working directory.
Future upgrades will allow user to specify the operations and files individually.

## License
[MIT]