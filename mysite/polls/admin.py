from django.contrib import admin
from .models import CreatorOneToOne, CreationOneToOne, MTOCreation, OTMCreator, MTMCreation, MTMCreator

admin.site.register(CreatorOneToOne)
admin.site.register(CreationOneToOne)
admin.site.register(MTOCreation)
admin.site.register(OTMCreator)

admin.site.register(MTMCreation)
admin.site.register(MTMCreator)
