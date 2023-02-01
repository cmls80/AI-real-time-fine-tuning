import openai
import requests
from bs4 import BeautifulSoup

API_KEY = ''

openai.api_key = API_KEY 
model = 'text-davinci-003'
endpoint = "https://api.open-ai.com/v1/events/real-time"

def search_web(query):
    response = openai.Completion.create(
        engine=model,
        prompt=query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response['choices'][0]['text']
    return message

def update_model():
        website = "" 
        response = requests.get('website')
        soup = BeautifulSoup(response.content, 'html.parser')(

    )
        
        
        latest_information = soup.get_text()(

    )
        openai.Completion.update('text-davinci-003', 'latest_information')
    
        update_model('update')(
    )   
        query = input("Ask me a question")
        
        result = search_web('query')(

    )
    
        print("answers", result)