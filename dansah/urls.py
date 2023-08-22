"""
URL configuration for dansah project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Dansah Admin"
# Add the below line
admin.site.index_title = "Dansah  App"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/homeslider/", include("homeslider.urls")),
    path("api/homeactivities/", include("homeactivities.urls")),
    path("api/homeministriesmaterial/", include("homeministriesmaterial.urls")),
    path("api/homeevents/", include("homeevents.urls")),
    path("api/profiles/", include("profiles.urls")),
    path("api/quoteoftheday/", include("quoteoftheday.urls")),
    path("api/role/", include("role.urls")),
    path("api/powerliving/", include("powerliving.urls")),
    path("api/socialmedia/", include("socialmedia.urls")),
    path("api/prayerconnect/", include("prayerconnect.urls")),
    path("api/prayercity/", include("prayercity.urls")),
    path("api/leadershipinstitute/", include("leadershipinstitute.urls")),
    path("api/contact/", include("contact.urls")),
    path("api/home/", include("home.urls")),
]
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # imp for what you want to achieve.
