import requests as r
import os as s
try:

    import colorama
    from colorama import Fore as color
except:
    print('Install colorama lib: pip install colorama')
import sys, argparse
s.system('cls' if s.name == 'nt' else 'reset')
x = r"""
                ,----------------,              ,---------,
            ,-----------------------,          ,"        ,"|
          ,"                      ,"|        ,"        ,"  |
         +-----------------------+  |      ,"        ,"    |
         |  .-----------------.  |  |     +---------+      |
         |  |                 |  |  |     | -==----'|      |
         |  |  Hacker Target  |  |  |     |         |      |
         |  |  API            |  |  |/----|`---=    |      |
         |  |  List           |  |  |   ,/|==== ooo |      ;
         |  |  Subdomains !   |  |  |  // |(((( [33]|    ,"
         |  `-----------------'  |," .;'| |((((     |  ,"
         +-----------------------+  ;;  | |         |,"         
            /_)______________(_/  //'   | +---------+           
       ___________________________/___  `,                      
      /  oooooooooooooooo  .o.  oooo /,   \,"-----------
     / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
    /_==__==========__==_ooo__ooo=_/'   /___________,"
    `-----------------------------'

    Use VPN, LIMITED API!
    Usage: python3 scan.py -v ufrj.br    (VHOSTS) (IP'S AUTO SAVE FILE.TXT)
    Usage: python3 scan.py -r ufrj.br    (REVERSE IP LOKUUP)

    u g0t it? ;)

"""
print(x)
try:
        
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", action="store", help='To find vhosts')
    parser.add_argument("-r", action="store", help='To reverse IP lookup')
    argument = parser.parse_args()
    if sys.argv[2].startswith('http://') or sys.argv[2].startswith('https://'):
        print('[MSG] ~: NO HTTP/HTTPS')
        exit()
        
    try:
        print(color.GREEN+'\n[+] ~ Wait...\n')
        try:
            if r.get(f'http://www.{sys.argv[2]}').status_code == 200:
                print(color.GREEN+f'[+] ~ URL: http://www.{sys.argv[2]} [ON]')
        except:
            pass
        try:
            if r.get(f'http://{sys.argv[2]}').status_code == 200:
                print(color.GREEN+f'[+] ~ URL: http://{sys.argv[2]} [ON]')
        except:
            pass
        try:
            if r.get(f'https://{sys.argv[2]}').status_code == 200:
                print(color.GREEN+f'[+] ~ URL: https://{sys.argv[2]} [ON]')
        except:
            pass
        try:
            if r.get(f'https://www.{sys.argv[2]}').status_code == 200:
                print(color.GREEN+f'[+] ~ URL: https://www.{sys.argv[2]} [ON]')
        except:
            pass
            
    except:
        print(color.RED+'\n[+] ~ Website OFFLINE\n[+] ~ Exit... ')
        exit()
    
    def reverseiplookup():
        ht = r.get(f"http://api.hackertarget.com/reverseiplookup/?q={sys.argv[2]}").text
        ht = ht.split()
        for i in range(len(ht)):
            print(color.GREEN+f'[+] ~ Site: '+color.WHITE+f'{ht[i]}\n')
        print(color.YELLOW+f'\n[+] ~ DOMAINS FOUND: [{int(i)}]')
        
    def hostsearch():
        global ht
        ht = f"http://api.hackertarget.com/hostsearch/?q={sys.argv[2]}"
    def filter_config():
        global req
        global count
        req = req.replace(',', ' ')
        req = req.split()
        count = 0
        while count < len(req):
            print(color.GREEN+f'[+] ~ Site: '+color.WHITE+ f'{req[count]}')
            print(color.GREEN+f'[+] ~ IP: '+color.WHITE+f'{req[count+1]}\n')
            file = open(f'ips.{sys.argv[2]}.txt', 'a')
            write = file.writelines(f'{req[count+1]}\n')
            
            count = count + 2
            
        print(color.YELLOW+f'[+] ~ DOMAINS FOUND: [{int(count/2)}]')
        print(color.YELLOW+f'[+] ~ IPS SAVED IN: ips.{sys.argv[2]}.txt')       
    
    if argument.v:
        hostsearch()
        req = (r.get(ht).text)
        filter_config()

        
    if argument.r:
        reverseiplookup()
    
except:
    pass 
 
