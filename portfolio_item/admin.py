from django.contrib import admin

from .models import (
    About,
    Service,
    Education,
    Experience,
    Skill,
    PortfolioCategory,
    Portfolio
)

admin.site.register(About)
admin.site.register(Service)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(PortfolioCategory)
admin.site.register(Portfolio)