from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('brands.urls')),
    path('api/v1/', include('colors.urls')),

]
