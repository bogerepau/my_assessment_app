from django.contrib import admin


from .models import User, Quiz, Subject, Question, Answer, Student,  TakenQuiz, StudentAnswer

admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)


