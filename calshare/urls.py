from django.conf.urls import url, include
from .views import urlpatterns


urlpatterns = [
    url(r'^api/', include(urlpatterns)),
]
