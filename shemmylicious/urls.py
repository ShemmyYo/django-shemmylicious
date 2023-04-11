from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('accounts/', include('allauth.urls')),
]

# Configure Admin Titles
admin.site.site_header = "Shemmylicious Admin Area"
admin.site.site_title = "Shemmylicious"
admin.site.index_title = "Welcome to the Shemmylicious Page Admin area!"