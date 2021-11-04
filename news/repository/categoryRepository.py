from news.models import category_product

def getCategory():
    listCategory = None
    listCategory = category_product.objects.all()
    return listCategory