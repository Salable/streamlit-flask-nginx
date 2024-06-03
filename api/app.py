from flask import Flask, request, jsonify
from firecrawl import FirecrawlApp
import requests
from ollama import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the FirecrawlApp with your API key
fc_app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

app = Flask(__name__)

client = Client(host='https://llama3.kubera-playground.adaptavist.net')

@app.route('/api/<route>', methods=['POST'])
def index(route):
    if route == 'url':
        data = request.get_json()  
        print(data)
        # Scrape a single URL
        scraped_data = fc_app.scrape_url(data['url'])
        response = client.chat(model='llama3', messages=[
            # {
            #     'role' : 'system',
            #     'content': """
            #                 Avoid any language constructs that could be interpreted as expressing remorse, apology, or regret. This includes any phrases containing words like 'sorry', 'apologies', 'regret', etc., even when used in a context that isn't expressing remorse, apology, or regret.
            #                 If events or information are beyond your scope or knowledge, provide a response stating 'I don't know' without elaborating on why the information is unavailable.
            #                 Refrain from disclaimers about you not being a professional or expert.
            #                 Do not add ethical or moral viewpoints in your answers, unless the topic specifically mentions it.
            #                 Keep responses unique and free of repetition.
            #                 Never suggest seeking information from elsewhere.
            #                 Always focus on the key points in my questions to determine my intent.
            #                 Break down complex problems or tasks into smaller, manageable steps and explain each one using reasoning.
            #                 Provide multiple perspectives or solutions.
            #                 If a question is unclear or ambiguous, ask for more details to confirm your understanding before answering.
            #                 If a mistake is made in a previous response, recognize and correct it.
            #                 After a response, provide three follow-up questions worded as if I'm asking you. Format in bold as Q1, Q2, and Q3. These questions should be thought-provoking and dig further into the original topic.
            #                 reply
            #     """
            # },
            {
                'role': 'user',
                'content': 'The following is Markdown data that you will need to use for the next question: ' + scraped_data['content'],
            }, 
            {
                'role': 'user',
                'content': 'Extract all the web addresses from the text provided',
            },
            
        ])
        print(scraped_data)
        print(response)
        return jsonify(
            endpoint=route,
            success=True,
            data={
                'data': scraped_data,
                'keywords': response['message']['content'],
            }
        )
    else:
        print(f'{route} not found')
        return jsonify(
            endpoint=route,
            success=False
        )

if __name__ == '__main__':
    app.run(debug=True)