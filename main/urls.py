from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('k/', include('filer.server.urls')),
    path('', include('user.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('nadmin/',admin.site.urls),
    path('comment/', include('comment.urls')),
    path("a/", include("account.urls")),
    path('tinymce/', include('tinymce.urls')),
    path("b/", include("blog.urls")),
    path("t/", include("teams.urls")),
    path("m/", include("meeting.urls")),
    path("a_r/", include("attendance_request.urls")),
    path("c/", include("contacts.urls")),
    path("e/", include("calendarapp.urls")),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('td/', include('todo.urls', namespace="todo")),
    path('filer/', include('filer.urls')),
    # path('robots.txt',robots),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
