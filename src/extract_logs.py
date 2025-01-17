import os
import argparse
import subprocess

def fetch_logs_for_date(url, date, output_file):

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Stream logs from the URL using curl
    curl_command = ["curl", url]
    matching_lines = 0

    with subprocess.Popen(curl_command, stdout=subprocess.PIPE, text=True) as process, open(output_file, "w") as output:
        for line in process.stdout:
            print(line)
            if date in line:  # Match the date (YYYY-MM-DD) at the start of the line
                output.write(line)
                matching_lines += 1

    if matching_lines > 0:
        print(f"Logs for {date} have been saved to {output_file}. ({matching_lines} lines)")
    else:
        print(f"No logs found for {date}.")


parser = argparse.ArgumentParser(description="Retrieve logs for a specific date.")
parser.add_argument("date", type=str)
parser.add_argument("url", type=str)
parser.add_argument("--output", type=str, default="output.txt")

args = parser.parse_args()

fetch_logs_for_date(args.url, args.date, args.output)
