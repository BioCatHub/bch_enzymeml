import unittest
from mainapp import app


class FlaskrestxTest(unittest.TestCase):
    """
    Unit tests defined for mainapp.py
    """
    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.client = app.test_client()

    def test_create_app(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()