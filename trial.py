import google.generativeai as genai
from dotenv import load_dotenv
import os
import re
from playwright.sync_api import sync_playwright

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

initial_prompt = "You are an expert in browser automation using Playwright and Python. Your task is to guide a Playwright automation script through the Notion signup process. At each step, you will be provided with a screenshot of the current browser page, and your sole responsibility is to generate the EXACT Playwright command (and nothing else) that should be executed next to progress the signup. You must only output the Playwright command, without any explanatory text, comments, or additional information. You have access to the environment variables os.getenv('NAME'), os.getenv('EMAIL_ID'), and os.getenv('PASSWORD') for the signup process, which you should use where appropriate. For example, if the screenshot shows a text box with the label 'enter email', your output should be page.get_by_label('enter email').type(os.getenv('EMAIL_ID')). Also when giving the playwright command be careful that there could be multiple buttons wich could contain common words like continue so make sure the command accounts for this issue so that the wrong button would not be clicked."
response = chat.send_message(initial_prompt)
print(f"Model's initial response: {response.text}")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://notion.so/signup")
    num=1
    page.screenshot(path=f"screenshot{num}.png", full_page=True)
    uploaded_file = genai.upload_file(path=f"screenshot{num}.png", display_name=f"screenshot{num}")
    response = chat.send_message([uploaded_file, "This is the screenshot of the browser page please provide the next playwright command to complete the notions signup process. If the signup is complete respond with 'completed' as the mesage."])
    print(response.text)
    text = response.text
    lines = text.strip().split('\n')
    command_lines = [line for line in lines if not line.startswith('```')]
    cleaned_command = '\n'.join(command_lines).strip()
    print(f"Cleaned command: {cleaned_command}")
    exec(cleaned_command, globals(), locals())
    num=num+1
    page.screenshot(path=f"screenshot{num}.png", full_page=True)
    uploaded_file = genai.upload_file(path=f"screenshot{num}.png", display_name=f"screenshot{num}")
    response = chat.send_message([uploaded_file, "This is the screenshot of the browser page please provide the next playwright command to complete the notions signup process. If the signup is complete respond with 'completed' as the mesage."])
    print(response.text)
    text = response.text
    lines = text.strip().split('\n')
    command_lines = [line for line in lines if not line.startswith('```')]
    cleaned_command = '\n'.join(command_lines).strip()
    print(f"Cleaned command: {cleaned_command}")
    exec(cleaned_command, globals(), locals())
    num=num+1
    page.screenshot(path=f"screenshot{num}.png", full_page=True)
    uploaded_file = genai.upload_file(path=f"screenshot{num}.png", display_name=f"screenshot{num}")
    response = chat.send_message([uploaded_file, "This is the screenshot of the browser page please provide the next playwright command to complete the notions signup process. If the signup is complete respond with 'completed' as the mesage."])
    print(response.text)
    text = response.text
    lines = text.strip().split('\n')
    command_lines = [line for line in lines if not line.startswith('```')]
    cleaned_command = '\n'.join(command_lines).strip()
    print(f"Cleaned command: {cleaned_command}")
    exec(cleaned_command, globals(), locals())
    num=num+1
    page.screenshot(path=f"screenshot{num}.png", full_page=True)