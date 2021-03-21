from django.contrib import admin
from django.urls import path
from tours import views
from tours.views import custom_handler404, custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main'),
    path('departure/<str:departure>/', views.departure_view, name='depart'),
    path('tour/<int:tour_id>/', views.tour_view, name='tour'),
]

handler404 = custom_handler404
handler500 = custom_handler500
