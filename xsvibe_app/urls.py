from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='xsvibez'),
    path('free_beat/', views.free_beat, name='free_beat'),
    path('download_music/<str:id>', views.download_music, name='download_music'),
    path('download_video/<str:id>', views.download_video, name='download_video'),
    path('free_beat_download/<str:id>', views.free_beat_download, name='free_beat_download'),
    path('listen_download/<str:id>', views.listen_download, name='listen_download'),
    path('free_listen_download/<str:id>', views.free_listen_download, name='free_listen_download'),
    
    path('listen/<str:id>', views.listen, name='listen'),
    path('free_listen/<str:id>', views.free_listen, name='free_listen'),


    path('music/', views.music, name='music'),
    path('video/', views.video, name='video')

]
