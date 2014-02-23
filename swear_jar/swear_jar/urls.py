from django.conf.urls import patterns, include, url
from swear_jar_core import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^newuser/', views.newUser, name='newUser'),
    url(r'^userswore/', views.userSwore, name='userSwore'),
    url(r'^userpaid/', views.userPaid, name='userPaid'),
    url(r'^signin/', views.signIn, name='signIn'),
    url(r'^amountdue/', views.amountDue, name='amountDue')
    # Examples:
    # url(r'^$', 'swear_jar.views.home', name='home'),
    # url(r'^swear_jar/', include('swear_jar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
