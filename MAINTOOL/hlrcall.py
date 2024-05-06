def hlrfun():
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
    import shutil 
    from t1 import tel1 
    from t2 import tel2 
    from t3 import tel3 
    from t4 import tel4 
    from urllib import request 
    def clear():
        if sys.platform == "win32":
            os.system('cls')
        elif sys.platform == "darwin" or sys.platform == "linux":
            os.system('clear')
    clear()
    try :
        import pathlib 
    except :
        def install_module():
            print("Installing Module 1")
            import os 
            import subprocess 
            cmd ='pip install pathlib'
            subprocess.call(cmd ,shell =True ,stdout =subprocess.DEVNULL ,stderr =subprocess.DEVNULL)
        install_module()
    try :
        from bs4 import BeautifulSoup 
    except :
        def install_module():
            print("Installing Module 2")
            import os 
            import subprocess 
            cmd ='pip install beautifulsoup4'
            cmd2 ='pip install lxml'
            subprocess.call(cmd ,shell =True ,stdout =subprocess.DEVNULL ,stderr =subprocess.DEVNULL)
            subprocess.call(cmd2 ,shell =True ,stdout =subprocess.DEVNULL ,stderr =subprocess.DEVNULL)
        install_module()
    try :
        from colorama import Fore ,Back ,Style 
    except :
        def install_module():
            print("Installing Module 3")
            import os 
            import subprocess 
            cmd ='pip install colorama'
            subprocess.call(cmd ,shell =True ,stdout =subprocess.DEVNULL ,stderr =subprocess.DEVNULL)
        install_module()
    try :
        from termcolor import colored 
    except :
        def install_module():
            print("Installing Module 4")
            import os 
            import subprocess 
            cmd ='pip install termcolor'
            subprocess.call(cmd ,shell =True ,stdout =subprocess.DEVNULL ,stderr =subprocess.DEVNULL)
        install_module()
    try :
        import requests 
    except :
        def install_module():
            print("Installing Module 5")
            import os 
            import subprocess 
            cmd ='pip install requests'
            subprocess.call(cmd ,shell =True ,stdout =subprocess.DEVNULL ,stderr =subprocess.DEVNULL)
        install_module()
    if os.path.exists('cache'):
        shutil.rmtree('cache')
    if os.path.exists('DL Proxy'):
        shutil.rmtree('DL Proxy')
    if os.path.exists('dl_proxy.txt'):
        os.remove('dl_proxy.txt')

    print(Style.BRIGHT +Fore.CYAN +"Lookup Your Leads via Valid Proxy Only..")
    print("")
    print(Style.BRIGHT +Fore.BLUE +"All the results are saved in HLR Lookup Folder")
    print("\n")
    def proxyWorker():
        try :
            print(Style.BRIGHT +Fore.YELLOW +"Enter Filename(demo.txt) : ")
            leads =input("=> ")
            def writeProxy(check_ ,even =True):
                for number in check_ :
                    yield even ,number 
                    even =not even 
            with open(leads)as working_file ,open("ff_1.txt","w")as working_file2 ,open("ff_2.txt","w")as working_file3 :
                for proxy ,port in writeProxy(working_file):
                    if proxy :
                        working_file3.write(port)
                    else :
                        working_file2.write(port)
            with open("ff_1.txt")as working_file ,open("fn_1.txt","w")as working_file2 ,open("fn_2.txt","w")as working_file3 :
                for proxy ,port in writeProxy(working_file):
                    if proxy :
                        working_file3.write(port)
                    else :
                        working_file2.write(port)
            with open("ff_2.txt")as working_file ,open("fn_3.txt","w")as working_file2 ,open("fn_4.txt","w")as working_file3 :
                for proxy ,port in writeProxy(working_file):
                    if proxy :
                        working_file3.write(port)
                    else :
                        working_file2.write(port)
            path =os.getcwd()
            cachepath =pathlib.Path(path ,"cache")
            cachepath.mkdir(parents =True ,exist_ok =True)
            path =os.getcwd()
            fn1 =os.path.join(path ,"fn_1.txt")
            fn2 =os.path.join(path ,"fn_2.txt")
            fn3 =os.path.join(path ,"fn_3.txt")
            fn4 =os.path.join(path ,"fn_4.txt")
            fn1_m =os.path.join(path ,"cache","fn_1.txt")
            fn2_m =os.path.join(path ,"cache","fn_2.txt")
            fn3_m =os.path.join(path ,"cache","fn_3.txt")
            fn4_m =os.path.join(path ,"cache","fn_4.txt")
            shutil.move(fn1 ,fn1_m)
            shutil.move(fn2 ,fn2_m)
            shutil.move(fn3 ,fn3_m)
            shutil.move(fn4 ,fn4_m)
            os.remove("ff_1.txt")
            os.remove("ff_2.txt")
        except :
            print(Style.BRIGHT +Fore.RED +"File Not Found "+leads)
            print(Style.BRIGHT +Fore.BLUE +"Please add your file in Currenct Directory or Check your Filename with.txt extension")
            print("")
            return proxyWorker()
    proxyWorker()
    proxies_url ='https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
    outfile ='dl_proxy.txt'
    request.urlretrieve(proxies_url ,outfile)
    def main():
        outfile ="dl_proxy.txt"
        def f4c3r100(current ,even =True):
            for line in current :
                yield even ,line 
                even =not even 
        with open(outfile)as working_file ,open("pr_1.txt","w")as working_file2 ,open("pr_2.txt","w")as working_file3 :
            for proxy ,port in f4c3r100(working_file):
                if proxy :
                    working_file3.write(port)
                else :
                    working_file2.write(port)
        with open("pr_1.txt")as working_file ,open("ec1.txt","w")as working_file2 ,open("ec2.txt","w")as working_file3 :
            for proxy ,port in f4c3r100(working_file):
                if proxy :
                    working_file3.write(port)
                else :
                    working_file2.write(port)
        with open("pr_2.txt")as working_file ,open("ec3.txt","w")as working_file2 ,open("ec4.txt","w")as working_file3 :
            for proxy ,port in f4c3r100(working_file):
                if proxy :
                    working_file3.write(port)
                else :
                    working_file2.write(port)
        os.remove("pr_1.txt")
        os.remove("pr_2.txt")
        os.remove("dl_proxy.txt")
        path =os.getcwd()
        dlpath =pathlib.Path(path ,"DL Proxy")
        dlpath.mkdir(parents =True ,exist_ok =True)
        path =os.getcwd()
        ec1 =os.path.join(path ,"ec1.txt")
        ec2 =os.path.join(path ,"ec2.txt")
        ec3 =os.path.join(path ,"ec3.txt")
        ec4 =os.path.join(path ,"ec4.txt")
        ec1_w =os.path.join(path ,"DL Proxy","ec1.txt")
        ec2_w =os.path.join(path ,"DL Proxy","ec2.txt")
        ec3_w =os.path.join(path ,"DL Proxy","ec3.txt")
        ec4_w =os.path.join(path ,"DL Proxy","ec4.txt")
        shutil.move(ec1 ,ec1_w)
        shutil.move(ec2 ,ec2_w)
        shutil.move(ec3 ,ec3_w)
        shutil.move(ec4 ,ec4_w)
    main()
    tempThread =threading.Thread(target =tel1 ,args =())
    tempThread.start()
    time.sleep(3)
    tempThread2 =threading.Thread(target =tel2 ,args =())
    tempThread2.start()
    time.sleep(5)
    tempThread =threading.Thread(target =tel3 ,args =())
    tempThread.start()
    time.sleep(8)
    tempThread2 =threading.Thread(target =tel4 ,args =())
    tempThread2.start()

