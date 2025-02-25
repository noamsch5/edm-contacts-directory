class Artist:
    def __init__(self, name, genre, contact_info):
        self.name = name
        self.genre = genre
        self.contact_info = contact_info

    def __repr__(self):
        return f"Artist(name={self.name}, genre={self.genre}, contact_info={self.contact_info})"