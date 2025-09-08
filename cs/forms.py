# cs/forms.py
from django import forms
from dbcreate.models import Ticket_tbl, TLP_tbl

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket_tbl
        fields = [
            'Ticket_number',
            'Classification',
            'Severity',
            'Score',
            'TLP',
            'Vulnerability',
            'Description',
            'Recommendations',
            'file_reference',
            'file_enc',
            'Responder',
            'acknowledged_by',
        ]
        widgets = {
            'Ticket_number': forms.TextInput(attrs={'class': 'form-control req'}),
            'Classification': forms.Select(attrs={'class': 'form-control'}),
            'Severity': forms.Select(attrs={'class': 'form-control'}),
            'Score': forms.NumberInput(attrs={'class': 'form-control'}),
            'Vulnerability': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'Recommendations': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'file_reference': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file_enc': forms.TextInput(attrs={'class': 'form-control'}),
            'Responder': forms.Select(attrs={'class': 'form-control'}),
            'acknowledged_by': forms.Select(attrs={'class': 'form-control'}),
            'TLP': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        required_fields = ['Ticket_number', 'Classification', 'Severity', 'TLP']
        for field_name in required_fields:
            self.fields[field_name].required = True
            self.fields['Ticket_number'].label = 'Ticket number <span class="text-danger">*</span>'
            self.fields['Classification'].label = 'Classification <span class="text-danger">*</span>'
            self.fields['Severity'].label = 'Severity <span class="text-danger">*</span>'
            self.fields['TLP'].label = 'TLP <span class="text-danger">*</span>'
