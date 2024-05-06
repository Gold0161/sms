#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import init 
from termcolor import colored 
from colorama import Fore ,Back ,Style 
import time, os, sys

def clear():
    if sys.platform == "win32":
        os.system('cls')
    elif sys.platform == "darwin" or sys.platform == "linux":
        os.system('clear')

def typing(banner):
    for letter in banner :
        print(Style.BRIGHT +Fore.GREEN +letter ,end ='',flush =True)
        time.sleep(.16)
def loop():
    banner =(Style.BRIGHT +Fore.YELLOW +'We are the Mastering of Dark Code, Our Dark Leads Bot can generate all US Banking Leads.')
    print(banner)
    print('')
    banner ='\tDEOBFUSCATED BY @F4C3R100'
    print('''
\033[37;1m
      NO!                          MNO!
     MNO!!      \033[34m[\033[32mSCARLETTA\033[34m]       \033[37mMNNOO!
   MMNO!                           MNNOO!!
 MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!
 !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!
       ! MMMMMMMMMMMMMPPPPOOOOIII! !
        MMMMMMMMMMMMPPPPPOOOOOOII!!
        MMMMMOOOOOOPPPPPPPPOOOOMII!
        MMMMM..    OPPMMP    .,OMI!
        MMMM::   \033[34mo\033[37m.,OPMP,.\033[34mo\033[37m   ::I!!
          NNM:::.,,OOPM!P,.::::!!
         MMNNNNNOOOOPMO!!IIPPO!!O!
         MMMMMNNNNOO:!!:!!IPPPPOO!
          MMMMMNNOOMMNNIIIPPPOO!!
             MMMONNMMNNNIIIOO!
           MN MOMMMNNNIIIIIO! OO
          MNO! IiiiiiiiiiiiI OOOO
     NNN.MNO!   O\033[35m!!!!!!!!!\033[37mO   OONO NO!
    MNNNNNO!    OOOOOOOOOOO    MMNNON!
      MNNNNO!    PPPPPPPPP    MMNON!
         OO!                   ON!

        \033[32;1mDeobfuscated by @f4c3r100

\033[31;1;5mBiggest Scammer Bitch :\033[0;37m @xMarvel_official , @xMarvel_admin\033[0m
\033[31;1mDox Of xMarvel : \033[32mhttps://doxbin.org/upload/xMarvelAdminDox\033[0m
    '''
   )
    typing(banner)
    print('')
clear()
loop()

print("")
print(Style.BRIGHT +Fore.CYAN +"Select Option")
print("")
print(Style.BRIGHT +Fore.GREEN +"1. \033[37mDark Leads Bot")
print(Style.BRIGHT +Fore.GREEN +"2. \033[37mHLR Validation")
print("\n")
print(Style.BRIGHT +Fore.BLUE +"Enter Option :\033[33m ")
opts =input("=> ")
if opts =="1":
    from dl import evilleads 
    evilleads()
elif opts =="2":
    from hlrcall import hlrfun 
    hlrfun()
else :
    print(Style.BRIGHT +Fore.RED +"Wrong option")
    time.sleep(5)