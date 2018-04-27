"""
This module includes all the logic triggered by endpoints
"""
from functools import wraps
from app.Controller import Controller
from app.EndPointParams import SignupParams, SigninParams, MealParams, ResetParams, RsvpParams

<<<<<<< HEAD
from flask_restful import  Resource
=======
from flask_restful import Resource
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
from flask import session


CONTROLLER = Controller()

<<<<<<< HEAD
def auth_required(func):
    """Wrapper to check user authorization"""
    @wraps(func)
    def auth(*args, **kargs):
        """checks for if the user is logged in through the session"""
        if not session['signed_in']:
            return {"success":False,
                    'message': 'Authentication is required to access this resource'}, 401
        return func(*args, **kargs)
    return auth

=======
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
class Signup(SignupParams, Resource):
    """
    Class provides logic for signing up a user
    """
    def post(self):
        """
        listens for a post request then registers user
        """
        args = self.param.parse_args()
        user_data = {
            "username":args['username'],
            "email":args['email'],
            "password":args['password']
        }
<<<<<<< HEAD
        resp = CONTROLLER.signupUser(user_data)
=======
        resp = CONTROLLER.sign_up_user(user_data)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401
<<<<<<< HEAD
=======
        
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
class Authentication(SigninParams, Resource):
    """
    Class contains logic that authenticates the users
    """
    def get(self):
        """
        Triggered by a get request and logs out the user
        """
        if 'user' in session:
            session.pop('user')
            session['signed_in'] = False

            return {'success':True, 'message':'user signed out'}
        else:
            return {'success':False, 'message':'Try logging in first :-)'}
    def post(self):
        """
        Triggered by a post request and logs in the user
        """
        args = self.param.parse_args()
<<<<<<< HEAD
        resp = CONTROLLER.signinUser(args['email'], args['password'])
=======
        resp = CONTROLLER.sign_in_user(args['email'], args['password'])
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            session['user'] = args['email']
            session['signed_in'] = True
            return resp, 201
        else:
            return resp, 401
<<<<<<< HEAD
class ResetPassword(ResetParams, Resource):
=======
class ForgotPassword(ResetParams, Resource):
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
    """
    Class contains logic to reset users password
    """
    @auth_required
    def post(self):
        """
        Triggered by a post request and resets users password
        """
        args = self.param.parse_args()
<<<<<<< HEAD
        resp = CONTROLLER.resetPassword(args['email'], args['password'])
=======
        resp = CONTROLLER.reset_password(args['email'], args['password'])
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401

<<<<<<< HEAD
class CreateMeal(MealParams, Resource):
=======
class add_meal(MealParams, Resource):
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
    """
    Class contains logic to add and retrieve meal
    """
    @auth_required
    def get(self):
        """
        Triggered by get request and retrieves all meals
        """
<<<<<<< HEAD
        resp = CONTROLLER.retrieveAllMeals()
=======
        resp = CONTROLLER.retrieve_all_mealss()
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401
    @auth_required
    def post(self):
        """
        Triggered by a post request and adds a meal
        """
        args = self.param.parse_args()
<<<<<<< HEAD
        event_data = {
=======
        meal_data = {
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
            'name':args['name'],
            'price':args['price'],
            'rsvp':[]
        }
<<<<<<< HEAD
        resp = CONTROLLER.addMeal(meal_data)
=======
        resp = CONTROLLER.add_meal(meal_data)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401
class Meal(Resource):
    """
    Class contains logic to retrieveeingle meal and delete meals
    """
    @auth_required
<<<<<<< HEAD
    def put(self, eventId):
        """
        Triggered by a put request and retrieves a single meal
        """
        resp = CONTROLLER.retriveSingelMeal(session['user'], mealId)
=======
    def put(self, mealId):
        """
        Triggered by a put request and retrieves a single meal
        """
        resp = CONTROLLER.retrieve_single_meal(session['user'], mealId)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409
    @auth_required
    def delete(self, mealId):
        """
        triggered by a delete request and deletes meal specified
        """
<<<<<<< HEAD
        resp = CONTROLLER.deleteSingleMeal(session['user'], mealId)
=======
        resp = CONTROLLER.delete_single_meal(session['user'], mealId)
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409
class Menu(Resource):
    """
    Class contains logic to retrieve menu 
    """
    @auth_required
    def get(self, menu):
        """
        Triggered by a put request and retrieves menu
        """
        resp = CONTROLLER.retriveMenu(session['user'], menu)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409
<<<<<<< HEAD
=======
    @auth_required
    def post(self):
        """
        Triggered by a post request and adds a menu
        """
        args = self.param.parse_args()
        meal_data = {
            'name':args['name'],
            'price':args['price'],
            'rsvp':[]
        }
        resp = CONTROLLER.add_meal(meal_data)
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401
   
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
class Rsvp(RsvpParams, Resource):
    """
    Class manipulates Rsvp of meals
    """
    @auth_required
    def post(self, mealId):
        """
        Triggered by a post method and adds user to rsvp list
        """
        args = self.param.parse_args()
<<<<<<< HEAD
        resp = CONTROLLER.addRsvp(session['user'], mealId, args['clientEmail'])
=======
        resp = CONTROLLER.add_rsvp(session['user'], mealId, args['client_email'])
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409
    @auth_required
    def get(self, mealId):
        """
        Triggered ny get and retrieves a single rsvp
        """
        args = self.param.parse_args()
<<<<<<< HEAD
        resp = CONTROLLER.retriveRsvp(args['clientEmail'], mealId)
=======
        resp = CONTROLLER.retrieve_rsvp(args['client_email'], mealId)
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409