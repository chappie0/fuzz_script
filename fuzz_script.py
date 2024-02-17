import subprocess
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Run wfuzz with different wordlists.')
parser.add_argument('--url', type=str, required=True, help='The URL to fuzz')
args = parser.parse_args()

# URL provided by the user
url = args.url

# List of wfuzz commands with different wordlists
commands = [
    "wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404,301,403,302 {}/FUZZ",
    "wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/CGIs.txt --hc 404,301,403,302 {}/FUZZ",
    "wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/dsstorewordlist.txt --hc 404,301,403,302 {}/FUZZ",
    "wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/Common-DB-Backups.txt --hc 404,301,403,302 {}/FUZZ",
    "wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/Common-PHP-Filenames.txt --hc 404,301,403,302 {}/FUZZ",
    "wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/quickhits.txt --hc 404,301,403,302 {}/FUZZ",
    "wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/ror.txt --hc 404,301,403,302 {}/FUZZ",
    "wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/RobotsDisallowed-Top1000.txt --hc 404,301,403,302 {}/FUZZ",
    "wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/Randomfiles.fuzz.txt --hc 404,301,403,302 {}/FUZZ"
]

# Execute each command
for command in commands:
    formatted_command = command.format(url)
    subprocess.run(formatted_command, shell=True)
