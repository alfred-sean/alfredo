from rest_framework.exceptions import ParseError
from communities.serializers import CommunityListSerializer
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.exceptions import ParseError

from ..views import CommunityListView
from ..serializers import CommunityListSerializer, CommunityDetailSerializer
from .factories import CommunityFactory


class TestListView(TestCase):
    def setUp(self):
        CommunityFactory(capacity=100)
        CommunityFactory(capacity=300)
        CommunityFactory(capacity=500)

    def test_get_serializer_class(self):
        request = APIRequestFactory()
        request.query_params = {}
        view = CommunityListView(request=request)

        serializer_class = view.get_serializer_class()

        self.assertEqual(serializer_class, CommunityListSerializer)

    def test_get_serializer_class_with_detail_query_param(self):
        request = APIRequestFactory()
        request.query_params = {"detail": True}
        view = CommunityListView(request=request)

        serializer_class = view.get_serializer_class()

        self.assertEqual(serializer_class, CommunityDetailSerializer)

    def test_get_queryset_capacity_lt_gt(self):
        request = APIRequestFactory()
        request.query_params = {"capacity_lt": 400, "capacity_gt": 200}
        view = CommunityListView(request=request)

        queryset = view.get_queryset()

        self.assertEqual(len(queryset), 1)

        community = queryset.first()
        self.assertEqual(community.capacity, 300)

    def test_get_queryset_capacity_lt_gt_raise_error_if_lt_less_than_gt(self):
        request = APIRequestFactory()
        request.query_params = {"capacity_lt": 200, "capacity_gt": 400}
        view = CommunityListView(request=request)

        with self.assertRaises(ParseError):
            view.get_queryset()
