from django import forms
from .models import ContactRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        exclude = ['status', 'ip_address', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('company', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('origin', css_class='form-group col-md-6 mb-3'),
                Column('destination', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('weight', css_class='form-group col-md-4 mb-3'),
                Column('volume', css_class='form-group col-md-4 mb-3'),
                Column('service_type', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            'cargo_description',
            'message',
            Submit('submit', _('Отправить запрос'), css_class='btn btn-primary mt-3 w-100 py-3 text-lg font-bold')
        )
