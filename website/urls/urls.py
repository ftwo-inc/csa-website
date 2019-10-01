from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="website-home-page"),
    url(r'^enroll/$', views.EnrollView.as_view(), name="enroll-details"),
    url(r'^about/$', views.AboutView.as_view(), name="about-details"),
    url(r'^privacy/$', views.PrivacyView.as_view(), name="privacy-details")
]
