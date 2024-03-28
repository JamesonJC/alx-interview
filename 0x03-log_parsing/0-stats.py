#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    parts = line.strip().split()
    if len(parts) < 9:
        return None, None
    try:
        file_size = int(parts[-1])
        status_code = int(parts[-2])
    except ValueError:
        return None, None
    return file_size, status_code


def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            if file_size is None or status_code is None:
                continue
            total_size += file_size
            status_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
