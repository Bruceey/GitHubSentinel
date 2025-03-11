# src/llm.py

import requests
import json

class LLM:
    def __init__(self, api_key):
        self.url = "https://qianfan.baidubce.com/v2/chat/completions"
        self.headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
        }

    def generate_daily_report(self, markdown_content):
        prompt = f"Please summarize the following project updates into a formal daily report:\n\n{markdown_content}"

        payload = json.dumps({
        # "model": "qwq-32b",
        "model": "ernie-4.0-turbo-8k-latest",
        "messages": [{
                "role": "user",
                "content": prompt
        }],
        # "max_completion_tokens": 500
        })

        response = requests.post(self.url, headers=self.headers, data=payload).json()
        return response['choices'][0]['message']['content'].strip()
    

if __name__ == "__main__":
    import os
    llm = LLM(os.getenv('BAIDU_API_KEY'))
    with open('daily_progress/langchain-ai_langchain_2025-03-11.md') as f:
        markdown_content = f.read()
    report = llm.generate_daily_report(markdown_content)
    print(report)
