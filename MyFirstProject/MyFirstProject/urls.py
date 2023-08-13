from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',include('website.urls')),
    path('admin/', admin.site.urls),
    path('members/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    path('api/',include('api.urls'))
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

