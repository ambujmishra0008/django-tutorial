from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    resume = forms.FileField()

    def clean_resume(self):
        resume = self.files.get('resume')
        file_name = resume.name
        if not file_name.endswith('.csv'):
            raise forms.ValidationError("please upload csv file")


