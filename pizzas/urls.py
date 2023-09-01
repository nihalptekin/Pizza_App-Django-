from django.urls import path, include
from .views import home, pizzas, order, my_orders



    #tirnak icinde pathi beirtir daha sonra degisiklik yaparsam ileride diger kodlarlada da degisilik yapmma lazim. 
    # Bu yüzden name verip kolayca geyebiliyorum degisebiliyorum. 
urlpatterns = [
    path('', home, name='home'),
    path('pizzas', pizzas, name='pizzas'),
    path('order/<int:pk>', order, name='order'),
    path('my_orders', my_orders, name='my_orders'),
]

