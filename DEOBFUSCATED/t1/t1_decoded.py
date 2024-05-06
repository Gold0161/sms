import requests 
import json 
import sys 
import requests ,sys 
import os ,time 
from itertools import islice 
import threading 
from bs4 import BeautifulSoup 
import pathlib 
from colorama import init 
from termcolor import colored 
from colorama import Fore ,Back ,Style 
init(autoreset =True)
from prx import prxgen 
def tel1():
    proxy_file =open("./cache/"+"fn_1.txt","r")
    path =os.getcwd()
    hlr_lookup =pathlib.Path(path ,"HLR Lookup")
    hlr_lookup.mkdir(parents =True ,exist_ok =True)
    def lookUp():
        proxyfile =open("./DL Proxy/"+"ec1.txt","r")
        while True :
            proxy =proxyfile.readline()
            if not proxy :
                proxyfile.close()
                time.sleep(1)
                print("Please Wait..Generating Proxy")
                prxgen()
                time.sleep(20)
                return lookUp()
            try :
                proxy =f'http://{proxy}'
                ip_url ='https://ipecho.net/plain/'
                ipCheck =requests.get(ip_url ,proxies ={"http":proxy ,"https":proxy },timeout =3)
                time.sleep(0.5)
                ipAddr =requests.get(ip_url ,proxies ={"http":proxy ,"https":proxy },timeout =3)
                print(Style.BRIGHT +Fore.GREEN +"Valid Proxy Address : ",ipAddr.text)
                for i in range(10):
                    proxy =proxy_file.readline()
                    if not proxy :
                        abort =input("Enter : ")
                        break 
                    ip_url =f'https://api.telnyx.com/anonymous/v2/number_lookup/{proxy}'
                    response =requests.get(ip_url)
                    result =response.json()
                    print(Style.BRIGHT +Fore.YELLOW +result ['data']['carrier']['name'])
                    carrier =result ['data']['carrier']['name']
                    carriername =result ['data']['carrier']['name']
                    if not carrier =="":
                        carrierFile =carriername +".txt"
                        directory = str(hlr_lookup)+"/"+str(carrierFile)
                        workingFile =open(directory ,"a")
                        workingFile.writelines(proxy)
                        workingFile.close()
                    elif carrier =="":
                        Invalid ="Invalid_numbers.txt"
                        directory = str(hlr_lookup)+"/"+str(Invalid)
                        workingFile =open(directory ,"a")
                        workingFile.writelines(proxy)
                        workingFile.close()
                    else :
                        print("Invalid Number")
            except :
                print(Style.BRIGHT +Fore.RED +"Invalid Proxy "+proxy)
    lookUp()

