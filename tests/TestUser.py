import unittest
from app.Users import Users

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = Users()
        self.user_data = {
                'email': 'user@bright.com',
                'password': 'pass123',
                'username':'test user'
            }
        self.user_data2 = {
                'email': 'user2@bright.com',
                'password': 'pass123',
                'username':'test user'
            }

    def testusercreation(self):
        self.assertTrue(self.user.add_user(self.user_data).get('success')) 
        self.assertEqual(1, len(self.user.get_users().get('message')))

    def testduplicateuseraddition(self):
        self.assertTrue(self.user.add_user(self.user_data).get('success')) 
        self.assertEqual(1, len(self.user.get_users().get('message')))

        self.assertFalse(self.user.add_user(self.user_data).get('success')) 
    def testmultipleusercreation(self):
        self.assertTrue(self.user.add_user(self.user_data).get('success')) 
        self.assertEqual(1, len(self.user.get_users().get('message')))

        self.assertTrue(self.user.add_user(self.user_data2).get('success')) 
        self.assertEqual(2, len(self.user.get_users().get('message')))
    def testgetsingleuser(self):
        self.assertTrue(self.user.add_user(self.user_data).get('success')) 
        self.assertEqual(1, len(self.user.get_users().get('message')))

        result = self.user.get_user("user@bright.com").get('message')
        self.assertIn("user@bright.com", result.get('email'))

    def testdelete_user(self):
        self.assertTrue(self.user.add_user(self.user_data).get('success')) 
        self.assertEqual(1, len(self.user.get_users().get('message')))

        self.assertTrue(self.user.add_user(self.user_data2).get('success')) 
        self.assertEqual(2, len(self.user.get_users().get('message')))

        self.assertTrue(self.user.delete_user("user@bright.com").get('success'))
        self.assertEqual(1, len(self.user.get_users().get('message')))

    def testupdateuser(self):
        self.assertTrue(self.user.add_user(self.user_data).get('success')) 
        self.assertEqual(1, len(self.user.get_users().get('message')))
        new_data = {
            'email':'another@email.com',
            'password':'mypass123',
            'username':'user tested'
        }
        userresult = self.user.update_user("user@bright.com", new_data)
        self.assertTrue(userresult.get('success'))
        result = self.user.get_user("another@email.com")
        self.assertIn("user tested", result.get('message').get('username'))
        