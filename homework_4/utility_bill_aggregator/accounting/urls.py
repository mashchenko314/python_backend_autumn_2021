from django.contrib import admin
from django.urls import path, include
from accounting.views import index, get_account_detail, get_account_list, add_account_type, add_account, edit_account, search_accounts, delete_account

from rest_framework.routers import DefaultRouter

from .views import AccountViewSet

router = DefaultRouter()
router.register(r'api/accounts', AccountViewSet, basename='accounts')


urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += router.urls
