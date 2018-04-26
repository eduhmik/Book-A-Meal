"""
Module contains all the routes required by the API
"""
from app import API as restful
from app import views as funcs

restful.add_resource(funcs.Signup, '/api/v1/auth/signup')
restful.add_resource(funcs.Authentication, '/api/v1/auth/signin')
restful.add_resource(funcs.ForgotPassword, '/api/v1/auth/forgot-password')
restful.add_resource(funcs.add_meal, '/api/v1/meals')
restful.add_resource(funcs.Meal, '/api/v1/meals/<mealId>')
restful.add_resource(funcs.Rsvp, '/api/v1/meal/<mealId>/rsvp')

