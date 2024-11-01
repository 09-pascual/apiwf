import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from workflowapiapi.models import User

# With this file I can use to create auth tokens, auth_user with password without it having to be in model 

@csrf_exempt
def register_user(request):
    try:
        req_body = json.loads(request.body.decode())
        
        # First create auth user for password/token
        auth_user = AuthUser.objects.create_user(
            username=req_body['username'],
            password=req_body['password']
        )
        
        # Create token
        token = Token.objects.create(user=auth_user)
        
        # Create your custom user without password
        custom_user = User.objects.create(
            username=req_body['username'],
            first_name=req_body['first_name'],
            last_name=req_body['last_name'],
            birth_date=req_body['birth_date'],
            phone_number=req_body['phone_number'],
            nickname=req_body['nickname'],
            role=req_body['role']
        )
        
        data = json.dumps({
            "valid": True,
            "token": token.key,
            "user_id": custom_user.id,
            "username": custom_user.username,
            "role": custom_user.role
        })
        return HttpResponse(data, content_type='application/json')
            
    except Exception as ex:
        # If anything fails, cleanup any created users
        if 'auth_user' in locals():
            auth_user.delete()
        if 'custom_user' in locals():
            custom_user.delete()
            
        data = json.dumps({
            "valid": False,
            "error": str(ex)
        })
        return HttpResponse(data, content_type='application/json')

@csrf_exempt
def login_user(request):
    try:
        body = request.body.decode('utf-8')
        req_body = json.loads(body)
        
        # Authenticate using auth_user
        auth_user = authenticate(username=req_body['username'], 
                               password=req_body['password'])
        
        if auth_user is not None:
            # Get your custom user
            custom_user = User.objects.get(username=auth_user.username)
            # Get or create token
            token, created = Token.objects.get_or_create(user=auth_user)
            
            data = json.dumps({
                "valid": True,
                "token": token.key,
                "user_id": custom_user.id,
                "username": custom_user.username,
                "role": custom_user.role
            })
            return HttpResponse(data, content_type='application/json')
        else:
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')
            
    except Exception as ex:
        data = json.dumps({
            "valid": False,
            "error": str(ex)
        })
        return HttpResponse(data, content_type='application/json')