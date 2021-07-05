from rest_framework import serializers
from .models import Address, Community


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
        ]


class CommunityDetailSerializer(serializers.ModelSerializer):
    """
    Builds a relationship with the address - address serialized as ordered dict
    >>> CommunityDetailSerializer(community).data
    {
        'address': OrderedDict(
            [
                ('id', 'f019ff54-a417-49fe-9c8b-0ec940164026'),
                ('address_1', '27394 Richard Lock Apt. 047'),
                ('address_2', '25873 Jesse Island Suite 121'),
                ('city', 'West Gloriaville'),
                ('state', 'Kansas'),
                ('zip_code', '33290')
            ]),
        'capacity': 590,
        'description': 'Particular church sport model. Letter until our relate '
                    'trip interview right. Six none seek notice relate '
                    'treatment attention. Within interest inside.',
        'fax_number': '1117910445',
        'id': '0b1901d4-e2b6-40d2-a88b-4cde70492eb8',
        'name': 'Ramos, Gordon and Graham',
        'phone_number': '+1-753-721-1225x2090'
    }
    """

    address = AddressSerializer()

    class Meta:
        model = Community
        fields = [
            "id",
            "name",
            "description",
            "address",
            "capacity",
            "phone_number",
            "fax_number",
        ]


class CommunityListSerializer(serializers.ModelSerializer):
    """
    No address object

    >>> CommunityListSerializer(community).data
    {
        'address': UUID('f019ff54-a417-49fe-9c8b-0ec940164026'),
        'capacity': 590,
        'description': 'Particular church sport model. Letter until our relate '
                    'trip interview right. Six none seek notice relate '
                    'treatment attention. Within interest inside.',
        'fax_number': '1117910445',
        'id': '0b1901d4-e2b6-40d2-a88b-4cde70492eb8',
        'name': 'Ramos, Gordon and Graham',
        'phone_number': '+1-753-721-1225x2090'
    }
    """

    class Meta:
        model = Community
        fields = [
            "id",
            "name",
            "description",
            "capacity",
            "phone_number",
            "fax_number",
        ]
