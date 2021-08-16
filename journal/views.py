from django.shortcuts import render
from .models import Notebook, Ticker, OrderType

# Create your views here.
def index(request):
    #scripts = Notebook.objects.order_by('-fieldDate')
    scripts = Notebook.objects.all()
    return render(request, 'journal/journal.html', { 'scripts':scripts,})