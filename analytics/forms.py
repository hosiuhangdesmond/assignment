from django import forms

class SimpleCSVImportForm(forms.Form):
    csv_file = forms.FileField(label="Upload CSV file")