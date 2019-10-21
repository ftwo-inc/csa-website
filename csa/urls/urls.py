from django.conf.urls import url
from csa import views
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^dash/home/$', views.DashboardView.as_view(), name="csa-dashboard"),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('csa.urls.api'), name="api"),
    url(r'^', include('website.urls.urls'), name="website-page"),
]

if settings.DEBUG:

    urlpatterns += static('/static', document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
