
#!/usr/bin/python

import argparse
import os

parser = argparse.ArgumentParser(description="Notification script")

# Required
parser.add_argument('-a', '--action', dest='action', type=str, help='The action type', required=True)

# Optional
parser.add_argument('-u', '--user', dest='user', type=str, help='The user who committed the action')
parser.add_argument('-s', '--server', dest='server', type=str, help='The server name')
parser.add_argument('-t', '--title', dest='title', type=str, help='The played item title')
parser.add_argument('-c', '--count', dest='count', type=str, help='The number of movies played concurently', default=0)
parser.add_argument('-p', '--poster', dest='poster', type=str, help='The played item\'s poster image')

args = parser.parse_args()

if args.poster:
	args.poster = args.poster.replace('http://', 'https://')
	args.poster = args.poster.replace('.jpg', 'l.jpg') # https://api.imgur.com/models/image

os.system('../manage.py torrent_push --badge %s' % args.count)

if args.action == 'Play':
	os.system('../manage.py torrent_push --title "%s" --body "Started %s" --attachment "%s" --sound "Default"' % (args.user, args.title, args.poster))
elif args.action == 'Stop':
	pass
	# os.system('../manage.py torrent_push --title "%s" --body "Stopped %s" --attachment "%s"' % (args.user, args.title, args.poster))
elif args.action == 'Resume':
	pass
	# os.system('../manage.py torrent_push --title "%s" --body "Resumed %s" --attachment "%s"' % (args.user, args.title, args.poster))
elif args.action == 'Pause':
	pass
	# os.system('../manage.py torrent_push --title "%s" --body "Paused %s" --attachment "%s"' % (args.user, args.title, args.poster))
