#!/usr/bin/python3
"""Module that reads stdin line by line and computes metrics"""
import stat
import sys


total_size = 0
status_codes = {}
line_count = 0

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 2:
        continue
    status = parts[-2]
    try:
        size = int(parts[-1])
    except ValueError:
        continue
    total_size += size
    if status not in status_codes:
        status_codes[status] = 0
    status_codes[status] += 1
    line_count += 1
    if line_count % 10 == 0:
        print("File size: {}".format(total_size))
        for code in sorted(status_codes):
            print("{}: {}".format(code, status_codes[code]))
