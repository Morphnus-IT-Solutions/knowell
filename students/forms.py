from django import forms

from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].input_formats = ['%d-%m-%Y']
