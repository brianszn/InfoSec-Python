import hashlib
try:
    import colorama
    from colorama import Fore as color
except:
    print(" \nImport Colorama lib")
import os
import argparse 
import sys
os.system("cls||clear")

ban = """
 ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ███╗   ██╗██╗████████╗ █████╗ 
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗████╗  ██║██║╚══██╔══╝██╔══██╗
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██╔██╗ ██║██║   ██║   ███████║
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██║╚██╗██║██║   ██║   ██╔══██║
╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║ ╚████║██║   ██║   ██║  ██║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝
 
 ► Coded 4Study by: br6dsk                                 Slow, but efficient
 ► Github: github.com/br6dsk                               be patient :)
 ► Decode with BruteForce && Encode to HASH
 ► Cryptonita.py --help for the options
"""
print(color.GREEN, f"{ban}")
parser = argparse.ArgumentParser()
parser.add_argument("--md5", action="store", help='Decode HASH MD5')
parser.add_argument("--sha1", action="store", help='Decode HASH SHA1')
parser.add_argument("--sha256", action="store", help='Decode HASH SHA256')
parser.add_argument("--sha512", action="store", help='Decode HASH SHA512')
parser.add_argument("--encode", action='store')
argument = parser.parse_args()

def not_found():
    print(" \n[+] ► {} Password Not Found!".format(color.RED))
    f = input(color.GREEN + " \n[+] ► PRESS [ENTER] TO EXIT")
    exit()
def crack_md5():
    hash_md5 = sys.argv[2]
    print(f" \n[+] ► MD5 Hash: {hash_md5}")
    wlist = input(" \n[+] ► Insert your Wordlist: ")
    read_file = open(wlist, "r", encoding="utf-8", errors="ignore").readlines()
    for lines in range(0, len(read_file)):
        cracked_md5 = hashlib.md5(read_file[lines].replace("\n", "").encode()).hexdigest()
        if hash_md5 == cracked_md5:
            print(open(wlist, 'r'))
            print(" \n[+] ► Decoded! Password: {} {}".format(color.RED, read_file[lines].replace("\n", "")))
            f = input(color.GREEN +" \n[+] ► PRESS [ENTER] TO EXIT")
            exit()
    not_found()
def crack_sha1():
    hash_sha1 = sys.argv[2]
    print(f" \n[+] ► sha1 Hash: {hash_sha1}")
    wlist = input(" \n[+] ► Insert your Wordlist: ")
    read_file = open(wlist, "r", encoding="utf-8", errors="ignore").readlines()
    for lines in range(0, len(read_file)):
        cracked_sha1 = hashlib.sha1(read_file[lines].replace("\n", "").encode()).hexdigest()
        if hash_sha1 == cracked_sha1:
            print(" \n[+] ► Decoded! Password:{} {}".format(color.RED, read_file[lines].replace("\n", "")))
            f = input(color.GREEN +" \n[+] ► PRESS [ENTER] TO EXIT")
            exit()
    not_found()
def crack_sha256():
    hash_sha256 = sys.argv[2]
    print(f" \n[+] ► sha256 Hash: {hash_sha256}")
    wlist = input(" \n[+] ► Insert your Wordlist: ")
    read_file = open(wlist, "r", encoding="utf-8", errors="ignore").readlines()
    for lines in range(0, len(read_file)):
        cracked_sha256 = hashlib.sha256(read_file[lines].replace("\n", "").encode()).hexdigest()
        if hash_sha256 == cracked_sha256:
            print(" \n[+] ► Decoded! Password: {} {}".format(color.RED, read_file[lines].replace("\n", "")))
            f = input(color.GREEN +" \n[+] ► PRESS [ENTER] TO EXIT")
            exit()
    not_found()
def crack_sha512():
    hash_sha512 = sys.argv[2]
    print(f" \n[+] ► sha512 Hash: {hash_sha512}")
    wlist = input(" \n[+] ► Insert your Wordlist: ")
    read_file = open(wlist, "r", encoding="utf-8", errors="ignore").readlines()
    for lines in range(0, len(read_file)):
        cracked_sha512 = hashlib.sha512(read_file[lines].replace("\n", "").encode()).hexdigest()
        if hash_sha512 == cracked_sha512:
            print(" \n[+] ► Decoded! Password: {} {}".format(color.RED, read_file[lines].replace("\n", "")))
            f = input(color.GREEN +" \n[+] ► PRESS [ENTER] TO EXIT")
            exit()
    not_found()
if argument.md5:
    crack_md5()
elif argument.sha1:
    crack_sha1()
elif argument.sha256:
    crack_sha256()
elif argument.sha512:
    crack_sha512()
def encode():
    to_hash = sys.argv[2]
    cracked = hashlib.md5(to_hash.encode()).hexdigest()
    array_encode = [hashlib.md5(to_hash.encode()).hexdigest(), hashlib.sha1(to_hash.encode()).hexdigest(), hashlib.sha256(to_hash.encode()).hexdigest(), hashlib.sha512(to_hash.encode()).hexdigest()]
    for i in range(0, len(array_encode)):
        if array_encode[i] == array_encode[0]:
            print("[+] ► MD5! Hash: {}".format(array_encode[i]))
        if array_encode[i] == array_encode[1]:
            print("[+] ► SHA1! Hash: {}".format(array_encode[i]))
        if array_encode[i] == array_encode[2]:
            print("[+] ► SHA256! Hash: {}".format(array_encode[i]))
        if array_encode[i] == array_encode[3]:
            print("[+] ► SHA512! Hash: {}".format(array_encode[i])) 
    wait = input(" \n[+] ► PRESS [ENTER] TO EXIT")
if argument.encode:
    encode()  
