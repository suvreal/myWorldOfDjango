from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second', views.indexSecond, name='indexSecond'),
    path('extra/', views.extraInfoIndex, name='extraInfoIndex'),
    path('all/', views.allPeoples, name='allPeoples'),
    path('addpeoples/', views.addPeoples, name='addPeoples'),
    path('addpeoples/addpeoplerecord/', views.addPeopleRecord, name='addPeopleRecord'),
    path('all/delete/<int:id>', views.deletePeopleRecord, name='deletePeopleRecord'),
    path('all/update/<int:id>', views.updatePeoples, name='updatePeoples'),
    path('all/update/updatePeopleRecord/<int:id>', views.updatePeopleRecord, name='updatePeopleRecord'),
]
