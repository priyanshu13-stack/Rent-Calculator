from django.shortcuts import render, redirect
from .models import RentEntry
from .forms import RentForm

def calculate_rent(request):
    last_electricity_units = request.session.get('last_electricity_units', 0)
    if request.method == 'POST':
        form = RentForm(request.POST)
        form.fields['last_electricity_units'].initial = last_electricity_units
        if form.is_valid():
            rent_entry = form.save(commit=False)
            electricity_usage = rent_entry.current_electricity_units - last_electricity_units
            if electricity_usage < 0:
                form.add_error('current_electricity_units', 'Current electricity units cannot be less than last month electricity units.')
            else:
                rent_entry.save()
                electricity_bill = electricity_usage * rent_entry.cost_per_unit
                total_rent = rent_entry.monthly_rent + electricity_bill
                request.session['last_electricity_units'] = rent_entry.current_electricity_units
                return render(request, 'rent/result.html', {
                    'monthly_rent': rent_entry.monthly_rent,
                    'electricity_usage': electricity_usage,
                    'cost_per_unit': rent_entry.cost_per_unit,
                    'electricity_bill': electricity_bill,
                    'total_rent': total_rent
                })
    else:
        form = RentForm()
        form.fields['last_electricity_units'].initial = last_electricity_units
    
    return render(request, 'rent/calculate_rent.html', {'form': form})

def reset_last_units(request):
    request.session['last_electricity_units'] = 0
    return redirect('calculate_rent')
