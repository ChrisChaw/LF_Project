from django.conf.urls import url
from api import views
urlpatterns = [
    url(r'^degreecourse/$',views.DegreeCourse.as_view()),
    url(r'^degreecourse/(?P<pk>\d+)/$',views.DegreeCourseDetail.as_view()),

    url(r'^course/$', views.Course.as_view()),
    url(r'^course/(?P<pk>\d+)/$', views.CourseDetail.as_view()),
]
