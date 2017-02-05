from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_store.views.product', name='product'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^', include('store.urls', namespace='store')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
