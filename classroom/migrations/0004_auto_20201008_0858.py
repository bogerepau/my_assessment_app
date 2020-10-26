
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20201008_0820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='topic',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='topic',
            new_name='name',
        ),
    ]
