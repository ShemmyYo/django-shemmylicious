from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import handler_404, handler_500, handler_403, handler_400


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Configure Admin Titles
admin.site.site_header = "Shemmylicious Admin Area"
admin.site.site_title = "Shemmylicious"
admin.site.index_title = "Welcome to the Shemmylicious Page Admin area!"


# Handlers
handler404 = handler_404
handler500 = handler_500
handler403 = handler_403
handler400 = handler_400
