from django.shortcuts import render, HttpResponse

# Create your views here.
# A view ( in oher words, a view function) refers to a function
# that is caled when its corresonding URL is visited in the browser

#ALL view funtions must take in the variable request as the first arguement
def index(request):
    return render(request, 'books/index.template.html')