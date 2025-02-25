# README.md

# EDM Contacts Directory

## Overview
The EDM Contacts Directory is a Python application designed to collect and manage contact information for EDM producers and DJs. Users can input a producer or DJ's name and receive their genre and contact information, including email addresses.

## Features
- Search for artists by name
- Retrieve genre and contact information
- Manage artist contacts efficiently

## Project Structure
```
edm-contacts-directory
├── src
│   ├── app.py               # Entry point of the application
│   ├── database
│   │   ├── contacts.py      # Manage contact information
│   │   └── db_manager.py    # Database connection and interactions
│   ├── models
│   │   └── artist.py        # Artist class definition
│   ├── services
│   │   ├── contact_service.py # Handle contact-related operations
│   │   └── search_service.py  # Search functionality for artists
│   └── utils
│       ├── validators.py     # Input validation functions
│       └── formatters.py     # Output formatting functions
├── data
│   └── artists.json          # JSON file storing artist data
├── tests
│   ├── test_contact_service.py # Unit tests for contact service
│   └── test_search_service.py   # Unit tests for search service
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files to ignore by Git
└── README.md                  # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd edm-contacts-directory
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
streamlit run src/app.py
```

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.