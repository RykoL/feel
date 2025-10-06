from django.shortcuts import render
from django.contrib.auth.decorators import login_not_required
# Create your views here.


@login_not_required
def landing_page(request):
    return render(request, "public/landing_page.html")
