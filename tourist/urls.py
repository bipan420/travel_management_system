from django.urls import path
from .views import AddTouristsView,AllTouristView,editTourist,deleteTourist
# editTourist,AllTouristView,deleteTourist

urlpatterns = [
    path('add-tourist/',AddTouristsView.as_view(),name='add_tourist'),
    path('edit/<int:id>/',editTourist,name='edit_tourist'),
    path('all-tourist/',AllTouristView.as_view(),name='all_tourist'),
    path('delete/<int:id>/',deleteTourist,name='delete_tourist')
 ]
