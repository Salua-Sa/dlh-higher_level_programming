#!/usr/bin/python3
"""Module that reads stdin line by line and computes metrics"""
import sys


def main():
    """Read log lines from stdin and print status codes"""
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
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
        if status in status_codes:
            status_codes[status] += 1
        line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    main()
