from django.shortcuts import render , redirect , HttpResponse
from InstiPro.EmailBackEnd import EmailBackEnd
from django.contrib.auth import  login as auth_login
from django.contrib.auth import authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from InstiPro.models import CustomUser


def BASE(request):
    return render(request,'base.html')


def select_position(request):
    if request.method == 'POST':
        position = request.POST.get('position')
        if position in ('TEACHER', 'HOD', 'STUDENT'):
            request.session['selected_position'] = position
            return redirect('login')
    return render(request, 'select_position.html')


def login(request):

    selected_position = request.session.get('selected_position')

    if not selected_position:
        return redirect('select_position')

    return render(request, 'login.html', {'selected_position': selected_position})


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd().authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),
                                        position=request.POST.get('position')
                                        )
        if user:
            auth_login(request, user)
            selected_position = request.session.get('selected_position')

            if selected_position == 'HOD':
                print("Redirecting to hod_home")
                return redirect('hod_home')
            elif selected_position == 'TEACHER':
                return redirect('staff_home')
            elif selected_position == 'STUDENT':
                return redirect('student_home')
            else:
                messages.error(request, 'Invalid position!')
                return redirect('login')
        else:
            messages.error(request, 'Email and Password are invalid!')
            return redirect('login')

    return redirect('login')



def doLogout(request):
    logout(request)
    messages.success(request, 'You Have Logged Out Successfully!')
    return redirect('login')


def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    # print(user)
    context = {
        "user":user,
    }
    return render(request,'profile.html',context)


def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        password = request.POST.get('password')
        
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.profile_pic = profile_pic

            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic
            if password !=None and password != "":
                customuser.set_password(password)
            
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully!')
            return redirect('profile')
        except:
            messages.error(request, 'Failed To Update Your Profile!')
            
    return render(request, 'profile.html')



