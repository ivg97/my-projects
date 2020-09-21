from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import  render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

@login_required
def dashboard(request):
    '''Checkng user autorizations '''
    return render(request, 'account/dashboard.html', {
        'section': 'dachboard'
    })

def user_login(request):
    ''''''
    if request.method == 'POST':
        form = LoginForm(request.POST) # create object form in data
        print('#' * 70)
        print(form)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, # collation input data on data from database
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfukky')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else: # if request.method == 'GET'
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


# Create your views here.
