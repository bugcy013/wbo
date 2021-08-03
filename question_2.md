**Simple Grep program**
* help page
```
wbo  ➜ python3 SimpleGrep.py -h
usage: SimpleGrep.py [-h] [-f FILE] [-a AFTER_LINE_NO] [-b BEFORE_LINE_NO] [-s SEARCH_STR]

Simple Grep

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE
  -a AFTER_LINE_NO, --after_line_no AFTER_LINE_NO
  -b BEFORE_LINE_NO, --before_line_no BEFORE_LINE_NO
  -s SEARCH_STR, --search_str SEARCH_STR
wbo  ➜
```
* Failure handling
```
wbo  ➜ python3 SimpleGrep.py -f ucd_templates.csv -a 10 -b 20 -s "False"
CRITICAL  | 2021-08-03 08:24:47,425 | search     | Unable to locate the file, so exiting file = ucd_templates.csv
wbo  ➜
```
```
wbo  ➜ python3 SimpleGrep.py -f /Users/dhanasekaran/Downloads/report-5l3Kuj8Bv-run-z69621ijz.csv -a 20 -b 10 -s "Hello"
CRITICAL  | 2021-08-03 08:27:17,043 | search     | Not a valid range for grep 'before_line_no' = 10 and 'after_line_no' = 20, 'search_str' = Hello
wbo  ➜
```