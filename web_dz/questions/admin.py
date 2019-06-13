from django.contrib import admin
from questions.models import Question, Profile, Tag, Answer

admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Answer)

# login: admin
# password: adminpassword


