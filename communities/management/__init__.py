from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument(
            "num_facilities", type=int, help="Number of facilities to create"
        )

    def handle(self, *args, **options):
        num_facilities = options.get("num_facilities", 12)
        print(num_facilities)
