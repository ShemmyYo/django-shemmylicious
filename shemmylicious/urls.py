from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    # path('accounts/', include('allauth.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configure Admin Titles
admin.site.site_header = "Shemmylicious Admin Area"
admin.site.site_title = "Shemmylicious"
admin.site.index_title = "Welcome to the Shemmylicious Page Admin area!"