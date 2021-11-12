from django.contrib import admin
from django.urls import path, include
from accounting.views import index, get_account_detail, get_account_list, add_account_type, add_account, edit_account, search_accounts

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', get_account_list,  name='account_list'),
    path('accounts/<int:account_id>/', get_account_detail),
    path('accounts/search', search_accounts),
    path('account_type/add', add_account_type),
    path('account/add', add_account),
    path('account/edit/<int:account_id>', edit_account),
]
