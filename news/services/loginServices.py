from news.repository import loginRepository

def login(username,password):
    loginCheck = None
    try:
        loginCheck = loginRepository.checkLogin(username, password)
    except Exception as e:
        print("can not get data to login")
    
    return loginCheck

def insertCustomer(username,password,address,phone):
    InsertResult = "Can't insert customer please try again"
    try:
        if(loginRepository.insertCustomer(username,password,address,phone) == True):
            InsertResult = "Insert customer success"
    except Exception as e:
        print("can not insert data to customer table")

    return InsertResult

def updateCustomer(id, address, sdt):
    result = False
    try:
        if(loginRepository.updateCustomer(id, address, sdt)):
            result = True
    except Exception as e:
        print("can not update data to customer table")
    
    return result

def searchCustomer(id):
    return loginRepository.getCustomer(id)