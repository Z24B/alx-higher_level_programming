#!/usr/bin/python3
"""File with script that reads stdin line by line and computes metrics"""


import sys

# Dictionary to store counts of status codes
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        # Split the line into parts using whitespace as delimiter
        parts = line.strip().split()
        # Extract file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Update line count
        line_count += 1

        # If 10 lines have been read, print the metrics
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    # Print the metrics when CTRL + C is pressed
    print(f"Total file size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
