# Let us start by importing the much needed Ollama-Python library :
import ollama_python
import llm_axe
from bs4 import BeautifulSoup
from llm_axe import OnlineAgent

#import beautifulsoup4
from ollama_python.endpoints import ModelManagementAPI

# We can declare the Ollama Model Management API's endpoint, so we can start with issuing commands to get the model :

ModelManagerAPI = ollama_python.endpoints.ModelManagementAPI(base_url="http://localhost:11434/api")
#ModelManagerAPI = ollama_python.endpoints.ModelManagementAPI(base_url="http://localhost:12345")

# ... next, let us take all the variables storing the different prompts we will need later, and keep them here in order for them to be globally available to all our functions :

nmap_report = """Starting Nmap 7.94SVN ( https://nmap.org/ ) at 2025-02-11 14:47 AST

Nmap scan report for scanme.nmap.org (45.33.32.156)

Host is up (0.085s latency).

Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f

Not shown: 991 closed tcp ports (reset)

PORT      STATE    SERVICE

22/tcp    open     ssh

25/tcp    filtered smtp

80/tcp    open     http

135/tcp   filtered msrpc

139/tcp   filtered netbios-ssn

445/tcp   filtered microsoft-ds

4444/tcp  filtered krb524

9929/tcp  open     nping-echo

31337/tcp open     Elite

Device type: general purpose

Running: Linux 5.X

OS CPE: cpe:/o:linux:linux_kernel:5

OS details: Linux 5.0 - 5.4

Network Distance: 18 hops



OS detection performed. Please report any incorrect results at https://nmap.org/submit/ ."""

clamav_report = """/home/bryce/Desktop/malicious.exe: Win.Trojan.MSShellcode-7 FOUND

----------- SCAN SUMMARY -----------
Known viruses: 8720640
Engine version: 1.4.2
Scanned directories: 0
Scanned files: 1
Infected files: 1
Data scanned: 0.07 MB
Data read: 0.07 MB (ratio 1.00:1)
Time: 8.706 sec (0 m 8 s)
Start Date: 2025:02:18 11:46:34
End Date:   2025:02:18 11:46:43"""

nikto_report = """Nikto v2.5.0/
+ Target Host: scanme.nmap.org
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options: 
+ GET /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. 
See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/: 
+ GET /index: Uncommon header 'tcn' found, with contents: list.
+ GET /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' 
were found: index.html. See: http://www.wisec.it/sectou.php?id=4698ebdc59d15,https://exchange.xforce.ibmcloud.com/vulnerabilities/8275: 
+ HEAD Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, OPTIONS .
+ GET /images/: Directory indexing found.
+ GET /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/: """

wapiti_report = open("wapiti_report.html","r").read()

decoded_wapiti_report = BeautifulSoup(wapiti_report,"html.parser")
decoded_wapiti_text   = decoded_wapiti_report.getText()

# Let us add the reports to this list. This is done to make it easier for us to interate through every report when submitting the prompts for the LLM :

reports_list = [nmap_report, nikto_report, clamav_report, decoded_wapiti_text]




# {decoded_wapiti_text}
# #{nmap_report}"""
# {wapiti_report}""" , {clamav_report} and {nikto_report}"""
##Here is the report {nmap_report}"""

#   Let us add a variable and store the system prompt in it :

system_instruction_boxy = """
Please use Obsidian-compatible Markdown formatting, as you see in the following example : 


Report Layout:
--------------
# List of Current Vulnerabilities

 Here is a list of the vulnerabilities found in the scan :

>> 1. Unpatched SSH Server
>> 2. Open HTTP Port (80/tcp)
>> 3. Filtered SMTP Port (25/tcp)
>> 4. Filtered MSRPC Port (135/tcp)
>> 5. Filtered NetBIOS-SSN Port (139/tcp)
>> 6. Filtered Microsoft-DS Port (445/tcp)
>> 7. Filtered krb524 Port (4444/tcp)
>> 8. Open NPING-ECHO Port (9929/tcp)
>> 9. Open Elite Port (31337/tcp)

--------------------------------------------------------

# Details 

 #### Open HTTP Port (80/tcp)

 ##### What does it do ?

 The open HTTP port allows unauthorized access to web applications, enabling attackers to execute malicious code, steal sensitive data, or take control of the system.

 ##### How concerned shall I be? (CVSS Report)

 CVSS Score: 2/10

 ##### How can I remedy/mitigate it ?

 Close the HTTP port or restrict access to authorized users and IP addresses.

--------------------------------------------------------

 #### Filtered SMTP Port (25/tcp)

 ##### What does it do ?

 The filtered SMTP port allows attackers to send spam emails, potentially leading to phishing attacks or malware distribution.

 ##### How concerned shall I be? (CVSS Report)

 CVSS Score: 5/10

 ##### How can I remedy/mitigate it ?

 Configure the SMTP server to filter out suspicious emails and block unauthorized access.

--------------------------------------------------------


 #### Filtered NetBIOS-SSN Port (139/tcp)

 ###### What does it do ?

 The filtered NetBIOS-SSN port allows attackers to execute malicious code, potentially leading to system compromise or data theft.

 ##### How concerned shall I be? (CVSS Report)

 CVSS Score: 8/10

 ##### How can I remedy/mitigate it ?

 Close the NetBIOS-SSN port or restrict access to authorized users and IP addresses.

--------------------------------------------------------"""



# ... next, let us create a function to pull the desired model :

def ollama_model_gogetter(modelname):
    #  ... let us use it to pull the model from the Ollama-Python library:

    try:
        TheGetter = ModelManagerAPI.pull(modelname)
        print(f"Model {modelname} has been downloaded successfully!")
    except Exception as e:
        print(f"Error : {e}")
    # Debugging Statements
    print(TheGetter.status)
    ModelManagerAPI.list_local_models()


# Let us download a Cybersecurity-based LLM :

#ollama_model_gogetter("ALIENTELLIGENCE/cybersecuritythreatanalysisv2")


#######################################################################################################################################

# Let us create an empty list to hold the chat history :

chat_history = []

def the_ollama_generator():  # (nmap_report, nikto_report, clamav_report, wapiti_report):

    #   What we need to do here is to use the GenerateAPI library, where we indicate Ollama's API Endpoint, and we select our LLM :

    #from ollama_python import endpoints
    #generation_api = ollama_python.endpoints.GenerateAPI(model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2",base_url="http://127.0.0.1:11434/api")


    from llm_axe import OllamaChat
    #/api
    llm = OllamaChat(host="http://127.0.0.1:11434",model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2") # Windows
    #llm = OllamaChat(host="http://127.0.0.1:12345",model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2") # NixOS


    # generation_api = ollama_python.endpoints.GenerateAPI(model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2",base_url="http://127.0.0.1:12345/api")

    #   Since we get a prompt response successfully from the previous test prompt, let us store an example nmap report :


    #print(decoded_wapiti_text)



    # ... in anticipation of the prompts we will get, let us create a list to hold all the prompt responses :



    #   ... Now , we generate the response :
    try:

        from llm_axe import Agent, OnlineAgent

        for report in reports_list:
            # Let us proceed with defining the generalized prompt, with the report variable being added to the generalized prompt :

            prompt_text = f""""We have ran a series of network, web-application and malware scans of the user's system. Please generate a clear, concise and user-friendly concise report
                indicating the vulnerabilities found, each vulnerability's rating (0-10 from 0 being harmless , to 10 being catastrophic). Afterwards, 
                please generate a detailed report which will start with a list of vulnerabities found in the application's output from the scan, then indicate he name of the vulnerability, 
                what does it do (explaining each vulnerability), How concerned should the user be (find the CVSS score) , how the user can remedy/resolve/mitigate them, and add an advice for the future.  
                The audience (user) is a non-technical individual, and we would like the user to understand each vulnerability, understand its severity, guide the user step-by-step on the remediation of 
                each vulnerability, and provide advice for the future. The system instruction sent with this prompt indicates the layout of the desired report, and please conform to the Obsidian callout 
                strategy indicated in the system prompt . Please insure the information is as accurate as possible by conducting online searches, and please find the CVSS scores for each vulnerability via online searching. 
                I will include the reports now : 
                {report}
            Each block is dedicated to a vulnerability. In Obsidian, there is a feature called 'Callouts' that color the entire box that contains the text a different color,
            depending on the word between [!  and ]. 
            (sidenote : Please feel free to add emojis to enhance the look and delivery of the report)
             Thus, you will respect the following rules: 

            1. For a vulnerability with a CVSS score between 1-3  ,  Please use [!attention]
            2. For a vulnerability with a CVSS score between 3-6  , Please use [!warning]
            3. For a vulnerability with a CVSS score between 7-10 , Please use [!danger]

            Box Style :
            ==============

            > [!warning]
            >
            >
            >  #### Open HTTP Port (80/tcp)
            >
            >> [!question] 
            >> What does it do ?
            >>
            >>> The open HTTP port allows unauthorized access to web applications, enabling attackers to execute malicious code, steal sensitive data, or take control of the system.
            >
            >> [!question] 
            >> How concerned shall I be? (CVSS Report)
            >>
            >>> CVSS Score: 2/10
            >
            >> [!question]  
            >> How can I remedy/mitigate it ?
            >>
            >>> Close the HTTP port or restrict access to authorized users and IP addresses.
            >
            ========================================================================================="""

            agent = Agent(llm,custom_system_prompt=system_instruction_boxy,temperature=0.3,stream=False)
            #,num_ctx=4096)

            the_searcher = OnlineAgent(llm, additional_system_instructions=system_instruction_boxy, temperature=float(0.3),stream=False)

            print("Please wait ... generating report!")

            # answer = agent.ask(prompt_text)
            online_answer = the_searcher.search(prompt=prompt_text,history=chat_history)

            # Let us add the online_answer we will get to the chat_history list :


            chat_history.append(online_answer)

            # Let us print the generated response :

            print(online_answer)

            return online_answer

    except Exception as e:
        print(f"Error In Response Generation : {e}")

    # Now, let us create a function to summarise our reports into one concise report :

def the_summarizer():

    from llm_axe import Agent,OllamaChat

    #llm = OllamaChat(host="http://127.0.0.1:11434",model="hf.co/Melvin56/DeepSeek-R1-Distill-Qwen-7B-abliterated-v2-GGUF:latest") # Windows
    #llm = OllamaChat(host="http://127.0.0.1:12345",model="hf.co/Melvin56/DeepSeek-R1-Distill-Qwen-7B-abliterated-v2-GGUF:latest") # NixOS
    llm = OllamaChat(host="http://127.0.0.1:11434",model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2") # Windows


    # Please the above in the documentary for the project with rationalization!

    # Let us create a variable to hold the prompt for the summarizer function :

    summarized_report_prompt = f""""We have ran a series of network, web-application and malware scans of the user's system, and produced four different reports from each application.
                    Please generate a clear, concise and user-friendly summarized report indicating all the vulnerabilities found, each vulnerability's rating (0-10 from 0 being harmless , to 10 being catastrophic). Afterwards, 
                   please  start with a list of vulnerabilities retrieved from the reports ,then indicate the name of the vulnerability, what does it do (explaining each vulnerability), How concerned should the user be (find the CVSS score) , how the user can remedy/resolve/mitigate them, and add an advice for the future.  
                   The audience (user) is a non-technical individual, and we would like thed user to understand each vulnerability, understand its severity, guide the user step-by-step on the remediation of 
                   each vulnerability, and provide advice for the future. The system instruction sent with this prompt indicates the layout of the desired report, and please conform to the Obsidian callout 
                   strategy indicated in the system prompt . 
                   I will include the reports now : 
                   {chat_history}
               Each block is dedicated to a vulnerability. In Obsidian, there is a feature called 'Callouts' that color the entire box that contains the text a different color,
               depending on the word between [!  and ]. 
               (sidenote : Please feel free to add emojis to enhance the look and delivery of the report)
                Thus, you will respect the following rules: 

               1. For a vulnerability with a CVSS score between 1-3  ,  Please use [!attention]
               2. For a vulnerability with a CVSS score between 3-6  , Please use [!warning]
               3. For a vulnerability with a CVSS score between 7-10 , Please use [!danger]

               Box Style :
               ==============

               > [!warning]
               >
               >
               >  #### Open HTTP Port (80/tcp)
               >
               >> [!question] 
               >> What does it do ?
               >>
               >>> The open HTTP port allows unauthorized access to web applications, enabling attackers to execute malicious code, steal sensitive data, or take control of the system.
               >
               >> [!question] 
               >> How concerned shall I be? (CVSS Report)
               >>
               >>> CVSS Score: 2/10
               >
               >> [!question]  
               >> How can I remedy/mitigate it ?
               >>
               >>> Close the HTTP port or restrict access to authorized users and IP addresses.
               >
               ========================================================================================="""

    try:

        agent = Agent(llm, custom_system_prompt=system_instruction_boxy, temperature=0.3, stream=False)
        reports_summary = agent.ask(prompt=summarized_report_prompt)

        # Let us print the summarized report :
        print(reports_summary)
        return reports_summary

    except TimeoutError as t:
        print(f"Ahem ... there has been the dreaded {t} error! ")

    except Exception as e:
        print(f" Dang it ... this horrid {e} error has joined our midsts!")





the_ollama_generator()
print("Hold on to dear life ... now generating the summarised report!")
the_summarizer()
#the_ollama_generator()









