from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('api', views.VisitView)

# Decided to go with generics.ListAPIView to get read only api.

urlpatterns = [
        # path('', include(router.urls)),
        path('', views.VisitView.as_view(), name='api'),
]
