# Generated by Django 4.0.2 on 2022-02-10 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostTags',
            new_name='PostTag',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='cat_namey',
            new_name='cat_name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='dj_blog/static/img/Users Images/'),
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_blog.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_blog.user')),
            ],
        ),
    ]
