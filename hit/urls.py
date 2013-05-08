from django.conf.urls import patterns, include, url
from nav import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r"^session/$", views.session, name='session'),
	url(r"^session/submitwork/$", views.submitwork, name='submitwork'),
    # Examples:
    # url(r'^$', 'hit.views.home', name='home'),
    # url(r'^hit/', include('hit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
