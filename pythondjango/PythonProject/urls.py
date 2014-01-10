from django.conf.urls import patterns, include, url
#from blog.views import index
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'PythonProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),//3 method 
#     url(r'^blog/index/$','blog.views.index'),//1
    url(r'^blog/index/$','index'),
#      url(r'^blog/index/(\d{2})/$','index'),
)
