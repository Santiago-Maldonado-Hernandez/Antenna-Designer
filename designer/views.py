from django.shortcuts import render
from django.http import HttpResponse
from .forms import FrequencyForm



def home(request):
	return render(request, 'designer/home.html')

def horn(request):
	return render(request, 'designer/horn.html')

def dipole(request):
	return render(request, 'designer/dipole.html')

# Create your views here.

def FrequencyForm(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/dipole/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'designer/dipole.html', {'form': form})
