from django.urls import path
from . import views
from django.conf import settings             
from django.conf.urls.static import static   


urlpatterns = [
        path('', views.index, name='home'),
        path('posts/create/', views.create_post, name='create_post'),
        path('posts/<int:post_id>/update/', views.update_post, name='update_post'),
        path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
        path('<int:post_id>', views.show, name='show'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
