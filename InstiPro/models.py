from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    position = models.CharField(max_length=50,default='HOD')
    profile_pic = models.ImageField(upload_to='media/profile_pic',null=True, blank=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + "   to   " + self.session_end

class Student(models.Model):
    admin = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course , on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year , on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    username = models.CharField(max_length=255 , default="Ravi")  
    roll_number = models.CharField(max_length=20)  
    student_password = models.CharField(max_length=50 , default=12345678) 
    mobile_number = models.CharField(max_length=15)
    student_email = models.EmailField(default="example@example.com") 

    father_name = models.CharField(max_length=255)  
    father_mobile = models.CharField(max_length=15) 
    mother_name = models.CharField(max_length=255) 
    mother_mobile = models.CharField(max_length=15)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255 , default="Ravi")
    last_name = models.CharField(max_length=255, default="kaur") 
    first_name = models.CharField(max_length=255, default="sarab")
    staff_password = models.CharField(max_length=50 , default=12345678) 
    mobile_number = models.CharField(max_length=15, default=1234567890)
    staff_email = models.EmailField(default="example@example.com")
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.username

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField(default="Hello")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True , default=0)
    
    def __str__(self):
        return self.staff_id.admin.username
    
class Staff_Leave(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=100, null=True)
    end_date = models.CharField(max_length=100, null=True)
    message = models.TextField()
    status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name +" "+ self.staff_id.admin.last_name
    
class Student_Leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    # roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=100, null=True)
    end_date = models.CharField(max_length=100, null=True)
    message = models.TextField()
    status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name +" "+ self.student_id.admin.last_name
    
class Student_Notification(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField(default="Hello")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True , default=0)
    
    def __str__(self):
        return self.roll_number.admin.username
    
class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(default="okay")
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name
    
class Student_Feedback(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(default="okay")
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.roll_number.admin.username
    
class Attendence(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendence_date = models.DateField()
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_id.name
    
class Attendence_Report(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendence_id = models.ForeignKey(Attendence , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name