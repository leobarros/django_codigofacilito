from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codigofacilito.views.home', name='home'),
    # url(r'^codigofacilito/', include('codigofacilito.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^$', include('blog.urls')),
    url(r'^codigofacilito/blog', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
