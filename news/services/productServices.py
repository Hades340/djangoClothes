from news.repository import productRepositiry

def getAllProduct(arg):
    listProduct = None
    try:
        listProduct = productRepositiry.getAllProduct()
    except Exception as e:
        print("Error get all products")
    return listProduct

def getProductByCategoryId(id):
    listProductCategory = None
    try:
        if(bool(id) != False):
            listProductCategory = productRepositiry.getProductByCategoryId(id)
    except Exception as e:
        print("Error get products with category "+id)
    return listProductCategory

def getProductDetailById(idproduct):
    ProductCategory = None
    try:
        if(bool(idproduct)):
            ProductCategory = productRepositiry.getProductDetailById(idproduct)
    except Exception as e:
        print("Error get product with id "+ idproduct)
    return ProductCategory

def getProductBySale():
    productSale = None
    try:
        productSale = productRepositiry.getProductBySale()
    except Exception as e:
        raise e
    
    return productSale

def getProductNews():
    productNews = None
    try:
        productNews = productRepositiry.getProductNew()
    except Exception as e:
        raise e
    
    return productNews

def getProductMore(id):
    productMore = None
    try:
        productMore = productRepositiry.getProductMore(id)
    except Exception as e:
        raise e

    return productMore


def getProductByID(id):
    product = None
    try:
        product = productRepositiry.getProductById(id)
    except Exception as e:
        raise e

    return product