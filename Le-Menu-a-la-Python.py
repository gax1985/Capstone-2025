
# Let us start by greeting, and add a command prompting the user to enter their choice :

import os
import subprocess
import time
import socket
from ipaddress import ip_address

print("Good Day! I am a helpful Cybersecurity guide, and I am here to check up on your nice computer that you have there. ")
print("May I ask you to choose one of the following options, to determine our course of action:")

print("""1. Network Scans (with nmap)
2. Web Application Scans (with wapiti and nikto)
3. File Scanning (with ClamAV)""")

# Now, we can turn the user's choice into reality : 

choice = input("Please Enter your Selection ( please enter 1,2,3 or type the letter 'q' to exit ) :")


###################################### NMAP Function #################################




if choice == "1":
    print("**********************************************************************************************")
    print("******************************** The Lovely NMAP Network Scans *******************************")
    print("**********************************************************************************************")
    print("\n\n Please choose one of the following NMAP Network Vulnerability Scans : \n\n")
    print("1. NMAP NSE Comprehensive Vulnerability Scan")
    print("2. NMAP Service-Version NSE Vulnerability Scan")
    print("3. NMAP Under-The-Radar Scan")
    print("\n\n")
    nmap_choice = input("Please enter your choice '(Please enter 1,2,3 or q to exit)' : ")

# Now, let us implement the mechanism of conducting the actions mandated by the user's choice :


    while nmap_choice != "q" or "Q":

# ... since all of the scans involving nmap require the IP Address of the host, let us obtain it for our uses :

        ip_address = socket.gethostbyname(socket.gethostname())

        if nmap_choice == "1":
            print("\n\nCertainly! Your Wish is My Command! One Comprehensive NMAP Vulnerability Scan coming right up!\n\n")
            print("\n\n")
            print("Please Wait! I appreciate your patience")
            print("[*     ]")
            time.sleep(1)
            print("[**   ]")
            time.sleep(1)
            print("[***  ]")
            time.sleep(1)
            print("[**** ]")
            time.sleep(1)
            print("[*****]")
            command = subprocess.run(["nmap","--script=vuln*","-O","-Pn",ip_address])
            comprehensive_nmap_command_output = command.stdout

        elif nmap_choice == "2":
            print("\n\nCertainly! Your Wish is My Command! One NMAP Service-Version NSE Vulnerability Scan coming right up!\n\n")
            print("\n\n")
            print("Please Wait! I appreciate your patience")
            print("[*     ]")
            time.sleep(1)
            print("[**   ]")
            time.sleep(1)
            print("[***  ]")
            time.sleep(1)
            print("[**** ]")
            time.sleep(1)
            print("[*****]")
            command = subprocess.run(["nmap", "-sV","--script vuln", "-O","-Pn", ip_address])
            service_version_nmap_command_output = command.stdout

        elif nmap_choice == "3":

            print("\n\nCertainly! Your Wish is My Command! One Super-Stealthy NMAP Scan coming right up!\n\n")
            print("\n\n")
            print("Please Wait! I appreciate your patience")
            print("[*     ]")
            time.sleep(1)
            print("[**   ]")
            time.sleep(1)
            print("[***  ]")
            time.sleep(1)
            print("[**** ]")
            time.sleep(1)
            print("[*****]")
            command = subprocess.run(["nmap", "-sS" "-T 1", "--max-rate 25","--max-retries 3", "-Pn", ip_address])

    if choice == "q" or choice == "Q":
        exit()



