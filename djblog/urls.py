"""djblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from djzen.urls import zen_url
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

import blog.views
import temple.views

urlpatterns = [
    zen_url('admin/', admin.site.urls),
    zen_url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    zen_url('posts/<slug>/', blog.views.post_list),
    zen_url('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    zen_url('home/', temple.views.index),
    zen_url('classes/', temple.views.classes),
    zen_url('classes/all/', temple.views.ClassListView.as_view(), name='class'),
    zen_url('classes/all/<int>', temple.views.book_detail_view),
    zen_url('accounts/', include('django.contrib.auth.urls')),
    # zen_url('volunteer/', temple.views.volunteer),
    # zen_url('volunteer/<slug>', temple.views.volunteer_sector),
    # zen_url('donate/', temple.views.donate),
    # zen_url('donate/<slug>', temple.views.donate_sector),

]
