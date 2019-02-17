from django.contrib import admin
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from graphene_django.views import GraphQLView


urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'graphql/', GraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
