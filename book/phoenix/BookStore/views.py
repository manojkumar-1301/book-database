from django.shortcuts import render, redirect, get_object_or_404
from BookStore.models import UserModel, BookDetail, OrderDetail


# Create your views here.

def login(request):
    if request.method=='POST':
        user=request.POST.get('username')
        paswd=request.POST.get('password')
        try:
            check=UserModel.objects.get(username=user,password=paswd)
            return redirect('ShowBook')

        except:
         pass
    return render(request,'login.html')


def User(request):
    if request.method == 'POST':
        User_Obj=UserModel.objects.create(username=request.POST.get('username'),
                                          userid=request.POST.get('userid'),
                                          password=request.POST.get('password'),
                                          mobilenumber=request.POST.get('mobile_number'),
                                          email=request.POST.get('email'),
                                          gender=request.POST.get('gender'))
        id(User_Obj.id)
        print(id)
        return redirect('ShowUser')
    return render(request, 'usermodel.html')

def Book(request):
    if request.method =='POST':
        Book_Obj=BookDetail.objects.create(Book_Name=request.POST.get('bookname'),
                                           Book_Code=request.POST.get('bookcode'),
                                           Author_Name=request.POST.get('authorname'),
                                           Date=request.POST.get('date'),
                                           Status=request.POST.get('status'),
                                           Created_By=request.POST.get('created_by'),
                                           Created_Date=request.POST.get('created_date'), )
        id(Book_Obj.id)
        print(id)
        return redirect('ShowBook')
    return render(request,"bookdetail.html")

def Order(request):
    if request.method=='POST':
        Order_Obj=OrderDetail.objects.create(Book_Id=request.POST.get('bookId'),
                                            Total_Count=request.POST.get('totalCount'),
                                            Total_Price=request.POST.get('totalPrice'),
                                            Delivery_Date=request.POST.get('deliveryDate'),
                                            Status=request.POST.get('status'),
                                            Created_By=request.POST.get('createdBy'),
                                            Created_Date=request.POST.get('cretedDate'))
        id=Order_Obj.id
        print(id)
        return redirect('ShowOrder')
    return render(request,"orderdetail.html")

def ShowBook(request):
    obj=BookDetail.objects.all()
    return render(request, 'show.html',{'data':obj})

def ShowUser(request):
    obj=UserModel.objects.all()
    return render(request,'showuser.html',{'data':obj})

def ShowOrder(request):
    obj=OrderDetail.objects.all()
    return render(request,'showorder.html',{'data':obj})

def add_order(request):
    return redirect('Order')

def add_book(request):
    return redirect('Book')

def sorder(request):
    return redirect('ShowOrder')

def sbook(request):
    return redirect('ShowBook')

def newacc(request):
    return redirect('User')
def edit(request,pk):
    print(pk)
    obj=BookDetail.objects.get(id=pk)

    if request.method=='POST':
          BookDetail.objects.filter(id=pk).update(Book_Name=request.POST.get('bookname'),
                                           Book_Code=request.POST.get('bookcode'),
                                           Author_Name=request.POST.get('authorname'),

                                           Status=request.POST.get('status'),
                                            )
          return redirect('ShowBook')
    return render(request,'edit.html',{'obj':obj})

def delete(request,pk):
    try:
          BookDetail.objects.filter(id=pk).delete()

          return redirect('ShowBook')
    except:
      pass
    return render(request,'edit.html',{'obj':obj})

def odelete(request,pk):
    try:
          OrderDetail.objects.filter(id=pk).delete()

          return redirect('ShowOrder')
    except:
      pass
    return render(request,'oedit.html',{'obj':obj})

def oedit(request,pk):
    print(pk)
    obj=OrderDetail.objects.get(id=pk)

    if request.method=='POST':
          OrderDetail.objects.filter(id=pk).update(Book_Id=request.POST.get('bookId'),
                                           Total_Count=request.POST.get('totalCount'),
                                           Total_Price=request.POST.get('totalPrice'),
                                           Delivery_Date=request.POST.get('deliveryDate'),
                                           Status=request.POST.get('status')
                                            )
          return redirect('ShowOrder')
    return render(request,'oedit.html',{'obj':obj})

def uedit(request,pk):
    print(pk)
    obj=UserModel.objects.get(id=pk)

    if request.method=='POST':
          UserModel.objects.filter(id=pk).update(username=request.POST.get('username'),
                                          userid=request.POST.get('userid'),
                                          password=request.POST.get('password'),
                                          mobilenumber=request.POST.get('mobile_number'),
                                          email=request.POST.get('email'),
                                          gender=request.POST.get('gender'))

          return redirect('ShowUser')
    return render(request,'uedit.html',{'obj':obj})

def udelete(request,pk):
    try:
          UserModel.objects.filter(id=pk).delete()

          return redirect('ShowUser')
    except:
      pass
    return render(request,'uedit.html',{'obj':obj})