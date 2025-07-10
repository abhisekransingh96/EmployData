from django.shortcuts import render
from .forms.forms import EmployeeRegistrationForm,UserForm
from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
print("Abhisek")
def display_toy(request):
    print("Abhisek")
    my_dict={'product1':"car","product2":"Rocket","product3":"bike"}
    return render(request,'myapp/product.html',my_dict)


def display_shirt(request):
    my_dict={'product1':"blue_Shirt","product2":"Red_shirt","product3":"green_shirt"}
    return render(request,'myapp/product.html',my_dict)


def index_link(request):
    return render(request,"myapp/index.html")
# Admin Registration and Login page
def AdminRegg(request):
    if request.method=="POST":
        admin_form=UserForm(request.POST)
        if admin_form.is_valid():
            user = admin_form.save(commit=False)  # Don't save to DB yet
            user.set_password(admin_form.cleaned_data['password'])  # Hash password
            user.save()


    admin_form = UserForm()
    return render(request, 'myapp/admin.html', {'form': admin_form})


# Employee registration and log in page
def  EmpReg(request):
    print('Abhisek')
    if request.method=="POST":
        formdata=EmployeeRegistrationForm(request.POST)

        if formdata.is_valid():
            first_name=formdata.cleaned_data['first_name']
            last_name=formdata.cleaned_data['last_name']
            salary=formdata.cleaned_data['salary']
            email=formdata.cleaned_data['email']
            password=formdata.cleaned_data['password']
            con_password=formdata.cleaned_data['conf_password']

            data=Employee(first_name=first_name,last_name=last_name,salary=salary,email=email,pasword=password,con_password=con_password)
            data.save()

        else:
            return render(request, 'myapp/empreg.html', {'form': formdata})






    formdata=EmployeeRegistrationForm()
    return  render(request,'myapp/empreg.html',{'form':formdata})

#
#
# data=x=Employee.objects.filter(id__range=(0,3))
# >>> data
# <QuerySet [<Employee: Rakesh>, <Employee: gokur>, <Employee: alexa>]>
#
#
# >>> data=x=Employee.objects.filter(id__in=[0,1,2,3,4])
# >>> data
# <QuerySet [<Employee: Rakesh>, <Employee: gokur>, <Employee: alexa>]>
#
# >>> data=x=Employee.objects.all().order_by('salary')
# >>> data
# <QuerySet [<Employee: Rakesh>, <Employee: alexa>, <Employee: gokur>]>
# >>> data=x=Employee.objects.all().order_by('-salary')
# >>> data
# <QuerySet [<Employee: gokur>, <Employee: alexa>, <Employee: Rakesh>]>
#
# >>> data=x=Employee.objects.all().order_by('-salary')[0]
# >>> data
# <Employee: gokur>
#
# >>> data=x=Employee.objects.all().order_by('-salary')[2]
# >>> data
# <Employee: Rakesh>
#
#
# >>> data=x=Employee.objects.values('salary')
# >>> data
# <QuerySet [{'salary': 5000}, {'salary': 12000}, {'salary': 7000}]>
#
# >>> data=x=Employee.objects.values_list('salary')
# >>> data
# <QuerySet [(5000,), (12000,), (7000,)]>
#
#
# >>> data=x=Employee.objects.only('salary')
# >>> for i in data:
# ...     print([i.id,i.salary])
# ...
# [1, 5000]
# [2, 12000]
# [3, 7000]
#
# >>> data=Employee(first_name='Abhisek',last_name='ransingh',salary=20000)
# >>> data.save()
#
# >>> data=Employee.objects.create(first_name='Arjun',last_name='khetriya',salary=20000)
# >>> data
# <Employee: Arjun>
#
#
# >>> data=[Employee(first_name='john',last_name='td',salary=2000),Employee(first_name='Alice',last_name='gd',salary=2000000)]
# >>> data
#
# from django.db.models import Avg,Sum,Min,Max,Count
# >>> data=x=Employee.objects.all().aggregate(Avg("salary"))
# >>> data
# {'salary__avg': 12800.0}
# >>> data=x=Employee.objects.all().aggregate(Sum("salary"))
# >>> data
# {'salary__sum': 64000}
# >>> data=x=Employee.objects.all().aggregate(Min("salary"))
# >>> data
# {'salary__min': 5000}
# >>> data=x=Employee.objects.all().aggregate(Max("salary"))
# >>> data
# {'salary__max': 20000}
# >>> data=x=Employee.objects.all().aggregate(Count("salary"))
# >>> data
# {'salary__count': 5}
#
# data=x=Employee.objects.get(id=1)
#  data.first_name="syam"
#  data.save()



