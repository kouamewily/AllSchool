from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import Student, Cours, Session_year, CustomerUser

class StudAll(resources.ModelResource):
    classe = fields.Field(
        column_name='classe',
        attribute='cours_id',
        widget=ForeignKeyWidget(Cours,field='name'),
    )
    session = fields.Field(
        column_name='session',
        attribute='session_year_id',
        widget=ForeignKeyWidget(Session_year,field='session_start')
    )
    user = fields.Field(
        column_name='username',
        attribute='adm',
        widget=ForeignKeyWidget(CustomerUser,field='username')
    )
    class Meta:
        model = Student
        exclude = ('session_year_id','adm','cours_id','created_at','update_at')
        