"""
Module contains Meals model
"""
class Meals(object):
    """
    class contains methods that manipulates meal models
    """
    def __init__(self):
        self.meals_dict = {}
<<<<<<< HEAD
    def create_meal(self, mealData):
        """
        creates meals
        """
        name = mealData.get('name')
        if mealData.get('creator') and mealData.get('name'):
            if 'creator' in mealData:
                creator = mealData.get('creator')
=======
    def create_meal(self, meal_data):
        """
        creates meals
        """
        name = meal_data.get('name')
        if meal_data.get('creator') and meal_data.get('name'):
            if 'creator' in meal_data:
                creator = meal_data.get('creator')
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c

                if creator in self.meals_dict:
                    if name in self.meals_dict.get(creator):
                        return {'success':False,
                                'message':'Duplicate meal, choose a different name'}
                    else:
                        user_meals = self.meals_dict.get(creator)
<<<<<<< HEAD
                        user_meals.update({name:mealData})
                        return {'success':True, 'message':'Meal succesfully added'}
                else:
                    new_meal = {creator:{name:mealData}}
=======
                        user_meals.update({name:meal_data})
                        return {'success':True, 'message':'Meal succesfully added'}
                else:
                    new_meal = {creator:{name:meal_data}}
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
                    self.meals_dict.update(new_meal)
                    return {'success':True, 'message':'First Meal added, Hurray!!'}
            else:
                return {'success':False, 'message':'no user field provided'}
        else:
<<<<<<< HEAD
            return {'success':False, 
                    'message':'ensure you have the meal name and your email filled'}

    def getMeals(self):
=======
            return {'success':False, 'message':'ensure you have the meal name and your email filled'}

    def get_meals(self):
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        """
        gets all meals
        """
        return {'success':True, 'message':self.meals_dict}

<<<<<<< HEAD
    def getUserMeals(self, userEmail):
        """
        gets a users meals
        """
        if self.meals_dict.get(userEmail):
            return {'success':True, 'message':self.meals_dict.get(userEmail)}
        else:
            return {'success':False, 'message':'No meals for this user'}
    def deleteMeal(self, userEmail, mealName):
        """
        deletes a meal
        """
        if userEmail in self.meals_dict:
            if mealName in self.meals_dict.get(userEmail):
                self.meals_dict.get(userEmail).pop(mealName)
=======
    def get_user_meals(self, user_email):
        """
        gets a users meals
        """
        if self.meals_dict.get(user_email):
            return {'success':True, 'message':self.meals_dict.get(user_email)}
        else:
            return {'success':False, 'message':'No meals for this user'}
    def delete_meal(self, user_email, meal_name):
        """
        deletes a meal
        """
        if user_email in self.meals_dict:
            if meal_name in self.meals_dict.get(user_email):
                self.meals_dict.get(user_email).pop(meal_name)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
                return {'success':True, 'message':'Meal deleted'}
            else:
                return {'success':False, 'message':'Meal not found'}
        else:
            return {'success':False, 'message':'user does not have any meals'}
<<<<<<< HEAD
    def getMeal(self, userEmail, mealName):
        """
        gets specific meal
        """
        resp = self.getUserMeals(userEmail)
        if resp.get('success'):
            if resp.get('message').get(mealName):
                return {'success':True, 'message':resp.get('message').get(mealName)}
=======
    def get_meal(self, user_email, meal_name):
        """
        gets specific meal
        """
        resp = self.get_user_meals(user_email)
        if resp.get('success'):
            if resp.get('message').get(meal_name):
                return {'success':True, 'message':resp.get('message').get(meal_name)}
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
            else:
                return {'success':False, 'message':'meal does not exist'}
        else:
            return {'success':False, 'message':resp.get('message')}
<<<<<<< HEAD
    def editMeal(self, userEmail, mealName, new_meal):
        """
        edits specific meal
        """
        resp = self.deleteMeal(userEmail, mealName)
=======
    def edit_meal(self, user_email, meal_name, new_meal):
        """
        edits specific meal
        """
        resp = self.delete_meal(user_email, meal_name)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            resp = self.create_meal(new_meal)
            if resp.get('success'):
                return {'success':True, 'message':'Meal successfully edited'}
            else:
                return {'success':False, 'message':resp.get('message')}
        else:
            return {'success':False, 'message':resp.get('message')}

<<<<<<< HEAD
    def rsvpMeal(self, userEmail, mealName, clientEmail):
        """
        adds rsvpto meal
        """
        if userEmail in self.meals_dict:
            if mealName in self.meals_dict.get(userEmail):
                rsvp = self.meals_dict.get(userEmail).get(mealName).get('rsvp')
                rsvp.append(clientEmail)
=======
    def rsvp_meal(self, user_email, meal_name, client_email):
        """
        adds rsvpto meal
        """
        if user_email in self.meals_dict:
            if meal_name in self.meals_dict.get(user_email):
                rsvp = self.meals_dict.get(user_email).get(meal_name).get('rsvp')
                rsvp.append(client_email)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
                return {'success':True, 'message':rsvp}
            else:
                return {'success':False, 'message':"cannot find the meal"}
        else:
            return {'success':False, 'message':"user does not exist"}
<<<<<<< HEAD
    def getRsvpForMeal(self, userEmail, mealName):
        """
        gets all the rsvp for meal
        """
        if userEmail in self.meals_dict:
            if mealName in self.meals_dict.get(userEmail):
                resp = self.meals_dict.get(userEmail).get(mealName).get('rsvp')
=======
    def get_rsvp_for_meal(self, user_email, meal_name):
        """
        gets all the rsvp for meal
        """
        if user_email in self.meals_dict:
            if meal_name in self.meals_dict.get(user_email):
                resp = self.meals_dict.get(user_email).get(meal_name).get('rsvp')
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
                return {'success':True, 'message':resp}
            else:
                return {'success':False, 'message':"cannot find the meal"}
        else:
            return {'success':False, 'message':'user does not exist'}
