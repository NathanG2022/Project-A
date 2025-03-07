from bs4 import BeautifulSoup
import requests
import certifi
import re

try:
    # Secure GET request
    url = 'https://www.lwsd.org/help/contact-us'
    response = requests.get(url, verify=certifi.where())
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    ### **1 Find Specific Contact Info (Tel, Fax, Safety Tip Line)**
    print("\n Extracted Contact Details:")
    contact_labels = soup.find_all(string=re.compile(r'Tel:|Fax:|Safety Tip Line|Facility issues', re.IGNORECASE))

    extracted_info = []
    for label in contact_labels:
        text = label.parent.get_text(strip=True)  # Get the text including the parent
        extracted_info.append(text)

    if extracted_info:
        print("\n".join(extracted_info))
    else:
        print("No contact details found. The structure may have changed.")

    ### **2 Extract Only Valid Phone Numbers**
    print("\n Extracted Phone Numbers (Filtered):")
    phone_numbers = set()  # Using a set to avoid duplicates

    all_text = soup.get_text()  # Extract all visible text
    matches = re.findall(r'\b\d{3}[-.]\d{3}[-.]\d{4}\b', all_text)  # Match valid phone numbers

    for num in matches:
        phone_numbers.add(num.strip())  # Strip extra spaces and add to set

    if phone_numbers:
        for num in phone_numbers:
            print(num)
    else:
        print("No phone numbers found.")

except requests.exceptions.SSLError as ssl_error:
    print(f"SSL error occurred: {ssl_error}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")



