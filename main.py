import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content, find_phone_number, find_email


st.title("WebScraper Project ChainLink")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the Website")
    result = scrape_website(url)
    body_cotent = extract_body_content(result)
    clean_content = clean_body_content(body_cotent)
    phone_number = find_phone_number(clean_content)
    email = find_email(clean_content)
    
    st.session_state.dom_content = body_cotent
    st.session_state.phone_number = phone_number
    st.session_state.email = email
    
    
    with st.expander("View Contact Information"):
        st.text_area("Phone Numbers", phone_number, height=300)
        st.text_area("Emails", email, height=300)
        st.text_area("Content", body_cotent, height=300)
    
#if "dom_content" in st.session_state:
#    parse_description = st.text_area("Describe what you want to parse")

#    if st.button("Parse Content"):
#        if parse_description:
#            st.write("Parsing the content...")

            # Parse the content with Ollama
#            dom_chunks = split_dom_content(st.session_state.dom_content)
#            parsed_result = parse_with_ollama(dom_chunks, parse_description)
#            st.write(parsed_result)