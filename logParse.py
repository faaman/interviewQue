#!/usr/bin/python3

# A Python CLI application that will parse logs of various kinds
# A test suite must be included
# hij: use regex module
# do not use the 'head', 'tail' or 'grep' utilities
# Usage: ./logParse.py [OPTION]... [FILE]
# options needed: -h
# options needed: -f (--first NUM, Print first NUM lines) - if this is chosen, NUM is mandatory?
# options needed: -l (--last NUM, Print last NUM lines)
# options needed: -t (--timestamps, Print lines that contain a timestamp in HH:MM:SS format)
# options needed: -i (--ipv4, Print lines that contain an IPv4 address, matching IPs are highlighted)
# options needed: -I (--ipv6, Print lines that contain an IPv6 address, std notation, matching IPs are highlighted)
# If FILE is omitted, standard input is used instead


from sys import argv
import re
import datetime

totalArgs = len(argv)
numLines = 0
optionList = []
count = 0
script = argv[0]

i = 1
for k in range(0, totalArgs - 2):
    optionList.append(argv[i])
    i = i+1

########################

# find out total number of lines in file, if file does not exist, get standard input from user
def catchingNoFiles():
    try:
        filename = argv[totalArgs - 1]
        with open(filename, 'r') as fp:
            for count, line in enumerate(fp):
                pass
        print('Total Lines', count + 1)
        return filename, count
    except FileNotFoundError:
        print("There is no valid file mentioned.")
        linesCmd = input("How many lines of text would you like to input? ")
        target = open('standardIpText.txt', 'w')
        line1 = input("Input line: ")
        target.write(line1)
        for li in range(1, int(linesCmd)):
            line1 = input("Input line: ")
            target.write("\n")
            target.write(line1)
        target.close()
        count = int(linesCmd) - 1
        filename = 'standardIpText.txt'
        print('Total Lines', int(count) + 1)
        return filename, count


# a loop for all the options the user has

for i in range(0, totalArgs-2):

    # help option - a bit of a duct tape approach
    if optionList[i] == '-h' or optionList[i] == '--help':
        helpTxt = open("/home/fati/PycharmProjects/pythonTau/venv/redHatQue/help.txt")
        print(helpTxt.read())
        helpTxt.close()

    # first lines option
    if optionList[i] == '-f' or optionList[i] == '--first':
        filename, count = catchingNoFiles()
        txt = open(filename)
        # the below is an abrupt ending
        if int(count) < int(optionList[i+1]):
            exit()
        try:
            if int(optionList[i+1]) >= 0 or int(optionList[i+1]) <= count:
                numLines = optionList[i+1]
            else:
                numLines = 0
        except IndexError:
            numLines = 0
        except ValueError:
            numLines = 0
        print("These are the first", int(numLines), "lines from the file: ")
        lines = txt.readlines()
        for j in range(0, int(numLines)):
            print(lines[j])
        txt.close()

    # last lines option
    if optionList[i] == '-l' or optionList[i] == '--last':
        filename, count = catchingNoFiles()
        txt = open(filename)
        # the below is an abrupt ending
        if int(count) < int(optionList[i+1]):
            exit()
        try:
            if int(optionList[i+1]) >= 0 or int(optionList[i+1]) <= count:
                numLines = optionList[i+1]
            else:
                numLines = 0
        except IndexError:
            numLines = 0
        except ValueError:
            numLines = 0
        print("These are the last", int(numLines), "lines from the file: ")
        lines = txt.readlines()
        startHere = int(count)+1 - int(numLines)
        for j in range(startHere, int(count)+1):
            print(lines[j])
        txt.close()

    # find all timestamps
    if optionList[i] == '-t' or optionList[i] == '--timestamps':
        filename, count = catchingNoFiles()
        txt = open(filename)
        print("These are the lines from the file that contain timestamps: ")
        lines = txt.readlines()
        for m in range(0, int(count)+1):
            if re.search('\d{2}:\d{2}:\d{2}', lines[m]):
                try:
                    myDate = re.findall('\d{2}:\d{2}:\d{2}', lines[m])
                    strDate = str(myDate)

                    splitTime = strDate.split(':')
                    tempHr = re.findall('\d{2}', splitTime[0])
                    tempMi = re.findall('\d{2}', splitTime[1])
                    tempSe = re.findall('\d{2}', splitTime[2])

                    if (int(tempHr[0])) >= 0 and (int(tempHr[0])) <= 24:
                        if (int(tempMi[0])) >= 0 and (int(tempMi[0])) <= 59:
                            if (int(tempSe[0])) >= 0 and (int(tempSe[0])) <= 59:
                                print("At line: ", m+1)
                                print(lines[m])

                except ValueError:
                    pass
                except IndexError:
                    pass
        txt.close()


    if optionList[i] == '-i' or optionList[i] == '--ipv4':
        filename, count = catchingNoFiles()
        txt = open(filename)
        print("These are the lines from the file that contain an IPv4 address: ")
        lines = txt.readlines()
        pattern = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"
        for j in range(0, int(count)+1):
            if re.search(pattern, lines[j]):
                print("At line: ", j+1)
                print(lines[j])
        txt.close()

    if optionList[i] == '-I' or optionList[i] == '--ipv6':
        filename, count = catchingNoFiles()
        txt = open(filename)
        print("These are the lines from the file that contain an IPv6 address: ")
        lines = txt.readlines()
        pattern = r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}| ([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:) {1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
        for j in range(0, int(count)+1):
            if re.search(pattern, lines[j]):
                print("At line: ", j+1)
                print(lines[j])
        txt.close()
