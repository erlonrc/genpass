# Genpass

## Random Password Generator
This is a command-line utility written in Python to generate secure random passwords.

## Features:
- Generates random passwords with printable characters from the ASCII table.

## Installation
1. Clone the GitHub repository:
```bash
git clone https://github.com/erlonicr/genpass.git
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
sudo apt install xclip # Only for Linux
```
3. Navigate to the project directory:
```bash
cd genpass
```
4. Execute the script:
```bash
genpass.py
```

**Note:** An alias for this command can be created (refer to your system's documentation for details).

## Usage Options
- `-l [length]`, `--length [length]`: Sets the password length. The default value is 16 characters.
- `-c`, `--copy`: Copies the generated password to the clipboard.
- `-H`, `--hide`: Suppresses the printing of the password in the terminal.

## Example of use:
- Generate a 16-character password and copy it to the clipboard:
```bash
genpass.py -c
```
- Generate a 32-character password and copy it to the clipboard without printing it to the terminal:
```bash
genpass.py -Hc -l32
```

## License
This project is licensed under the MIT license.
