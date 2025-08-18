"""
Django command to wait for the database to be available before proceeding with other commands.
"""
from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
import time

class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...\n")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['users_db'])
                db_up = True
            except (Psycopg2Error, OperationalError) as e:
                self.stdout.write(f"Database unavailable, waiting 1 second - {e}\n")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
