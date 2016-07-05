from django.conf.urls import include, url

urlpatterns = [
    # API
    url(r'^api/', include('users.api.urls'))
]




