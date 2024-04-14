import replicate

def repli_call(prompt_topic : str):
    input = {
        "top_p": 1,
        "prompt": prompt_topic,
        "temperature": 0.75,
        "system_prompt": "Write an article on the given topic. The article must be under 800 words. The article should be be lengthy. It must be a generic.",
        "max_new_tokens": 800,
        "repetition_penalty": 1
    }

    return_string = ""
    for event in replicate.stream(
        "meta/llama-2-7b-chat",
        input=input
    ):
        return_string = return_string+str(event)
    return return_string



# Try this code out and see how much better the Model is in generating the desired output
# repli_call("Windows Operating System")




