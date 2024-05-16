#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys
from collections import defaultdict

def parse_line(line):
    try:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            return status_code, file_size
    except (IndexError, ValueError):
        pass
    return None, None

def main():
    status_counts = defaultdict(int)
    total_file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None:
                status_counts[status_code] += 1
                total_file_size += file_size
                line_count += 1

                if line_count % 10 == 0:
                    print(f"Total file size: File size: {total_file_size}")
                    for code in sorted(status_counts.keys()):
                        if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                            print(f"{code}: {status_counts[code]}")
                    print()

    except KeyboardInterrupt:
        print("\nKeyboard interruption detected. Printing final statistics:")
        print(f"Total file size: File size: {total_file_size}")
        for code in sorted(status_counts.keys()):
            if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                print(f"{code}: {status_counts[code]}")

if __name__ == "__main__":
    main()