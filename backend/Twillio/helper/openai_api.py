import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = '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'


def text_complition(name: str, health_problem: str) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    try:
        print("\n") 
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'You are a professional writer and you write headers in Hinglish language for notifications that send on mobile phone.  write one notification on topic {health_problem} , which are engaging, little bit of clickbait, and high chance user clicks on it. Add a bit of personalization for {name} who he is suffering from {health_problem} to increase conversion in notification as well. Keep it short, and crisp.\nAns - ',
            temperature=0.9,
            max_tokens=2500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
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

def text_complete(name:str,health_problem: str,title: str):
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'Que -Write an article personalised for {name} who has {health_problem} in around 500 words who has came to your website clicking on the link - {title}. This is written by Bajaj Finanse. \nAns - ',
            temperature=0.9,
            max_tokens=2500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['Ans -']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        print("No article is printed")
        return {
            'status': 0,
            'response': ''
        }
