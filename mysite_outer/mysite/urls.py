from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('dashboard', include('mainApp.urls')),
    path('convert', include('mainApp.urls')),
    path('download', include('mainApp.urls'))
]