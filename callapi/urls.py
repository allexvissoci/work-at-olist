"""callapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from record.views import StartRecordView, EndRecordView
from bill.views import BillView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'startrecord', StartRecordView, base_name='start_record')
router.register(r'endrecord', EndRecordView, base_name='end_record')
router.register(r'bill', BillView, base_name='bill')
urlpatterns += router.urls
