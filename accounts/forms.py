from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RestaurantForm(UserCreationForm):
    email = forms.CharField(label=_(u'Email'),max_length=254, required=True, widget=forms.EmailInput())
    # first_name = forms.CharField(label=_(u'first_name'),max_length=200, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام خود را وارد کنید'
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی خود را وارد کنید'
        self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری برای خود انتخاب کنید'
        self.fields['password1'].widget.attrs['placeholder'] = 'گذرواژه مناسب برای خود انتخاب کنید'
        self.fields['password2'].widget.attrs['placeholder'] = 'گذرواژه انتخابی خود را دوباره وارد کنید'
        self.fields['email'].label = 'پست الکترونیکی'

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email', 'password1', 'password2')


class CustomerForm(UserCreationForm):
    email = forms.CharField(label=_(u'Email'),max_length=254, required=True, widget=forms.EmailInput())
    # name = forms.CharField(label=_(u'name'),max_length=200, required=True)
    image = forms.ImageField(label=_(u'Image'), required=False)
    city = forms.CharField(label='شهر',max_length=500, required=True)
    address = forms.CharField(label='آدرس',max_length=1000,required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام خود را وارد کنید'
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی خود را وارد کنید'
        self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری برای خود انتخاب کنید'
        self.fields['password1'].widget.attrs['placeholder'] = 'گذرواژه مناسب برای خود انتخاب کنید'
        self.fields['password2'].widget.attrs['placeholder'] = 'گذرواژه انتخابی خود را دوباره وارد کنید'
        self.fields['email'].label = 'پست الکترونیکی'

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1', 'password2', 'city', 'address' , 'image')
