from django.urls import path
from .views import NotificationListView, NotificationMarkAsReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('mark-as-read/', NotificationMarkAsReadView.as_view(), name='notification-mark-read'),
]