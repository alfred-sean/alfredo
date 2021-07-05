from django.urls import path, include
from rest_framework.routers import DefaultRouter
from communities.views import (
    community_detail_view,
    community_list_view,
)

# communities/
# communities/<uuid>
urlpatterns = [
    path("", community_list_view, name="community_detail"),
    path("<uuid:pk>/", community_detail_view, name="community_detail"),
]
