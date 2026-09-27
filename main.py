import requests
from colorama import Fore, Style
import os
import random
import string
import sys
import time

# Read example usernames from file
def read_example_usernames(file_path="examplenames.txt"):
    with open(file_path, "r") as file:
        return file.read().splitlines()

# Username generation function
def generate_username(min_length=4, max_length=15):
    characters = string.ascii_letters + string.digits
    username_length = random.randint(min_length, max_length)
    username = ''.join(random.choice(characters) for _ in range(username_length))
    return username

# Generate a random username by mashing together examples
def generate_mashed_username(usernames, min_length=4, max_length=15):
    random.shuffle(usernames)
    mashed_username = ''.join(usernames[:2])  # Combine two usernames
    mashed_username = mashed_username[:max_length]  # Ensure max length
    mashed_username = mashed_username.replace(' ', '')  # Remove spaces
    return mashed_username

# Validate a single username using the Roblox API
def validate_username(username):
    url = f"https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:  # Username is valid and available
            return f"{Fore.GREEN}Valid: {username}{Style.RESET_ALL}"
        elif data['code'] == 1:
            return f"{Fore.RED}Invalid: {username} (already in use){Style.RESET_ALL}"
        elif data['code'] == 2:
            return f"{Fore.RED}Invalid: {username} (not appropriate for Roblox){Style.RESET_ALL}"
        elif data['code'] == 10:
            return f"{Fore.YELLOW}Invalid: {username} (might contain private information){Style.RESET_ALL}"
    else:
        return f"{Fore.RED}Unable to access Roblox API{Style.RESET_ALL}"

# Save valid username to a file
def save_valid_username(username):
    filename = "valid.txt"  # Save all valid usernames in a single file
    with open(filename, 'a') as file:
        file.write(username + '\n')

# Developer Info
def show_developer_info():
    print(f"\n{Fore.CYAN}Thank you to jprocks101 for the base idea and concept!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}This script was expanded and improved by Void with additional features such as random username generation, improved handling, and better user interface.{Style.RESET_ALL}")
    print(f"{Fore.GREEN}This is a forked version of 1.0, with significant changes and improvements leading to the release of 2.0.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Old Version (1.0): https://github.com/jprocks101/Roblox-Username-Checker{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}New Version (2.0): https://github.com/VVoiddd/Roblox-Username-Checker{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Follow Void at: https://www.twitch.tv/voidedluvr{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Check out Void's other projects at: https://github.com/VoidedLuvr{Style.RESET_ALL}")
    print("\n")
    input(f"{Fore.MAGENTA}[{Fore.RESET}Press Enter to return to the menu{Fore.MAGENTA}]{Fore.RESET}")  # Wait for user to press Enter

# Progress bar function
def update_progress_bar(iteration, total, bar_length=50):
    progress = (iteration / total)
    arrow = '=' * int(round(progress * bar_length) - 1)
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f"\r[{arrow}{spaces}] {int(progress * 100)}%")
    sys.stdout.flush()

# Remove duplicates from list
def remove_duplicates(usernames):
    seen = set()
    unique_usernames = []
    for username in usernames:
        if username not in seen:
            unique_usernames.append(username)
            seen.add(username)
    return unique_usernames

# Main function to handle user choices
while True:
    print()
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
    print(f"{Fore.BLUE}██   ██  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████      ██    ██     ██████      ██████  ")
    print(f" ██ ██  ██      ██   ██ ██      ██      ██  ██  ██      ██   ██     ██    ██          ██    ██  ████ ")
    print(f"  ███   ██      ███████ █████   ██      █████   █████   ██████      ██    ██      █████     ██ ██ ██ ")
    print(f" ██ ██  ██      ██   ██ ██      ██      ██  ██  ██      ██   ██      ██  ██      ██         ████  ██ ")
    print(f"██   ██  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██       ████       ███████ ██  ██████  {Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}                    Developed   By   Caleb/888  {Style.RESET_ALL}\n")
    
    print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Choose an option:")
    print(f"{Fore.MAGENTA}[{Fore.RESET}1{Fore.MAGENTA}]{Fore.RESET} Manually enter a username")
    print(f"{Fore.MAGENTA}[{Fore.RESET}2{Fore.MAGENTA}]{Fore.RESET} Check a list of usernames from a file")
    print(f"{Fore.MAGENTA}[{Fore.RESET}3{Fore.MAGENTA}]{Fore.RESET} Generate random usernames")
    print(f"{Fore.MAGENTA}[{Fore.RESET}4{Fore.MAGENTA}]{Fore.RESET} Generate mashed-up username from examples")
    print(f"{Fore.MAGENTA}[{Fore.RESET}5{Fore.MAGENTA}]{Fore.RESET} Developer Info")
    print(f"{Fore.MAGENTA}[{Fore.RESET}0{Fore.MAGENTA}]{Fore.RESET} Exit")
    choice = input(f"{Fore.MAGENTA}[{Fore.RESET}>{Fore.MAGENTA}]{Fore.RESET} ")

    if choice == '1':
        username = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter a username: ")
        result = validate_username(username)
        print(result)
    elif choice == '2':
        filename = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter the filename of the usernames file (must include .txt): ")
        
        # Read usernames from file and show loading progress
        with open(filename, "r") as file:
            usernames = file.read().splitlines()
        
        print(f"{Fore.CYAN}Done! {len(usernames)} Amount of Usernames Loaded{Style.RESET_ALL}")

        # Check for duplicates
        duplicate_usernames = [username for username in usernames if usernames.count(username) > 1]
        if duplicate_usernames:
            print(f"{Fore.YELLOW}Oh No! We've Detected Duped Usernames! Would You Like the Application To Remove Them? (y/n){Style.RESET_ALL}")
            user_response = input(f"{Fore.MAGENTA}[{Fore.RESET}>{Fore.MAGENTA}]{Fore.RESET} ")
            if user_response.lower() == 'y':
                usernames = remove_duplicates(usernames)
                print(f"{Fore.GREEN}Duplicates have been removed.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Dupes were not removed.{Style.RESET_ALL}")
        
        valid_usernames = 0
        invalid_usernames = 0

        # Validate usernames and update progress bar
        for i, username in enumerate(usernames):
            result = validate_username(username)
            print(f"\r{result}", end="")
            if "Valid" in result:
                valid_usernames += 1
                save_valid_username(username)  # Save valid usernames to the file
            else:
                invalid_usernames += 1
            update_progress_bar(i + 1, len(usernames))  # Update the progress bar
            time.sleep(0.1)  # Optional delay for demonstration

        print(f"\n{Fore.GREEN}Valid Usernames: {valid_usernames}{Style.RESET_ALL}")
        print(f"{Fore.RED}Invalid Usernames: {invalid_usernames}{Style.RESET_ALL}")
    
    elif choice == '3':
        min_len = int(input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter the minimum length for the username (4-15): "))
        max_len = int(input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter the maximum length for the username (4-15): "))

        if 4 <= min_len <= 15 and 4 <= max_len <= 15 and min_len <= max_len:
            num_usernames = int(input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} How many usernames would you like to generate? "))
            valid_usernames = []
            invalid_usernames = []

            for _ in range(num_usernames):
                generated_username = generate_username(min_len, max_len)
                print(f"{Fore.CYAN}Generated Username: {generated_username}{Style.RESET_ALL}")
                
                result = validate_username(generated_username)
                print(result)

                if "Valid" in result:
                    valid_usernames.append(generated_username)
                    save_valid_username(generated_username)
                else:
                    invalid_usernames.append(generated_username)

            print(f"\n{Fore.GREEN}Usernames Generated: {num_usernames}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Valid Usernames: {len(valid_usernames)}{Style.RESET_ALL}")
            print(f"{Fore.RED}Invalid Usernames: {len(invalid_usernames)}{Style.RESET_ALL}")
            for username in invalid_usernames:
                print(f"Invalid: {username} (already in use)")

        else:
            print(f"{Fore.RED}Invalid length. Please enter values between 4 and 15 for both min and max length.{Style.RESET_ALL}")
    
    elif choice == '4':
        # Load example usernames and show progress bar
        usernames = read_example_usernames()
        print(f"{Fore.CYAN}Loaded {len(usernames)} example usernames!{Style.RESET_ALL}")
        num_usernames = int(input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} How many mashed-up usernames would you like to generate? "))
        
        print(f"\n{Fore.CYAN}Generating mashed-up usernames...{Style.RESET_ALL}")
        for i in range(num_usernames):
            mashed_username = generate_mashed_username(usernames)
            result = validate_username(mashed_username)
            print(f"{Fore.CYAN}Mashed-up Username: {mashed_username} - {result}{Style.RESET_ALL}")
            time.sleep(0.5)  # Optional delay for visual effect
            
    elif choice == '5':
        show_developer_info()
    elif choice == '0':
        break
    else:
        print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")
