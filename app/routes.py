"""
Module contains all the routes required by the API
"""
from app import API as restful
from app import views as funcs

restful.add_resource(funcs.Signup, '/api/auth/signup')
restful.add_resource(funcs.Signin, '/api/auth/signin')
restful.add_resource(funcs.ForgotPassword, '/api/auth/forgot-password')
restful.add_resource(funcs.AddMeal, '/api/meals')
restful.add_resource(funcs.Meals, '/api/meals/<mealId>')
restful.add_resource(funcs.Rsvp, '/api/event/<mealId>/rsvp')
