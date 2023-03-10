from django.urls import path, include

# include api urls of each app here
urlpatterns = [
    path('core/', include('apps.core.api.v1.urls')),
    path('listings/', include('apps.listings.api.v1.urls')),
    path('realtors/', include('apps.realtors.api.v1.urls')),
]
