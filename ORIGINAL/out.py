import requests #line:1
import json #line:2
import sys #line:3
import requests ,sys #line:4
import os ,time #line:5
from itertools import islice #line:6
import threading #line:7
from bs4 import BeautifulSoup #line:8
import pathlib #line:9
from colorama import init #line:10
from termcolor import colored #line:11
from colorama import Fore ,Back ,Style #line:12
init (autoreset =True )#line:13
from prx import prxgen #line:14
def tel1 ():#line:16
    OO00000O0OO0O0O00 =open ("./cache/"+"fn_1.txt","r")#line:19
    OO0OOO000OO0OOO0O =os .getcwd ()#line:20
    OO0O0000OOO0O000O =pathlib .Path (OO0OOO000OO0OOO0O ,"HLR Lookup")#line:21
    OO0O0000OOO0O000O .mkdir (parents =True ,exist_ok =True )#line:22
    def O0000O0OOOO000O00 ():#line:26
        O0OO000000O0O0OOO =open ("./DL Proxy/"+"ec1.txt","r")#line:28
        while True :#line:30
            OOOOOO0OOOO00OOOO =O0OO000000O0O0OOO .readline ()#line:31
            if not OOOOOO0OOOO00OOOO :#line:33
                O0OO000000O0O0OOO .close ()#line:34
                time .sleep (1 )#line:35
                print ("Please Wait..Generating Proxy")#line:36
                prxgen ()#line:37
                time .sleep (20 )#line:38
                return O0000O0OOOO000O00 ()#line:39
            try :#line:42
                OOO0O0000O0O00OO0 =f
http://{OOOOOO0OOOO00OOOO}'#line:44
                OOO0OO0OOO0O0O00O ='https://ipecho.net/plain/'#line:45
                O0O000O000O0OO00O =requests .get (OOO0OO0OOO0O0O00O ,proxies ={"http":OOO0O0000O0O00OO0 ,"https":OOO0O0000O0O00OO0 },timeout =3 )#line:47
                time .sleep (0.5 )#line:48
                OOO00OO000O0000O0 =requests .get (OOO0OO0OOO0O0O00O ,proxies ={"http":OOO0O0000O0O00OO0 ,"https":OOO0O0000O0O00OO0 },timeout =3 )#line:49
                print (Style .BRIGHT +Fore .GREEN +"Valid Proxy Address : ",OOO00OO000O0000O0 .text )#line:50
                for O000OO0O0O000000O in range (10 ):#line:52
                    OOOO0O000000O000O =OO00000O0OO0O0O00 .readline ()#line:53
                    if not OOOO0O000000O000O :#line:56
                        OO0OO000O0O0OOO0O =input ("Enter : ")#line:58
                        OO0OO000O0O0OOO0O =input ("Enter : ")#line:59
                        break #line:60
                    OOO0OO0OOO0O0O00O =f'https://api.telnyx.com/anonymous/v2/number_lookup/{OOOO0O000000O000O}'#line:62
                    OO0OO0OO00OO0O0O0 =requests .get (OOO0OO0OOO0O0O00O )#line:63
                    OOOO00O0OOOOO0OO0 =OO0OO0OO00OO0O0O0 .json ()#line:64
                    print (Style .BRIGHT +Fore .YELLOW +OOOO00O0OOOOO0OO0 ['data']['carrier']['name'])#line:66
                    OOOO0OOOOO0OO0O0O =OOOO00O0OOOOO0OO0 ['data']['carrier']['name']#line:68
                    O00O0O00000000O00 =OOOO00O0OOOOO0OO0 ['data']['carrier']['name']#line:69
                    if not OOOO0OOOOO0OO0O0O =="":#line:71
                        O0O000O0OO0OO00O0 =O00O0O00000000O00 +".txt"#line:72
                        O0O0000O000O0O0OO =OO0O0000OOO0O000O /O0O000O0OO0OO00O0 #line:73
                        OOO0OO0OO0000O000 =open (O0O0000O000O0O0OO ,"a")#line:74
                        OOO0OO0OO0000O000 .writelines (OOOO0O000000O000O )#line:75
                        OOO0OO0OO0000O000 .close ()#line:76
                    elif OOOO0OOOOO0OO0O0O =="":#line:78
                        OOOO0O000O0O00O0O ="Invalid_numbers.txt"#line:79
                        O0O0000O000O0O0OO =OO0O0000OOO0O000O /OOOO0O000O0O00O0O #line:80
                        OOO0OO0OO0000O000 =open (O0O0000O000O0O0OO ,"a")#line:81
                        OOO0OO0OO0000O000 .writelines (OOOO0O000000O000O )#line:82
                        OOO0OO0OO0000O000 .close ()#line:83
                    else :#line:85
                        print ("Invalid Number")#line:86
            except :#line:88
                print (Style .BRIGHT +Fore .RED +"Invalid Proxy "+OOOOOO0OOOO00OOOO )#line:89
    O0000O0OOOO000O00 ()#line:92

