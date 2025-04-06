File Handling Script in Python:

This Python script demonstrates basic file handling operations in Python, including:

Reading a file with error handling
Writing to a file
Appending to the file
Reading the modified file content

How It Works
Reading from a File:
Tries to open a file named sample.txt for reading.
If the file is not found, a FileNotFoundError is caught and a message is displayed.

Writing and Appending to a File:

If sample.txt is not found or after reading completes, the script proceeds to open output.txt.
Prompts the user to input text, which is written to output.txt.
Prompts again to append additional text to the file.
Finally, reads and prints the entire content of output.txt.

Files Used
sample.txt: Input file to be read (must exist in the same directory).
output.txt: File to which user input is written and appended.


If sample.txt is not present, the script will still continue to execute the file writing and appending operations.

All file operations are done with proper open/close handling.

