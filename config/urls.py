from django.contrib import admin
from django.urls import (path, re_path, include)
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings
from django.views import defaults as default_views
from django.conf.urls.i18n import i18n_patterns

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True
# )





urlpatterns = i18n_patterns(
    path('', include('techapps.techpages.urls', namespace="techpages")),
    path('api/',include('techapps.techusers.urls')),
    path('api/',include('techapps.techemails.urls')),
    path('api/',include('techapps.techorders.urls')),
    path('',include('techapps.techblog.urls')),
   #  re_path('(?!.*(static))',TemplateView.as_view(template_name="index.html")),
   #  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   #  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   #  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
   prefix_default_language=False
)

urlpatterns+= [
   path('techadmin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
   # This allows the error pages to be debugged during development, just visit
   # these url in browser to see how these error pages look like.
   urlpatterns += [
      path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
      ),
      path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
      ),
      path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
      ),
      path("500/", default_views.server_error),
   ]
   if "debug_toolbar" in settings.INSTALLED_APPS:
      import debug_toolbar

      urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
