from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('allPost/',views.allPost,name="allPost"),
    path('post/',views.post,name="post"),
    path('details/<int:id>',views.details,name="details"),
    path('updatePost/<int:id>',views.updatePost,name="updatePost"),
    path('category/<int:id>/<int:data>',views.single,name="one_category"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)