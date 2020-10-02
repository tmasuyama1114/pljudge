from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path
from django.views.generic import TemplateView
=======
from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView

>>>>>>> tmp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
<<<<<<< HEAD
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
=======
    path('accounts/', include('allauth.urls')),
    path('pljudge/', include('pljudge.urls')),
>>>>>>> tmp
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns