from django.shortcuts import render
from .models import EnterpriseSegment

# Create your views here.
def mainindex(request):
    #scripts = Notebook.objects.order_by('-fieldDate')
    scripts = EnterpriseSegment.objects.all()
    return render(request, 'mainindex/mainindex.html', { 'scripts':scripts,})