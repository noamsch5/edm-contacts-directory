import unittest
from src.services.search_service import search_artist

class TestSearchService(unittest.TestCase):

    def test_search_artist_found(self):
        # Assuming we have a mock artist data for testing
        mock_artist_data = [
            {"name": "DJ Sample", "genre": "House", "contact_info": "dj.sample@example.com"},
            {"name": "Producer Example", "genre": "Techno", "contact_info": "producer.example@example.com"}
        ]
        
        # Mocking the search function to return the mock data
        result = search_artist("DJ Sample", mock_artist_data)
        self.assertEqual(result['name'], "DJ Sample")
        self.assertEqual(result['genre'], "House")
        self.assertEqual(result['contact_info'], "dj.sample@example.com")

    def test_search_artist_not_found(self):
        mock_artist_data = [
            {"name": "DJ Sample", "genre": "House", "contact_info": "dj.sample@example.com"}
        ]
        
        result = search_artist("Unknown DJ", mock_artist_data)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()