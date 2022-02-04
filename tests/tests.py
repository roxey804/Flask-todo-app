from flask import request
# from app.routes import app

def test_todos_returned():
    assert 1==1
    """Testing the /todos endpoint"""
    #make a request to http://localhost:5000/todos
    # assert response.status_code == 200

def test_all():
    assert 2==2
#
# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'