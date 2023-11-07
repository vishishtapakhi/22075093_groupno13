from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from InstiPro.models import Course, Session_Year, CustomUser, Student  , Subject , Student_Notification , Student_Feedback , Attendence , Attendence_Report , Student_Leave
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    student = Student.objects.get(admin= request.user)
    context = {
        'student':student,
    }
    return render(request,'STUDENT/home.html', context)

@login_required(login_url='/')
def NOTIFICATION(request):
    student = Student.objects.get(admin = request.user)
    roll_number = student.roll_number

    notification = Student_Notification.objects.filter(roll_number=student)

    context = {
        'notification' : notification,
    }

    return render(request,'STUDENT/notification.html',context)

@login_required(login_url='/')
def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('student_notification')

@login_required(login_url='/')
def STUDENT_FEEDBACK(request):
    student = Student.objects.get(admin=request.user)
    roll_number = student.roll_number

    feedback_history = Student_Feedback.objects.filter(roll_number=student)

    context = {
        'feedback_history' : feedback_history,
    }
    return render(request,'STUDENT/feedback.html',context)

@login_required(login_url='/')
def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        
        student = Student.objects.get(admin=request.user)
        roll_number = student.roll_number

        feedback_obj = Student_Feedback(
            roll_number=student,
            feedback=feedback,
            feedback_reply=" ",
        )
        feedback_obj.save()
        messages.success(request, 'Your Feedback Is Successfully Submitted!!')
        return redirect('student_feedback')
    return render(request, 'STUDENT/feedback.html')

@login_required(login_url='/')
def STUDENT_VIEW_ATTENDENCE(request):
    student = Student.objects.get(admin=request.user)
    roll_number = student.roll_number
    subjects = Subject.objects.filter(course=student.course_id)
    action=request.GET.get('action')

    get_subject=None
    attendence_report=None

    if action is not None:
        if request.method=="POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)

            attendence_report = Attendence_Report.objects.filter(student_id=student,attendence_id__subject_id=subject_id)

    context = {
        'subjects':subjects,
        'action':action,
        'get_subject':get_subject,
        'attendence_report':attendence_report,
    }

    return render(request,'STUDENT/view_attendance.html',context)

@login_required(login_url='/')
def STUDENT_APPLY_LEAVE(request):
    student = Student.objects.get(admin=request.user.id)
    student_leave_history = Student_Leave.objects.filter(student_id=student)
    
    context = {
        'student_leave_history': student_leave_history,
    }
    return render(request, 'STUDENT/apply_leave.html', context)

@login_required(login_url='/')
def STUDENT_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        leave_message = request.POST.get('leave_message')
        
        student = Student.objects.get(admin=request.user.id)
        leave = Student_Leave(
            student_id=student,
            start_date=start_date,
            end_date=end_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request, 'You have successfully applied for leave!')
        return redirect('student_apply_leave')
    
def ACADEMIC_LINK(request):
    return render(request, 'STUDENT/academic_link.html')