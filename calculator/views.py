from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculator(request):
    
    #Input area
    age = request.GET.get('age')
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    
    nep_conc = request.GET.get('nep_conc')
    nep_dr = request.GET.get('nep_dr')
    
    epi_conc = request.GET.get('epi_conc')
    epi_dr = request.GET.get('epi_dr')
    
    #Output area
    nep_result = 0
    epi_result = 0
    
    #Calculation area
    if weight and nep_conc and nep_dr:
        weight = int(weight)
        nep_conc = float(nep_conc)
        nep_dr = float(nep_dr)
        #NEP Calculation
        nep_result = 60*weight*nep_dr/nep_conc
    else:
        nep_result = "!!Please fill all the fields!!"
        
    if weight and epi_conc and epi_dr:
        weight = int(weight)
        epi_conc = float(epi_conc)
        epi_dr = float(epi_dr)
        #NEP Calculation
        epi_result = 60*weight*epi_dr/epi_conc
    else:
        epi_result = "!!Please fill all the fields!!"
        
    return render(request, 'calculator/calculator.html', {'nep_result':nep_result, 'epi_result':epi_result})