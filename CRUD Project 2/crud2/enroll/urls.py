from django.urls import path
from . import views 

urlpatterns = [
#     path('', views.add_show, name="addandshow"),
    path('', views.UserAddAndShowView.as_view(), name='addandshow'),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name="deletedata"),
    path('<int:id>/', views.UpdateUserView.as_view(), name="updatedata"),
]

