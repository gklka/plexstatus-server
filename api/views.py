from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST

from push_notifications.models import APNSDevice

@require_POST
def add_token(request):
	# Input parsing
	token = request.POST.get('token')
	if not token:
		return HttpResponse("Token parameter is missing", status=400);

	device_name = request.POST.get('device_name')
	if not device_name:
		device_name = "Plex Status consumer"

	device_id = request.POST.get('device_id')
	if not device_id:
		device_id = None

	# Saving token
	obj, created = APNSDevice.objects.get_or_create(registration_id=token)
	obj.name = device_name
	obj.device_id = device_id
	obj.save()

	# Response
	response = {
		"success": True,
		"response": {}
	}
	return JsonResponse(response);
