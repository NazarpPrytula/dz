from django.contrib import admin
from django.urls import path, include
from hw3.views import PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('Post/', include(PostView)),
]