"""
Module contains Meals model
"""
class Meals(object):
    """
    class contains methods that manipulates meal models
    """
    def __init__(self):
        self.meals_dict = {}
    def create_meal(self, mealData):
        """
        creates meals
        """
        name = mealData.get('name')
        if mealData.get('creator') and mealData.get('name'):
            if 'creator' in mealData:
                creator = mealData.get('creator')

                if creator in self.meals_dict:
                    if name in self.meals_dict.get(creator):
                        return {'success':False,
                                'message':'Duplicate meal, choose a different name'}
                    else:
                        user_meals = self.meals_dict.get(creator)
                        user_meals.update({name:mealData})
                        return {'success':True, 'message':'Meal succesfully added'}
                else:
                    new_meal = {creator:{name:mealData}}
                    self.meals_dict.update(new_meal)
                    return {'success':True, 'message':'First Meal added, Hurray!!'}
            else:
                return {'success':False, 'message':'no user field provided'}
        else:
            return {'success':False, 
                    'message':'ensure you have the meal name and your email filled'}

    def getMeals(self):
        """
        gets all meals
        """
        return {'success':True, 'message':self.meals_dict}

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
                return {'success':True, 'message':'Meal deleted'}
            else:
                return {'success':False, 'message':'Meal not found'}
        else:
            return {'success':False, 'message':'user does not have any meals'}
    def getMeal(self, userEmail, mealName):
        """
        gets specific meal
        """
        resp = self.getUserMeals(userEmail)
        if resp.get('success'):
            if resp.get('message').get(mealName):
                return {'success':True, 'message':resp.get('message').get(mealName)}
            else:
                return {'success':False, 'message':'meal does not exist'}
        else:
            return {'success':False, 'message':resp.get('message')}
    def editMeal(self, userEmail, mealName, new_meal):
        """
        edits specific meal
        """
        resp = self.deleteMeal(userEmail, mealName)
        if resp.get('success'):
            resp = self.create_meal(new_meal)
            if resp.get('success'):
                return {'success':True, 'message':'Meal successfully edited'}
            else:
                return {'success':False, 'message':resp.get('message')}
        else:
            return {'success':False, 'message':resp.get('message')}

    def rsvpMeal(self, userEmail, mealName, clientEmail):
        """
        adds rsvpto meal
        """
        if userEmail in self.meals_dict:
            if mealName in self.meals_dict.get(userEmail):
                rsvp = self.meals_dict.get(userEmail).get(mealName).get('rsvp')
                rsvp.append(clientEmail)
                return {'success':True, 'message':rsvp}
            else:
                return {'success':False, 'message':"cannot find the meal"}
        else:
            return {'success':False, 'message':"user does not exist"}
    def getRsvpForMeal(self, userEmail, mealName):
        """
        gets all the rsvp for meal
        """
        if userEmail in self.meals_dict:
            if mealName in self.meals_dict.get(userEmail):
                resp = self.meals_dict.get(userEmail).get(mealName).get('rsvp')
                return {'success':True, 'message':resp}
            else:
                return {'success':False, 'message':"cannot find the meal"}
        else:
            return {'success':False, 'message':'user does not exist'}
