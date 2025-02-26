import streamlit as st
from database.contacts import ContactManager

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

if __name__ == "__main__":
    main()
