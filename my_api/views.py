from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from .models import User, FibDB
from .fotms import RegForm
import json
import sqlite3
from django.contrib.auth.hashers import make_password, check_password
from .refresh import create_token, check_token

def index(request):
    template = loader.get_template('my_api/index.html')

    context = {
        
    }

    return HttpResponse(template.render(context, request))


def user(request):
    conn = sqlite3.connect('/home/kir/Projects/test_porject_api/project_api/db.sqlite3')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        req_token = request.headers['Token']
        check = check_token(req_token)

        if check['is_valid'] == 'True':
            rows = cursor.execute(''' select id, login, email, name, surname, phone from my_api_user ''').fetchall()
            rows_list = {'data':[dict(row) for row in rows]}
            rows_list['new_token'] = check['token']
            return JsonResponse(rows_list)
        else:
            return HttpResponse('refresh your token')
    except:
        return HttpResponse('access only with token')


def current_user(request, user_id):
    conn = sqlite3.connect('/home/kir/Projects/test_porject_api/project_api/db.sqlite3')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        req_token = request.headers['Token']
        check = check_token(req_token)
        
        if check['is_valid'] == 'True':
            rows = cursor.execute(f''' select id, login, email, name, surname, phone from my_api_user where id={user_id} ''')
            rows_list = {'data':[dict(row) for row in rows]}
            rows_list['new_token'] = check['token']

            if len(rows_list) == 0:
                return HttpResponse('There is no user with this ID')
            else:
                return JsonResponse(rows_list, safe=False)
        else:
            return HttpResponse('refresh your token')
    except:
        return HttpResponse('access only with token')



def register(request):
    error = ''
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
             intermediate = form.save(commit=False)
             intermediate.psw_hash = make_password(intermediate.psw_hash)
             intermediate.save()
             return HttpResponseRedirect('/my_api')
        else:
            error = 'form not valid'
    
    form = RegForm()
    template = loader.get_template('my_api/reg.html')

    context = {
        'form': form,
        'error': error                
    }

    return HttpResponse(template.render(context, request))


def login_page(request):
    conn = sqlite3.connect('/home/kir/Projects/test_porject_api/project_api/db.sqlite3')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == 'POST':
        login = request.POST['login']
        psw = request.POST['psw']

        try:
            login_data = User.objects.get(login=login)
        except:
            return HttpResponse('invalid data')

        if check_password(psw, login_data.psw_hash):
            create = create_token(login=login)

            if create:
                return HttpResponse('correct')
            else:
                return HttpResponse('error')

        else:
            return HttpResponse('invalid data')
        
    template = loader.get_template('my_api/login.html')

    context = {
                
    }

    return HttpResponse(template.render(context, request))


def fibonacci(request, num):

    try:
        conn = sqlite3.connect('/home/kir/Projects/test_porject_api/project_api/db.sqlite3')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        try:
            value_from_db = FibDB.objects.get(id=num)
            return HttpResponse(value_from_db.value)
        except:
            n = num
            num_1 = 0
            num_2 = 1
            i = 0

            try:
                while i < n - 1:
                    num_sum = num_1 + num_2
                    num_1 = num_2
                    num_2 = num_sum
                    # cursor.execute(f""" insert into my_api_fibdb values {num_2} """)
                    i = i + 1

                number = str(num_2)
                return HttpResponse(number)
            except:
                return HttpResponse('error')

    except:
        return HttpResponse('invalid value entered')

# Create your views here.
