import os
import requests
from time import sleep

# Window

os.system("color 6")

# Interface

print("\n\n\n")
print("                                 ██╗░░░░░░█████╗░░█████╗░░█████╗░████████╗░█████╗░██████╗░")
print("                                 ██║░░░░░██║░░██║██║░░╚═╝███████║░░░██║░░░██║░░██║██████╔╝")
print("                                 ██║░░░░░██║░░██║██║░░██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗")
print("                                 ███████╗╚█████╔╝╚█████╔╝██║░░██║░░░██║░░░╚█████╔╝██║░░██")
print("                                 ________________________________________________________")
print("\n\n\n")



IP = str(input("                                              Inserez l'IP ici > "))
print("\n\n\n")

response = requests.post("http://ip-api.com/batch", json=[
  {"query": (IP)}
]).json()


for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")