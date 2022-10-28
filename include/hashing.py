import hashlib , base64 , time
from .display import red,lblu,grn,ylw,clear



def Encoding():
    clear()
    print(f"\n {red}✹ {grn}Enter the desired text")
    try:
        tXt = input(f"\n{red}❯❯{lblu} ").encode()
    except:
        exit()

    print(f"{red}──────────────────────────────────────────────")

    print(f"""
{ylw}[{grn}+{ylw}] {red}MD5      {lblu}➜ {grn}{hashlib.md5(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}SHA1     {lblu}➜ {grn}{hashlib.sha1(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}SHA224   {lblu}➜ {grn}{hashlib.sha224(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}SHA256   {lblu}➜ {grn}{hashlib.sha256(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}SHA384   {lblu}➜ {grn}{hashlib.sha384(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}SHA512   {lblu}➜ {grn}{hashlib.sha512(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}BLAKE2b  {lblu}➜ {grn}{hashlib.blake2b(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}BLAKE2s  {lblu}➜ {grn}{hashlib.blake2s(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}SHA3_224 {lblu}➜ {grn}{hashlib.sha3_224(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}SHA3_256 {lblu}➜ {grn}{hashlib.sha3_256(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}SHA3_384 {lblu}➜ {grn}{hashlib.sha3_384(tXt).hexdigest()}
{ylw}[{grn}+{ylw}] {red}SHA3_512 {lblu}➜ {grn}{hashlib.sha3_512(tXt).hexdigest()}

{ylw}[{grn}+{ylw}] {red}BASE64   {lblu}➜ {grn}{base64.b64encode(tXt).decode()}
{ylw}[{grn}+{ylw}] {red}BASE32   {lblu}➜ {grn}{base64.b32encode(tXt).decode()}
{ylw}[{grn}+{ylw}] {red}BASE85   {lblu}➜ {grn}{base64.b85encode(tXt).decode()}
{ylw}[{grn}+{ylw}] {red}BASE16   {lblu}➜ {grn}{base64.b16encode(tXt).decode()}
""")
    print(f"{red}──────────────────────────────────────────────\n")



def decoding(type):
    clear()
    print(f"\n {red}✹ {grn}Enter the hash")

    try:
        hashvalue = input(f"\n{red}❯❯{lblu} ")
    except:
        exit() 
    print(f"\n {red}✹ {grn}Enter the address of the wordlist")
    try:
        filePath = input(f"\n{red}❯❯{lblu} ")
    except:
        exit() 
    
    with open(filePath , "r+") as wordlist:
        list = wordlist.read().splitlines()

    if type == "md5":
        for txt in list:
            hash = hashlib.md5(txt.encode()).hexdigest()  
            print(f"    {grn}{txt} {lblu}➜ {red}{hash} " , end="\r")
            time.sleep(0.1)
            if hash == hashvalue:
                clear()
                print(f"\n{red}──────────────────{ylw}[ {red}Hash {grn}found {ylw}]{red}─────────────────────────")
                print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
                """)
                print(f"{red}─────────────────────────────────────────────────────────")
                break
        clear()
        print(f"\n{red}──────────────────{ylw}[ Hash {red}Not{ylw} found ]{red}─────────────────────────")
        print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
        """)
        print(f"{red}─────────────────────────────────────────────────────────────")

            
    elif type == "sha1":
        for txt in list:
            hash = hashlib.sha1(txt.encode()).hexdigest()  
            print(f"    {grn}{txt} {lblu}➜ {red}{hash} " , end="\r")
            time.sleep(0.1)
            if hash == hashvalue:
                clear()
                print(f"\n{red}──────────────────{ylw}[ {red}Hash {grn}found {ylw}]{red}─────────────────────────")
                print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
                """)
                print(f"{red}─────────────────────────────────────────────────────────")
                break
        clear()
        print(f"\n{red}──────────────────{ylw}[ Hash {red}Not{ylw} found ]{red}─────────────────────────")
        print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
        """)
        print(f"{red}─────────────────────────────────────────────────────────────")
    elif type == "sha256":
        for txt in list:
            hash = hashlib.sha256(txt.encode()).hexdigest()  
            print(f"    {grn}{txt} {lblu}➜ {red}{hash} " , end="\r")
            time.sleep(0.1)
            if hash == hashvalue:
                clear()
                print(f"\n{red}──────────────────{ylw}[ {red}Hash {grn}found {ylw}]{red}─────────────────────────")
                print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
                """)
                print(f"{red}─────────────────────────────────────────────────────────")
                break
        clear()
        print(f"\n{red}──────────────────{ylw}[ Hash {red}Not{ylw} found ]{red}─────────────────────────")
        print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
        """)
        print(f"{red}─────────────────────────────────────────────────────────────")
    elif type == "sha384":
        for txt in list:
            hash = hashlib.sha384(txt.encode()).hexdigest()  
            print(f"    {grn}{txt} {lblu}➜ {red}{hash} " , end="\r")
            time.sleep(0.1)
            if hash == hashvalue:
                clear()
                print(f"\n{red}──────────────────{ylw}[ {red}Hash {grn}found {ylw}]{red}─────────────────────────")
                print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
                """)
                print(f"{red}─────────────────────────────────────────────────────────")
                break
        clear()
        print(f"\n{red}──────────────────{ylw}[ Hash {red}Not{ylw} found ]{red}─────────────────────────")
        print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
        """)
        print(f"{red}─────────────────────────────────────────────────────────────")
    elif type == "sha512":
        for txt in list:
            hash = hashlib.sha512(txt.encode()).hexdigest()  
            print(f"    {grn}{txt} {lblu}➜ {red}{hash} " , end="\r")
            time.sleep(0.1)
            if hash == hashvalue:
                clear()
                print(f"\n{red}──────────────────{ylw}[ {red}Hash {grn}found {ylw}]{red}─────────────────────────")
                print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
                """)
                print(f"{red}─────────────────────────────────────────────────────────")
                break
        clear()
        print(f"\n{red}──────────────────{ylw}[ Hash {red}Not{ylw} found ]{red}─────────────────────────")
        print(f"""
    {red}[{grn}+{red}] {ylw}HASH {lblu}➜ {red}{hash}
    {red}[{grn}+{red}] {ylw}TXT  {lblu}➜ {grn}{txt}
        """)
        print(f"{red}─────────────────────────────────────────────────────────────")
