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
<<<<<<< HEAD
    def signupUser(self, user_data):
        """
        signup users
        """
        resp = self.users.addUser(user_data)
=======
    def sign_up_user(self, user_data):
        """
        signup users
        """
        resp = self.users.add_user(user_data)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return {'success':True, 'message':'user registered'}
        else:
            return {'success':False, 'message':resp.get('message')}
<<<<<<< HEAD
    def signinUser(self, email, password):
        """
        signs us in
        """
        resp = self.users.getUser(email)
=======
    def sign_in_user(self, email, password):
        """
        signs us in
        """
        resp = self.users.get_user(email)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            print(password)
            print(resp.get('message').get('password'))
            if password == resp.get('message').get('password'):
                return {'success':True, 'message':'user credentials verified'}
            else:
                return {'success':False, 'message':'user credentials wrong'}
        else:
            return {'success':False, 'message':resp.get('message')}
<<<<<<< HEAD
    def resetPassword(self, email, newPass):
        """
        resets passwords
        """
        resp = self.users.getUser(email)
        if resp.get('success'):
            user = resp.get('message')
            user['password'] = newPass
            resp = self.users.updateUser(email, user)
=======
    def reset_password(self, email, new_pass):
        """
        resets passwords
        """
        resp = self.users.get_user(email)
        if resp.get('success'):
            user = resp.get('message')
            user['password'] = new_pass
            resp = self.users.update_user(email, user)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
            if resp.get('success'):
                return {'success':True, 'message':'password reset successfully'}
            else:
                return {'success':False, 'message':'password was not reset'}
        else:
            return {'success':False, 'message':resp.get('message')}

<<<<<<< HEAD
    def addMeal(self, mealData):
        """
        creates a meal
        """
        resp = self.meals.create_meal(mealData)
=======
    def add_meal(self, meal_data):
        """
        creates a meal
        """
        resp = self.meals.create_meal(meal_data)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return {'success':True, 'message':'Meal added'}
        else:
            return {'success':False, 'message':resp.get('message')}
<<<<<<< HEAD
    def retrieveMeal(self, email):
        """
        retrieves meals
        """
        resp = self.meals.getUserMeals(email)
=======
    def retrieve_meal(self, email):
        """
        retrieves meals
        """
        resp = self.meals.get_user_meals(email)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            mymeals = []
            for key in resp.get('message'):
                mymeals.append(resp.get('message').get(key))
            return {'success':True, 'message':mymeals}
        else:
            return {'success':False, 'message':resp.get('message')}
<<<<<<< HEAD
    def retriveSingelMeal(self, email, mealname):
        """
        gets single meal
        """
        resp = self.meals.getMeal(email, mealname)
=======
    def retrieve_single_meal(self, email, meal_name):
        """
        gets single meal
        """
        resp = self.meals.get_meal(email, meal_name)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get("success"):
            return {'success':True, "message":resp.get("message")}
        else:
            return {'success':False, "message":resp.get("message")}
<<<<<<< HEAD
    def deleteSingleMeal(self, email, mealname):
        """
        deletes a single meal
        """
        resp = self.meals.deleteMeal(email, mealname)
=======
    def delete_single_meal(self, email, meal_name):
        """
        deletes a single meal
        """
        resp = self.meals.delete_meal(email, meal_name)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return {'success':True, 'message':resp.get('message')}
        else:
            return {'success':False, 'message':resp.get('message')}

<<<<<<< HEAD
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
=======
    def retrieve_all_mealss(self):
        """
        retrieves all meals
        """
        resp = self.meals.get_meals()
        if resp.get('success'):
            resp = resp.get('message')
            meal_list = []
            for key in resp:
                for user_meal in resp.get(key):
                    meal_list.append(resp.get(key).get(user_meal))
            return {'success':True, 'message':meal_list}
        else:
            return {'success':False, 'message':resp.get('message')}

    def retrieveMenu(self):
        """
        retrieves menu
        """
        resp = self.meals.get_meals()
        if resp.get('success'):
            resp = resp.get('message')
            meal_list = []
            for key in resp:
                for user_meal in resp.get(key):
                    meal_list.append(resp.get(key).get(user_meal))
            return {'success':True, 'message':meal_list}
        else:
            return {'success':False, 'message':resp.get('message')}

    def add_rsvp(self, user_email,meal_name,email):
        """
        adds a rsvp to meal
        """
        rsvpresp = self.meals.rsvp_meal(user_email, meal_name, email)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if rsvpresp.get('success'):
            return {'success':True, 'message':rsvpresp.get('message')}
        else:
            return {'success':False, 'message':rsvpresp.get('message')}
<<<<<<< HEAD
    def retriveRsvp(self, email, meal):
=======
    def retrieve_rsvp(self, email, meal):
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        """
        retrieves all rsvp for single user
        """
        resp = self.meals.getRsvpForMeal(email, meal)
        return resp
                      