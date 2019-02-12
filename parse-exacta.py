#!/usr/bin/env python3

import sys
import fileinput

def add_to_record(r, s):
    """Adds string s to record string r.
    Returns new record string and true if s ends with ```
    """
    end = s[-4:-1]
    return (r+s, end=='```')


def extract_record_number(s):
    """Gets number from s

    Example
            For s=='EX Pool Final: 2925'
            Return==2925
    """
    colon = s.find(':')
    return s[colon+1:].strip()


def write_record(r, index):
    nl = r.find('\n')
    nr = extract_record_number(r[:nl])
    
    r = r[nl+1:]                  # Remove header
    lines = r.splitlines()
    lines_last_index = len(lines)

    for i, line in enumerate(lines):
        line.strip()

        # Get the index of missing value
        gi = line.find(':')
        gap = int(line[:gi])

        line = line[gi+1:]
        values = line.split()
        values_last_index = len(values)

        print("KKS,%s,%s," % (index, nr), end='')
        for j, value in enumerate(values):
            if j == gap-1:
                print('-', end='')
            else:
                print(value, end='')

            if j < values_last_index-1:
                print(',', end='')

        if j < lines_last_index-1:
            print()

    print('```')
    

def main():
    input_record = ""
    index = 0

    for line in fileinput.input():
        (input_record, full) = add_to_record(input_record, line)
        if full:
            index += 1
            write_record(input_record, index)
            input_record = ""



if __name__== "__main__":
  main()
