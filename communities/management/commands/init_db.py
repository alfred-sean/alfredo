from django.core.management.base import BaseCommand

from communities.factories import CommunityFactory


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument(
            "-n", "--num_facilities", type=int, help="Number of facilities to create"
        )

    def handle(self, *args, **options):
        num_facilities = options.get("num_facilities")
        if not num_facilities:
            num_facilities = 12

        CommunityFactory.create_batch(num_facilities)
