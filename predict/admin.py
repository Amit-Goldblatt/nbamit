from django.contrib import admin
from .models import Team, Game, Rtg_history

# Register your models here.
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Rtg_history)
