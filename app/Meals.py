"""
Module contains Meals model
"""
class Meals(object):
    """
    class contains methods that manipulates meal models
    """
    def __init__(self):
        self.meals_dict = {}
    def create_meal(self, meal_data):
        """
        creates meals
        """
        name = meal_data.get('name')
        if meal_data.get('creator') and meal_data.get('name'):
            if 'creator' in meal_data:
                creator = meal_data.get('creator')
                if creator in self.meals_dict:
                    if name in self.meals_dict.get(creator):
                        return {'success':False,
                                'message':'Duplicate meal, choose a different name'}
                    else:
                        user_meals = self.meals_dict.get(creator)
                        user_meals.update({name:meal_data})
                        return {'success':True, 'message':'Meal succesfully added'}
                else:
                    new_meal = {creator:{name:meal_data}}
                    self.meals_dict.update(new_meal)
                    return {'success':True, 'message':'First Meal added, Hurray!!'}
            else:
                return {'success':False, 'message':'no user field provided'}
        else:
            return {'success':False, 'message':'ensure you have the meal name and your email filled'}

    def get_meals(self):
        """
        gets all meals
        """
        return {'success':True, 'message':self.meals_dict}
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
                return {'success':True, 'message':'Meal deleted'}
            else:
                return {'success':False, 'message':'Meal not found'}
        else:
            return {'success':False, 'message':'user does not have any meals'}
    def get_meal(self, user_email, meal_name):
        """
        gets specific meal
        """
        resp = self.get_user_meals(user_email)
        if resp.get('success'):
            if resp.get('message').get(meal_name):
                return {'success':True, 'message':resp.get('message').get(meal_name)}
            else:
                return {'success':False, 'message':'meal does not exist'}
        else:
            return {'success':False, 'message':resp.get('message')}
    def edit_meal(self, user_email, meal_name, new_meal):
        """
        edits specific meal
        """
        resp = self.delete_meal(user_email, meal_name)
        if resp.get('success'):
            resp = self.create_meal(new_meal)
            if resp.get('success'):
                return {'success':True, 'message':'Meal successfully edited'}
            else:
                return {'success':False, 'message':resp.get('message')}
        else:
            return {'success':False, 'message':resp.get('message')}
    def rsvp_meal(self, user_email, meal_name, client_email):
        """
        adds rsvpto meal
        """
        if user_email in self.meals_dict:
            if meal_name in self.meals_dict.get(user_email):
                rsvp = self.meals_dict.get(user_email).get(meal_name).get('rsvp')
                rsvp.append(client_email)
                return {'success':True, 'message':rsvp}
            else:
                return {'success':False, 'message':"cannot find the meal"}
        else:
            return {'success':False, 'message':"user does not exist"}
    def get_rsvp_for_meal(self, user_email, meal_name):
        """
        gets all the rsvp for meal
        """
        if user_email in self.meals_dict:
            if meal_name in self.meals_dict.get(user_email):
                resp = self.meals_dict.get(user_email).get(meal_name).get('rsvp')
                return {'success':True, 'message':resp}
            else:
                return {'success':False, 'message':"cannot find the meal"}
        else:
            return {'success':False, 'message':'user does not exist'}
