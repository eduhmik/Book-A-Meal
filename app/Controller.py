"""
Module contains the controller
"""
from app.Users import Users
from app.Meals import Meals
class Controller(object):
    """
    Class manipulates models
    """
    def __init__(self):
        self.users = Users()
        self.meals = Meals()
    def signupUser(self, user_data):
        """
        signup users
        """
        resp = self.users.addUser(user_data)
        if resp.get('success'):
            return {'success':True, 'message':'user registered'}
        else:
            return {'success':False, 'message':resp.get('message')}
    def signinUser(self, email, password):
        """
        signs us in
        """
        resp = self.users.getUser(email)
        if resp.get('success'):
            print(password)
            print(resp.get('message').get('password'))
            if password == resp.get('message').get('password'):
                return {'success':True, 'message':'user credentials verified'}
            else:
                return {'success':False, 'message':'user credentials wrong'}
        else:
            return {'success':False, 'message':resp.get('message')}
    def resetPassword(self, email, newPass):
        """
        resets passwords
        """
        resp = self.users.getUser(email)
        if resp.get('success'):
            user = resp.get('message')
            user['password'] = newPass
            resp = self.users.updateUser(email, user)
            if resp.get('success'):
                return {'success':True, 'message':'password reset successfully'}
            else:
                return {'success':False, 'message':'password was not reset'}
        else:
            return {'success':False, 'message':resp.get('message')}

    def addMeal(self, mealData):
        """
        creates a meal
        """
        resp = self.meals.create_meal(mealData)
        if resp.get('success'):
            return {'success':True, 'message':'Meal added'}
        else:
            return {'success':False, 'message':resp.get('message')}
    def retrieveMeal(self, email):
        """
        retrieves meals
        """
        resp = self.meals.getUserMeals(email)
        if resp.get('success'):
            mymeals = []
            for key in resp.get('message'):
                mymeals.append(resp.get('message').get(key))
            return {'success':True, 'message':mymeals}
        else:
            return {'success':False, 'message':resp.get('message')}
    def retriveSingelMeal(self, email, mealname):
        """
        gets single meal
        """
        resp = self.meals.getMeal(email, mealname)
        if resp.get("success"):
            return {'success':True, "message":resp.get("message")}
        else:
            return {'success':False, "message":resp.get("message")}
    def deleteSingleMeal(self, email, mealname):
        """
        deletes a single meal
        """
        resp = self.meals.deleteMeal(email, mealname)
        if resp.get('success'):
            return {'success':True, 'message':resp.get('message')}
        else:
            return {'success':False, 'message':resp.get('message')}

    def retrieveAllMeals(self):
        """
        retrieves all meals
        """
        resp = self.meals.getMeals()
        if resp.get('success'):
            resp = resp.get('message')
            MEALLIST = []
            for key in resp:
                for USERMEAL in resp.get(key):
                    MEALLIST.append(resp.get(key).get(USERMEAL))
            return {'success':True, 'message':MEALLIST}
        else:
            return {'success':False, 'message':resp.get('message')}
    def addRsvp(self, useremail,mealname,email):
        """
        adds a rsvp to meal
        """
        rsvpresp = self.meals.rsvpMeal(useremail, mealname, email)
        if rsvpresp.get('success'):
            return {'success':True, 'message':rsvpresp.get('message')}
        else:
            return {'success':False, 'message':rsvpresp.get('message')}
    def retriveRsvp(self, email, meal):
        """
        retrieves all rsvp for single user
        """
        resp = self.meals.getRsvpForMeal(email, meal)
        return resp
                      