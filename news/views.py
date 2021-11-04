from django.shortcuts import render,redirect
from django.http import *
from .form import loginForm,registerForm
from django.http import HttpResponseRedirect
from news.services import categoryServices, loginServices,orderServices,productServices
# Create your views here.
def index(request):
    context = {"category":categoryServices.getCategory(),
                "productNew":productServices.getProductNews(),
                "productSale":productServices.getProductBySale()}
    return render(request,"news/index.html",context)

def product(request,product_category):
    context = {"category":categoryServices.getCategory(),
                "productCategory":productServices.getProductByCategoryId(product_category)}
    return render(request,"news/product.html",context)

def productDetail(request, product_id):
    context = {"category":categoryServices.getCategory(),
                "productDetail":productServices.getProductByID(product_id),
                "productMore":productServices.getProductMore(product_id)}
    return render(request,"news/product_detail.html",context)

def login(request):
    messages = None
    if(request.method == 'POST'):
        form = loginForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            result = loginServices.login(username,password)
            if (bool(result) == False):
                messages = 'Username or password is not corrected ! Please try again'
                return render(request,"news/login.html",{'result':messages})
            else:
                request.session['User'] = {'customer':result.username,
                                            'id': result.id,
                                            'address':result.address,
                                            'phone':result.phone}
                #request.session['id'] = result.id
                return HttpResponseRedirect("/")
        else:
            return render(request,"news/login.html",{"result":messages})
    else:
        return render(request,"news/login.html")

def register(request):
    if(request.method == 'POST'):
        form = registerForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            phone = form.cleaned_data["phone"]
            address = form.cleaned_data["address"]
            result = loginServices.insertCustomer(username,password,address,phone)
            alert = "danger"
            if(result == "Insert customer success"):
                alert = "success"
            return render(request,"news/register.html",{'result':result,"alert":alert})
    else:
        return render(request,"news/register.html")

def cart(request):
    total = 0;
    if 'carts' in request.session:
        cart = request.session["carts"]
        for key,value in cart.items():
            total += int(value['thanhtien'])
    context = {"category":categoryServices.getCategory(),"total":total}
    return render(request,"news/cart.html",context)

def logout(request):
    try:
        del request.session['User']
        if 'carts' in request.session:
            del request.session['carts']
        
        return redirect("/")
    except KeyError:
        pass
    return redirect("/")

def pay(request):
    total = 0;
    if 'carts' in request.session:
        cart = request.session["carts"]
        for key,value in cart.items():
            total += int(value['thanhtien'])
    
    context = {"total":total,
                "category":categoryServices.getCategory(),
                "customer":loginServices.searchCustomer(request.session["User"]["id"])}
    return render(request,"news/pay.html",context)


def addCart(request):
    carts = {}
    if request.is_ajax():
        resultCheck = ''
        if 'cart' in request.session:
            carts = request.session["carts"]
        if 'User' in request.session:
            idSP = request.POST.get("id")
            SL = request.POST.get("num")
            mauSac = request.POST.get("color")
            kichCo = request.POST.get("size")
            sp = productServices.getProductDetailById(idSP)
            if idSP in carts.keys():
                itemCart = {
                    'names' : sp.name,
                    'imgs' : str(sp.img),
                    'prices' : sp.price,
                    'soluongs':int(carts[idSP]["soluongs"])+int(SL),
                    'mauSacs':mauSac,
                    'kichCos':kichCo,
                    'thanhtien':int(carts[idSP]["thanhtien"])+(int(SL)*sp.price)
                }
            else:
                itemCart = {
                    'names' : sp.name,
                    'imgs' : str(sp.img),
                    'prices' : sp.price,
                    'soluongs':int(SL),
                    'mauSacs':mauSac,
                    'kichCos':kichCo,
                    'thanhtien': int(SL) * sp.price
                }
            carts[idSP] = itemCart
            request.session['carts'] =  carts
            resultCheck = 'Thêm sản phẩm vào giỏ hàng thành công'
        else: 
            resultCheck = 'Bạn chưa đăng nhập để mua hàng'
    return JsonResponse({"success":resultCheck},status = 200)

def updateCart(request):
    if request.is_ajax():
        cart = request.session["carts"]
        resultCheck = ''
        id = request.POST.get("id")
        num = request.POST.get("soLuong")
        if id in cart.keys():
           upNum = (int(num) - cart[id]["soluongs"])
           cart[id]["soluongs"] += upNum
           cart[id]["thanhtien"] = (cart[id]["soluongs"]*int(cart[id]["prices"]))
           request.session['carts'] =  cart
           resultCheck = 'Tăng số lượng thành công'
        else:
            resultCheck = 'Tăng số lượng thất bại'
    return JsonResponse({"success":resultCheck,"cart":cart},status = 200)

def deleteCart(request):
    resultCheck = ''
    if request.is_ajax():
        cart = request.session["carts"]
        id = request.POST.get("id")
        if id in cart.keys():
            cart[id]["soluongs"] = 0
            del cart[id]
            if(len(cart) == 0):
                del request.session['carts']
                resultCheck = 'Xóa sản phẩm trong giỏ hàng thành công'
            else:
                request.session['carts'] =  cart
                resultCheck = 'Xóa sản phẩm trong giỏ hàng thành công'
        else:
            resultCheck = 'Sản phẩm này không tồn tại trong giỏ hàng'
    return JsonResponse({"success":resultCheck,"cart":cart},status = 200)
    
def updateAddressAndPhoneCustomer(request):
    resultCheck = False
    if request.is_ajax():
        id = request.POST.get("id")
        nameChange = request.POST.get("PhoneChange")
        PhoneChange = request.POST.get("PhoneChange")
        AddressChange = request.POST.get("AddressChange")
        if loginServices.updateCustomer(id,AddressChange,PhoneChange):
            resultCheck = True
    return JsonResponse({"success":resultCheck},status = 200)

def thanhToan(request):
    respontCheck = "Mua hàng không thành công";
    if request.is_ajax():
        cart = request.session["carts"]
        user = request.session['User']
        total = 0;
        for key,value in cart.items():
            total += int(value['thanhtien'])
        if(orderServices.insertOrderAndOderdetail(cart,user["id"],total)):
            respontCheck = "Mua hàng thành công";
    return JsonResponse({"success":respontCheck},status = 200)



