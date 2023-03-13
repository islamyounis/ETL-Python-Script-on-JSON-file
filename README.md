# JSON-data-is-transformed-by-python-script-and-saved-as-a-CSV-file.
a script transforms JSON files to a DataFrame and commit each file to a sperate CSV file 

**Script details**

The Script itself must do the following before and after trasforamtion:

- One positional argument which is the directory path with that have the files.
- One optional argument -u. If this argument is passed will maintain the UNIX format of timpe stamp and if not passed the time stamps will be converted.
- Check if the files have any dublicates in between checksum and print a messeage that indicate that.
- Print a message after converting each file with the number of rows transformed and the path of this file
- At the end of this script print the total excution time.
