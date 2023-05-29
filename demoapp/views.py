from django.shortcuts import render
from demoapp.forms import LogForm
# Create your views here.
from django.http import HttpResponse
from . import forms
from .models import Menu
def home(request):
   path = request.path
   scheme = request.scheme
   method = request.method
   address = request.META['REMOTE_ADDR']
   user_agent = request.META['HTTP_USER_AGENT']
   path_info = request.path_info
   mssg = f"""<br>
        <br>Path: {path}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>Address: {address}
        <br>User Agent: {user_agent}
        <br>Path info :{path_info}
   
   """
   return  HttpResponse(mssg, content_type ='text/html', charset='utf-8')

def sayHello(request):
    content = '<html><body style="background-color:black"> \
                <p style = "color: red"> This is my second webpage: Hello </p> \
               </body></html>'
    return HttpResponse(content)

def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 

def pathview(request, name, id):
    return HttpResponse("Name: {} User: {}".format(name,id))

def qryview(request):
    name = request.GET['name']
    id = request.get['id']

    return HttpResponse('Username: {} Id: {}'.format(name,id))


#we have to create a view function for the url path 
def menuitems(request,dish):
    items = {
        'pasta':'Pasta is a type of noodles',
        'falafel': 'Falafel are deep fried patties',
        'cheesecake': 'Cheesecake is a type of dessert',

    }
    description = items[dish]
    return HttpResponse(f"<h2 style='color:red'> {dish}</h2>"+ f"<h3 style='color:green'>{description}</h3>")

#To render the form 
def form_view(request):
    form = LogForm()
    #We save the form to the DB
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request,'home.html',context)

    #rendering a template with view

def about(request):
    text = {
        'about':"Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."
    }

    context = {'text':text}
    return render(request, 'about.html', context)


def checkname(request, name):
    person = {'first_name':'Roger', "profession":"Teacher"}
    lang = ['javascript', "python", "java", "c++", "Ruby", "rust"]
    dct = {'digits': ['One', 'Two', 'Three'],'tens': ['Ten', 'Twenty', 'Thirty']} 
    context = {'name':name, "person":person, "lang":lang, 'dct':dct}
    
    return render(request, 'checkname.html', context )


def menu(request):
    # menuitems = {'name':"Greek Salad"}

    newmenu = {
        'mains':[
            {'name':'falafel', 'price':'12'},
            {'name':'sharwama', 'price':'15'},
            {'name':'gyro', 'price':'10'},
            {'name':'bread', 'price':'12'},
        ]
    }
    return render(request, 'menu.html', newmenu)

def menu_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu':newmenu}

    return render(request, 'menu.html', newmenu_dict)
    