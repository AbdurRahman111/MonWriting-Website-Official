from django.shortcuts import render, redirect
from .froms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from article.models import article_category, Article_table, article_chapter, article_subchapter, track_views, search_log
from .models import Profile

def signup_function(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created for {username}!")
            return redirect('login_function')
        else:
            messages.error(request, "Invalid Info")
    contex = {
        'form': form
        }

    if request.user.is_authenticated:
        return redirect('user_profile')
    return render(request, 'signup_function.html', contex)


def submit_signup(request):
    # check the post peramiters
    sign_email = request.POST['email']
    sign_password = request.POST['password1']
    confirm_sign_password = request.POST['password2']
    sign_first_name = request.POST['first_name']
    sign_last_name = request.POST['last_name']

    # chech the error inputs
    user_email_info = User.objects.filter(email=sign_email)

    erorr_message = ""
    if user_email_info:
        # messages.error(request, "Email Already Exist")
        erorr_message = "Email Already Exist"

    elif sign_password != confirm_sign_password:
        # messages.error(request, "Passwords are not match")
        erorr_message = "Passwords are not match"

    elif len(sign_password) < 7:
        # messages.error(request, "Passwords Must be Al least 7 Digits")
        erorr_message = "Passwords Must be Al least 7 Digits"

    if not erorr_message:
        # create user
        myuser = User.objects.create_user(sign_email, sign_email, sign_password)
        myuser.first_name = sign_first_name
        myuser.last_name = sign_last_name
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Successfully created account!")
        return redirect('login_function')
    else:
        context= {
        'email':sign_email,
        'password1':sign_password,
        'password2':confirm_sign_password,
        'first_name':sign_first_name,
        'last_name':sign_last_name,
        'erorr_message':erorr_message
        }

        return render(request, 'signup_function.html', context)


def login_function(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You're LogedIN")
        else:
            messages.warning(request, "Username OR Password is incorect!!")
    if request.user.is_authenticated:
        return redirect('update_profile')
    return render(request, 'login_function.html')


def logout_funciotn(request):
    logout(request)
    messages.warning(request, "You're Loged Out!")
    return redirect('index')



@login_required
def update_profile(request):
    if request.method == 'POST':
        # u_form = UserUpdateForm(request.POST,instance=request.user)
        # p_form = ProfileUpdateForm(request.POST,
        #                            request.FILES,
        #                            instance=request.user.profile)
        # if u_form.is_valid() and p_form.is_valid():
        #     u_form.save()
        #     p_form.save()
        #     messages.success(request, "Your account has been updated!!")
        #     return redirect('update_profile')

        profile_image = request.FILES.get('profile_image')
        designation = request.POST.get('designation')
        bio = request.POST.get('bio')
        facebook_profile = request.POST.get('facebook_profile')
        linkedin_profile = request.POST.get('linkedin_profile')
        Instagram_profile = request.POST.get('Instagram_profile')
        twitter_profile = request.POST.get('twitter_profile')

        var_update_profile = Profile.objects.get(user = request.user)
        var_update_profile.designation = designation
        if profile_image:
            var_update_profile.image = profile_image
        var_update_profile.bio = bio
        var_update_profile.facebook_profile = facebook_profile
        var_update_profile.linkedin_profile = linkedin_profile
        var_update_profile.Instagram_profile = Instagram_profile
        var_update_profile.twitter_profile = twitter_profile
        var_update_profile.save()
        messages.success(request, "Your account has been updated!!")
        return redirect('update_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        get_user = request.user
        get_profile = Profile.objects.get(user=get_user)

        var_follow = False
        if request.user.is_authenticated:
            if request.user in get_profile.followers.all():
                var_follow = True
        else:
            pass


        contex = {
            'u_form':u_form,
            'p_form':p_form,

            'get_user': get_user,
            'get_profile': get_profile,
            'var_follow': var_follow,
        }
        return render(request, 'profile_update.html',contex)