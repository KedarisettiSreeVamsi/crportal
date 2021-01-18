from django.urls import path, include


urlpatterns = [
    path('all_files/', views.files, name="files"),
    path('upload/', views.upload_file, name="upload"),
]