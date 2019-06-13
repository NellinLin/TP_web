# Generated by Django 2.1.7 on 2019-05-17 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0004_auto_20190416_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.PositiveIntegerField(choices=[(1, 'Нравится'), (2, 'Не нравится')])),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='rating',
        ),
        migrations.AddField(
            model_name='vote',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question', verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'question')},
        ),
    ]
