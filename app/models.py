from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
	USER = (
		(1,'ADMIN'),
		(2,'STAFF'),
		(3,'ELEVE'),
		)

	user_type = models.CharField(choices=USER,max_length=50,default=1)
	profile_pic = models.ImageField(upload_to='media/profile_pic')

class Cours(models.Model):

	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Session_year(models.Model):
	session_start = models.CharField(max_length=100)
	session_end  = models.CharField(max_length=100)

	def __str__(self):
		return self.session_start + " au " + self.session_end

class Student(models.Model):
	adm = models.OneToOneField(CustomerUser,on_delete=models.CASCADE)
	address = models.TextField()
	genre = models.CharField(max_length=100)
	cours_id = models.ForeignKey(Cours,on_delete=models.DO_NOTHING)
	session_year_id = models.ForeignKey(Session_year,on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.adm.first_name + " " + self.adm.last_name

class Staff(models.Model):
	adm = models.OneToOneField(CustomerUser,on_delete=models.CASCADE)
	address =  models.TextField()
	genre = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.adm.username

class Subject(models.Model):
	name = models.CharField(max_length=100)
	course = models.ForeignKey(Cours,on_delete=models.CASCADE)
	staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Notif_Staff(models.Model):
	staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(null=True,default=0)

	def __str__(self):
		return self.staff_id.adm.first_name


class Notif_Stud(models.Model):
	stud_id = models.ForeignKey(Student,on_delete=models.CASCADE)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(null=True,default=0)

	def __str__(self):
		return self.stud_id.adm.first_name
class Staff_Leave(models.Model):
	staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
	data = models.CharField(max_length=100)
	message = models.TextField()
	status = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.staff_id.adm.first_name

class Staff_Feedback(models.Model):
	staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
	feedback = models.TextField()
	feedback_reply = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.staff_id.adm.first_name

class Stud_Feedback(models.Model):
	stud_id = models.ForeignKey(Student,on_delete=models.CASCADE)
	feedback = models.TextField()
	feedback_reply = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.stud_id.adm.first_name

class Attendance(models.Model):
	subject_id = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
	attendance_data = models.DateField()
	session_id = models.ForeignKey(Session_year,on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return  self.subject_id.name

class Attendance_report(models.Model):
	stud_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
	attend_id = models.ForeignKey(Attendance,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.stud_id.adm.first_name

class StudResult(models.Model):
	stud_id = models.ForeignKey(Student,on_delete=models.CASCADE)
	subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
	evaluation = models.IntegerField()
	exam_class = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	update_at = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.stud_id.adm.first_name





