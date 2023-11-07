from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from InstiPro.models import Course, Session_Year, CustomUser, Student , Staff , Subject , Staff_Notification , Staff_Leave , Student_Notification , Staff_Feedback , Student_Feedback , Attendence,Attendence_Report , Student_Leave
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender= 'Male').count()
    student_gender_female = Student.objects.filter(gender= 'Female').count()

    # Retrieve the course-wise student counts
    course_student_counts = {}
    courses = Course.objects.all()
    for course in courses:
        course_student_counts[course.name] = Student.objects.filter(course_id=course).count()
    total_count = student_count + staff_count

    context = {
        'student_count':student_count,
        'subject_count':subject_count,
        'course_count':course_count,
        'staff_count':staff_count,
        'student_gender_female' : student_gender_female,
        'student_gender_male': student_gender_male,
        'course_student_counts': course_student_counts,
        'total_count' : total_count,
    }
    # print(student_gender_male, student_gender_female)
    return render(request,'HOD/home.html',context)


@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        student_image = request.FILES.get('student_image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        roll_number = request.POST.get('roll_number')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        father_name = request.POST.get('father_name')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_mobile = request.POST.get('mother_mobile')
        student_email = request.POST.get('student_email')
        username = request.POST.get('username')
        student_password = request.POST.get('student_password')

        if CustomUser.objects.filter(email=student_email).exists():
            messages.warning(request, "Email Is Already Taken!")
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username Is Already Taken!")
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                profile_pic=student_image,
                email=student_email,
                position='STUDENT'
            )
            user.set_password(student_password)  # Corrected line
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin=user,
                address=address,
                first_name =first_name,
                last_name = last_name,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
                roll_number = roll_number,
                student_email = student_email,
                mobile_number = mobile_number,
                student_password = student_password,
                username = username,
            )
            student.save()
            messages.success(request, user.first_name +" "+ user.last_name +" "+ "Is Successfully Added!")

            return redirect('add_student')

    context = {
        'course': course,
        'session_year': session_year,
    }
    return render(request, 'HOD/add_student.html', context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()
    context = {
        'student' : student,
    }
    return render(request, 'HOD/view_student.html', context)

@login_required(login_url='/')
def EDIT_STUDENT(request,roll_number):
    student = Student.objects.filter(roll_number = roll_number)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    
    context = {
        'student':student,
        'course' :course,
        'session_year' :session_year,
    }
    return render(request,'HOD/edit_student.html', context)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        student_email = request.POST.get('student_email')
        username = request.POST.get('username')
        student_password = request.POST.get('student_password')
        
        student = Student.objects.get(roll_number = roll_number)
        student.first_name = first_name
        student.last_name = last_name
        student.gender = gender
        student.mobile_number = mobile_number
        student.address = address
        student.username = username
        student.student_email = student_email
        student.student_password = student_password
        
        if student_password !=None and student_password != "":
                student.admin.set_password(student_password)
        
        student.save()

        messages.success(request,'Records Are Successfully Updated!')
        return redirect('view_student')
        
    return render(request, 'HOD/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,roll_number):
    student = Student.objects.get(roll_number=roll_number)
    student_user = student.admin  

    student_user.delete()
    student.delete()
    
    messages.success(request,"Record Is Successfully Deleted")
    return redirect('view_student')

@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
    
        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,"Course Is Successfully Added")
        return redirect('add_course')
    return render(request,'HOD/add_course.html')

@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request,'HOD/view_course.html',context)

@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course = Course.objects.get(id=id)

    context = {
        'course' : course ,
    }
    return render(request,'HOD/edit_course.html',context)

@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
    
        course.save()
        messages.success(request,"Course Is Successfully Updated!")
        return redirect('view_course')

    return render(request,'HOD/edit_course.html')

@login_required(login_url='/')
def DELETE_COURSE(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request,"Course Is Successfully Deleted!")
    return redirect('view_course')

@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method =="POST":
        staff_image = request.FILES.get('staff_image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        staff_email = request.POST.get('staff_email')
        username = request.POST.get('username')
        staff_password = request.POST.get('staff_password')

        if CustomUser.objects.filter(email=staff_email).exists():
            messages.warning(request, "Email Is Already Taken!")
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username Is Already Taken!")
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                profile_pic=staff_image,
                email=staff_email,
                position='TEACHER'
            )
            user.set_password(staff_password) 
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                first_name =first_name,
                last_name = last_name,
                gender=gender,
                staff_email = staff_email,
                mobile_number = mobile_number,
                staff_password = staff_password,
                username = username,
            )
            staff.save()
            messages.success(request, user.first_name +" "+ user.last_name +" "+ "Is Successfully Added!")

            return redirect('add_staff')

    return render(request,'HOD/add_staff.html')

@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()
    context = {
        'staff' : staff,
    }
    return render(request,'HOD/view_staff.html',context)

@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id=id)
    context = {
        'staff' : staff,
    }
    return render(request,'HOD/edit_staff.html',context)

@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('id')
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        staff_email = request.POST.get('staff_email')
        username = request.POST.get('username')
        staff_password = request.POST.get('staff_password')
        
        staff = Staff.objects.get(id=staff_id)
        staff.first_name = first_name
        staff.last_name = last_name
        staff.gender = gender
        staff.mobile_number = mobile_number
        staff.address = address
        staff.username = username
        staff.staff_email = staff_email
        staff.staff_password = staff_password
        
        if staff_password !=None and staff_password != "":
            staff.admin.set_password(staff_password)
        
        staff.save()

        messages.success(request,'Records Are Successfully Updated!')
        return redirect('view_staff')

    return render(request,'HOD/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request, id):
    staff = Staff.objects.get(id=id)
    staff_user = staff.admin  

    staff_user.delete()
    staff.delete()

    messages.success(request, "Record Is Successfully Deleted!")
    return redirect('view_staff')

@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()
    
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        
        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)
        
        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request,"Subject Is Successfully Added")
        return redirect('add_subject')
    
    context = {
        'course' : course,
        'staff' : staff,
    }
    
    return render(request, 'HOD/add_subject.html', context)

@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context = {
        'subject' : subject,
    }
    return render(request,'HOD/view_subject.html',context)

@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id=id)
    course  = Course.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject' : subject ,
        'course' : course,
        'staff' : staff,
    }
    return render(request,'HOD/edit_subject.html',context)

@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course')
        staff_id = request.POST.get('staff')
        subject_id = request.POST.get('subject_id')

        subject = Subject.objects.get(id=subject_id)
        subject.name = name

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject.course = course
        subject.staff = staff

        subject.save()
        messages.success(request, "Subject Is Successfully Updated!")
        return redirect('view_subject')

    return render(request, 'HOD/edit_subject.html')


@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request,"Subject Is Successfully Deleted!")
    return redirect('view_subject')

@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end
        )
        session.save()
        messages.success(request,"Session Is Successfully Created!")
        return redirect('add_session')

    return render(request,'HOD/add_session.html')

@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session_Year.objects.all()
    context = {
        'session' : session,
    }
    return render(request , 'HOD/view_session.html',context)

@login_required(login_url='/')
def EDIT_SESSION(request,id):
    session = Session_Year.objects.get(id=id)
    context = {
        'session' : session,
    }
    return render(request,'HOD/edit_session.html',context)

@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_start = request.POST.get('session_year_start')
        session_end = request.POST.get('session_year_end')

        session = Session_Year.objects.get(id=session_id)

        session.session_start = session_start
        session.session_end = session_end
    
        session.save()
        messages.success(request,"Session Is Successfully Updated!")
        return redirect('view_session')

    return render(request,'HOD/edit_session.html')

@login_required(login_url='/')
def DELETE_SESSION(request,id):
    session = Session_Year.objects.get(id=id)
    session.delete()
    messages.success(request,"Session Is Successfully Deleted!")
    return redirect('view_session')

@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification =  Staff_Notification.objects.all().order_by('-id')[0:5]
     
    context = {
        'staff' : staff ,
        'see_notification':see_notification,
    }
    return render(request,'HOD/staff_notification.html',context)

@login_required(login_url='/')
def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(id=staff_id)
        notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request,"Notification Is Successfully Sent!")
        return redirect('staff_send_notification')
    
@login_required(login_url='/')
def STUDENT_SEND_NOTIFICATION(request):
    student = Student.objects.all()
    see_notification =  Student_Notification.objects.all().order_by('-id')[0:5]
     
    context = {
        'student' : student,
        'see_notification':see_notification,
    }
    return render(request,'HOD/student_notification.html',context)


@login_required(login_url='/')
def SAVE_STUDENT_NOTIFICATION(request):
    if request.method == "POST":
        message = request.POST.get('message')
        roll_number = request.POST.get('roll_number')
       
        student = Student.objects.get(roll_number=roll_number)
        stud_notification = Student_Notification(
            roll_number=student,
            message=message,
        )
        stud_notification.save()
        messages.success(request, "Notification Is Successfully Sent!")
        return redirect('student_send_notification')


@login_required(login_url='/')
def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()
    
    context = {
        'staff_leave':staff_leave
    }
    return render(request, 'HOD/staff_leave.html', context)

@login_required(login_url='/')
def STAFF_APPROVE_LEAVE(request, id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    messages.success(request,"Leave Approved!!")
    return redirect('staff_leave_view')

@login_required(login_url='/')
def STAFF_DISAPPROVE_LEAVE(request, id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    messages.success(request,"Leave Rejected!!")
    return redirect('staff_leave_view')


@login_required(login_url='/')
def STUDENT_LEAVE_VIEW(request):
    student_leave = Student_Leave.objects.all()
    
    context = {
        'student_leave':student_leave
    }
    return render(request, 'HOD/student_leave.html', context)

@login_required(login_url='/')
def STUDENT_APPROVE_LEAVE(request, id):
    leave = Student_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    messages.success(request,"Leave Approved!!")
    return redirect('student_leave_view')

@login_required(login_url='/')
def STUDENT_DISAPPROVE_LEAVE(request, id):
    leave = Student_Leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    messages.error(request,"Leave Rejected!!")
    return redirect('student_leave_view')

@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by('-id')[0:5]
    context = {
       'feedback' : feedback ,
       'feedback_history':feedback_history,
    }
    return render(request,'HOD/staff_feedback.html',context)

@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method=="POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()

        return redirect('staff_feedback_reply')
    
@login_required(login_url='/')
def STUDENT_FEEDBACK(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by('-id')[0:5]

    context = {
       'feedback' : feedback ,
       'feedback_history' : feedback_history,
    }
    return render(request,'HOD/student_feedback.html',context)

@login_required(login_url='/')
def STUDENT_FEEDBACK_SAVE(request):
    if request.method=="POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()

        return redirect('student_feedback_reply')

@login_required(login_url='/')    
def VIEW_ATTENDENCE(request):

    subject = Subject.objects.all()
    session_year = Session_Year.objects.all()

    action = request.GET.get('action')
    get_subject=None
    get_session_year=None
    attendence_date=None
    attendence_report=None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendence_date = request.POST.get('attendence_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            attendence = Attendence.objects.filter(subject_id=get_subject , attendence_date =attendence_date)
            for i in attendence:
                attendence_id = i.id 
                attendence_report = Attendence_Report.objects.filter(attendence_id = attendence_id)
    context = {
        'subject':subject,
        'session_year':session_year,
        'action':action,  
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'attendence_date':attendence_date ,
        'attendence_report':attendence_report,
    }
    return render(request,'HOD/view_attendance.html',context)
