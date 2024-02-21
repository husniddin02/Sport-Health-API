# users/models/user.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class CustomUserManager(UserManager):
    """
    Переопределенный менеджер пользователей для работы с моделью пользователей.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с указанным адресом электронной почты и паролем.

        Args:
            email (str): Адрес электронной почты пользователя.
            password (str): Пароль пользователя.
            extra_fields (dict): Дополнительные поля пользователя.

        Returns:
            User: Созданный пользователь.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создает и сохраняет суперпользователя с указанным адресом электронной почты и паролем.

        Args:
            email (str): Адрес электронной почты суперпользователя.
            password (str): Пароль суперпользователя.
            extra_fields (dict): Дополнительные поля суперпользователя.

        Returns:
            User: Созданный суперпользователь.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    Пользовательская модель пользователя для управления учетными записями пользователей.
    """

    username = models.CharField("Имя пользователя", max_length=50, unique=True)
    """
    Уникальное имя пользователя.
    """

    first_name = models.CharField("Имя", max_length=65)
    """
    Имя пользователя.
    """

    last_name = models.CharField("Фамилия", max_length=65)
    """
    Фамилия пользователя.
    """

    email = models.EmailField("Эл.почта", unique=True)
    """
    Уникальный адрес электронной почты пользователя.
    """

    avatar = models.ImageField("Фото", upload_to="avatar/", null=True, blank=True)
    """
    Фото профиля пользователя.
    """

    create_time = models.DateTimeField("Время создания", auto_now_add=True)
    """
    Время создания записи о пользователе.
    """

    update_time = models.DateTimeField("Время обновления", auto_now=True)
    """
    Время обновления записи о пользователе.
    """

    height = models.DecimalField("Рост", max_digits=5, decimal_places=2, null=True, blank=True)
    """
    Рост пользователя.
    """

    weight = models.DecimalField("Вес", max_digits=5, decimal_places=2, null=True, blank=True)
    """
    Вес пользователя.
    """

    date_of_birth = models.DateField("Дата рождения", null=True, blank=True)
    """
    Дата рождения пользователя.
    """

    GENDER_CHOICES = [
        ('Male', 'Мужской'), 
        ('Female', 'Женский'),
    ]
    gender = models.CharField("Пол", max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    """
    Пол пользователя.
    """
    
    is_active = models.BooleanField("Активный", default=True)
    """
    Флаг активности пользователя.
    """

    is_superuser = models.BooleanField("Супер пользователь", default=False)
    """
    Флаг суперпользователя.
    """

    is_staff = models.BooleanField(default=False)
    """
    Флаг принадлежности к штату сотрудников.
    """

    USERNAME_FIELD = "email"
    """
    Поле, используемое в качестве имени пользователя при аутентификации.

    Note:
        Для аутентификации пользователя используется адрес электронной почты.
    """

    objects = CustomUserManager()
    """
    Менеджер пользователей для работы с моделью пользователя.
    """

    def __str__(self):
        return f"({self.id}) {self.username}"
        """
        Возвращает строковое представление объекта пользователя.

        Returns:
            str: Строковое представление пользователя в формате (id) username.
        """
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
        """
        Проверяет, имеет ли пользователь указанное разрешение.

        Args:
            perm (str): Имя разрешения.
            obj (object, optional): Объект для проверки разрешения. По умолчанию None.

        Returns:
            bool: True, если пользователь имеет указанное разрешение, в противном случае False.
        """
    
    def has_module_perms(self, app_label):
        return self.is_superuser
        """
        Проверяет, имеет ли пользователь разрешения на доступ к модулю.

        Args:
            app_label (str): Метка приложения.

        Returns:
            bool: True, если пользователь имеет разрешения на доступ к модулю, в противном случае False.
        """

    def save(self, *args, **kwargs) -> None:
        self.username = self.email[:self.email.index("@")]
        return super().save(*args, **kwargs)
        """
        Переопределенный метод сохранения объекта пользователя.

        Note:
            Устанавливает имя пользователя на основе адреса электронной почты.

        Returns:
            None
        """

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        """
        Метаданные модели пользователя.
        """

User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'