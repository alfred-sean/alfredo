from rest_framework import generics, viewsets
from rest_framework.exceptions import ParseError
from .models import Address, Community
from .serializers import (
    CommunityDetailSerializer,
    CommunityListSerializer,
    AddressSerializer,
)

# Create your views here.
class CommunityListView(generics.ListCreateAPIView):
    """
    http://localhost:8005/communities/?capacity_gt=200&capacity_lt=500&detail=True
    """

    queryset = Community.objects.all()
    serializer_class = CommunityListSerializer

    def get_serializer_class(self):
        """
        http://localhost:8005/communities/?detail=True
        """
        if self.request.query_params.get("detail"):
            return CommunityDetailSerializer
        return self.serializer_class

    def get_queryset(self):
        """
        http://localhost:8005/communities/?capacity_gt=200&capacity_lt=500
        """
        queryset = self.queryset.all()

        capacity_lt = self.request.query_params.get("capacity_lt")
        capacity_gt = self.request.query_params.get("capacity_gt")

        if capacity_lt and capacity_gt and capacity_lt < capacity_gt:
            raise ParseError("capacity_gt must be less than capacity_lt")

        if capacity_lt:
            queryset = queryset.filter(capacity__lt=capacity_lt)
        if capacity_gt:
            queryset = queryset.filter(capacity__gt=capacity_gt)
        return queryset


community_list_view = CommunityListView.as_view()


class CommunityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunityDetailSerializer


community_detail_view = CommunityDetailView.as_view()


#
# Here's the same thing, but built with Viewsets
#


class CommunityViewSet(viewsets.ModelViewSet):
    """
    http://localhost:8005/communities/?capacity_gt=200&capacity_lt=500&detail=True
    """

    queryset = Community.objects.all()
    serializer_class = CommunityDetailSerializer

    def get_queryset(self):
        """
        http://localhost:8005/communities/?capacity_gt=200&capacity_lt=500
        """
        queryset = self.queryset.all()

        capacity_lt = self.request.query_params.get("capacity_lt")
        capacity_gt = self.request.query_params.get("capacity_gt")

        if capacity_lt and capacity_gt and capacity_lt < capacity_gt:
            raise ParseError("capacity_gt must be less than capacity_lt")

        if capacity_lt:
            queryset = queryset.filter(capacity__lt=capacity_lt)
        if capacity_gt:
            queryset = queryset.filter(capacity__gt=capacity_gt)
        return queryset


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
