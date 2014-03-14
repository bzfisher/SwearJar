from django.conf.urls import patterns, include, url
from swearJarApp import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^userswore/', views.userSwore, name='userSwore'),
    url(r'^userpaid/', views.userPaid, name='userPaid'),
    url(r'^amountdue/', views.amountDue, name='amountDue'),
    url(r'^register/', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^login/', views.user_login, name='login'),
        url(r'^login/', views.user_login, name='login')
    # Examples:
    # url(r'^$', 'swear_jar.views.home', name='home'),
    # url(r'^swear_jar/', include('swear_jar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
