def weird(number):
    print("number is",number)
    return number**3
def some_function():
    number = 21
    x = 10
    print("x is",number)

returned_this = some_function()
print(returned_this)

def strange(username):
    print("username is",username)
    return "captain"
def some_function():
    username = "John"
    username = strange("Doe")
    print("username is",username)
returned_this = some_function()
print(returned_this)

  