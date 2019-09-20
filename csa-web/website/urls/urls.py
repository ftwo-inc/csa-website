from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="website-home-page"),
    url(r'^course/$', views.CourseView.as_view(), name="course-details"),
    url(r'^about/$', views.AboutView.as_view(), name="about-details")
]
