#Let us start by importing the much needed Ollama-Python library :

import ollama_python

from ollama_python.endpoints import ModelManagementAPI

# We can declare the Ollama Model Management API's endpoint, so we can start with issuing commands to get the model :

ModelManagerAPI = ollama_python.endpoints.ModelManagementAPI(base_url="http://localhost:11434/api")
print(ModelManagerAPI.__getstate__())


# ... next, let us create a function to pull the desired model :

def ollama_model_gogetter(modelname):

#  ... let us use it to pull the model from the Ollama-Python library:

    modelname = str(modelname)
    TheGetter = ModelManagerAPI.pull(modelname)

    # Debugging Statements
    print(TheGetter.status)
    ModelManagerAPI.list_local_models()

# Let us download a Cybersecurity-based LLM :

#ollama_model_gogetter("ALIENTELLIGENCE/cybersecuritythreatanalysisv2")


def the_ollama_generator(): #nmap_report,nikto_report,clamav_report,wapiti_report):

#   What we need to do here is to use the GenerateAPI library, where we indicate Ollama's API Endpoint, and we select our LLM :

    generation_api = ollama_python. endpoints.GenerateAPI(base_url="http://127.0.0.1:11434/api",model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2")

#    messages = [{'role':'user','content':'Could you please explain MiTM?'}]
    prompt_text = "Could you please explain MiTM?"
                     #'system', 'content' : 'You are a Cybersecurity Expert, with many years of experience in Cybersecurity. You are a friendly, professional, and have an eye for detail. You are an expert at vulnerability assessment report generation, where you convey the results of network vulnerability assessments, web application vulnerability assessments and malicious file scanning in a friendly, accurate and as non-technical as possible. We would like to be approachable to a wide variety of audiences, thus this is the reason behind this instruction.'}]

    answer = generation_api.generate(prompt=prompt_text,options=dict(temperature=float(0.7)),raw=False,system='You are a Cybersecurity Expert with many years of experience in Cybersecurity. You are a friendly professional and have an eye for detail.You are an expert at vulnerability assessment report generation where you convey the results of network vulnerability assessments web application vulnerability assessments and malicious file scanning in a friendly accurate and as non-technical as possible. We would like to be approachable to a wide variety of audiences thus this is the reason behind this instruction.',format="json")
         #                               ,context=
         #                               ,total_duration=
         #                               ,load_duration=
         #                               ,prompt_eval_duration=
         #                               ,eval_count=
         #                               ,eval_duration=
         # )
    prompt_response = answer.response
    return prompt_response


the_ollama_generator()










