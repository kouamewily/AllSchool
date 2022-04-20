from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Cours, Session_year,CustomerUser,Student,Staff,Subject,Notif_Staff,Staff_Leave,Staff_Feedback,Attendance,Attendance_report,StudResult
from django.contrib import messages


@login_required(login_url='/')
def Home(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':
			return render(request,'Staff/home.html')
	return redirect('login')

@login_required(login_url='/')
def Notif_recev(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':

			staff = Staff.objects.filter(adm=request.user.id)

			for i in staff:
				staff_id = i.id

				notifs = Notif_Staff.objects.filter(staff_id=staff_id)

				context = {
				'notifs':notifs
				}

				return render(request,'Staff/notif_recev.html',context)
	return redirect('login')

@login_required(login_url='/')
def CommeLu(request,status):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':
			notif = Notif_Staff.objects.get(id=status)
			notif.status = 1
			notif.save()
			return redirect('notif_recev')
	return redirect('login')

@login_required(login_url='/')
def Depart_conge(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':
			prof = Staff.objects.filter(adm=request.user.id)
			for i in prof:
				staff_id = i.id
				historique_conge = Staff_Leave.objects.filter(staff_id=staff_id)
				context = {
					'historique_conge':historique_conge
				}
				return  render(request,'Staff/depart_conge.html',context)
	return redirect('login')
@login_required(login_url='/')
def Conge_save(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':
			if request.method == "POST":
				leave_date = request.POST.get('date_conge')
				leave_message = request.POST.get('message_conge')
				staff = Staff.objects.get(adm=request.user.id)
				leave = Staff_Leave(
					staff_id=staff,
					data=leave_date,
					message=leave_message,

				)
				leave.save()
				return redirect('depart_conge')
	return redirect('login')

@login_required(login_url='/')
def  Staff_feedback(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':
			staff_id = Staff.objects.get(adm=request.user.id)
			historique_feedback = Staff_Feedback.objects.filter(staff_id=staff_id)
			context = {
				'historique_feedback':historique_feedback
			}
			return  render(request,'Staff/feedback.html',context)
	return redirect('login')
@login_required(login_url='/')
def Staff_feedback_save(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':
			if request.method == "POST":
				feedback = request.POST.get('feedback')
				staff = Staff.objects.get(adm=request.user.id)

				feedback = Staff_Feedback(
					staff_id=staff,
					feedback=feedback,
					feedback_reply=""
				)
				feedback.save()
				return redirect('feedback')
	return redirect('login')

@login_required(login_url='/')
def Staff_take_attendance(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':
			staff = Staff.objects.get(adm=request.user.id)
			subject = Subject.objects.filter(staff=staff)
			session = Session_year.objects.all()
			action = request.GET.get('action')

			students = None
			get_session = None
			get_subject = None
			if action is not None:
				if request.method =="POST":
					subject_id = request.POST.get('subject_id')
					session_id = request.POST.get('session_id')
					get_subject = Subject.objects.get(id=subject_id)
					get_session = Session_year.objects.get(id=session_id)

					subject = Subject.objects.filter(id=subject_id)
					for i in subject:
						student_id = i.course.id
						students = Student.objects.filter(cours_id=student_id)
			context = {
				'subject':subject,
				'session':session,
				'get_subject':get_subject,
				'get_session':get_session,
				'action':action,
				'students':students

			}
			return render(request,'Staff/take_attendance.html',context)
	return redirect('login')

@login_required(login_url='/')
def Save_attendance(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':
			if request.method == "POST":
				subject_id = request.POST.get('subject_id')
				session_id = request.POST.get('session_id')
				attend_date = request.POST.get('attend_date')
				student_id	= request.POST.getlist('student_id')

				get_subject = Subject.objects.get(id=subject_id)
				get_session = Session_year.objects.get(id=session_id)

				attendance = Attendance(
					subject_id=get_subject,
					session_id=get_session,
					attendance_data=attend_date
				)
				attendance.save()
				for i in student_id:
					stud_id = i
					int_stud = int(stud_id)

					p_students = Student.objects.get(id=int_stud)
					attendance_report = Attendance_report(
						stud_id=p_students,
						attend_id=attendance
					)
					attendance_report.save()
			return redirect('staff_take_attendance')
	return redirect('login')

@login_required(login_url='/')
def Staff_view_attendance(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':
			staff_id = Staff.objects.get(adm=request.user.id)
			subject = Subject.objects.filter(staff=staff_id)
			session = Session_year.objects.all()
			action = request.GET.get('action')
			get_subject = None
			get_session = None
			attendance_date = None
			attendace_report=None
			if action is not None:
				if request.method == "POST":
					subject_id = request.POST.get('subject_id')
					session_id = request.POST.get('session_id')
					attendance_date = request.POST.get('attendance_date')
					get_subject = Subject.objects.get(id=subject_id)
					get_session = Session_year.objects.get(id=session_id)
					attendace = Attendance.objects.filter(subject_id=get_subject,attendance_data=attendance_date)
					for i in attendace:
						attendace_id = i.id
						attendace_report = Attendance_report.objects.filter(attend_id=attendace_id)

			context = {
				'subject':subject,
				'session':session,
				'action':action,
				'get_subject':get_subject,
				'get_session':get_session,
				'attendance_date':attendance_date,
				'attendace_report':attendace_report
			}
			return render(request,'Staff/view_attendance.html',context)
	return redirect('login')
@login_required(login_url='/')
def Staff_ajout_note(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':

			staff = Staff.objects.get(adm=request.user.id)
			subjects = Subject.objects.filter(staff=staff)
			session_year =Session_year.objects.all()
			action = request.GET.get('action')

			get_subject = None
			get_session = None
			studs = None
			if action is not None:
				if request.method == "POST":
					subject_id = request.POST.get('subject_id')
					session_year_id = request.POST.get('session_id')

					get_subject = Subject.objects.get(id=subject_id)
					get_session = Session_year.objects.get(id=session_year_id)

					subjects = Subject.objects.filter(id=subject_id)
					for i in subjects:
						stud_id = i.course.id
						studs = Student.objects.filter(cours_id=stud_id)

			context = {
				'subject':subjects,
				'session':session_year,
				'action':action,
				'get_subject':get_subject,
				'get_session':get_session,
				'studs':studs
			}
			return render(request,'Staff/ajout_note.html',context)
	return redirect('login')
@login_required(login_url='/')
def Staff_save_note(request):
	if request.user.is_authenticated:
		curr_user = request.user
		if curr_user.user_type == '2':

			if request.method == "POST":
				subject_id = request.POST.get('subject_id')
				session_id = request.POST.get('session_id')
				student_id = request.POST.get('student_id')
				evaluation = request.POST.get('evaluation')
				examen	   = request.POST.get('examen')

				get_stud = Student.objects.get(adm=student_id)
				get_subject = Subject.objects.get(id=subject_id)

				check_exists = StudResult.objects.filter(subject_id=get_subject,stud_id=get_stud).exists()
				if check_exists:
					result = StudResult.objects.get(subject_id=get_subject,stud_id=get_stud)
					result.evaluation = evaluation
					result.exam_class = examen
					result.save()
					return  redirect('staff_ajout_note')
				else:
					result = StudResult(
						stud_id=get_stud,
						subject_id=get_subject,
						evaluation=evaluation,
						exam_class=examen

					)
					result.save()
					return  redirect('staff_ajout_note')
	return redirect('login')