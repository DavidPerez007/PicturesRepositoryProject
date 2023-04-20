from django.contrib.auth.models import User
from django.forms import ValidationError


def create_user(form):
    user = User.objects.create_user(
        username=form.cleaned_data.get('username'),
        password=form.cleaned_data.get('password'),
        # email= request.POST['email']
        # legal_age = request.POST['legal']
        # ADD SOME OTHER FIELDS LIKE +18 AND EMAIL
    )
    return user

def validate_image_size(value):
    limit = 2 * 1024 * 1024  # 2MB
    if value.size > limit:
        raise ValidationError('La imagen es demasiado grande (máximo 2MB)')

def validate_image_type(value):
    valid_types = ['image/jpeg', 'image/png']
    if value.content_type not in valid_types:
        raise ValidationError('Formato de imagen no válido (JPEG/PNG)')