import os
import openai
import argparse
import re

api_key='sk-***********************'
max_input_length = 12

#main function
def main():
    print("App is running.. .")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input","-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(f"user_input: {user_input}")
    if validate_prompt_length(user_input):

        res = generate_snippet(user_input)
        print(res)
        print("----")
        print()
        res1 = generate_keywords(user_input)
        print(res1)
    else:
        raise ValueError(f"Submitted input {user_input} is too long. Input length must be under {max_input_length} charcters!")

# checking the length of the input
def validate_prompt_length(prompt: str) -> bool:
    return len(prompt) <= 12

# generating snippet
def generate_snippet(prompt: str) -> str:
    openai.api_key=api_key

    subject = "coffee"
    new_prompt = f"Genrate branding snippet for ..{prompt}"
    print(new_prompt)

    response = openai.Completion.create(engine="davinci-instruct-beta-v3", prompt=new_prompt, max_tokens=40)
    
    # extracting only text from array
    branding_text: str = response['choices'][0]['text']
    # removing any white space
    branding_text = branding_text.strip()

    # checking if sentence is ending or not
    last_char = branding_text[-1]
    if last_char not in (".","!","?"):
        branding_text += "..."
    
    return branding_text



# generating keywords for the input
def generate_keywords(prompt: str) -> str:
    openai.api_key=api_key

    
    new_prompt = f"Genrate branding keywords for ..{prompt}"
    print(new_prompt)

    response = openai.Completion.create(engine="davinci-instruct-beta-v3", prompt=new_prompt, max_tokens=40)
    
    # extracting only text from array
    branding_keywords: str = response['choices'][0]['text']
    # removing any white space
    branding_keywords = branding_keywords.strip()
    branding_keywords = re.split(",|\n|-|;", branding_keywords)

    cleaned_branding_keywords = [k.lower().strip() for k in branding_keywords]
    cleaned_branding_keywords= [k for k in branding_keywords if len(k) >0]

    return cleaned_branding_keywords

    





if __name__ == "__main__":
    main()