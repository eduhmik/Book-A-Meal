"""
Module contains user model
"""
class Users(object):
    """
    class contains methods to manipulate users
    """
    def __init__(self):
        self.users_dict = {}
<<<<<<< HEAD
    def addUser(self, userData):
        """
        Adds user
        """
        EMAIL = userData.get('email')
        if EMAIL in self.users_dict:
            return {"success":False, 'message':"user with that email already exists"}
        else:
            self.users_dict.update({EMAIL:userData})
            return {"success":True, 'message':"user created successfully"}
    def getUsers(self):
=======
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
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        """
        gets all users
        """
        if self.users_dict:
            return {'success':True, "message":self.users_dict}
        else:
            return {'success':False, "message":'no users in the system yet'}
<<<<<<< HEAD
    def getUser(self, email):
=======
    def get_user(self, email):
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        """
        gets specific user
        """
        if email in self.users_dict:
            return {'success':True, 'message':self.users_dict.get(email)}
        else:
            return {'success':False, 'message':"user not found"} 
<<<<<<< HEAD
    def deleteUser(self, email):
=======
    def delete_user(self, email):
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        """
        deletes user
        """
        if email in self.users_dict:
            self.users_dict.pop(email)
            return {'success':True, 'message':'user deleted'}
        else:
            return {'success':True, 'message':"user does not exist"}
<<<<<<< HEAD
    def updateUser(self, email, newUserData):
        """
        updates user details
        """
        if self.deleteUser(email).get('success'):
            if self.addUser(newUserData).get('success'):
                return {'success':True, 'message':'user details updated'}
            else:
                return {'success':False, 'message':self.addUser(newUserData).get('success').get('message')}
        else:
            return {'success':False, 'message':self.deleteUser(email).get('message')}
=======
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
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
