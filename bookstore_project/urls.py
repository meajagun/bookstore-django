"""bookstore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),  # django admin app

    # accounts management
    # allauth user accounts management app
    path('accounts/', include('allauth.urls')),
    #path('accounts/', include('django.contrib.auth.urls')), # custom user accounts management app
    #path('accounts/', include('users.urls')), # users app

    # local apps
    path('', include('pages.urls')),  # pages app
    path('books/', include('books.urls')),  # books app)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # allows to see uploaded contents locally during development