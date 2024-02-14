from django.shortcuts import render,redirect,get_object_or_404
from crudapp.models import Employees

# Create your views here.
def index(request):
    emp = Employees.objects.all()
    context={
        'emp':emp,
    }
    return render(request,'index.html',context)

def add(request):
    if request.method == "POST":
       vname=request.POST.get('name')
       vemail=request.POST.get('email')
       vaddress=request.POST.get('address') 
       vphone=request.POST.get('phone') 

       add=Employees(
           name=vname,
           email=vemail,
           address=vaddress,
           phone=vphone



       ) 
       add.save()     
       return redirect('index')
    return render(request,'index.html')

def edit(request):
    emp = Employees.objects.all()
    context={
        'emp':emp,
    }
    return render(request,'index.html',context)

def update(request,id):
    if request.method == "POST":
       vname=request.POST.get('name')
       vemail=request.POST.get('email')
       vaddress=request.POST.get('address') 
       vphone=request.POST.get('phone') 

       update=Employees(
           id=id,
           name=vname,
           email=vemail,
           address=vaddress,
           phone=vphone
           ) 
       update.save()     
       return redirect('index')
    return render(request,'index.html')
# def update(request, id):
#     employee = get_object_or_404(Employees, id=id)

#     if request.method == "POST":
#         vname = request.POST.get('name')
#         vemail = request.POST.get('email')
#         vaddress = request.POST.get('address')
#         vphone = request.POST.get('phone')

#         # Update the existing object fields
#         employee.name = vname
#         employee.email = vemail
#         employee.address = vaddress
#         employee.phone = vphone

#         # Save the updated object
#         employee.save()

#         return redirect('index')
#     return render(request,'index.html')


def delete(request, id):
    if request.method == 'POST':
        emp = get_object_or_404(Employees, id=id)
        emp.delete()
        return redirect('index')
    # Handle GET requests or other methods if neede



   