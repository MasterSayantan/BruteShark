import os 
import sys
import time
import random
import subprocess


if sys.version_info < (3, 0):
    print("This script requires Python 3.")
    sys.exit(1)


try:
    from rich.console import Console
    from rich.table import Table
    from rich.box import SIMPLE_HEAVY
    from colorama import Fore
except ImportError as e:
    print(f"Error: {e}. Please install the required modules using:")
    print("pip install -r requirements.txt")
    sys.exit(1)

console = Console()

def clearScr():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = r""" 
 ____             _         ____  _   _    _    ____  _  __
| __ ) _ __ _   _| |_ ___  / ___|| | | |  / \  |  _ \| |/ /
|  _ \| '__| | | | __/ _ \ \___ \| |_| | / _ \ | |_) | ' / 
| |_) | |  | |_| | ||  __/  ___) |  _  |/ ___ \|  _ <| . \ 
|____/|_|   \__,_|\__\___| |____/|_| |_/_/   \_\_| \_\_|\_\

|----------------------------------------------------------------------------|
| Created By: Sayantan Saha                                                  |
| Checkout my LinkedIn: https: https://www.linkedin.com/in/mastersayantan/   |
| Lookup at my GitHub Account : https://github.com/MasterSayantan            |
|----------------------------------------------------------------------------|
    """

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

def display_table():
    table = Table(box=SIMPLE_HEAVY)

    table.add_column("Network Tools", justify="left", style="cyan", no_wrap=True)
    table.add_column("Finder Tools", justify="left", style="green", no_wrap=True)

    table.add_row("1. FTP Brute Force", "7. Admin Panel Finder")
    table.add_row("2. LDAP Brute Force", "8. Directory Finder")
    table.add_row("3. SSH Brute Force", "9. Subdomain Finder")
    table.add_row("4. Telnet Brute Force", "")
    table.add_row("5. WiFi Brute Force", "")
    table.add_row("6. RDP Brute Force", "")

    table.add_row("", "", "")
    table.add_row("", "[bold red]-" * 15 + " 00. EXIT " + "-" * 15 + "[/bold red]", "", end_section=True)
    console.print(table)

def execute_script(script_name):
    """Executes the script based on the user's choice."""
    script_path = os.path.join("files", script_name)
    
    if os.path.isfile(script_path):
        if os.name == 'nt':  
            subprocess.call(['python', script_path])
        else:  
            subprocess.call(['python3', script_path])
    else:
        print(Fore.RED + f"Script {script_name} not found in 'files' directory.")

def main():
    clearScr()
    logo()
    display_table()

    tools_mapping = {
        '1': 'ftp_bruteforce.py',
        '2': 'ldap_bruteforce.py',
        '3': 'ssh_bruteforce.py',
        '4': 'telnet_bruteforce.py',
        '5': 'wifi_bruteforce.py',
        '6': 'rdp_bruteforce.py',
        '7': 'admin_panel_finder.py',
        '8': 'directory_finder.py',
        '9': 'subdomain_finder.py',
        '00': 'exitBruteShark',
    }

    try:
        BruteShark = input("root@BruteShark:~# ")
        clearScr()

        if BruteShark in tools_mapping:
            if BruteShark == '00':
                print('\033[97m\nClosing BruteShark\nPlease Wait...\033[1;m')
                time.sleep(2)
                sys.exit()
            else:
                execute_script(tools_mapping[BruteShark])
        else:
            print("Invalid Input!")
    except KeyboardInterrupt:
        print('\033[97m\nScript interrupted by user.\033[1;m')
        sys.exit()

if __name__ == "__main__":
    main()
