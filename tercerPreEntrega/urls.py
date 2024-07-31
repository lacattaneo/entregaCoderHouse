
from django.contrib import admin
from django.urls import path, include
from appCoder.views import curso

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('AppCoder/', include('appCoder.urls'))
]
