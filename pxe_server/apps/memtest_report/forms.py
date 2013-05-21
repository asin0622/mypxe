from django import forms
from memtest_report.models import MemtestParam

class MemtestParamForm(forms.ModelForm):
    class Meta:
        model = MemtestParam