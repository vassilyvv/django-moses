# Generated by Django 4.2.7 on 2023-11-07 07:27

from django.db import migrations, models
import django.utils.timezone
import moses.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('email_candidate', models.EmailField(blank=True, max_length=254, verbose_name='Email candidate')),
                ('is_email_confirmed', models.BooleanField(default=False, verbose_name='Is email confirmed')),
                ('email_confirmation_pin', models.PositiveIntegerField(default=0, verbose_name='Email confirm PIN')),
                ('email_candidate_confirmation_pin', models.PositiveIntegerField(default=0, verbose_name='Email candidate confirm PIN')),
                ('email_confirmation_attempts', models.PositiveSmallIntegerField(default=0, verbose_name='Email confirm attempts')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('phone_number_candidate', models.CharField(blank=True, max_length=20, verbose_name='Phone number candidate')),
                ('is_phone_number_confirmed', models.BooleanField(default=False, verbose_name='Is phone number confirmed')),
                ('phone_number_confirmation_pin', models.PositiveIntegerField(default=0, verbose_name='Phone number confirm PIN')),
                ('phone_number_candidate_confirmation_pin', models.PositiveIntegerField(default=0, verbose_name='Phone number candidate confirm PIN')),
                ('phone_number_confirmation_attempts', models.PositiveSmallIntegerField(default=0, verbose_name='Phone number confirm attempts')),
                ('last_password_reset_sms_sent_at', models.DateTimeField(blank=True, null=True, verbose_name='Last password reset sms sent at')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=200, verbose_name='Last name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is staff')),
                ('preferred_language', models.CharField(choices=[('en', 'English')], default='en', max_length=10, verbose_name='Preferred language')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Created at')),
                ('mfa_secret_key', models.CharField(blank=True, default='', max_length=160)),
                ('last_phone_number_confirmation_pin_sent', models.DateTimeField(blank=True, null=True)),
                ('last_phone_number_candidate_confirmation_pin_sent', models.DateTimeField(blank=True, null=True)),
                ('userpic', models.ImageField(blank=True, null=True, upload_to='images/userpics/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='sites.site')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', moses.models.CustomUserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='customuser',
            constraint=models.UniqueConstraint(fields=('site', 'phone_number'), name='one_phone_number_per_site'),
        ),
        migrations.AddConstraint(
            model_name='customuser',
            constraint=models.UniqueConstraint(fields=('site', 'email'), name='one_email_per_site'),
        ),
    ]
