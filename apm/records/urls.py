from django.urls import path

from . import views

urlpatterns = [
    path('track/<int:play_id>/', views.track),
    path('plays/', views.register_play),
]
