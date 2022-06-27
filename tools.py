from socket import *
from colorama import *
def importantports():
    list = [21,22,23,25,53,67,68,80,88,
            110,137,139,143,161,162,389,
            443,520,546,547,587,902,993,
            995,1433,1434,1701,1723,3389,
            6129,1090,8080,3306,2121,2222,
            554,8291,2000,1080,445,2082
            ]
    ip = input(Fore.GREEN+"Enter IP:  ")
    for port in list:
        s =socket(AF_INET ,SOCK_STREAM)
        resualt = s.connect_ex((ip , port))
        if resualt == 0:
            print(Fore.GREEN+"port open: ",port)
def allport():
    list1 = range(1,65535)
    ip = input(Fore.GREEN+"Enter IP:  ")
    for port in list1:
        s =socket(AF_INET ,SOCK_STREAM)
        resualt = s.connect_ex((ip , port))
        if resualt == 0:
            print(Fore.GREEN+"port open: ",port)
        else:
            print(Fore.RED+"Port closed: ",port)
def banner():
    print(Fore.GREEN+"#"*50)
    print(Fore.GREEN+"#"*5+" "*40+"#"*5)
    print(Fore.GREEN+"#"*5+" "*10+Fore.YELLOW+"Important Port Scanner"+ " "*8+Fore.GREEN+"#"*5)
    print(Fore.GREEN+"#"*5+" "*10+Fore.YELLOW+"All Port Scanner"+" "*14+Fore.GREEN+"#"*5)
    print(Fore.GREEN+"#"*5+" "*40+"#"*5)
    print(Fore.GREEN+"#"*5+" "*6+Fore.RED+"Insta ID: "+Fore.BLUE+"@parham_.habibi"+ " "*9+Fore.GREEN+"#"*5)
    print(Fore.GREEN+"#"*5+" "*40+"#"*5)
    print(Fore.GREEN+"#"*50)
    print(" "*50)
banner()
print(Fore.BLUE+"Enter"+Fore.RED+" 1"+Fore.BLUE+" :"+Fore.GREEN+"Important ports")
print(Fore.BLUE+"Enter"+Fore.RED+" 2"+Fore.BLUE+" :"+Fore.GREEN+"All Port Scan")
print("-"* 40)
a = input(Fore.BLUE+'Enter : ')
if a == "1":
    importantports()
elif a == "2":
    allport()
else:
    print("Error! Try again")



