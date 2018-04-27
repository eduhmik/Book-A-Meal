import unittest
import requests
import json
from app import APP
class TestViews(unittest.TestCase):
    
    def set_up(self):
        self.app = APP.test_client()
        self.user_data = {
            'email': 'user@bright.com',
            'password': 'pass123',
            'username':'test user'
            }
        self.signin_data = {
            'email': 'user@bright.com',
            'password': 'pass123'
        }
        self.meal_data = {
            'name':'Rice and beef',
            'price':'450',
            'rsvp':[]
        }
        self.meal_data2 = {
            'name':'Chicken and chips',
            'price':'500',
            'rsvp':[]
        }

    def test_signup(self):
        resp = self.app.post('/api/v1/auth/signup', data=self.user_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post('/api/v1/auth/signin', data=self.signin_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

    
        resp = self.app.post('/api/v1/auth/forgot-password', data={
            'email': 'user@bright.com',
            'password': 'pass1231234'
        })

        resp = self.app.post('/api/v1/auth/signin', data={
            'email': 'user@bright.com',
            'password': 'pass1231234'
        })
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post('/api/v1/meals', data=self.meal_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.get('/api/v1/meals', data=self.meal_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.delete('/api/v1/meals/11', data=self.meal_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post('/api/v1/meals', data=self.meal_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post("/api/v1/meal/10/rsvp", data={'creator':'1','client_email':'myemail@gmail.com'})
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.get("/api/v1/meal/10/rsvp", data={'client_email':'1'})
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.put("/api/v1/manageRsvp", data={'event_id':'10', 'action':'accept', 'client_email':'myemail@gmail.com'})
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.put("/api/v1/manageRsvp", data={'event_id':'10', 'action':'reject', 'client_email':'myemail@gmail.com'})
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.put('/api/v1/events/10', data=self.meal_data2)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))
