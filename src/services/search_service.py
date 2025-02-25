def search_artist(artist_name, artists_data):
    """
    Searches for an artist in the provided artists data.

    Parameters:
    artist_name (str): The name of the artist to search for.
    artists_data (list): A list of artist dictionaries containing their details.

    Returns:
    dict or None: The artist's details if found, otherwise None.
    """
    for artist in artists_data:
        if artist['name'].lower() == artist_name.lower():
            return artist
    return None

def get_artist_genre_and_contact(artist_name, artists_data):
    """
    Retrieves the genre and contact information of an artist.

    Parameters:
    artist_name (str): The name of the artist.
    artists_data (list): A list of artist dictionaries containing their details.

    Returns:
    tuple: A tuple containing the genre and contact information if found, otherwise (None, None).
    """
    artist = search_artist(artist_name, artists_data)
    if artist:
        return artist['genre'], artist['contact_info']
    return None, None