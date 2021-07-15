from django.urls import path

from main.api import FaceDetectionAPI
from main.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main_view'),
    # API
    path('api/face_detection', FaceDetectionAPI.as_view(), name='face_detection_api'),
]