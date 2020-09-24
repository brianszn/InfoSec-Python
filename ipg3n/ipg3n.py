try:
    from colorama import Fore as color
except:
    print("\nImport Colorama: pip3 install colorama")
try:
    import random, socket
except:
    print("\nImport Socket: pip3 install socket")
import sys, os
os.system('clear')
banner = r"""

88                          ad888888b,
""                         d8"     "88
                                   a8P
88 8b,dPPYba,   ,adPPYb,d8      aad8"  8b,dPPYba,
88 88P'    "8a a8"    `Y88      ""Y8,  88P'   `"8a
88 88       d8 8b       88         "8b 88       88    Real ip Generator
88 88b,   ,a8" "8a,   ,d88 Y8,     a88 88       88    with open port.
88 88`YbbdP"'   `"YbbdP"Y8  "Y888888P' 88       88   [slow but eficient]
   88           aa,    ,88                               g00d luck :)
   88            "Y8bbdP"

Coded 4Study by: br6dsk
Github: github.com/br6dsk
Usage: python3 ipg3n.py <quantity of ip's to test> <port>
"""
print(color.GREEN + banner)
ip = "0.0.0.0"
try:
    quant = sys.argv[1]
    port = sys.argv[2]
    print(color.YELLOW + f'Quantity to generate: [{quant}]')
except:
    print("Example: python3 ipg3n.py 50 8080\n")
    exit()
array = ip.split('.')
ip_list = []
for z in range(int(quant)):
    array[0] = random.randint(10,255)
    array[1] = random.randint(0,255)
    array[2] = random.randint(0,255)
    array[3] = random.randint(0,255)
    p = f"{array[0]}.{array[1]}.{array[2]}.{array[3]}"
    ip_list.append(p)
print('\n')
ip_list[0] = '127.0.0.1'
c = 0
while c < len(ip_list):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if(sock.connect_ex((ip_list[c], int(port)))):
        print(color.RED + f'[{port}] : [CLOSED]             ' + ip_list[c])

    else:
        print(color.GREEN + f'[{port}] : [OPEN]               ' + color.WHITE + ip_list[c])
        file = open('open.txt', 'a')
        write = file.writelines(f'[{port}] : [OPEN]               ' + ip_list[c] + '\n')
    c+=1
    sock.close()
print(color.YELLOW + '\nFile saved as open.txt')
print(color.YELLOW + '\n[FINISH!]')
#br 
