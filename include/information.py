from requests import get , exceptions
from time import sleep
from socket import socket , gethostbyname
from os import system
from bs4 import BeautifulSoup
try:
    import nmap
except:
    system("pip install python-nmap")
try:
    import whois
except:
    system("pip install whois")
from .display import red,lblu,grn,ylw,lred,end,clear
#______________________________________________________
List = ['robots.txt','search/','admin/','login/','sitemap.xml','sitemap2.xml','config.php','wp-login.php','log.txt','update.php','INSTALL.pgsql.txt','user/login/','INSTALL.txt','profiles/','scripts/','LICENSE.txt','CHANGELOG.txt','themes/','inculdes/','misc/','user/logout/','user/register/','cron.php','filter/tips/','comment/reply/','xmlrpc.php','modules/','install.php','MAINTAINERS.txt','user/password/','node/add/','INSTALL.sqlite.txt','UPGRADE.txt','INSTALL.mysql.txt']
#______________________________________________________
def Admin():

    clear()
    print(f"\n {red}✹ {grn}Enter WebSite Address")
    try:
        url = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()

    file = open('include/AdminList.txt' , 'r')
    List = file.read().splitlines()
    file.close()        

    if "http" in url:
        url = (url+"/") 
    elif "https" in url:                
        url = (url+"/") 
    else:
        url = ('http://'+url+"/")    


    for i in List:
        URL = url+i
        try:
            r = get(URL)
        except exceptions.ConnectionError:
            print(f"{lblu}[{ylw}!{lblu}] {red}Check Your Internet connection {ylw}!")
            exit()
        if r.status_code == 200:
            print(f' {grn}{URL} {lblu}➜ {grn}Found') 
        else:
            print(f' {red}{URL} {lblu}➜ {red}Not Found') 

#______________________________________________________
def dnslookup():
    clear()
    print(f"\n {red}✹ {grn}Enter WebSite Address")
    try:       
        inp =  input(f"\n{red}❯❯{lblu} ")
    except:
        exit()
    try:
        result = get(f'http://api.hackertarget.com/dnslookup/?q={inp}').text
    except exceptions.ConnectionError:
        print(f"{lblu}[{ylw}!{lblu}] {red}Check Your Internet connection {ylw}!")
        exit()
    print(f"\n{red}──────────────{ylw}[ DNS Lookup ]{red}───────────────")
    print(f'{grn}{result}')
    print(f"{red}──────────────────────────────────────────────\n")

#______________________________________________________
def robots():
    clear()
    print(f"\n {red}✹ {grn}Enter WebSite Address")
    try:
        url = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()
    
    if 'http' in url:
        pass
    elif 'http' != url:
        url = ('http://'+url)
    print('\n')

    for i in List:
        ur = (url+"/"+i)

        try:
            reqs = get(ur)
        except exceptions.ConnectionError:
            print(f"{lblu}[{ylw}!{lblu}] {red}Check Your Internet connection {ylw}!")
            exit()

        if reqs.status_code == 200 or reqs.status_code == 405:
            print(f" {ylw}[{grn}✔{ylw}] {grn}{ur}")
        else:
            print(f" {ylw}[{red}✖{ylw}] {red}{ur}")

    
#______________________________________________________

def Cloud():
    
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
    clear()
    print(f"\n {red}✹ {grn}Enter WebSite Address")
    try:
        Domain = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()
    if Domain == "":
        exit()
    for sub in subdom:
        try:
            hosts = str(sub) + "." + str(Domain)
            bypass = gethostbyname(str(hosts))
            print (f" {ylw}[ {grn}{str(bypass)} {lblu}➜ {grn}{str(hosts)} {ylw}]")
        except Exception:
            exit()
#______________________________________________________
def Whois():
    clear()
    print(f"\n {red}✹ {grn}Enter WebSite Address")
    try:
        Domain = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()

    whois_information = whois.whois(Domain)

    print(f"\n{red}──────────────{ylw}[ Whois ]{red}───────────────")
    print(f"""
    {red}┏╼ {grn}DomainName     {ylw}: {lblu}{whois_information.domain_name}
    {red}┣╼ {grn}Registrar      {ylw}: {lblu}{whois_information.registrar}
    {red}┣╼ {grn}WhoisServer    {ylw}: {lblu}{whois_information.whois_server}
    {red}┣╼ {grn}CreationDate   {ylw}: {lblu}{whois_information.creation_date}
    {red}┣╼ {grn}ExpirationDate {ylw}: {lblu}{whois_information.expiration_date}
    {red}┣╼ {grn}UpdatedDate    {ylw}: {lblu}{whois_information.updated_date}
    {red}┣╼ {grn}NameServers    {ylw}: {lblu}{whois_information.name_servers}
    {red}┣╼ {grn}Status         {ylw}: {lblu}{whois_information.status}
    {red}┣╼ {grn}EmailAddresses {ylw}: {lblu}{whois_information.emails}
    {red}┣╼ {grn}Name           {ylw}: {lblu}{whois_information.name}
    {red}┣╼ {grn}Org            {ylw}: {lblu}{whois_information.org}
    {red}┣╼ {grn}Address        {ylw}: {lblu}{whois_information.address}
    {red}┣╼ {grn}City           {ylw}: {lblu}{whois_information.city}
    {red}┣╼ {grn}State          {ylw}: {lblu}{whois_information.state}
    {red}┣╼ {grn}Zipcode        {ylw}: {lblu}{whois_information.zipcode}
    {red}┗╼ {grn}Country        {ylw}: {lblu}{whois_information.country}
""")
    print(f"{red}──────────────────────────────────────────────\n")
            
#______________________________________________________

def findshareddns():
    clear()
    print(f"\n {red}✹ {grn}Enter WebSite Address")
    try:
        Domain = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()
    try:
        result = get(f'https://api.hackertarget.com/findshareddns/?q={Domain}').text
    except exceptions.ConnectionError:
        print(f"{lblu}[{ylw}!{lblu}] {red}Check Your Internet connection {ylw}!")
        exit()

    print(f"\n{red}──────────────{ylw}[ Find Share Ddns ]{red}───────────────")
    print(f'{grn}{result}')
    print(f"{red}──────────────────────────────────────────────\n")

#______________________________________________________
def httpheader():
    clear()
    print(f"\n {red}✹ {grn}Enter WebSite Address")
    try:
        Domain = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()
    try:
        result = get(f'https://api.hackertarget.com/httpheaders/?q={Domain}').text
    except exceptions.ConnectionError:
        print(f"{lblu}[{ylw}!{lblu}] {red}Check Your Internet connection {ylw}!")
        exit()

    print(f"\n{red}──────────────{ylw}[ Http Header ]{red}───────────────")
    print(f'{grn}{result}')
    print(f"{red}──────────────────────────────────────────────\n")

#______________________________________________________

def portscan():

    clear()
    print(f"\n {red}✹ {grn}Enter IP or Domain")
    try:
        Domain = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()
    print(f"\n{red}──────────────{ylw}[ Port Scan ]{red}───────────────\n")

    nm = nmap.PortScanner()
    nm.scan(Domain)

    for host in nm.all_hosts():
        print(f"{red}❰ {lblu}{host} {ylw}- {lblu}{nm[host].hostname()} {red}❱")
        print(f"    {red}┗ {ylw}STATE {lblu}: {grn}{nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f'        {red}┣ {ylw}{proto}'  )

            lport = nm[host][proto]

            print(f"\n{grn}PORT\t{grn}STATE")
            for port in lport:
                print(f"{red}{port}\t{red}{lport[port]['state']}")

    print(f"\n{red}──────────────────────────────────────────────\n")
#______________________________________________________

def Location():
    clear()
    print(f"\n {red}✹ {grn}Enter IP Address")
    try:
        IP = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()
    try:
        result = get(f'http://ip-api.com/json/{IP}').json()
        print(f"""  
    {grn}[{red}+{grn}] {lblu}COUNTRY {red}::: {ylw}{result['country']}
    {grn}[{red}+{grn}] {lblu}COUNTRY CODE {red}::: {ylw}{result['countryCode']}
    {grn}[{red}+{grn}] {lblu}REGION {red}::: {ylw}{result['region']}
    {grn}[{red}+{grn}] {lblu}REGION NAME {red}::: {ylw}{result['regionName']}
    {grn}[{red}+{grn}] {lblu}CITY {red}::: {ylw}{result['city']}
    {grn}[{red}+{grn}] {lblu}ZIP {red}::: {ylw}{result['zip']}
    {grn}[{red}+{grn}] {lblu}LAT {red}::: {ylw}{result['lat']}
    {grn}[{red}+{grn}] {lblu}LON {red}::: {ylw}{result['lon']}
    {grn}[{red}+{grn}] {lblu}TIME ZONE {red}::: {ylw}{result['timezone']}
    {grn}[{red}+{grn}] {lblu}ISP {red}::: {ylw}{result['isp']}
    {grn}[{red}+{grn}] {lblu}ORG {red}::: {ylw}{result['org']}
    {grn}[{red}+{grn}] {lblu}AS {red}::: {ylw}{result['as']}
    {grn}[{red}+{grn}] {lblu}IP {red}::: {ylw}{result['query']}
    {grn}[{red}+{grn}] {lblu}GOOGLE MAP {red}::: {ylw}https://www.google.com/maps/@{result['lat']},{result['lon']},13z
""")
    except exceptions.ConnectionError:
        print(f"{lblu}[{ylw}!{lblu}] {red}Check Your Internet connection {ylw}!")
        exit()
#______________________________________________________
def Full_Lookup():
    clear()
    print(f"\n {red}✹ {grn}Enter WebSite Address")
    try:
        url = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()
    try:
        data = get(f"https://{url}.sitexpired.com/" , headers={
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
            "Referer" : "https://www.sitexpired.com/"
        }).text
        soup = BeautifulSoup(data , "html.parser")
        title = soup.find("p",class_="text-sm-left").text
        Overview = soup.find("p",class_="card-text").text
        time = soup.find("time").text
        HTTP_Header = soup.find("small").text
        Full_Whois = ((str(soup.find("pre")).replace("<br/>" , '\n')).replace("</pre>" , '')).replace("<pre>" , '')
    except AttributeError:
        print("AttributeError !!!")
        exit()
    except exceptions.ConnectionError:
        print(f"{lblu}[{ylw}!{lblu}] {red}Check Your Internet connection {ylw}!")
        exit()

    print(f"""\n{red}──────────────{ylw}[ FULL Lookup ]{red}───────────────
{red}# {ylw}TITLE \n
{grn}{title}\n
{red}# {ylw}OVERVIEW \n
{grn}{Overview}\n
{red}# {ylw}UPDATE TIME\n
{grn}{time}\n 
{red}# {ylw}HTTP HEADER ANALYSIS
{grn}{HTTP_Header}\n
{red}# {ylw}FULL WHOIS\n
{grn}{Full_Whois}\n
{red}────────────────────────────────────────────
""")
#______________________________________________________
def Revers_IP():
    clear()
    print(f"\n {red}✹ {grn}Enter IP Address")

    try:
        IP = input(f"\n{red}❯❯{lblu} ")
    except:
        exit()

    try:
        data = get(f"https://www.sitexpired.com/reverse-ip/{IP}" , headers={
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
            "Referer" : "https://www.sitexpired.com/"
        }).text
    except exceptions.ConnectionError:
        print(f"{lblu}[{ylw}!{lblu}] {red}Check Your Internet connection {ylw}!")
        exit()

    soup = BeautifulSoup(data , "html.parser")
    # title = soup.find("p",class_="card-text").text 
    sites = soup.find_all("div",class_="muted marginBottom_5")
    Recently_Viewed = soup.find_all("li",class_="list-group-item d-flex justify-content-between align-items-center")   
    
    print(f"{red}──────────────{ylw}[ Reverse IP ]{red}───────────────")

    for RIP in sites:  
        DoM = (RIP.find("small").text).split(" ")[1]
        print(f"{lblu}❯ {grn}{DoM}")
    
    print(f"\n{lred}# Recently Viewed{end}\n")  

    for RV in Recently_Viewed:
        dOm = RV.find("a").text
        SeC = RV.find("span").text
        print(f"{lblu}{dOm} {red}╼ {ylw}{SeC} ")

    print(f"\n{red}───────────────────────────────────────────")
