from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com'),
            User.objects.create_user(username='batman', email='batman@dc.com'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com'),
        ]

        # Create activities
        Activity.objects.create(name='Run', user_email='ironman@marvel.com', team='Marvel')
        Activity.objects.create(name='Swim', user_email='cap@marvel.com', team='Marvel')
        Activity.objects.create(name='Fly', user_email='batman@dc.com', team='DC')
        Activity.objects.create(name='Lift', user_email='wonderwoman@dc.com', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=200)
        Leaderboard.objects.create(team='DC', points=180)

        # Create workouts
        Workout.objects.create(name='Pushups', difficulty='Medium')
        Workout.objects.create(name='Sprints', difficulty='Hard')
        Workout.objects.create(name='Yoga', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
