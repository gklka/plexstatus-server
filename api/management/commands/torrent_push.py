from django.core.management.base import BaseCommand, CommandError

from push_notifications.models import APNSDevice

class Command(BaseCommand):
    help = 'Sends a torrent-type push notification for every registered device'

    def add_arguments(self, parser):
        parser.add_argument('--title', type=str, help="The notification title (bold first line)")
        parser.add_argument('--body', type=str, help="The notification secondary line")
        parser.add_argument('--badge', type=int, default=-1, help="The badge count. Use -1 to don't change badge value")
        parser.add_argument('--attachment', type=str, help="Attachment URL if any")
        parser.add_argument('--sound', type=str, help="Sound name, if any")

    def handle(self, *args, **options):
        for device in APNSDevice.objects.filter(active=True):
            self.stdout.write("Sending push to %s (title: %s, body: %s)..." % (device, options["title"], options["body"]))

            extra = {
                "aps": {}
            }

            if (options["title"]):
                extra["aps"]["alert"] = {
                   "title": options["title"],
                    "body": options["body"]
                }

            if (options["badge"] >= 0):
                extra["aps"]["badge"] = options["badge"]

            if (options["sound"]):
                extra["aps"]["sound"] = options["sound"]

            if (options["attachment"]):
                extra["aps"]["mutable-content"] = 1
                extra["aps"]["data"] = {
                    "attachment-url": options["attachment"]
                }

            device.send_message("Will be removed anyway", extra=extra)
