#----------------imports----------------------
from passlib.hash import des_crypt,md5_crypt,apr_md5_crypt,bcrypt,sha256_crypt,unix_disabled,scram
import sys,argparse
import time
import datetime
import pyfiglet
from hashid import HashID
#---------------------------------------------

#-----------------------------argparse-----------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Your target  hash",type=str)
parser.add_argument('-w','--wordlist',help="Wordlist path")
parser.add_argument('-m','--method',help="type of hash")
parser.add_argument('-l','--list',help='print list of methods (python3 brute.py -l show)')
args = parser.parse_args()
#------------------------------------------------------------------------

#--------vars---------------
hasher = HashID()
target = args.target
wordlst = args.wordlist
method = args.method
lst = args.list
lst_hashtype = ["des","md5","MD5-Apache(apr)","bcrypt","sha256","unix-disabled","scram"]
hello_text = pyfiglet.figlet_format("Bruter")
results = hasher.identifyHash(target)
#---------------------------
def crack(target,wordlist):
    print(hello_text)
    print(f"        dev 0.1  by rmdm   happy cracking :)")
    print("-"*40)
    print(f"Target Hash:{target}")
    print("-"*40)
    try:
        with open(wordlist,"r",encoding="UTF-8",errors="ignore") as f:
            for count,line in enumerate(f,1):
                passwd = line.strip()
                print(f"Checked:{passwd}\n")
                if method is None:
                    for m in results:
                        print(f"Name: {m.name}")
                        return False
                if method=="apr":
                    if apr_md5_crypt.verify(passwd,target):
                         print(f"Pass Found:{line}")
                         return True
                elif method=="bcrypt":
                    if bcrypt.verify(passwd,target):
                        print(f"Pass Found:{line}")
                        return True
                elif method=="sha256":
                    if sha256_crypt.verify(passwd,target):
                        print(f"Pass Found: {line}")
                        return True
                elif method=="unix-disabled":
                    if unix_disabled.verify(passwd,target):
                        print(f"Pass Found:{line}")
                        return True
                elif method=="md5":
                    if md5_crypt.verify(passwd,target):
                        print(f"Pass Found {line}")
                        return True
                elif method=="des":
                    if des_crypt.verify(passwd,target):
                        print(f"Pass Found{line}")
                        return True
                elif method=="scram":
                    if scram.verify(passwd,target):
                        print(f"Pass Found{line}")
                        return True

    except FileNotFoundError:
        print("File not found")
    
    print("Pass Not found,try different wordlist")
    return False
#------------------------------------------------
def choosefunc():
    if lst=="show":
        for i in lst_hashtype:
            print(i)
    else:
        crack(target,wordlst)
choosefunc()

