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


def the_ollama_generator(): #nmap_report,nikto_report,clamav_report,wapiti_report):

#   What we need to do here is to use the GenerateAPI library, where we indicate Ollama's API Endpoint, and we select our LLM :
    from ollama_python import endpoints
    generation_api = ollama_python.endpoints.GenerateAPI(model="ALIENTELLIGENCE/cybersecuritythreatanalysisv2",base_url="http://127.0.0.1:11434/api")

#   Let us add a variable and store the system prompt in it :

    # system_instruction = {
    #         "role": "system",
    #         "content": "You are a Cybersecurity Expert with many years of experience in Cybersecurity. You are a friendly professional and have an eye for detail. You are an expert at vulnerability assessment report generation where you convey the results of network vulnerability assessments, web application vulnerability assessments and malicious file scanning in a friendly, accurate and as non-technical as possible. We would like to be approachable to a wide variety of audiences, thus this is the reason behind this instruction."
    #     }
    system_instruction = "You are a Cybersecurity Expert with many years of experience in Cybersecurity. You are a friendly professional and have an eye for detail. You are an expert at vulnerability assessment report generation where you convey the results of network vulnerability assessments, web application vulnerability assessments and malicious file scanning in a friendly, accurate and as non-technical as possible. We would like to be approachable to a wide variety of audiences, thus this is the reason behind this instruction."
#    messages = [{'role':'user','content':'Could you please explain MiTM?'}]
    prompt_text = "Could you please explain a Man in the middle attack in detail?"
                     #'system', 'content' : 'You are a Cybersecurity Expert, with many years of experience in Cybersecurity. You are a friendly, professional, and have an eye for detail. You are an expert at vulnerability assessment report generation, where you convey the results of network vulnerability assessments, web application vulnerability assessments and malicious file scanning in a friendly, accurate and as non-technical as possible. We would like to be approachable to a wide variety of audiences, thus this is the reason behind this instruction.'}]

#   ... Now , we generate the response :
    try:
        answer = generation_api.generate(prompt=prompt_text,options=dict(temperature=float(0.7)),system=system_instruction)#,format="json")
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










