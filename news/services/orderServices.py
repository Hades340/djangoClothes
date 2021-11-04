from news.repository import orderRepository

def insertOrderAndOderdetail(cart,id_customer,total):
    result = False
    try:
       if orderRepository.insertOder(total,id_customer):
           order = orderRepository.itemLast()
           for key, value in cart.items():
                print(value["soluongs"])
                print(value["thanhtien"])
                if orderRepository.insertOderDetail(order.id,key,value["soluongs"],value["thanhtien"]):
                    result = True
                else:
                    result = False        
    except Exception as e:
        print(result)
    return result