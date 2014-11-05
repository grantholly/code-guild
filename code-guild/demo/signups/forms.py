from django import forms

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit

from .models import SignUp

# ModelForm shortcut
class SignUpForm(forms.ModelForm):
    class Meta:
	model = SignUp
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper.form_class = "form-inline"
        self.helper.layout = Layout("first_name", "last_name", "email")
        self.helper.form_method = "post"
        self.helper.add_input(Submit('submit', 'Sign Up', css_class="btn-default"))


# crispy form
class SignUpCrispyForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="first name")
    last_name = forms.CharField(max_length=50, label="last_name")
    email = forms.EmailField(label="email")
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
	super(SignUpCrispyForm, self).__init__(*args, **kwargs)
	self.helper.form_id = "signup"
	self.helper.form_class = "form-inline"
	self.helper.layout = Layout("first_name", "last_name", "email")
	self.helper.form_method = "post"
	self.helper.add_input(Submit('submit', 'Sign Up', css_class="btn-default"))

# cripsy class based form
class CrispyClassSignUpForm(forms.Form):
    def __init__(self, *args, **kwargs):
	super(CrispySignUpForm, self).__init__(*args, **kwargs)
	self.helper = FormHelper()
        self.helper.form_class = "form-inline"
	self.helper.layout = Layout("first_name", "last_name", "email")
	self.helper.form_method = "post"
	self.helper.add_input(Submit('submit', 'Submit'))	

    first_name = forms.CharField(
	label = "first name",
	max_length = 50,
    )
    last_name = forms.CharField(
	label = "last name",
	max_length = 50,
    )
    email = forms.EmailField()
    
