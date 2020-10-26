
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_create_initial_subjects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='name',
            new_name='topic',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='topic',
        ),
    ]
