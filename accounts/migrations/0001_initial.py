# Сгенерировано Django

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.timezone import now
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='пароль')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='последний вход')),
                ('is_superuser', models.BooleanField(default=False, help_text='Обозначает, что этот пользователь имеет все права без явного назначения их.')),
                ('username', models.CharField(error_messages={'unique': 'Пользователь с таким именем пользователя уже существует.'}, help_text='Обязательно. 150 символов или меньше. Только буквы, цифры и символы @/./+/-/_.', max_length=150, unique=True, validators=[UnicodeUsernameValidator()], verbose_name='имя пользователя')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='фамилия')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='адрес электронной почты')),
                ('is_staff', models.BooleanField(default=False, help_text='Обозначает, может ли пользователь войти на этот сайт администратора.')),
                ('is_active', models.BooleanField(default=True, help_text='Обозначает, следует ли относиться к этому пользователю как к активному. Снимите этот флажок вместо удаления учетных записей.')),
                ('date_joined', models.DateTimeField(default=now, verbose_name='дата регистрации')),
                ('is_author', models.BooleanField(default=False)),
                ('avatar', models.ImageField(default='avatars/default.jpeg', upload_to='avatars/')),
                ('groups', models.ManyToManyField(blank=True, help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения, предоставленные каждой из его групп.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='группы')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Конкретные разрешения для этого пользователя.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='разрешения пользователя')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
                'abstract': False,
            },
        ),
    ]
