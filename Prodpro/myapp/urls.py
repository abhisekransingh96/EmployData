from django.urls import path
from .views import  index_link,display_toy,display_shirt,EmpReg,AdminRegg

urlpatterns = [

    path('',index_link),
    path('toy',display_toy),
    path('Shirt',display_shirt),
    path('emp',EmpReg),
    path('admin',AdminRegg),


]
