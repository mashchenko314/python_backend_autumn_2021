import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.views.decorators.http import require_POST, require_GET
from .models import Account, Service
from rest_framework import viewsets
from .serializers import AccountSerializer
from rest_framework.response import Response

class AccountViewSet(viewsets.ModelViewSet):
    
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


    
def index(request):
    user_name = 'Лена'
    num_accounts = 20
    return render(request, "index.html",
     context={'user_name':user_name,'num_accounts':num_accounts})

def get_account_list(request):
    if request.method == 'GET':
       accounts = Account.objects.filter()
       data = [
           {
               'id': account.id,
               'personal_account': account.personal_account,
               'month': account.month,
               'year': account.year
            } for account in accounts
        ]
       return JsonResponse({'accounts': data})
    else:
        return HttpResponseNotAllowed('GET')


def get_account_detail(request, account_id):
    if request.method == 'GET':
        try:
            account = Account.objects.get(id=account_id)
            account_detail = {
                'personal_account': account.personal_account,
                'month': account.month,
                'year': account.year,
                'payment_amount': account.payment_amount,
                'indications': account.indications,
                'electronic_receipt_filename': account.electronic_receipt_filename,
                'is_paid': account.is_paid,
                'service_type': account.service_type.type
            }
        except Account.DoesNotExist:
            return HttpResponseNotFound()
        else:
            return JsonResponse(account_detail)
    else:
        return HttpResponseNotAllowed('GET')


def add_account(request):
    if request.method == 'POST':
        try:
            service = Service.objects.get(id=int(request.POST['service_id']))
            new_account = Account.objects.create(
               personal_account=request.POST['personal_account'],
               month=request.POST['month'],
               year=request.POST['year'],
               payment_amount=request.POST['payment_amount'],
               indications=request.POST['indications'],
               electronic_receipt_filename=request.POST['electronic_receipt_filename'],
               address=request.POST['address'],
               is_paid=request.POST['is_paid'],
               service_type=service,
               )
            new_account.save()
        except KeyError:
             return JsonResponse({'message': 'Required parameter not entered.'})
        else:
            return JsonResponse({'message': 'New account successfully added.'})
    else:
        return HttpResponseNotAllowed('POST')
    
@require_POST
def edit_account(request, account_id):
    try:
        Account.objects.all().filter(id=account_id).update( 
            is_paid=bool(request.POST['is_paid'])
        )
    except Account.DoesNotExist:
        return HttpResponseNotFound()
    except KeyError:
             return JsonResponse({'message': 'Required parameter not entered.'})
    else:
        return JsonResponse({'message': 'The account was successfully edited.'})

@require_GET
def delete_account(request, account_id):
    try:
        account = Account.objects.get(id=account_id)
        account.delete()
    except Account.DoesNotExist:
        return HttpResponseNotFound()
    else:
        return JsonResponse({'message': 'The account was successfully deleted.'})

def add_account_type(request):
    pass

def search_accounts(request):
    pass
