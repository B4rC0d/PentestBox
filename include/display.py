from platform import system as name
from time import sleep
from os import system

HEADER = '\033[95m'
bblu = '\033[94m'
lblu = '\033[96m'
grn = '\033[32m'
ylw = '\033[93m'
red = '\033[91m'
end = '\033[0m'
lred = "\033[2;31;5m"



Ascii_main = f"""
{grn}       +--------------+     {ylw}[ {grn}Pentest Box {ylw}]
{grn}      /|             /|         
{grn}     / |            / |       {red}Coded By {lblu}➜ {ylw}B4rC0d
{grn}    *--+-----------*  |       {red}Channel  {lblu}➜ {ylw}BlackFoxSecurityTeam
{grn}    |  |           |  |       {red}GitHub   {lblu}➜ {ylw}BlackFoxTM
{grn}    |  |           |  |
{grn}    |  +-----------+--+
{grn}    | /            | /
{grn}    |/             |/
{grn}    *--------------*                                                   
"""


def clear():
    sleep(1)
    if name() == "Windows":
        system('cls')
    elif name() == "Linux" or name() == "Darwin":
        system('clear')


def main_banner():
    clear()
    print(Ascii_main)
    sleep(0.5)
    print(f" {red}1{grn} ➞ {ylw}Information Gathering")
    sleep(0.5)
    print(f" {red}2{grn} ➞ {ylw}hashing")
    sleep(0.5)
    print(f"\n {red}3{grn} ➞ {ylw}Exit ...")
    sleep(0.5)


def information():
    clear()
    print(Ascii_main)
    sleep(0.2)
    print(f" {red}1{grn} ➞ {ylw}Admin Page Finder")
    sleep(0.2)
    print(f" {red}2{grn} ➞ {ylw}Robots Scanner")
    sleep(0.2)
    print(f" {red}3{grn} ➞ {ylw}DNS Lookup")
    sleep(0.2)
    print(f" {red}4{grn} ➞ {ylw}Whois")
    sleep(0.2)
    print(f" {red}5{grn} ➞ {ylw}Find Shared DNS")
    sleep(0.2)
    print(f" {red}6{grn} ➞ {ylw}Show HTTP Header")
    sleep(0.2)
    print(f" {red}7{grn} ➞ {ylw}IP location Finder")
    sleep(0.2)
    print(f" {red}8{grn} ➞ {ylw}Port Scan")
    sleep(0.2)
    print(f" {red}9{grn} ➞ {ylw}Bypass Cloud Flare")
    sleep(0.2)
    print(f" {red}10{grn} ➞ {ylw}Revers IP")
    sleep(0.2)
    print(f" {red}11{grn} ➞ {ylw}Full Lookup")
    sleep(0.2)
    print(f"\n {red}99{grn} ➞ {ylw}Exit ...")
    sleep(0.2)

def hashing():
    clear()
    print(Ascii_main)
    sleep(0.2)
    print(f"\n {red}1{grn} ➞ {ylw}decode")
    sleep(0.2)
    print(f" {red}2{grn} ➞ {ylw}encode")

def DecodeMenu():
    clear()
    print(Ascii_main)
    sleep(0.2)
    print(f"\n {red}1{grn} ➞ {ylw}MD5")
    sleep(0.2)
    print(f" {red}2{grn} ➞ {ylw}SHA1")
    sleep(0.2)
    print(f" {red}3{grn} ➞ {ylw}SHA-256")
    sleep(0.2)
    print(f" {red}4{grn} ➞ {ylw}SHA-384")
    sleep(0.2)
    print(f" {red}5{grn} ➞ {ylw}SHA-512")
