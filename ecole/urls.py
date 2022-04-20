"""ecole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Staff_Views, Students_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.Base, name='base'),

    # la partie login
    path('', views.Login, name='login'),
    path('doLogin', views.Dologin, name='dologin'),
    path('dologout',views.Dologout, name='dologout'),

    #profile 

    path('Profile/', views.PRofile, name='profile'),
    path('Profile/modifier', views.Profile_modif,name='profile_modif'),

    #la partie Administration

    path('Administration/acceuil/',Hod_Views.Home, name='homeadmin'),
    path('Administration/Ajout_eleve/', Hod_Views.Add_student, name='add_student'),
    path('Administration/Liste_eleve/',Hod_Views.Liste_eleve,name='view_student'),
    path('Administration/Edit_eleve/<str:id>',Hod_Views.Edit_eleve, name='edit_student'),
    path('Administration/Update_eleve', Hod_Views.Update_eleve, name='update_eleve'),
    path('Administration/Delete_eleve/<str:adm>',Hod_Views.Delete_eleve, name='delete_eleve'),

    #Staff ou Enseignants

    path('Administration/Ajout_staff/',Hod_Views.Ajout_staff,name='add_staff'),
    path('Administration/Liste_staff/',Hod_Views.Liste_staff, name='view_staff'),
    path('Administration/Edit_staff/<str:id>',Hod_Views.Edit_staff,name='edit_staff'),
    path('Administration/Update_staff', Hod_Views.Update_staff, name='update_staff'),
    path('Administration/Delete_staff/<str:adm>',Hod_Views.Delete_staff, name='delete_staff'),

    # partie classe 

    path('Administration/Ajout_classe/',Hod_Views.Ajout_classe, name='add_classe'),
    path('Administration/Liste_classe', Hod_Views.Liste_classe, name='view_course'),
    path('Administration/Edit_Classe/<str:id>',Hod_Views.Edit_classe,name='edit_classe'),
    path('Administration/Update_classe/',Hod_Views.Update_classe,name='update_classe'),
    path('Administration/Delete_classe/<str:id>',Hod_Views.Delete_classe,name='delete_classe'),

    #Matières
    path('Administration/Ajout_matiere/',Hod_Views.Ajout_matiere,name='add_subject'),
    path('Administration/Liste_matiere',Hod_Views.Liste_Subject,name='view_matiere'),
    path('Administration/Edit_matiere/<str:id>',Hod_Views.Edit_subject,name='edit_subject'),
    path('Administration/Update_matiere/',Hod_Views.Update_matiere,name='update_matiere'),
    path('Administration/Delete_matiere/<str:id>',Hod_Views.Delete_subject,name='delete_subject'),

    path('Administration/Ajout_session/',Hod_Views.Ajout_session,name='add_session'),
    path('Administration/List_session/',Hod_Views.List_session,name='list_session'),
    path('Administration/Edit_session/<str:id>',Hod_Views.Edit_session,name='edit_session'),

    path('Administration/Prof/Notif',Hod_Views.Staff_envoi_notif,name='envoi_notif_staff'),
    path('Administration/Prof/Save_notif',Hod_Views.Save_staff_notif,name='save_staff_notif'),
    path('Administration/Prof/Voir_conge',Hod_Views.Voir_depart_conge,name='voir_depart_conge'),
    path('Administration/Prof/approuve_conge/<str:id>',Hod_Views.Approuve_conge,name='approuve_conge'),
    path('Administration/Prof/desapprouve_conge/<str:id>',Hod_Views.Desapprouve_conge,name='desapprouve_conge'),
    path('Administration/Prof/Feedback', Hod_Views.Staff_feedback_reply,name='staff_feedback'),
    path('Administration/Prof/Feedback_save', Hod_Views.Staff_feedback_reply_save,name='staff_feedback_save'),
    path('Administration/Eleve/notif', Hod_Views.Send_stud_notif,name='send_stud_notif'),
    path('Administration/Eleve/notif_save', Hod_Views.Save_stud_notif,name='save_stud_notif'),
    path('Administration/Stud/Feedback', Hod_Views.Stud_feedback_reply,name='stud_feedback_reply'),
    path('Administration/Stud/Feedback_save', Hod_Views.Stud_feedback_reply_save,name='stud_feedback_save'),
    path('Administration/Absence_eleve',Hod_Views.view_attend,name='view_attend'),
    path('Administration/eleve/export_csv', Hod_Views.export_csv,name='export_csv'),
    #Url des enseignants
    path('Prof/',Staff_Views.Home, name='home_staff'),
    path('Prof/Recev_notif/',Staff_Views.Notif_recev,name='notif_recev'),
    path('Prof/CommeLu/<str:status>',Staff_Views.CommeLu,name='comme_lu'),
    path('Prof/depart_conge',Staff_Views.Depart_conge,name='depart_conge'),
    path('Prof/conge_save', Staff_Views.Conge_save,name='depart_save'),
    path('Prof/feedback', Staff_Views.Staff_feedback,name='feedback'),
    path('Prof/feedback_save', Staff_Views.Staff_feedback_save,name='feedback_save'),
    path('Prof/Take_Attendance',Staff_Views.Staff_take_attendance,name='staff_take_attendance'),
    path('Prof/Save_Attendance',Staff_Views.Save_attendance,name='staff_save_attendance'),
    path('Prof/view_attendance',Staff_Views.Staff_view_attendance,name='staff_view_attendance'),
    path('Prof/ajout_note',Staff_Views.Staff_ajout_note,name='staff_ajout_note'),
    path('Prof/save_note',Staff_Views.Staff_save_note,name='staff_save_note'),

    #Url des etudiants
    path('Stud/Home',Students_Views.Stud_home,name='home_stud'),
    path('Stud/Recev_notif/', Students_Views.Notif_recev, name='notif_recev'),
    path('Stud/CommeLu/<str:status>',Students_Views.CommeLu,name='comme_lu_eleve'),
    path('Stud/stud_feedback', Students_Views.Stud_feedback,name='stud_feedback'),
    path('Stud/stud_feedback_save', Students_Views.Stud_feedback_save,name='stud_feedback_save'),
    path('Stud/View_Attendance',Students_Views.Stud_view_attend,name='stud_view_attend'),
    path('Stud/view_result',Students_Views.Stud_view_result,name='stud_view_result'),



]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
