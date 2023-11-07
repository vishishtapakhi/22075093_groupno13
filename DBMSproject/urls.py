from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views , HOD_views , STAFF_views , STUDENT_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('base/',views.BASE , name='base'),

    #login path
    path('', views.select_position, name='select_position'),
    path('login/', views.login, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('doLogout' , views.doLogout, name='logout'),

    #profile update
    path('profile',views.PROFILE , name='profile'),
    path('profile/update', views.PROFILE_UPDATE,name='profile_update'),
    
    
    
    # HOD
    # THIS.....IS....HOD......PANEL
    
    path('HOD/home',HOD_views.HOME , name='hod_home'),
    # STUDENT_HOD
    path('HOD/Student/Add', HOD_views.ADD_STUDENT, name='add_student'),
    path('HOD/Student/View',HOD_views.VIEW_STUDENT, name='view_student'),
    path('HOD/Student/Edit/<str:roll_number>',HOD_views.EDIT_STUDENT, name='edit_student'),
    path('HOD/Student/Update',HOD_views.UPDATE_STUDENT, name='update_student'),
    path('HOD/Student/Delete<str:roll_number>', HOD_views.DELETE_STUDENT, name='delete_student'),
    # COURSE_HOD
    path('HOD/Course/Add', HOD_views.ADD_COURSE, name='add_course'),
    path('HOD/Course/View', HOD_views.VIEW_COURSE, name='view_course'),
    path('HOD/Course/Edit/<str:id>',HOD_views.EDIT_COURSE, name='edit_course'),
    path('HOD/Course/Update', HOD_views.UPDATE_COURSE, name='update_course'),
    path('HOD/Course/Delete/<str:id>', HOD_views.DELETE_COURSE, name='delete_course'),
    # STAFF_HOD
    path('HOD/Staff/Add', HOD_views.ADD_STAFF, name='add_staff'),
    path('HOD/Staff/View', HOD_views.VIEW_STAFF, name='view_staff'),
    path('HOD/Staff/Edit/<str:id>', HOD_views.EDIT_STAFF, name='edit_staff'),
    path('HOD/Staff/Update', HOD_views.UPDATE_STAFF, name='update_staff'),
    path('HOD/Staff/Delete/<str:id>', HOD_views.DELETE_STAFF, name='delete_staff'),
    # notification staff
    path('HOD/Staff/Send_Notification', HOD_views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),
    path('HOD/staff/save_notification', HOD_views.SAVE_STAFF_NOTIFICATION , name='save_staff_notification'),
    # notification student
    path('HOD/student/send_notification', HOD_views.STUDENT_SEND_NOTIFICATION , name='student_send_notification'),
    path('HOD/student/save_notification', HOD_views.SAVE_STUDENT_NOTIFICATION , name='save_student_notification'),
    # leave apply for staff
    path('HOD/Staff/Leave_View', HOD_views.STAFF_LEAVE_VIEW, name='staff_leave_view'),
    path('HOD/Staff/Approve_Leave/<str:id>', HOD_views.STAFF_APPROVE_LEAVE, name='staff_approve_leave'),
    path('HOD/Staff/Disapprove_Leave/<str:id>', HOD_views.STAFF_DISAPPROVE_LEAVE, name='staff_disapprove_leave'),
    # leave apply for student
    path('HOD/Student/Leave_View', HOD_views.STUDENT_LEAVE_VIEW, name='student_leave_view'),
    path('HOD/Student/Approve_Leave/<str:id>', HOD_views.STUDENT_APPROVE_LEAVE, name='student_approve_leave'),
    path('HOD/Student/Disapprove_Leave/<str:id>', HOD_views.STUDENT_DISAPPROVE_LEAVE, name='student_disapprove_leave'),
    # SUBJECT_HOD
    path('HOD/Subject/Add', HOD_views.ADD_SUBJECT, name='add_subject'),
    path('HOD/Subject/View', HOD_views.VIEW_SUBJECT, name='view_subject'),
    path('HOD/Subject/Edit/<str:id>', HOD_views.EDIT_SUBJECT, name='edit_subject'),
    path('HOD/Subject/Update', HOD_views.UPDATE_SUBJECT, name='update_subject'),
    path('HOD/Subject/Delete/<str:id>',HOD_views.DELETE_SUBJECT , name='delete_subject'),
    # SESSION_HOD
    path('HOD/Session/Add',HOD_views.ADD_SESSION , name='add_session'),
    path('HOD/Session/View',HOD_views.VIEW_SESSION , name='view_session'),
    path('HOD/Session/Edit/<str:id>',HOD_views.EDIT_SESSION , name='edit_session'),
    path('HOD/Session/Update',HOD_views.UPDATE_SESSION , name='update_session'),
    path('HOD/Session/Delete/<str:id>',HOD_views.DELETE_SESSION , name='delete_session'),
    # staff feedback
    path('HOD/Staff/feedback',HOD_views.STAFF_FEEDBACK,name="staff_feedback_reply"),
    path('HOD/Staff/feedback/save',HOD_views.STAFF_FEEDBACK_SAVE,name="staff_feedback_reply_save"),
    # student feedback
    path('HOD/Student/feedback',HOD_views.STUDENT_FEEDBACK,name="student_feedback_reply"),
    path('HOD/Student/feedback/save',HOD_views.STUDENT_FEEDBACK_SAVE,name="student_feedback_reply_save"),
    # student attendance
    path('HOD/View/Attendence',HOD_views.VIEW_ATTENDENCE ,name="view_attendence"),
    
    
    # STAFF 
    # STAFF PANEL FROM DOWN HERE
    path('STAFF/home', STAFF_views.HOME, name='staff_home'),
    path('STAFF/Notification',STAFF_views.NOTIFICATION , name="notification"),
    path('STAFF/Mark_As_Done/<str:status>',STAFF_views.STAFF_NOTIFICATION_MARK_AS_DONE , name="staff_notification_mark_as_done"),
    path('STAFF/Apply_Leave', STAFF_views.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
    path('STAFF/Apply_Leave_Save', STAFF_views.STAFF_APPLY_LEAVE_SAVE, name='staff_apply_leave_save'),
    # feedback
    path('STAFF/Feedback' , STAFF_views.STAFF_FEEDBACK , name="staff_feedback"),
    path('STAFF/Feedback/Save' , STAFF_views.STAFF_FEEDBACK_SAVE , name="staff_feedback_save"),
    # take attendance
    path('STAFF/Take_Attendence',STAFF_views.STAFF_TAKE_ATTENDENCE,name="staff_take_attendence"),
    path('STAFF/Save_Attendence',STAFF_views.STAFF_SAVE_ATTENDENCE ,name="staff_save_attendence"),
    path('STAFF/Vew_Attendence',STAFF_views.STAFF_VIEW_ATTENDENCE ,name="staff_view_attendence"),
    
    
    # STUDENT
    # STUDENT PANEL FROM DOWN HERE
    path('STUDENT/home', STUDENT_views.HOME, name= 'student_home'),
    path('STUDENT/Apply_Leave', STUDENT_views.STUDENT_APPLY_LEAVE, name='student_apply_leave'),
    path('STUDENT/Apply_Leave_Save', STUDENT_views.STUDENT_APPLY_LEAVE_SAVE, name='student_apply_leave_save'),
    # feedback
    path('STUDENT/Feedback' , STUDENT_views.STUDENT_FEEDBACK , name="student_feedback"),
    path('STUDENT/Feedback/Save',STUDENT_views.STUDENT_FEEDBACK_SAVE , name="student_feedback_save"),
    # attendance
    path('STUDENT/View_Attendence',STUDENT_views.STUDENT_VIEW_ATTENDENCE ,name="student_view_attendence"),
    path('STUDENT/Notification',STUDENT_views.NOTIFICATION , name="student_notification"),
    path('STUDENT/Mark_As_Done/<str:status>',STUDENT_views.STUDENT_NOTIFICATION_MARK_AS_DONE , name="student_notification_mark_as_done"),
    #academic links
    path('STUDENT/Academic_Link', STUDENT_views.ACADEMIC_LINK, name='academic_link'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)