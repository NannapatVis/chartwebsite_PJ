from django.contrib import admin
from graduate.models import Student1

class Student1Admin(admin.ModelAdmin):
    list_display = ('Order','Course','Std_no','Std_name','Std_state','End_year',
                    'Std_plan','Prof_main','Prof_Sec','Work_name','Publish_type','Journal_db',
                'Implementation','Journal_name','Date_start','Date_End','Cal_year')

admin.site.register(Student1, Student1Admin)

