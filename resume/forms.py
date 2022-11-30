from django.forms import ModelForm
from resume.models import Resume


# Create the form class.
class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['resume_name', 'name', 'phone', 'email', 'university_name', 'university_specialization', 'university_start_date',
                  'university_end_date', 'work_name', 'work_specialization', 'work_start_date', 'work_end_date', 'work_projects',
                  'skills', 'hobbies']