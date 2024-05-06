import requests 
import json 
import sys 
import os ,time 
from itertools import islice 
import threading 
from bs4 import BeautifulSoup 
import pathlib 
from colorama import init 
from termcolor import colored 
from colorama import Fore ,Back ,Style 
init(autoreset =True)
def tel2():
    leads_file =open("./cache/"+"fn_2.txt","r")
    path =os.getcwd()
    hlr_lookup =pathlib.Path(path ,"HLR Lookup")
    hlr_lookup.mkdir(parents =True ,exist_ok =True)
    def lookUp():
        proxy_file =open("./DL Proxy/"+"ec2.txt","r")
        while True:
            proxy =proxy_file.readline()
            if not proxy:
                proxy_file.close()
                time.sleep(26)
                return lookUp()
            try:
                proxy =f'http://{proxy}'.strip()
                ip_url ='https://ipecho.net/plain/'
                ipCheck =requests.get(ip_url ,proxies ={"http":proxy ,"https":proxy },timeout =3)
                time.sleep(0.5)
                ipAddr =requests.get(ip_url ,proxies ={"http":proxy ,"https":proxy },timeout =3)
                print(f"\033[34;1m[\033[32m+\033[34m] \033[37mValid Proxy Address: \033[32m{ipAddr.text}\033[0m")
                for i in range(15):
                    number =leads_file.readline()
                    if not number:
                        break
                    number = number.strip() 
                    ip_url =f'https://api.telnyx.com/anonymous/v2/number_lookup/{number}'
                    response =requests.get(ip_url)
                    if response.status_code == 429 or response.text == '':
                        Invalid ="Invalid_numbers.txt"
                        directory =hlr_lookup+"/"+Invalid 
                        workingFile =open(directory ,"a")
                        workingFile.writelines(number)
                        workingFile.close()
                        break
                    elif response.status_code == 200:
                        result =response.json()
                        print(f"\033[34;1m[\033[32m+\033[34m] \033[37mVALIDATED LEAD \033[34m| \033[32m{number} \033[34m| \033[32m{result['data']['carrier']['name']}\033[0m")
                        carrier =result ['data']['carrier']['name']
                        carriername =result ['data']['carrier']['name']
                        if not carrier =="":
                            carrierFile =carriername +".txt"
                            directory = str(hlr_lookup)+"/"+str(carrierFile) 
                            workingFile =open(directory ,"a")
                            workingFile.writelines(number)
                            workingFile.close()
                        elif carrier =="":
                            Invalid ="Invalid_numbers.txt"
                            directory = str(hlr_lookup)+"/"+str(Invalid) 
                            workingFile =open(directory ,"a")
                            workingFile.writelines(number)
                            workingFile.close()
                        else:
                            #print("Invalid Number")
                            pass
            except:
               print(f"\033[34;1m[\033[31m!\033[34m] \033[37mInvalid Proxy Address\033[0m")
    lookUp()

