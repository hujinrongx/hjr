from django.conf.urls import url
from app import views
urlpatterns = [
    url(r'^inbasics/$',views.inbasics),
    url(r'^main/$',views.main),
    url(r'^loginn/$',views.loginn),
    url(r'^login/$',views.login),
    url(r'^zhuce/$',views.zhucea),
    url(r'^zhucee/$',views.zhucee),
    url(r'^upphoto/$',views.up_photo),
    url(r'^upload/$',views.upload),
    url(r'^vip/$',views.vip),
    url(r'^ziliao/$',views.ziliao),
    url(r'^dubai/$',views.dubai),
    url(r'^indubai/$',views.indubai),
    url(r'^user5/$',views.user5),
    url(r'^inuser5/$',views.inuser5),
    url(r'^user6/$', views.user6),
    url(r'^inuser6/$', views.inuser6),
    url(r'^user7/$', views.user7),
    url(r'^inuser7/$', views.inuser7),
    url(r'^user8/$', views.user8),
    url(r'^inuser8/$', views.inuser8),
    url(r'^user9/$', views.user9),
    url(r'^inuser9/$', views.inuser9),
    url(r'^user10/$', views.user10),
    url(r'^inuser10/$', views.inuser10),
    url(r'^select/$', views.select),
    url(r'^sousuo/$', views.sousuo),
    url(r'^sel/$', views.select),
    url(r'^sai/$', views.sai),
    url(r'^s/$', views.s),



]