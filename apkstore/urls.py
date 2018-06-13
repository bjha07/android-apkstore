from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.main_page , name="main_page"),
    url(r'^addapkdetails/', views.addapkdetails , name="addapkdetails"),
    url(r'^addapksubdetails/', views.addapksubdetails , name="addapksubdetails"),
    url(r'^whatsappmessenger/', views.whatsappmessenger , name="whatsappmessenger"),
    url(r'^previous_version/$', views.previous_version , name="previous_version"),
    url(r'^teamworklogin/', views.teamworklogin , name="teamworklogin"),
    url(r'^teamworkpanel/', views.teamworkpanel , name="teamworkpanel"),
    url(r'^logout_view/', views.logout_view , name="logout_view"),
    url(r'^teamworkhome/', views.teamworkhome , name="teamworkhome"),
    url(r'^addcategory/', views.addcategory , name="addcategory"),
    url(r'^addcategory_bulk/', views.addcategory_bulk , name="addcategory_bulk"),
    url(r'^addsubcategory/', views.addsubcategory , name="addsubcategory"),
    url(r'^userregister/', views.userregister , name="userregister"),
    url(r'^main/', views.main_show , name="main_show"),
    url(r'^softdata_upload/', views.softdata_upload , name="softdata_upload"),
    url(r'^softdata_upload_update/', views.softdata_upload_update , name="softdata_upload_update"),
    url(r'^blog/', views.main_show_new , name="main_show_new"),
    url(r'^alp_new_apps/', views.alp_new_apps , name="alp_new_apps"),
    url(r'^alp_new_games/', views.alp_new_games , name="alp_new_games"),
    url(r'^home/', views.home , name="home"),
    url(r'^alp2_blog/', views.alp2_blog , name="alp2_blog"),
    url(r'^main_page/', views.main_page , name="main_page"),
    url(r'^androidapkstore/', views.open_with_id , name="open_with_id"),
    url(r'^addblog/', views.addblog , name="addblog"),
    url(r'^addblog_bulk/', views.addblog_bulk , name="addblog_bulk"),
    url(r'^search_apps/', views.search_apps , name="search_apps"),

    url(r'^robots/', views.robots , name="robots"),

   
    url(r'^action/shadow-fight-2-games-apps-apk-download-com.nekki.shadowfight/', views.BZDIIODBYN, name="BZDIIODBYN"),
   
]

