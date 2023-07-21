import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = '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'


def text_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    try:
        print(prompt)
        print("\n")
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'Que-{prompt}\nAns - ',
            temperature=0.2,
            max_tokens=2500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.1,
            stop=['Ans -']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }