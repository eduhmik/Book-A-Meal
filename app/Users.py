"""
Module contains user model
"""
class Users(object):
    """
    class contains methods to manipulate users
    """
    def __init__(self):
        self.users_dict = {}
    def add_user(self, user_data):
        """
        Adds user
        """
        EMAIL = user_data.get('email')
        if EMAIL in self.users_dict:
            return {"success":False, 'message':"user with that email already exists"}
        else:
            self.users_dict.update({EMAIL:user_data})
            return {"success":True, 'message':"user created successfully"}
    def get_users(self):
        """
        gets all users
        """
        if self.users_dict:
            return {'success':True, "message":self.users_dict}
        else:
            return {'success':False, "message":'no users in the system yet'}
    def get_user(self, email):
        """
        gets specific user
        """
        if email in self.users_dict:
            return {'success':True, 'message':self.users_dict.get(email)}
        else:
            return {'success':False, 'message':"user not found"} 
    def delete_user(self, email):
        """
        deletes user
        """
        if email in self.users_dict:
            self.users_dict.pop(email)
            return {'success':True, 'message':'user deleted'}
        else:
            return {'success':True, 'message':"user does not exist"}
    def update_user(self, email, new_user_data):
        """
        updates user details
        """
        if self.delete_user(email).get('success'):
            if self.add_user(new_user_data).get('success'):
                return {'success':True, 'message':'user details updated'}
            else:
                return {'success':False, 'message':self.add_user(new_user_data).get('success').get('message')}
        else:
            return {'success':False, 'message':self.delete_user(email).get('message')}
