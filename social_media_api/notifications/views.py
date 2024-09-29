

from django.http import JsonResponse
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    data = [{
        'actor': notification.actor.username,
        'verb': notification.verb,
        'timestamp': notification.timestamp
    } for notification in notifications]
    return JsonResponse({'notifications': data}, status=200)

@login_required
def mark_notifications_as_read(request):
    Notification.objects.filter(recipient=request.user, read=False).update(read=True)
    return JsonResponse({'message': 'Notifications marked as read'}, status=200)