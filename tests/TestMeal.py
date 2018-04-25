import unittest
from app.Meals import Meals

class TestMeals(unittest.TestCase):
    def setUp(self):
        self.meal = Meals()
        self.meal_data = {
            'name':'test meal',
            'price':'300',
            'rsvp':[]
        }
        self.meal_data2 = {
            'name':'test meal',
            'price':'450',
            'rsvp':[]
        }

    def testcreateMeal(self):
        self.assertTrue(self.meal.create_meal(self.meal_data).get('success')) 
        self.assertEqual(1, len(self.meal.getMeals().get('message')))

    def testGetUserMeals(self):
        self.assertTrue(self.meal.create_meal(self.meal_data).get('success')) 
        self.assertEqual(1, len(self.meal.getMeals().get('message')))

        resp = self.meal.getUserMeals("test@bright.com")
        self.assertTrue(resp.get('success'))
        self.assertEqual(1, len(resp.get('message')))
    def testDuplicateMeal(self):
        self.assertTrue(self.meal.create_meal(self.meal_data).get('success')) 
        self.assertEqual(1, len(self.meal.getMeals().get('message')))

        self.assertFalse(self.meal.create_meal(self.meal_data).get('success')) 
        self.assertEqual(1, len(self.meal.getMeals().get('message')))
    def testDifferentUserSameMealName(self):
        self.assertTrue(self.meal.create_meal(self.meal_data).get('success')) 
        self.assertEqual(1, len(self.meal.getMeals().get('message')))
        self.assertTrue(self.meal.create_meal(self.meal_data2).get('success')) 
        self.assertEqual(2, len(self.meal.getMeals().get('message')))
    def testGetSingleMeal(self):
        self.assertTrue(self.meal.create_meal(self.meal_data).get('success')) 
        self.assertEqual(1, len(self.meal.getMeals().get('message')))

        resp = self.meal.getMeal('test@bright.com','test meal')
        print(resp)
        self.assertTrue(resp.get('success'))
        self.assertIn('creator', resp.get("message"))
    def testRsvpMeal(self):
        self.assertTrue(self.meal.create_meal(self.meal_data).get('success')) 
        self.assertEqual(1, len(self.meal.getmeals().get('message')))
        resp = self.meal.rsvpMeal('test@bright.com','test meal', 'test2@bright.com')
        self.assertTrue(resp.get('success'))
        self.assertIn('test2@bright.com', resp.get('message'))
    def testDeleteMeal(self):
        self.assertTrue(self.meal.create_meal(self.meal_data).get('success')) 
        self.assertEqual(1, len(self.meal.getMeals().get('message')))
        resp = self.meal.deleteMeal('test@bright.com', 'test meal')
        self.assertTrue(resp.get('success')) 
        print(self.meal.getUserMeals("test@bright.com").get('message'))
        self.assertEqual("No meals for this user", self.meal.getUserMeals("test@bright.com").get('message'))
    def testEditMeal(self):
        self.assertTrue(self.meal.create_meal(self.meal_data).get('success')) 
        self.assertEqual(1, len(self.meal.getMeals().get('message')))

        meal_data2 = {
            'name':'mymeal',
            'location':'Nairobi',
            'rsvp':[]
        }

        resp = self.meal.editMeal('test@bright.com', 'test meal', meal_data2)

        print(resp)
        self.assertTrue(resp.get('success'))
        self.assertIn('mymeal', self.meal.getUserMeals("test@bright.com").get('message'))
