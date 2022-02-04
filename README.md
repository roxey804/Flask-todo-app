# About
A small Flask app that allows the user to create a todo item, view it and delete it.


## Models 
Todo object - id (int), description (str), deadline (datetime) and priority (bool)

## Running the app
*If you are using a virtualenv, ensure that is active!*
**Run the app**
`$ flask run`

**Reload changes**
You will have to restart the app 

## Routes
`/` - takes you to the welcome page that displays some text
`/api` - takes you to the SwaggerUI
`/hello` - renders the index.html template
`/todo` - creates a POST request to add a todo item (use Postman)
`/todo/<id>` - displays an individual todo by id
`/todos` - displays all todos from the db via a html template
`/todo/delete/<id>` - deletes the todo with the specified id DELETE HTTP method (use Postman)

## Testing
Tests are written using pytest and pytest flask
To run test: 

No need for frontend just return data with the API

#TODO:
finish up tests
add DELETE functionality
-Tidyup into db calls with handlers separated out from routes
-CRUD functionality separated from routes.py - single responsibility principle functions should only have 1 responsibility
-This makes things easier to test 
-how to hot-reload?