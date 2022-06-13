from django.contrib import admin
from .models import Folder, Post

# Pour que le modèle soit visible dans l'interface d'administration
admin.site.register(Post)
admin.site.register(Folder)

