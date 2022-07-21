import sys
import argparse
import os
import getpass

def start(username):
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--install", metavar="<package_name>", help = "AUR package installer")
    parser.add_argument("-u", "--update", metavar="<package_name>", help = "Updates package and rebuilds it as well. Requires the program to not be running.")

    args = parser.parse_args()

    if args.install:
        installer(package=args.install, username=username)
    elif args.update:
        updater(package=args.update, username=username)

def installer(package, username):
    os.system(f"git -C /home/{username}/AURa clone https://aur.archlinux.org/{package}.git")
    os.chdir(f"/home/{username}/AURa/{package}")
    os.system("makepkg -sri")

def updater(package, username):
    os.chdir(f"/home/{username}/AURa/{package}")
    os.system("git pull")
    os.system("makepkg -sri")

def initializer(username):
    if os.path.isdir(f"/home/{username}/AURa"):
        return
    else:
        os.chdir(f"/home/{username}/")
        os.system(f"mkdir AURa")

if __name__ == "__main__":
    username = getpass.getuser()
    initializer(username)
    start(username)