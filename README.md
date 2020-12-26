# Contact Book Server

Contact Book Server is a Flask API which provides basic CRUD functionalities for a Address Book App.

## Technology Used

1. Python
2. Flask
3. MongoDb


## API Endpoints

### /login
User must login with the regitered username and password. The response will be a JWT-Token which will be needed to access other APIs
#### Request body
``` json
{
    "user":"test"
}
```

#### Response

``` json 

```
``` json 
{
    "success": "success",
    "token": "***jwt-token***",
    "user": "test"
}
```

### /create_contact
 Create a new contact and add to Database. Contact must have a unique email id 
#### Request body
``` json
{
    "jwt_token":"ReNV2f0VGzPyJbf9v7RY9q1gie5eW2iIlguEuzpSqoc",
    "email":"superman@dc.com",
    "name":"Kent Clarke"
}
```

#### Response

``` json 
{
    "message": "",
    "status": "success"
}
```
``` json 
{
    "message": "Email Exists",
    "status": "error"
}
```


### /list_contacts
List all the contacts associated with the current user.
#### Request body
``` json
{
    "jwt_token":"***jwt-token***"
}
```
#### Response

``` json 
{
    "message": "",
    "results": [
        {
            "contact_id": "60g33",
            "email": "steverogers@avengers.com",
            "name": "Steve Rogers"
        },
        {
            "contact_id": "2j1d1",
            "email": "thor@avengers.com",
            "name": "Thor Odinson"
        }
    ],
    "status": "success"
}
```



