from django.urls import path

from startup.api.views import api_detail_startup_view

app_name='startup'

urlpatterns = [
    path('<slug>/', api_detail_startup_view, name='detail')

    ]