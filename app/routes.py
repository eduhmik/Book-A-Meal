"""
Module contains all the routes required by the API
"""
from app import API as restful
from app import views as funcs

<<<<<<< HEAD
restful.add_resource(funcs.Signup, '/api/auth/signup')
restful.add_resource(funcs.Signin, '/api/auth/signin')
restful.add_resource(funcs.ForgotPassword, '/api/auth/forgot-password')
restful.add_resource(funcs.AddMeal, '/api/meals')
restful.add_resource(funcs.Meals, '/api/meals/<mealId>')
restful.add_resource(funcs.Rsvp, '/api/event/<mealId>/rsvp')
=======
restful.add_resource(funcs.Signup, '/api/v1/auth/signup')
restful.add_resource(funcs.Authentication, '/api/v1/auth/signin')
restful.add_resource(funcs.ForgotPassword, '/api/v1/auth/forgot-password')
restful.add_resource(funcs.add_meal, '/api/v1/meals')
restful.add_resource(funcs.Meal, '/api/v1/meals/<mealId>')
restful.add_resource(funcs.Rsvp, '/api/v1/meal/<mealId>/rsvp')

>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
