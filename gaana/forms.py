from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from gaana.models import Artist, Album, Track, Playlist

class StringObjectField(forms.CharField):
    """Converts a string to the appropriate (presumably artist/album) object"""

    def __init__(self, model, *args, **kwargs):
        self.model = model
        forms.CharField.__init__(self, *args, **kwargs)

    def to_python(self, value):
        value = super(forms.CharField, self).to_python(value)
        return getObj(self.model, value)

    def clean(self, value):
        if not isinstance(value, self.model):
            return getObj(self.model, value)
        return value

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='Email Address', max_length=75)
    mobile_no = forms.CharField(label='Mobile Number', max_length=10)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'mobile_no',)

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("This email address already exists. Did you forget your password?")
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.mobile_no = self.cleaned_data["mobile_no"]
        user.is_active = True
        if commit:
            user.save()
        return user

class SongForm(forms.ModelForm):
    artist = StringObjectField(Artist, max_length=300)
    album = StringObjectField(Album, max_length=300)
    track = StringObjectField(Track, max_length=300)
    playlist = StringObjectField(Playlist, max_length=300)
    class Meta:
        model = User
        fields = ["artist", "album", "track", "playlist"]