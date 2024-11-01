import json
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from workflowapiapi.models import User

@csrf_exempt
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''

    if request.method == 'POST':
        body = request.body.decode('utf-8')
        req_body = json.loads(body)

        # Use the built-in authenticate method to verify
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({
                "valid": True, 
                "token": token.key, 
                "id": authenticated_user.id,
                "username": authenticated_user.username,
                "role": authenticated_user.role
            })
            return HttpResponse(data, content_type='application/json')

        else:
            # Bad login details were provided. So we can't log the user in.
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')

    return HttpResponseNotAllowed(permitted_methods=['POST'])

@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    try:
        new_user = User.objects.create(
            username=req_body['username'],
            password=req_body['password'],  # Note: This should be hashed
            first_name=req_body['first_name'],
            last_name=req_body['last_name'],
            birth_date=req_body['birth_date'],
            phone_number=req_body['phone_number'],
            nickname=req_body['nickname'],
            role=req_body['role']
        )
        
        # Hash the password
        new_user.set_password(req_body['password'])
        new_user.save()

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=new_user)

        # Return the token to the client
        data = json.dumps({
            "token": token.key, 
            "id": new_user.id,
            "valid": True,
            "role": new_user.role
        })
        return HttpResponse(data, content_type='application/json', status=status.HTTP_201_CREATED)
    
    except Exception as ex:
        data = json.dumps({
            "valid": False,
            "error": str(ex)
        })
        return HttpResponse(data, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)