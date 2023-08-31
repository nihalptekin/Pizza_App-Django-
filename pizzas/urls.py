from django.urls import path, include
from .views import home

urlpatterns = [
    #tirnak icinde pathi beirtir daha sonra degisiklik yaparsam ileride diger kodlarlada da degisilik yapmma lazim. 
    # Bu yüzden name verip kolayca geyebiliyorum degisebiliyorum. 
   path('', home, name="home"),

]
