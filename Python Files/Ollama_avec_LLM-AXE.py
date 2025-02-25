# Let us start by importing the much needed Ollama-Python library :
import ollama_python
import llm_axe
import beautifulsoup4
from ollama_python.endpoints import ModelManagementAPI

# We can declare the Ollama Model Management API's endpoint, so we can start with issuing commands to get the model :

ModelManagerAPI = ollama_python.endpoints.ModelManagementAPI(base_url="http://localhost:11434/api")


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

# ollama_model_gogetter("ALIENTELLIGENCE/cybersecuritythreatanalysisv2")


#######################################################################################################################################


def the_ollama_generator():  # (nmap_report, nikto_report, clamav_report, wapiti_report):

    #   What we need to do here is to use the GenerateAPI library, where we indicate Ollama's API Endpoint, and we select our LLM :

    #from ollama_python import endpoints
    #generation_api = ollama_python.endpoints.GenerateAPI(model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2",base_url="http://127.0.0.1:11434/api")


    from llm_axe import OllamaChat
    llm = OllamaChat(host="http://127.0.0.1:11434/api",model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2")
    # generation_api = ollama_python.endpoints.GenerateAPI(model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2",base_url="http://127.0.0.1:12345/api")

    #   Since we get a prompt response successfully from the previous test prompt, let us store an example nmap report :

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
+ GET /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/: 
+ GET /index: Uncommon header 'tcn' found, with contents: list.
+ GET /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' were found: index.html. See: http://www.wisec.it/sectou.php?id=4698ebdc59d15,https://exchange.xforce.ibmcloud.com/vulnerabilities/8275: 
+ HEAD Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, OPTIONS .
+ GET /images/: Directory indexing found.
+ GET /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/: """

    # with open("wapiti_report.html", "r") as f:
    #     extracted_report = beautifulsoup4(f, 'html.parser')
    #     extracted_report

    prompt_text = f""""We have ran a series of network, web-application and malware scans of the user's system. Please generate a clear, concise and user-friendly concise report
    indicating the vulnerabilities found, each vulnerability's rating (0-10 from 0 being harmless , to 10 being catastrophic). Afterwards, 
    please generate a detailed report explaining each vulnerability, its rating of severity,  the reason behind the rating of severity,
    how the user can resolve them, and add an advice for the future.  The audience (user) is a non-technical individual, and we would like the user to understand each vulnerability,
    understand its severity, guide the user step-by-step on the remediation of each vulnerability, and provide advice for the future. 
    I will include the reports now : {nmap_report} , {wapiti_report} , {clamav_report} and {nikto_report}"""
    ##Here is the report {nmap_report}"""

    #   Let us add a variable and store the system prompt in it :

    system_instruction = "You are a Cybersecurity Expert with many years of experience in Cybersecurity. You are a friendly professional and have an eye for detail. You are an expert at vulnerability assessment report generation where you convey the results of network vulnerability assessments, web application vulnerability assessments and malicious file scanning in a friendly, accurate and as non-technical as possible. We would like to be approachable to a wide variety of audiences, thus this is the reason behind this instruction."

    #   prompt_text = "Could you please explain a Man in the middle attack in detail?"

    #   ... Now , we generate the response :
    try:
        # answer = generation_api.generate(prompt=prompt_text, options=dict(temperature=float(0.3)),
        #                                  system=system_instruction)
        #                                ,format="json")
        #                               ,context=
        #                               ,total_duration=
        #                               ,load_duration=
        #                               ,prompt_eval_duration=
        #                               ,eval_count=
        #                               ,eval_duration=
        # )
        prompts_of_LLM = []
        prompts.append(prompt_text)
        answer = OllamaChat.ask(llm,prompts=prompts_of_LLM,temperature=0.3,stream=True)

        Try:
            for character in answer:
                print(character)
        Except:
                print("OOPs! Something is up with our brainy assistant!")

        #prompt_response = answer.response
        
        return prompt_response


    except Exception as e:
        print(f"Error In Response Generation : {e}")


print(the_ollama_generator())










