from django.shortcuts import render
from .models import Medicine
from .forms import MedicineSearchForm

def medicine_list_view(request):
    form = MedicineSearchForm(request.POST or None)
    medicines = Medicine.objects.all()

    if form.is_valid():
        search_text = form.cleaned_data.get('search_text')
        if search_text:
            medicines = medicines.filter(medicine_name__icontains=search_text)

    return render(request, 'index.html', {'form': form, 'medicines': medicines})
