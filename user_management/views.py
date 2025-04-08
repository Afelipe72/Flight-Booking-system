from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class CustomSignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user_management/signup.html'
    success_url = reverse_lazy('login')  # Redirect to login page after signup
