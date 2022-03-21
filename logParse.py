#!/usr/bin/python3

# current issues: cat log file -> cat test_0.log | ./util.py --first 10
# A test suite must be included
# do not use the 'head', 'tail' or 'grep' utilities

import sys
import argparse
import re
# import datetime (this could have been used)


# find out total number of lines in file, if file does not exist, get standard input from user
def catching_no_files(parser):
    try:
        found_file = parser.parse_args().filename
        with open(found_file, 'r') as fp:
            for count_file_lines, line in enumerate(fp):
                pass
        print('Total Lines', count_file_lines + 1)
        return found_file, count_file_lines
    except TypeError:
        print("There is no valid file mentioned, standard input will be used instead.")
        print("Note: If multiple options are chosen, user will be asked to input text individually for each option.")
        lines_cmd = input("How many lines of text would you like to input? ")
        target = open('standardIpText.txt', 'w')
        line1 = input("Input line: ")
        target.write(line1)
        try:
            for li in range(1, int(lines_cmd)):
                line1 = input("Input line: ")
                target.write("\n")
                target.write(line1)
            target.close()
            count_std_lines = int(lines_cmd) - 1
            new_file = 'standardIpText.txt'
            print('Total Lines', int(count_std_lines) + 1)
            return new_file, count_std_lines
        except ValueError:
            print("Not a valid range, program exiting.")
            exit()


def first_lines(filename, count, numLines):
    txt = open(filename)
    print("These are the first", int(numLines), "lines from the file: ")
    lines = txt.readlines()
    for j in range(0, int(numLines)):
        print(lines[j])
    txt.close()


def last_lines(filename, count, numLines, startHere):
    txt = open(filename)
    print("These are the last", int(numLines), "lines from the file: ")
    lines = txt.readlines()
    for j in range(startHere, int(count) + 1):
        print(lines[j])
    txt.close()


def find_timestamps(filename, count):
    txt = open(filename)

    print("These are the lines from the file that contain timestamps: ")
    lines = txt.readlines()
    for m in range(0, int(count) + 1):
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
                            print("At line: ", m + 1)
                            print(lines[m])

            except ValueError:
                pass
            except IndexError:
                pass
    txt.close()


def find_ipv4(filename, count):
    txt = open(filename)
    print("These are the lines from the file that contain an IPv4 address: ")
    lines = txt.readlines()
    pattern = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"
    for j in range(0, int(count)+1):
        if re.search(pattern, lines[j]):
            print("At line: ", j+1)
            print(lines[j])
    txt.close()


def find_ipv6(filename, count):
    txt = open(filename)
    print("These are the lines from the file that contain an IPv6 address: ")
    lines = txt.readlines()
    pattern = r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}| ([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:) {1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
    for j in range(0, int(count) + 1):
        if re.search(pattern, lines[j]):
            print("At line: ", j + 1)
            print(lines[j])
    txt.close()


def main():
    import argparse
    parser = argparse.ArgumentParser(description='A Python CLI application that will parse logs of various kinds')
    parser.add_argument('-f', '--first', nargs=1, default=0, help="Print first NUM lines")
    parser.add_argument('-l', '--last', nargs=1, default=0, help="Print last NUM lines")
    parser.add_argument('-t', '--timestamps', action='store_true',
                        help="Print lines that contain a timestamp in HH:MM:SS format")
    parser.add_argument('-i', '--ipv4', action='store_true',
                        help="Print lines that contain an IPv4 address, matching IPs are highlighted")
    parser.add_argument('-I', '--ipv6', action='store_true',
                        help="Print lines that contain an IPv6 address, std notation, matching IPs are highlighted")
    parser.add_argument('--filename', help="Input a filename. If FILE is omitted, standard input is used")
    parser.parse_args()

    goodfile, countlines = catching_no_files(parser)

    if parser.parse_args().first != 0:
        numLines = int(parser.parse_args().first[0])
        if int(countlines) < numLines:
            numLines = countlines + 1
            print("There are only", numLines, "lines in the file, and so.. ")
        first_lines(goodfile, countlines, numLines)

    if parser.parse_args().last != 0:
        numLines = int(parser.parse_args().last[0])
        if int(countlines) < numLines:
            startHere = 0
        else:
            startHere = int(countlines) + 1 - int(numLines)
        last_lines(goodfile, countlines, numLines, startHere)

    if parser.parse_args().timestamps != 0:
        find_timestamps(goodfile, countlines)

    if parser.parse_args().ipv4 != 0:
        find_ipv4(goodfile, countlines)

    if parser.parse_args().ipv6 != 0:
        find_ipv6(goodfile, countlines)


if __name__ == '__main__':
    sys.exit(main())
