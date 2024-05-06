import os ,time ,sys ,subprocess,shutil, pathlib

def prxgen():
    if os.path.exists('DL Proxy'):
        shutil.rmtree('DL Proxy')
    time.sleep(1)
    url ='https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
    outfile ='dl_proxy.txt'
    request.urlretrieve(url ,outfile)
    time.sleep(1)
    outfile ="dl_proxy.txt"
    def writeProxy(check_ ,even =True):
        for number in check_ :
            yield even ,number 
            even =not even 
    with open(outfile)as working_file ,open("pr_1.txt","w")as working_file2 ,open("pr_2.txt","w")as working_file3 :
        for LINE ,current_line in writeProxy(working_file):
            if LINE :
                working_file3.write(current_line)
            else :
                working_file2.write(current_line)
    with open("pr_1.txt")as working_file ,open("ec1.txt","w")as working_file2 ,open("ec2.txt","w")as working_file3 :
        for LINE ,current_line in writeProxy(working_file):
            if LINE :
                working_file3.write(current_line)
            else :
                working_file2.write(current_line)
    with open("pr_2.txt")as working_file ,open("ec3.txt","w")as working_file2 ,open("ec4.txt","w")as working_file3 :
        for LINE ,current_line in writeProxy(working_file):
            if LINE :
                working_file3.write(current_line)
            else :
                working_file2.write(current_line)
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

#prxgen()