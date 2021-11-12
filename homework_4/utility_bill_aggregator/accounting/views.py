import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound

def index(request):
    user_name = 'Лена'
    num_accounts = 20
    return render(request, "index.html",
     context={'user_name':user_name,'num_accounts':num_accounts})

def get_account_list(request):
    if request.method == 'GET':
        accounts = {
           1: {
               'personal_account': 141820,
               'mounth': 'october',
               'year': '2021',
               'type_accounts': 'elictricity',
               'status': 'paid'
            },
            2: {
                'personal_account': 14182043,
                'mounth': 'october',
                'year': '2021',
                'type_accounts': 'water',
                'status': 'paid'
            },
            3: {
                'personal_account': 14182012,
                'mounth': 'october',
                'year': '2021',
                'type_accounts': 'maintenance',
                'status': 'paid'
            }
        }
        return JsonResponse(accounts)
    else:
        return HttpResponseNotAllowed('GET')


def get_account_detail(request, account_id):
    if request.method == 'GET':
        account_details = {
            1: {
                'personal_account': 141820,
                'mounth': 'october',
                'year': '2021',
                'type_accounts': 'elictricity',
                'payment_amount': 2300,
                'indications': '980',
                'adress': 'Korolev, Frunze 1B, 45',
                'electronic_receipt': None,
                'status': 'paid'
            },
            2: {
                'personal_account': 14182043,
                'mounth': 'october',
                'year': '2021',
                'type_accounts': 'water',
                'payment_amount': 2300,
                'indications': 'cw-45, hw-90',
                'adress': 'Korolev, Frunze 1B, 45',
                'electronic_receipt': None,
                'status': 'paid'
            },
            3: {
                'personal_account': 14182012,
                'mounth': 'october',
                'year': '2021',
                'type_accounts': 'maintenance',
                'payment_amount': 2300,
                'indications': None,
                'adress': 'Korolev, Frunze 1B, 45',
                'electronic_receipt': None,
                'status': 'paid'
            }
        }
        try:
            account_detail = account_details[account_id]
        except KeyError:
            return HttpResponseNotFound()
        else:
            return JsonResponse(account_detail)
    else:
        return HttpResponseNotAllowed('GET')

def add_account(request):
    new_account = {
        'personal_account': None,
        'mounth': None,
        'year': '2021',
        'type_accounts': None,
        'payment_amount': None,
        'indications': None,
        'adress': None,
        'electronic_receipt': None,
        'status': 'not paid'     
    }
    if request.method == 'POST':
        try:
            new_account['personal_account'] = request.POST['personal_account']
            new_account['mounth'] = request.POST['mounth']
            new_account['year'] = request.POST['year']
            new_account['type_accounts'] = request.POST['type_accounts']
            new_account['payment_amount'] = request.POST['payment_amount']
            new_account['indications'] = request.POST['indications']
            new_account['adress'] = request.POST['adress']
            new_account['electronic_receipt']= request.FILES['electronic_receipt'].name
            new_account['status'] = request.POST['status']
        except KeyError:
             return JsonResponse({'message': 'Required parameter not entered.'})
        else:
            return JsonResponse({'message': 'New account successfully added.', 'account': new_account})
    else:
        return HttpResponseNotAllowed('POST')
    

def add_account_type(request):
    pass

def edit_account(request, account_id):
    pass

def search_accounts(request):
    pass
