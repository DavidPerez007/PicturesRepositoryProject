from django.contrib.auth.models import User


def create_user(form):
    user = User.objects.create_user(
        username=form.cleaned_data.get('username'),
        password=form.cleaned_data.get('password'),
        # email= request.POST['email']
        # legal_age = request.POST['legal']
        # ADD SOME OTHER FIELDS LIKE +18 AND EMAIL
    )
    return user
