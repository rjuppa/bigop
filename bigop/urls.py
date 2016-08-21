from django.conf.urls import include, url
from django.contrib import admin

from app.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
