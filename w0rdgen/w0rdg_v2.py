from colorama import Fore as color
import itertools, argparse, sys, time, os
from tqdm import tqdm
banner = """

██╗    ██╗ ██████╗ ██████╗ ██████╗  ██████╗ 
██║    ██║██╔═████╗██╔══██╗██╔══██╗██╔════╝ 
██║ █╗ ██║██║██╔██║██████╔╝██║  ██║██║  ███╗
██║███╗██║████╔╝██║██╔══██╗██║  ██║██║   ██║   Wordlist generator
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝	Based in Keywords.
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ 
                                            

 ► Coded 4Study by: br6dsk
 ► Github: github.com/br6dsk
 ► Use: w0rdg.py --threads 10 --keywords "keyword1 keyword2..." --columns COLUMNS
 ► Ex: w0rdg.py --threads 10 --keywords "love pass 1 2 3" --columns 4

"""
os.system('cls' if os.name == 'nt' else 'clear')
print(color.YELLOW + banner)
parser = argparse.ArgumentParser()
parser.add_argument("--keywords", action='store', help='Help us')
parser.add_argument("--columns", type=int, action='store', help='Keyword columns')
parser.add_argument("--threads", type = int, help = "Multithreading", required=True)
argument = parser.parse_args()
def gerar_keyword():
	keyword = sys.argv[4]
	array = keyword.split()
	quant = len(array)
	print(f" \n[☼] ► Keywords [☼]: {array} == {quant} ")
	print(f"[☼] ► WARNING: Column > {quant} == Error")
	print("[☼] ► Wait a moment... ")
	get = []
	for combinacao in itertools.permutations(array,int(sys.argv[6])):
		juntou = ''.join(combinacao)
		get.append(juntou)
		not_array_number = []
	print(color.RED +"\n")
	for i in tqdm(range(0, len(get))):
		if not get[i].isdigit():
			not_array_number.append(get[i])		
		file = open('wordlist.txt', 'a')
	write = file.writelines("\n".join(not_array_number))
	print(color.YELLOW +" \n[+] Finished [+]")
	print(color.YELLOW + " \n[+] ► File saved as: wordlist.txt")
if argument.keywords:
	gerar_keyword()
