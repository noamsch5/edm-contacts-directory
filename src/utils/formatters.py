def format_artist_info(artist):
    """Format artist information for display."""
    return f"**Name:** {artist['name']}\n**Genre:** {artist['genre']}\n**Contact Info:** {artist['contact_info']}"


def format_contact_list(contacts):
    """Format a list of contacts for display."""
    formatted_contacts = [format_artist_info(contact) for contact in contacts]
    return "\n\n".join(formatted_contacts)