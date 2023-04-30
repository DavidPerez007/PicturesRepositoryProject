from django.contrib.auth.models import User
from django.forms import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import psycopg2
from .models import Image
from PIL import Image as ImagePillow
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

def validate_image_size(img):
    limit = 0  # 150MB
    if img.size > limit:
        print("dentro de funcion")
        raise ValidationError('La imagen es demasiado grande (máximo 2MB)')

def validate_image_type(img):
    valid_types = ['image/jpeg', 'image/png']
    if img.content_type not in valid_types:
        raise ValidationError('Formato de imagen no válido (JPEG/PNG)')

def save_img(request, form):
    try:
        image_name = form.cleaned_data['image_name']
        description = form.cleaned_data['description']
        image = convert_image_to_bytes(request.FILES['image'])
        new_image = Image(name=image_name, description=description, image=image)
        new_image.save()
    except:
        print("Ya cayo el error")

    

def convert_image_to_bytes(image):
    if isinstance(image, InMemoryUploadedFile):
        return image.read()
    else:
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        return image_io.getvalue()
    

def unconvert_img(bytes):
    image = ImagePillow.open(BytesIO(bytes))
    image.show()

