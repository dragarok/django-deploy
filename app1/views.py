from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from app1.models import Topic, Webpage, AccessRecord
from app1.forms import UserProfileInfoForm, Userform, LoginForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    """
    webpage_list = AccessRecord.objects.order_by('date')
    # my_dict = {'insert_me': "You are fucking bastard"}
    context_dict = {'text': 'hello world', 'number': 100}
    # date_dict = {'access_records': webpage_list}
    """
    return render(request, 'index.html')  # ,context=context_dict)


@login_required
def special(request):
    return HttpResponse("You are logged in")

@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("account not  active")
        else:
            print("username and passwd don't match")
            return HttpResponse("invalid login details")
    else:
        return render(request, 'index.html')


def loginform_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Validated")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
    return render(request, 'form_page.html', {'form': form})


def signup_view(request):
    registered = False
    if request.method == 'POST':
        user_form = Userform(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            print("Validated")
            user = user_form.save()
            user.set_password(user.password)  # lecture 152
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return index(request)
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = Userform()
        profile_form = UserProfileInfoForm()

    return render(request, 'signup.html',
                  {'user_form': user_form,
                   'profile_form':profile_form,
                   'registered':registered})


def other(request):
    return render(request, 'app1/form.html')


