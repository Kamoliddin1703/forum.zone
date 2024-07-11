from .forms import LoginForm, RegistrationForm, EditAccountForm, EditProfileForm

def add_my_forms(request):
    return {
        'login_form': LoginForm(),
        'register_form': RegistrationForm(),
        'edit_account': EditAccountForm(instance=request.user if request.user.is_authenticated else None),
        'edit_profile': EditProfileForm()
    }