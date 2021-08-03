#!/usr/bin/env python

import os
import sys
import logging

level = "INFO"
logging.basicConfig(level=level, format="%(levelname)-10s| %(asctime)-10s | %(funcName)-10s | %(message)s")


class Grep:
    def __init__(self, before_line_no, after_line_no, search_str, file):
        self.before_line_no = before_line_no
        self.after_line_no = after_line_no
        self.search_str = search_str
        self.file = file
        self.line_range = list(range(self.after_line_no, self.before_line_no))

    def search(self):
        """
        Search for the given string in file and return lines containing that string,
        along with line numbers
        """
        line_number = 0
        list_of_results = []
        # Open the file in read only mode
        if not os.path.isfile(self.file):
            logging.critical("Unable to locate the file, so exiting file = %s", self.file)
            sys.exit(1)
        if not self.line_range:
            logging.critical("Not a valid range for grep 'before_line_no' = %s and 'after_line_no' = %s,"
                             " 'search_str' = %s", self.before_line_no, self.after_line_no, self.search_str)
            sys.exit(1)
        logging.critical("let's start grep the str 'before_line_no' = %s and 'after_line_no' = %s and 'search_str' = %s",
                         self.before_line_no, self.after_line_no, self.search_str)

        with open(self.file, 'r') as read_obj:
            # Read all lines in the file one by one
            for line in read_obj:
                # For each line, check if line contains the string
                line_number += 1
                if line_number in self.line_range:
                    if self.search_str in line:
                        # If yes, then add the line number & line as a tuple in the list
                        list_of_results.append((line_number, line.rstrip()))

        # Return list of tuples containing line numbers and lines where string is found
        return list_of_results


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Simple Grep')
    parser.add_argument('-f', '--file', type=str)
    parser.add_argument('-a', '--after_line_no', type=int)
    parser.add_argument('-b', '--before_line_no', type=int)
    parser.add_argument('-s', '--search_str', type=str)
    args = parser.parse_args()
    x = Grep(
        before_line_no=args.before_line_no,
        after_line_no=args.after_line_no,
        search_str=args.search_str,
        file=args.file
    )
    print(x.search())