
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

# Ahem ... so , based on a very kind tip from our guru Carson, I have implemented the Loading portion of the menu to a function : 
    
def DaLoader():
    """
    Purpose: to add a nice loading screen after making each selection ( inner TODO list: Learn How to Make an Accurate Progress Bar : - ) ) 
    """
    
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

# end def    
    

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

            # Let us load the Loading Page : 
            DaLoader()

            comprehensive_nmap_command = subprocess.run(["nmap","--script=vuln*","-O","-Pn",ip_address])
            comprehensive_nmap_command_output = comprehensive_nmap_command.stdout

        elif nmap_choice == "2":
            print("\n\nCertainly! Your Wish is My Command! One NMAP Service-Version NSE Vulnerability Scan coming right up!\n\n")
            print("\n\n")
            DaLoader()
            service_version_nmap_command = subprocess.run(["nmap", "-sV","--script vuln", "-O","-Pn", ip_address])
            service_version_nmap_command_output = service_version_nmap_command.stdout

        elif nmap_choice == "3":

            print("\n\nCertainly! Your Wish is My Command! One Super-Stealthy NMAP Scan coming right up!\n\n")
            print("\n\n")
            DaLoader()
            stealthy_nmap_command = subprocess.run(["nmap", "-sS" "-T 1", "--max-rate 25","--max-retries 3", "-Pn", ip_address])
            stealthy_nmap_scan_command_output = stealthy_nmap_command.stdout
        if choice == "q" or choice == "Q":
            exit()

# Now, let us take care of the next item on our list, the Wapiti menu :



###################################### Wapiti + Nikto Function #################################

############## WAPITI ###############

if choice == "2":
    print("**********************************************************************************************")
    print("****************************** The Trusty Web Application Scans ******************************")
    print("**********************************************************************************************")
    print("\n\n Please choose one of the following Web Application Vulnerability Scans : \n\n")
    print("1. Wapiti Cross-Site Scripting Web Application Scan")
    print("2. Wapiti SQL Injection Web Application Scan")
    print("3. Wapiti Deluxe Web Application Scan (All Comprehensive!)")
    print("4. Nikto Authentication Bypass Scan")
    print("5. Nikto Information Disclosure Scan")
    print("6. Nikto Super-Deluxe Scan")
    print("\n\n")
    web_application_choice = input("Please enter your choice '(Please enter 1,2,3,4,5,6 or q to exit)' : ")
# ... Since this menu is all about Web Application Testing, let us grab the system's IP address :

    ip_address = socket.gethostbyname(socket.gethostname())

    while web_application_choice != "q" or "Q":

        if web_application_choice == "1":

            print("\n\nCertainly! Your Wish is My Command! One Wapiti Cross-Site Scripting Scan coming right up!\n\n")
            print("\n\n")
            DaLoader()

            wapiti_cross_site_command = subprocess.run(
                ["wapiti", "-u", "http://" + ip_address, "--scope","folder","-m","xss"])
            wapiti_cross_site_command_output = wapiti_cross_site_command.stdout

        elif web_application_choice == "2":

            print("\n\nCertainly! Your Wish is My Command! One Wapiti SQL-Injection Scan coming right up!\n\n")
            print("\n\n")
            DaLoader()

            wapiti_sql_command = subprocess.run(
                ["wapiti", "-u", "http://" + ip_address, "--scope","folder","-m","sql"])
            wapiti_sql_command_output = wapiti_sql_command.stdout


        elif web_application_choice == "3":

            print("\n\nCertainly! Your Wish is My Command! One Wapiti Comprehensive Scan coming right up!\n\n")

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

            wapiti_full_command = subprocess.run(["wapiti", "-u", "http://" + ip_address])

            wapiti_full_command_output = wapiti_full_command.stdout

    ################ NIKTO ###################

        elif web_application_choice == "4":

            print("\n\nCertainly! Your Wish is My Command! One Nikto Authentication Bypass Scan coming right up!\n\n")

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

            nikto_authentication_bypass_command = subprocess.run(["nikto", "-Tuning=a", "-host=http://" + ip_address])

            nikto_authentication_bypass_command_output = nikto_authentication_bypass_command.stdout



        elif web_application_choice == "5":

            print("\n\nCertainly! Your Wish is My Command! One Nikto Information Disclosure Scan coming right up!\n\n")

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

            nikto_information_disclosure_command = subprocess.run(["nikto", "-Tuning=3", "-host=http://" + ip_address])

            nikto_information_disclosure_command_output = nikto_information_disclosure_command.stdout


        elif web_application_choice == "6":

            print("\n\nCertainly! Your Wish is My Command! One Nikto Super-Deluxe Scan coming right up!\n\n")

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

            nikto_super_deluxe_command = subprocess.run(["nikto", "-host=http://" + ip_address])

            nikto_super_deluxe_command_output = nikto_super_deluxe_command.stdout



    # The Correct Nikto options for -Tunings= are :
                               # 1     Interesting File / Seen in logs
                               # 2     Misconfiguration / Default File
                               # 3     Information Disclosure
                               # 4     Injection (XSS/Script/HTML)
                               # 5     Remote File Retrieval - Inside Web Root 
                               # 6     Denial of Service
                               # 7     Remote File Retrieval - Server Wide
                               # 8     Command Execution / Remote Shell
                               # 9     SQL Injection
                               # 0     File Upload
                               # a     Authentication Bypass
                               # b     Software Identification
                               # c     Remote Source Inclusion
                               # d     WebService

if choice == "3":
    print("**********************************************************************************************")
    print("********************************** The Trusty File  Scanner **********************************")
    print("**********************************************************************************************")
    print("\n\n Please choose one of the following Clam-AV File Scans : \n\n")
    print("1. ClamAV File Scan")
    print("2. ClamAV Directory Scan")
    print("\n\n")
    clamav_choice = input("Please enter your choice '(Please enter 1,2,3,4,5,6 or q to exit)' : ")

# Since all these options utilize ClamAV, let us make sure it has the latest Virus Definitions :

    subprocess.run(["sudo","freshclam"])

    while clamav_choice != "q" or "Q":

        if clamav_choice == "1":

            print("\n\nCertainly! Your Wish is My Command! One ClamAV File Scan coming right up!\n\n")
            print("\n\n")
            DaLoader()

            file_location = str(input("Please enter the location of the file you wish to scan : \n\n"))

            clamav_file_scan_command = subprocess.run(["clamscan",file_location])
            clamav_file_scan_command_output = clamav_file_scan_command.stdout


        elif clamav_choice == "2":

            print("\n\nCertainly! Your Wish is My Command! One ClamAV Folder Scan coming right up!\n\n")
            print("\n\n")
            DaLoader()

            file_location = str(input("Please enter the location of the folder you wish to scan : \n\n"))

            clamav_folder_scan_command = subprocess.run(["clamscan","-r",file_location])
            clamav_folder_scan_command_output = clamav_folder_scan_command.stdout

















