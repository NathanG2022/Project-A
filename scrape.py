import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import re
import phonenumbers

def scrape_website(website):
    print("Launching chrome browser...")
    
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        
        return html
    finally:
        driver.quit
        
def extract_body_content(html_content):
    soup=BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""
    
def find_phone_number(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    phone_number_string = "Extracted Phone Numbers: \n"
    country_code = "US" # need to change if international
    phone_numbers = set() 

    all_text = soup.get_text()  
    
    # might need to change if want to include international numbers and other formats
    # only works for xxx-xxx-xxx & xxx.xxx.xxxx
    matches = re.findall(r'\d{3}[-.\s]\d{3}[-.\s]\d{4}', all_text) 
    for num in matches:
        if phonenumbers.is_valid_number(phonenumbers.parse(num, country_code)):
            phone_numbers.add(num.strip())
    
    if phone_numbers: 
        for number in sorted(phone_numbers): 
            phone_number_string += f" {number}"
            phone_number_string += "\n"
        
    return phone_number_string

def find_email(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    email_string = "Extracted Emails: \n"
    emails = set() 

    all_text = soup.get_text()  
    
    matches = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', all_text) 
    for num in matches:
            emails.add(num.strip())
    
    if emails: 
        for number in sorted(emails): 
            email_string += f" {number}"
            email_string += "\n"
        
    return email_string


#i dont think both are needed (but is llm method)
def split_dom_content(dom_content, max_length=6000):
    return[
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
        
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content    
    