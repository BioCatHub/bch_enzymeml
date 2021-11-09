import unittest

from mainapp import AppInitializer


class FlaskrestxTest(unittest.TestCase):
    """
    Unit tests defined for mainapp.py
    """

    def setUp(self):
        app = AppInitializer.create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_create_app(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()