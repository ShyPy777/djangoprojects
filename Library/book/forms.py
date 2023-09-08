from book.models import Book
from book.models import Student
from django import forms
class bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
