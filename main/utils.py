from django.contrib.auth.models import User
from django.forms import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import psycopg2
from PIL import Image
from io import BytesIO


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



def convert_image_to_bytes(image):
    if isinstance(image, InMemoryUploadedFile):
        return image.read()
    else:
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        return image_io.getvalue()

def show_img(bytes):
    image = Image.open(BytesIO(bytes))
    image.show()