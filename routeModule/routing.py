from bottle import route, post, request, template,  redirect, response
@route("/")
@route("/index")
def index():
    if isLogged():
        return template("index")
    else:
        redirect("/login")
@route("/user/create")
def userCreate():
    if isLogged():
        return template("Crud/cadastrar")
    else:
        redirect("/login")
@post("/user-register/save")
def userRegister():
    return request.forms.get("firstname")
@route("/user/index")
def userCreate():
    if isLogged():
        return template("Crud/lista")
    else:
        redirect("/login")
@route("/login")
@route("/login/<error>")
def login( error= ''):
    if True is not isLogged():
        return template("Auth/login", error = error)
    return redirect("/index")

@route("/signin", method="POST")
def signIn():
    username = request.forms.get("username")
    password = request.forms.get("password")
    checkSignIn(username,password)

def checkSignIn(username,password):
    d = {"Daniel":"123","Costa":"234","Carlota":"345"}
    print(username, password)
    # print(d.keys())
    # print(d[username])
    if username in d.keys() and d[username] == password:
        response.set_cookie("logged","Yes")
        redirect("/index")
    else:
        redirect("/login/error")
def isLogged():
    ck = request.get_cookie("logged")
    if "Yes" == ck:
        return True
    else:
        return False