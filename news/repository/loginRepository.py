from news.models import customer

def checkLogin(username, password):
   login = None
   login = customer.objects.get(username__exact = username , password__exact = password)
   return login


def insertCustomer(username,password,address,phone):
    count = 0
    if(count == 0):
        customers = customer(username = username, password = password, address = address, phone =phone)
        customers.save()
        count += 1
    
    return bool(count)
    
def updateCustomer(id,address, sdt):
    count =0;
    if count == 0:
        customerFind = customer.objects.get(pk=id)
        if(customerFind != None):
            customerFind.address = address
            customerFind.phone = sdt
            customerFind.save()
            count+=1
    return bool(count)

def getCustomer(id):
    customerFind = None
    try:
        customerFind = customer.objects.get(pk=id)
    except Exception as e:
        print("Can't found")
    return customerFind

        
    