from django import forms


class cli(forms.Form):
    pseudo = forms.CharField(max_length=30)
    nom = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=128)
    sex = forms.CharField(max_length=10)
    localisation = forms.CharField(max_length=42)

    class Meta:
        verbose_name = "cli"
