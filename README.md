# Contact Book Server

Contact Book Server is a Flask API which provides basic CRUD functionalities for a Address Book App.


## Technology Used

1. Python
2. Flask
3. MongoDb

____

## Setup

1. Make sure you have Python3 
2. pip install -r requirements.txt
3. Run ``` python3 server.py ```

____

## API Endpoints

## POST /login
User must login with the regitered username and password. The response will be a JWT-Token which will be needed to access other APIs
#### Request body
``` json
{
    "user":"test"
}
```

#### Response
``` json 
{
    "success": "success",
    "token": "***jwt-token***",
    "user": "test"
}
```

## POST /create_contact
 Create a new contact and add to Database. Contact to add must have a unique email id 
#### Request body
``` json
{
    "jwt_token":"***jwt-token***",
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


## GET /list_contacts
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
API also supports Pagination with result limit within a page

eg:
``` html
/list_contacts/page=1&limit=10
```

## POST /remove_contact
Removes the contact from current users contact list.
#### Request body
``` json
{
    "jwt_token":"***jwt-token***",
    "contact_id" : "60g33"
}
```

#### Response

``` json 
{
    "message": "",
    "status": "success"
}
```

## GET /search_contacts
API returns a list of contacts matching either name or email. The search is done by MondoDB text search index. 
#### Request body
``` json
{
    "jwt_token":"***jwt-token***",
    "search_string":"superman"
}
```

#### Response

``` json 
{
    "message": "",
    "results": [
        {
            "contact_id": "jj4gd",
            "email": "superman@dc.com",
            "name": "Kent Clarke",
            "score": 0.6666666666666666
        }
    ],
    "status": "success"
}
```

## POST /update_contact
Updates the current users name, email or both.
#### Request body
``` json
{
    "jwt_token":"***jwt-token***",
    "email" : "brucewayne@wayneindustries.com",
    "name" : "Bruce Wayne",
    "contact_id" : "7440f",
    "fields_to_update": ["email","name"]
}
```

#### Response

``` json 
{
    "message": "",
    "status": "success"
}
```
## POST /add_contacts
Add existing contact to current users contact list.
#### Request body
``` json
{
    "jwt_token":"***jwt-token***",
    "contact_ids" : ["60g33"]
}
```

#### Response

``` json 
{
    "message": "",
    "status": "success"
}
```

## Unit Testing APIs
 1. cd into contact-book-server 
 2. Run ``` python3 test.py ```