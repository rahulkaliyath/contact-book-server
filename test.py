import unittest
import server
import json

BASE_URL = 'http://localhost:5000/'
jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCIsImV4cCI6MTYwOTE0MTI5NX0.ReNV2f0VGzPyJbf9v7RY9q1gie5eW2iIlguEuzpSqoc"

class TestContactBookAPI(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()
        self.app.testing = True

    def test_user_login(self):
        request_body= {"user":"test"}
        response = self.app.get(BASE_URL + 'login', data=json.dumps(request_body))
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'],"success")

    def test_list_contacts(self):
        request_body = {
            "jwt_token" : jwt_token
        }
        response = self.app.get(BASE_URL + 'list_contacts', data=json.dumps(request_body))
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'],"success")

    def test_list_contacts_with_pagination(self):
        request_body = {
            "jwt_token" : jwt_token
        }
        page = 1
        limit = 3 
        params =  '?page=' + str(page) +'&limit='+ str(limit)
        response = self.app.get(BASE_URL + 'list_contacts'+params,
         data=json.dumps(request_body))
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'],"success")
        self.assertEqual(len(data['results']),limit)

    def test_remove_contact(self):
        request_body={
            "jwt_token":jwt_token,
            "contact_id" : "60g33"
        }
        response = self.app.post(BASE_URL + 'remove_contacts', data=json.dumps(request_body))
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'],"success")


    def test_search_contacts(self):
        request_body={
            "jwt_token":jwt_token,
            "search_string" : "superman"
        }
        response = self.app.post(BASE_URL + 'search_contacts', data=json.dumps(request_body))
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'],"success")

    def test_update_contact(self):
        request_body={
            "jwt_token":jwt_token,
            "email" : "brucewayne@wayneindustries.com",
            "name" : "Bruce Wayne",
            "contact_id" : "7440f",
            "fields_to_update": ["email","name"]
        }
        response = self.app.post(BASE_URL + 'update_contact', data=json.dumps(request_body))
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'],"success")       


if __name__ == "__main__":
    unittest.main()