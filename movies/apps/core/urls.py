from django.conf.urls import patterns, url


urlpatterns = patterns('movies.apps.core.views',
    url(r'^/?$', "home", name="home"),
)
