from django.db.models import query
from news.models import customer, order,order_detail,product
from datetime import date
def insertOder(totalprices,id):
    result = False
    try:
        customerObject = customer.objects.get(pk=int(id))
        today = date.today()
        oders =  order(date_oder = today,id_Customer=customerObject,total=totalprices)
        oders.save();
        result = True
        print(result)
    except Exception as e:
        print("Lỗi thêm đơn hàng")
    return result
def insertOderDetail(order_id,product_id,quantity,total_price):
    result = False
    try:
        
        orderLast = order.objects.get(pk=int(order_id))
        productID = product.objects.get(pk=int(product_id))
        orderDetailNews = order_detail(order_id= orderLast,product_id=productID,quantity=quantity,total_price=total_price)
        orderDetailNews.save()
        result = True
        print("Đã thêm được vào DB")
    except Exception as e:
        print("không thể thêm")

    return result

def itemLast():
    print("ID ")
    orderID = order.objects.all().last()
    print("ID tìm được là ",orderID.id)
    return orderID