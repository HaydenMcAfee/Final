__author__ = 'faculty'

from application.models import Course, PreRequisite


from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = "adds sample entities to the application"

    def handle(self, *args, **options):
        Course.objects.all().delete()
        PreRequisite.objects.all().delete()

