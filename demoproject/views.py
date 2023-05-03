from django.http import HttpResponse, HttpResponseNotFound
#Here define the view functions for the different error response, passing an addition argument exception 
def handler404(request, exception):
    return HttpResponseNotFound("<h1>404: page not found</h1> <br><button onclick ='' href=''>Home Page</button>")
def home(request):
    return HttpResponse('Little lemon')