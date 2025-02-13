#Let us start by importing the much needed Ollama-Python library :
import ollama
import ollama_python

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

#ollama_model_gogetter("ALIENTELLIGENCE/cybersecuritythreatanalysisv2")


#######################################################################################################################################


def the_ollama_generator(): #(nmap_report,nikto_report,clamav_report,wapiti_report):

#   What we need to do here is to use the GenerateAPI library, where we indicate Ollama's API Endpoint, and we select our LLM :
    
    from ollama_python import endpoints
    generation_api = ollama_python.endpoints.GenerateAPI(model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2",base_url="http://127.0.0.1:11434/api")
    #generation_api = ollama_python.endpoints.GenerateAPI(model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2",base_url="http://127.0.0.1:12345/api")


#   Let us add a variable and store the system prompt in it :


    
    
    system_instruction = "You are a Cybersecurity Expert with many years of experience in Cybersecurity. You are a friendly professional and have an eye for detail. You are an expert at vulnerability assessment report generation where you convey the results of network vulnerability assessments, web application vulnerability assessments and malicious file scanning in a friendly, accurate and as non-technical as possible. We would like to be approachable to a wide variety of audiences, thus this is the reason behind this instruction."
    #prompt_text = "Could you please explain a Man in the middle attack in detail?"


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


    prompt_text = """"We have ran a series of network, web-application and malware scans of the user's system. Please generate a clear, concise and user-friendly concise report
    indicating the vulnerabilities found, each vulnerability's rating (0-10 from 0 being harmless , to 10 being catastrophic). Afterwards, 
    please generate a detailed report explaining each vulnerability, its rating of severity,  the reason behind the rating of severity,
    how the user can resolve them, and add an advice for the future. 

    Here is the {nmap_report}"""



#   ... Now , we generate the response :
    try:
        answer = generation_api.generate(prompt=prompt_text,options=dict(temperature=float(0.3)),system=system_instruction)#,format="json")
         #                               ,context=
         #                               ,total_duration=
         #                               ,load_duration=
         #                               ,prompt_eval_duration=
         #                               ,eval_count=
         #                               ,eval_duration=
         # )

        prompt_response = answer.response
        return prompt_response

        
    except Exception as e:
        print(f"Error In Response Generation : {e}")


print(the_ollama_generator())










