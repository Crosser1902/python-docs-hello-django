from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
    path('riaz/',views.riaz),
    path('runoob/',views.runoob)
]
