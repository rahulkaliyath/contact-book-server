import jwt


def authenticate(input_data=None):
    # user= input_data['user']
    encoded_jwt=input_data['jwt_token']

    secretKey = 'secret'
    try:
        data = jwt.decode(encoded_jwt,secretKey, algorithms=['HS256'])
    except jwt.exceptions.ExpiredSignatureError:
        return {
        "status": "error",
        "message": "Token has expired"
        },"expired"
    except:
        return  {
        "status": "error",
        "message": "Invalid Token"
        },"error"
    else:
        input_data['user'] = data['user'] 
        return input_data,"success"