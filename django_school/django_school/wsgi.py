
import os
from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_school.settings")


application = get_wsgi_application()
#application = DjangoWhiteNoise(application)

# os.environ["DJANGO_SETTINGS_MODULE"] = "myblog.settings"                                                                
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
