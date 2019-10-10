from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="website-home-page"),
    url(r'^enroll/$', views.EnrollView.as_view(), name="enroll-details"),
    url(r'^about/$', views.AboutView.as_view(), name="about-details"),
    url(r'^privacy/$', views.PrivacyView.as_view(), name="privacy-details"),
    url(r'^industry-speak/$', views.IndustrySpeakView.as_view(), name="industry-speak"),
    url(r'^franchise/$', views.FranchiseView.as_view(), name="franchise"),
    url(r'^courses/$', views.CoursesView.as_view(), name="courses")
]
