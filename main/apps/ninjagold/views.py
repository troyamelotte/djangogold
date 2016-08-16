from django.shortcuts import render, redirect
from random import randint
# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold']=0

    if not 'log' in request.session:
        request.session['log']=''

    return render(request, 'ninjagold/index.html')

def updategold(request):
    moneychange = 0
    if request.method == "POST":
        building = request.POST['building']
    if building == "farm":
        moneychange = randint(10,20)
        request.session['log'] = 'You went to the farm and got '+ str(moneychange) +' gold!'
    if building == "cave":
        moneychange = randint(5,10)
        request.session['log'] = 'You went to the cave and got '+ str(moneychange) +' gold!'
    if building == "house":
        moneychange = randint(2,5)
        request.session['log'] = 'You went to the house and got '+ str(moneychange) +' gold!'
    if building == "casino":
        moneychange = randint(-50,50)
        request.session['log'] = 'You went to the casino and got '+ str(moneychange) +' gold!'
    request.session['gold']+=moneychange
    return redirect('/')
