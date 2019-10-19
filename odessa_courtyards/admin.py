from django.contrib import admin
from .models import MemberRequest, FormBefore, ProblemArea
                    #FormAfter, ReformedAreas

admin.site.register(MemberRequest)
admin.site.register(FormBefore)
admin.site.register(ProblemArea)
