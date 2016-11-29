from django.core.management.base import BaseCommand, CommandError

from push_notifications.models import APNSDevice

class Command(BaseCommand):
    help = 'Sends a push notification for every registered device'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for device in APNSDevice.objects.filter(active=True):
            self.stdout.write("Sending push to %s..." % device)
            device.send_message("Will be removed anyway", extra={
                "aps": {
                    "alert": {
                       "title": "Push Test",
                        "body": "Test push message"
                    },
                    "sound": "default",
                    "mutable-content": 1,
                    "data": {
                        "attachment-url": "https://m.popkey.co/987552/NGLb3.gif"
                    }
                }
            })
