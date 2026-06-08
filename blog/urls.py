from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='home'),
        path('<int:post_id>', views.show, name='show'),
]