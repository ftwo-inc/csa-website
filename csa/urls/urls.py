from django.conf.urls import url
from csa import views

urlpatterns = [
    url(r'^dash/home/$', views.DashboardView.as_view(), name="csa-dashboard")
]
