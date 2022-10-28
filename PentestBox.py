from include import display , information , hashing



display.main_banner()
try:
    SelectNum = int(input(f"\n{display.red}❯❯{display.lblu} "))
except:
    exit()

if SelectNum == 1:
    display.information()
    try:
        SelectNum = int(input(f"\n{display.red}❯❯{display.lblu} "))
    except:
        exit()
    if SelectNum == 1:
        information.Admin()
    elif SelectNum == 2:
        information.robots()
    elif SelectNum == 3:
        information.dnslookup()
    elif SelectNum == 4:
        information.Whois()
    elif SelectNum == 5:
        information.findshareddns()
    elif SelectNum == 6:
        information.httpheader()
    elif SelectNum == 7:
        information.Location()
    elif SelectNum == 8:
        information.portscan()
    elif SelectNum == 9:
        information.Cloud()
    elif SelectNum == 10:
        information.Revers_IP()
    elif SelectNum == 11:
        information.Full_Lookup()
    else:
        exit()

elif SelectNum == 2:
    display.hashing()
    try:
        SelectNum = int(input(f"\n{display.red}❯❯{display.lblu} "))
    except:
        exit()
    if SelectNum == 1:
        display.DecodeMenu()
        try:
            SelectNum = int(input(f"\n{display.red}❯❯{display.lblu} "))
        except:
            exit()
        
        if SelectNum == 1:
            hashing.decoding(type="md5")
        elif SelectNum == 2:
            hashing.decoding(type="sha1")
        elif SelectNum == 3:
            hashing.decoding(type="sha256")
        elif SelectNum == 4:
            hashing.decoding(type="sha384")
        elif SelectNum == 5:
            hashing.decoding(type="sha512")
        else:
            exit()
    if SelectNum == 2:
        hashing.Encoding()
    else:
        exit()
elif SelectNum == 3:
    exit()

else:
    exit()
