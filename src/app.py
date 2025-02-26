import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
from database.contacts import ContactManager

def search_artist_contact(artist_name):
    """Search for artist contact information online"""
    # Common sources for EDM artist contacts
    search_urls = [
        f"https://www.google.com/search?q={artist_name}+edm+artist+management+contact+email",
        f"https://www.google.com/search?q={artist_name}+booking+contact+email",
        f"https://ra.co/dj/{artist_name.lower().replace(' ', '')}"
    ]
    
    emails = []
    genres = []
    
    for url in search_urls:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Look for email patterns
            email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
            found_emails = re.findall(email_pattern, response.text)
            emails.extend(found_emails)
            
            # Try to find genre information
            genre_keywords = ['techno', 'house', 'trance', 'dubstep', 'drum and bass', 'edm']
            text = soup.get_text().lower()
            found_genres = [genre for genre in genre_keywords if genre in text]
            genres.extend(found_genres)
            
        except Exception as e:
            st.error(f"Error searching {url}: {str(e)}")
    
    return list(set(emails)), list(set(genres))

# Version 1.0.1 - EDM Contacts Directory
def main():
    st.title("EDM Artists Directory")
    
    if 'contact_manager' not in st.session_state:
        st.session_state.contact_manager = ContactManager()
    
    with st.sidebar:
        st.header("Add New Artist Contact")
        new_name = st.text_input("Artist Name")
        new_genre = st.text_input("Genre")
        new_email = st.text_input("Email Contact")
        
        if st.button("Add Contact"):
            if new_name and new_genre and new_email:
                st.session_state.contact_manager.add_contact(new_name, new_genre, new_email)
                st.success(f"Added {new_name} to contacts!")
    
    st.header("Search Artist Contacts")
    search_name = st.text_input("Search for an artist:")
    
    if search_name:
        contact = st.session_state.contact_manager.get_contact(search_name)
        if contact:
            st.success("Artist found!")
            st.write(f"Name: {contact.name}")
            st.write(f"Genre: {contact.genre}")
            st.write(f"Contact: {contact.email}")
        else:
            st.error("Artist not found in directory.")
    
    st.header("All Contacts")
    contacts = st.session_state.contact_manager.list_contacts()
    for name, genre, email in contacts:
        with st.expander(f"{name} - {genre}"):
            st.write(f"Email: {email}")

    st.header("Online Search for Artist Contact Information")
    artist_name = st.text_input("Enter Artist Name:")
    
    if st.button("Search Contact Information"):
        if artist_name:
            with st.spinner(f'Searching for {artist_name}\'s contact information...'):
                emails, genres = search_artist_contact(artist_name)
                
                if emails:
                    st.success("Found Contact Information!")
                    st.subheader("Potential Contact Emails:")
                    for email in emails:
                        st.write(email)
                else:
                    st.warning("No email contacts found")
                    
                if genres:
                    st.subheader("Artist Genres:")
                    st.write(", ".join(genres))

if __name__ == "__main__":
    main()
