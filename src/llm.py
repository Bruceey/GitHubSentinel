# src/llm.py

import os
import requests
import json
from logger import LOG  # 导入日志模块

class LLM:
    def __init__(self):
        self.url = "https://qianfan.baidubce.com/v2/chat/completions"
        self.headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {os.getenv('BAIDU_API_KEY')}"
        }

        # 从TXT文件加载提示信息
        with open("prompts/report_prompt.txt", "r", encoding='utf-8') as file:
            self.system_prompt = file.read()

    
    def invoke_llm(self, messages, model='ernie-3.5-128k'):
        # 调用 百度 模型生成报告
        payload = json.dumps({
            # "model": "qwq-32b",
            # "model": "ernie-4.0-turbo-8k-latest",
            "model": model,
            "messages": messages,
            # "max_completion_tokens": 500
        })
        response = requests.post(self.url, headers=self.headers, data=payload)
        return response.json()

    def generate_daily_report(self, markdown_content, dry_run=False):
        # 使用从TXT文件加载的提示信息
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": markdown_content},
        ]

        if dry_run:
            # 如果启用了dry_run模式，将不会调用模型，而是将提示信息保存到文件中
            LOG.info("Dry run mode enabled. Saving prompt to file.")
            with open("daily_progress/prompt.txt", "w+") as f:
                # 格式化JSON字符串的保存
                json.dump(messages, f, indent=4, ensure_ascii=False)
            LOG.debug("Prompt saved to daily_progress/prompt.txt")
            return "DRY RUN"
        
        # 日志记录开始生成报告
        LOG.info("Starting report generation using 百度 model.")

        try:
            # 调用OpenAI GPT模型生成报告
            response = self.invoke_llm(messages)
            LOG.debug("百度 response: {}", response)
            # 返回模型生成的内容
            return response['choices'][0]['message']['content']
        except Exception as e:
            # 如果在请求过程中出现异常，记录错误并抛出
            LOG.error("An error occurred while generating the report: {}", e)
            raise
    

if __name__ == "__main__":
    llm = LLM()
    with open('daily_progress/langchain-ai_langchain_2025-03-11.md') as f:
        markdown_content = f.read()
    report = llm.generate_daily_report(markdown_content)
    print(report)
