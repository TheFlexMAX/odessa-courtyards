from django.contrib import admin
from .models import (
    Member,
    Jury,
    MemberRequest,
    FormBefore,
    ProblemArea,
    FormAfter,
    ReformedAreas,
    Mark,
)

# Register your models here.
admin.site.register(Member)
admin.site.register(Jury)
admin.site.register(MemberRequest)
admin.site.register(FormBefore)
admin.site.register(ProblemArea)
admin.site.register(FormAfter)
admin.site.register(ReformedAreas)
admin.site.register(Mark)