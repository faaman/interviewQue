# A Python CLI application that will parse logs of various kinds
# A test suite must be included
# hij: use regex module
# do not use the 'head', 'tail' or 'grep' utilities
# options needed: h
# options needed: -f (--first NUM, Print first NUM lines)
# options needed: -l (--last NUM, Print last NUM lines)
# options needed: -t (--timestamps, Print lines that contain a timestamp in HH:MM:SS format)
# options needed: -i (--ipv4, Print lines that contain an IPv4 address, matching IPs are highlighted)
# options needed: -I (--ipv6, Print lines that contain an IPv6 address, std notation, matching IPs are highlighted)

from sys import argv
import re

totalArgs = len(argv)

script = argv[0]
filename = argv[1]
option = argv[2]
if totalArgs == 4:
    numLines = argv[3]
else:
    numLines = 0

########################

# find out total number of lines in file
with open(filename, 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)

txt = open(filename)

# first lines option
if option == '-f' or option == '--first':
    print("These are the first required lines from the file: ")
    lines = txt.readlines()
    for i in range(0, int(numLines)):
        print(lines[i])

# last lines option
if option == '-l' or option == '--last':
    print("These are the last required lines from the file: ")
    lines = txt.readlines()
    startHere = (count+1)-int(numLines)
    for i in range(startHere, count+1):
        print(lines[i])

# find all timestamps
if option == '-t' or option == '--timestamps':
    print("These are the lines from the file that contain timestamps: ")
    lines = txt.readlines()
    for i in range(0, count):
        #if re.match('\d{2}:\d{2}:\d{2}', lines[i]):
        # The previous line has the limitation that it only shows true if the timestamp is at the beginning of line
        if re.search('\d{2}:\d{2}:\d{2}', lines[i]):
            print("At line: %i" % i)
            print(lines[i])


if option == '-i' or option == '--ipv4':
    print("These are the lines from the file that contain an IPv4 address: ")
    lines = txt.readlines()
    pattern = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"
    for i in range(0, count):
        if re.search(pattern, lines[i]):
            print("At line: %i" % i)
            print(lines[i])

if option == '-I' or option == '--ipv6':
    print("These are the lines from the file that contain an IPv6 address: ")
    lines = txt.readlines()
    pattern = r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}| ([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:) {1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
    for i in range(0, count):
        if re.search(pattern, lines[i]):
            print("At line: %i" % i)
            print(lines[i])


# Close the file after all usage
txt.close()
