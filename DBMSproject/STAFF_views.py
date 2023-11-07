from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from InstiPro.models import Course, Session_Year, CustomUser, Student , Staff , Subject , Staff_Leave , Staff_Notification,  Attendence_Report, Attendence, Staff_Feedback, Student_Feedback
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.filter().count()
    staff = Staff.objects.get(admin = request.user)
    staff_id = staff.id
    subject_count = Subject.objects.filter(staff_id = staff_id).count()
    leave_count = Staff_Leave.objects.filter(staff_id = staff_id).count()
    
    context = {
        'subject_count':subject_count,
        'student_count':student_count,
        'leave_count':leave_count,
        'staff':staff,
        'staff_id':staff_id
    }
    return render(request, 'STAFF/home.html', context)

@login_required(login_url='/')
def NOTIFICATION(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff: 
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id=staff_id)

        context = {
            'notification' : notification,
        }

    return render(request,'STAFF/notification.html',context)

@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('notification')

@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_Leave.objects.filter(staff_id = staff_id)
        
        context = {
            'staff_leave_history':staff_leave_history,
        }
        return render(request, 'STAFF/apply_leave.html', context)

@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        leave_message = request.POST.get('leave_message')
        
        staff = Staff.objects.get(admin = request.user.id)
        leave = Staff_Leave(
            staff_id = staff,
            start_date = start_date,
            end_date = end_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request, 'You Have Successfully Applied For Leave!!')
        return redirect('staff_apply_leave')

@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history' : feedback_history,
    }
    return render(request,'STAFF/feedback.html',context)


@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin=request.user.id)

        feedback_obj = Staff_Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_reply=" ",
        )
        feedback_obj.save()
        messages.success(request, 'Your Feedback Is Successfully Submitted!!')
        return redirect('staff_feedback')
    return render(request, 'STAFF/feedback.html')

@login_required(login_url='/')
def STAFF_TAKE_ATTENDENCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff=staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    students = None 

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id =session_year_id)

            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)
    context = {
        'subject' : subject , 
        'session_year' : session_year,
        'get_subject' : get_subject ,
        'get_session_year' : get_session_year,
        'action' : action,
        'students' : students,
    }
    return render(request,'STAFF/take_attendance.html',context)

@login_required(login_url='/')
def STAFF_SAVE_ATTENDENCE(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendence_date = request.POST.get('attendence_date')
        student_id = request.POST.getlist('student_id')

        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id =session_year_id)

        attendence = Attendence(
            subject_id = get_subject,
            attendence_date = attendence_date,
            session_year_id = get_session_year,
        )
        attendence.save()
        for i in student_id : 
            stud_id = i
            int_stud = int(stud_id)

            p_students = Student.objects.get(id=int_stud)
            attendence_report = Attendence_Report(
                student_id = p_students,
                attendence_id = attendence,
            )

            attendence_report.save()
        messages.success(request, 'Attendence saved successfully!!')
        return redirect('staff_take_attendence')

@login_required(login_url='/')   
def STAFF_VIEW_ATTENDENCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff_id = staff_id)
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
    return render(request,'STAFF/view_attendance.html',context)
