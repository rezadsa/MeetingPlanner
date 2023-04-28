from django.urls import path
from . import views


urlpatterns=[
   path('<int:id>',views.details,name='detail'),
   path('rooms',views.rooms_list,name='rooms'),
   path('form',views.form,name='form'),
]