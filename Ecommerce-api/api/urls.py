from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title = "Ecommerce api",
        default_version= '1.0.0',
        description= 'Api documentation of app'
    ),
    public=True
)


urlpatterns = [
    path("",schema_view.with_ui('swagger',cache_timeout=0)),
    path("accounts/",include("accounts.urls")),
    path("products/",include("products.urls")),
]