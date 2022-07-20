import unittest
from os import environ
from app import app, database

class Test(unittest.TestCase):

    def test_db_add_element(self):
        database.append({"name": "Geralt", "animal": "cat"})
        self.assertEqual({"name": "Geralt", "animal": "cat"}, database.__getitem__(0))

    def test_add_animal(self):
        payload = {
            "name":  "Geralt",
            "animal": "cat"}
        response = app.test_client().post('/', data=payload)
        print (response.text)
        assert "[BACKEND] Name: Geralt Animal: cat added to the database" == response.text
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()