
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_hours(logs):
    messages = [{"role": "user", "content": f"Summarize these logs: {logs}"}]
    response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
    return response.choices[0].message.content
