import unittest
from src.services.contact_service import validate_contact_info, format_contact_info

class TestContactService(unittest.TestCase):

    def test_validate_contact_info_valid(self):
        contact_info = {
            'name': 'DJ Example',
            'email': 'dj@example.com',
            'genre': 'House'
        }
        self.assertTrue(validate_contact_info(contact_info))

    def test_validate_contact_info_invalid_email(self):
        contact_info = {
            'name': 'DJ Example',
            'email': 'invalid-email',
            'genre': 'House'
        }
        self.assertFalse(validate_contact_info(contact_info))

    def test_format_contact_info(self):
        contact_info = {
            'name': 'DJ Example',
            'email': 'dj@example.com',
            'genre': 'House'
        }
        formatted_info = format_contact_info(contact_info)
        expected_output = "Name: DJ Example\nEmail: dj@example.com\nGenre: House"
        self.assertEqual(formatted_info, expected_output)

if __name__ == '__main__':
    unittest.main()