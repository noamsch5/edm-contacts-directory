import streamlit as st
from services.search_service import search_artist

def main():
    st.title("EDM Contacts Directory")
    
    producer_name = st.text_input("Enter the producer/DJ name:")
    
    if st.button("Search"):
        if producer_name:
            genre, contact_info = search_artist(producer_name)
            if genre and contact_info:
                st.success(f"Genre: {genre}")
                st.success(f"Contact Information: {contact_info}")
            else:
                st.error("No information found for the given producer/DJ name.")
        else:
            st.warning("Please enter a producer/DJ name.")

if __name__ == "__main__":
    main()