#!/usr/bin/env python3

import sys
import fileinput


#  Read whole file.
#    with open('data.txt', 'r') as myfile:
#        data=myfile.read().replace('\n', '')

def add_to_record(r, s):
    """Adds string s to record string r.
    Returns new record string and true if s ends with ```
    """
    end = s[-4:-1]
    return (r+s, end=='```')


def write_record(r):
    print(r)

def main():
    inr = ""                    # input record

    for line in fileinput.input():
        (inr, full) = add_to_record(inr, line)
        if full:
            write_record(inr)
            inr = ""



if __name__== "__main__":
  main()
