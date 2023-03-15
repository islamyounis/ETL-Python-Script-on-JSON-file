# JSON-data-is-transformed-by-python-script-and-saved-as-a-CSV-file.
a script transforms JSON files to a DataFrame and commit each file to a sperate CSV file 

**Script details**

The Script itself must do the following before and after trasforamtion:

- One positional argument which is the directory path with that have the files.
- One optional argument -u. If this argument is passed will maintain the UNIX format of timpe stamp and if not passed the time stamps will be converted.
- Check if the files have any dublicates in between checksum and print a messeage that indicate that.
- Print a message after converting each file with the number of rows transformed and the path of this file
- At the end of this script print the total excution time.


## Problem Description:

In 2012, URL shortening service Bitly partnered with the US government website USA.gov to provide a feed of anonymous data gathered from users who shorten links ending with .gov or .mil.
The text file comes in JSON format and with some keys and their description. 
- ```a``` Denotes information about the web browser and operating system.
- ```tz``` time zone.
- ```r``` URL the user come from.
- ```u``` URL where the user headed to.
- ```t``` Timestamp when the user start using the website in UNIX format.
- ```hc``` Timestamp when user exit the website in UNIX format.
- ```cy``` City from which the request intiated.
- ```ll``` Longitude and Latitude.
The output CSV files have the following columns:
- ```web_browser``` The web browser that has requested the service.
- ```operating_sys``` operating system that intiated this request.
- ```from_url``` The main URL the user came from in a short format.
- ```to_url``` The main URL the user went to in a short format.  
- ```city``` The city from which the the request was sent.
- ```longitude``` The longitude where the request was sent.
- ```latitude``` The latitude where the request was sent.
- ```time_zone``` The time zone that the city follow.
- ```time_in``` Time when the request started.
- ```time_out``` Time when the request is ended.
## Tools and Technologies:
- Python 
- Pandas
- NumPy
- Jupyter Notebook
- JSON
