from django.db.models import query
from news.models import product,product_detail

def getAllProduct():
    listProduct = product.objects.all()
    return listProduct

def getProductByCategoryId(id):
    listProductById = product.objects.filter(category_id__exact = id)
    return listProductById

def getProductDetailById(idproduct):
    productDetail = product.objects.get(pk=int(idproduct))
    return productDetail

def getProductById(idproduct):
    productDetail = product.objects.filter(id=idproduct)
    return productDetail

def getProductBySale():
    #query = "SELECT * FROM news_product where sale = '1' order by id DESC  limit 1"
    return product.objects.filter(sale__exact = '1').order_by("-id")[:1]

def getProductNew():
    return product.objects.all().order_by("-id")[:6]
   
def getProductMore(id):
    query = "select * from news.news_product where category_id_id = '"+str(id)+"' and id != '"+str(id)+"'  order by id DESC limit 3";
    return product.objects.raw(query)