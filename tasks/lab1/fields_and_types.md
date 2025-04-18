# Описание полей моделей и их передаваемых параметров.

# 1. Описание полей

Далее в этом блоке будет часто встречаться конструкция `**options` это означает что на вход данного класса можно передавать 
параметры, описываемые в блоке `2. Общие входные параметры поля`.

**AutoField** - целые числа с автоинкрементом. Используются для автоматической генерации уникальных целочисленных значений

1. `AutoField(**options)` - **IntegerField**, который автоматически увеличивается в соответствии с доступными идентификаторами. 
Вам обычно не нужно использовать это напрямую; поле первичного ключа будет автоматически добавлено в вашу модель, если 
вы не укажете иное. Гарантированно соответствует числам от **1** до **2147483647**.


2. `BigAutoField(**options)` - 64-разрядное целое число, очень похожее на **AutoField**, за исключением того, что оно 
гарантированно соответствует числам от **1** до **9223372036854775807**.


3. `SmallIntegerField(**options)` - Подобно **AutoField**, но допускает только значения в определенном (зависящим от базы данных) 
диапазоном. Значения от **1** до **32767** безопасны во всех базах данных, поддерживаемых Django.

**IntegerField** - целые числа

1. `IntegerField(**options)` - 32-разрядное целое число. Значения от -2147483648 до 2147483647 безопасны во всех базах 
данных, поддерживаемых Django.


2. `PositiveIntegerField(**options)` - Подобно IntegerField, но должно быть либо положительным, либо нулевым (0). 
Значения от 0 до 2147483647 безопасны во всех базах данных, поддерживаемых Django. 
Значение 0 принимается по причинам обратной совместимости.


3. `PositiveSmallIntegerField(**options)` - Как и PositiveIntegerField, но допускает значения только в определенной 
(зависящей от базы данных) точке. Значения от 0 до 32767 безопасны во всех базах данных, поддерживаемых Django.


4. `SmallIntegerField(**options)` - Подобно IntegerField, но допускает значения только в определенной (зависящей от базы данных) точке. 
Значения от -32768 до 32767 безопасны во всех базах данных, поддерживаемых Django.


5. `BigIntegerField(**options)` - 64-разрядное целое число, очень похожее на IntegerField, за исключением того, что оно 
гарантированно соответствует числам от -9223372036854775808 до 9223372036854775807. 
Виджет формы по умолчанию для этого поля TextInput


6. `PositiveBigIntegerField(**options)` - Как PositiveIntegerField, но допускает значения только в определенной 
(зависящей от базы данных) точке. Значения от 0 до 9223372036854775807 безопасны во всех базах данных, поддерживаемых Django.

**DecimalField** - Десятичное число

1. `DecimalField(max_digits=None, decimal_places=None, **options)` - Десятичное число с фиксированной точностью, 
представленное в Python экземпляром Decimal. Он проверяет ввод с помощью DecimalValidator.

`DecimalField` имеет следующие аргументы:

* `max_digits` - *Обязательно*. Максимально допустимое количество цифр в номере. 
Обратите внимание, что это число должно быть больше или равно `decimal_places`.


* `decimal_places` - *Обязательно*. Количество десятичных разрядов для хранения с числом.

Пример для максимально поддерживаемого числа 999.99:
```python
models.DecimalField(max_digits=5, decimal_places=2)
```

2. `FloatField(**options)` - Число с плавающей точкой, представленное в Python экземпляром float.

**BinaryField** - поле для хранения бинарных данных

1. `BinaryField(max_length=None, **options)` - Поле для хранения необработанных двоичных данных. 
Может быть назначено bytes, bytearray или memoryview.

`BinaryField` имеет следующие дополнительные аргументы:

* `max_length` - *Необязательно*. Максимальная длина (в байтах) поля. Максимальная длина обеспечивается при проверке 
Django с помощью MaxLengthValidator


**BooleanField** - булевый тип

1. `BooleanField(**options)` - True/False.

**CharField** - строковый тип

1. `CharField(max_length=None, **options)` - Строковое поле, для строк малого и большого размера. 
Для больших объемов текста используйте `TextField`. Виджет формы по умолчанию для этого поля TextInput.

`CharField` имеет следующие дополнительные аргументы:

* `max_length` - *Обязательно*. Максимальная длина (в символах) поля. `max_length` применяется на уровне базы данных 
и при проверке Django с использованием MaxLengthValidator.


* `db_collation` - *Необязательно*. Имя поля сортировки базы данных.

2. `TextField(**options)` - Большое текстовое поле. Виджет формы по умолчанию для этого поля Textarea. 
Если вы укажете атрибут `max_length`, он будет отражен в виджете Textarea автоматически сгенерированного поля формы. 
Однако это не применяется на уровне модели или базы данных. Для этого используйте `CharField`.


3. `EmailField(max_length=254, **options)` - Класс `CharField`, который проверяет, является ли значение действительным 
адресом электронной почты, используя EmailValidator


4. `URLField(max_length=200, **options)` - `CharField` для URL, проверяется валидатором URLValidator.


5. `SlugField(max_length=50, **options)` - это короткая метка для чего-либо, содержащая только буквы, цифры, подчеркивания 
или дефисы. Они обычно используются в URL.


6. `UUIDField(**options)` - Поле для хранения универсально уникальных идентификаторов. 
Использует класс Python UUID. При использовании в PostgreSQL сохраняется в типе данных uuid, иначе в char(32).
Универсально уникальные идентификаторы являются хорошей альтернативой `AutoField` для primary_key. 
База данных не будет генерировать UUID для вас, поэтому рекомендуется использовать default:

```python
import uuid

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
```

7. `GenericIPAddressField(protocol='both', unpack_ipv4=False, **options)` - Адрес IPv4 или IPv6 в строковом формате 
(например, 192.0.2.30 или 2a02:42fe::4). Виджет формы по умолчанию для этого поля TextInput.

`GenericIPAddressField` имеет следующие дополнительные аргументы:

* `protocol` - Ограничивает допустимый ввод для указанного протокола. Допустимые значения: 'both' (по умолчанию), 
'IPv4' или 'IPv6'. Соответствие регистронезависимо.


* `unpack_ipv4` - Распаковывает сопоставленные адреса IPv4 как ::ffff:192.0.2.1. Если опция включена, 
то адрес будет распакован в 192.0.2.1. По умолчанию отключена. Может использоваться только в том случае, если `protocol` 
установлено в 'both'.


**DateField** - тип даты

1. `DateField(auto_now=False, auto_now_add=False, **options)` - Дата, представленная в Python экземпляром `datetime.date`.

`DateField` имеет следующие дополнительные аргументы:

* `auto_now` - Автоматически устанавливает текущую дату каждый раз, когда объект `сохраняется`. 
Полезно для отметок времени последнего изменения. Обратите внимание, что текущая дата всегда используется; 
это не просто значение по умолчанию, которое вы можете переопределить.


* `auto_now_add` - Автоматически установливает поле на сейчас, когда объект `создается впервые`. 
Полезно для создания меток времени.


2. `DateTimeField(auto_now=False, auto_now_add=False, **options)` - Дата и время, представленные в Python экземпляром `datetime.datetime`.

**DurationField** - промежуток времени

1. `DurationField(**options)` - Поле для хранения периодов времени - смоделировано в Python с помощью `timedelta`. 
При использовании в PostgreSQL используемый тип данных представляет собой **interval**, а в Oracle тип данных представляет 
собой **INTERVAL DAY (9) TO SECOND (6)**. В противном случае используется **bigint** микросекунд.

**Хранение объектов**

1. `FileField(upload_to='', storage=None, max_length=100, **options)` - Поле для загрузки файла.

`FileField` имеет следующие дополнительные аргументы ([подробнее](https://django.fun/ru/docs/django/4.1/ref/models/fields/#filefield)):

* `upload_to`(тип: str или callable) - *Необязательно*. Этот атрибут обеспечивает способ указания каталога загрузки и имени файла и может быть установлен двумя способами. 
Если указать строковое значение или Path, оно может содержать форматирование strftime(), 
которое будет заменено датой/временем загрузки файла (чтобы загруженные файлы не заполняли заданный каталог)
```python
# file will be uploaded to MEDIA_ROOT/uploads
upload = models.FileField(upload_to='uploads/')
# or...
# file will be saved to MEDIA_ROOT/uploads/2015/01/30
upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
```
* `storage` (тип: django.core.files.storage.Storage) - *Необязательно*. Определяет класс хранилища, который будет 
использоваться для сохранения файлов. По умолчанию, используется хранилище `django.core.files.storage.FileSystemStorage`
```python
from django.core.files.storage import FileSystemStorage

custom_storage = FileSystemStorage(location='/path/to/custom/storage')

class MyModel(models.Model):
    file = models.FileField(upload_to='uploads/', storage=custom_storage)
```

2. `FilePathField(path='', match=None, recursive=False, allow_files=True, allow_folders=False, max_length=100, **options)` 
CharField, выбор которого ограничен именами файлов в определенном каталоге файловой системы. 

`FilePathField` имеет следующие дополнительные аргументы ([подробнее](https://django.fun/ru/docs/django/4.1/ref/models/fields/#filepathfield)):

* `path` - *Обязательно*. Абсолютный путь файловой системы к каталогу, из которого FilePathField должен получить свой выбор. 
Пример: "/home/images". `path` также может вызываться, например, функция для динамического задания пути во время выполнения. Пример:
```python
import os
from django.conf import settings
from django.db import models

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class MyModel(models.Model):
    file = models.FilePathField(path=images_path)
```

* `match` - *Необязательно*. Регулярное выражение в виде строки, которое FilePathField будет использовать для фильтрации 
имен файлов. Обратите внимание, что регулярное выражение будет применяться к базовому имени файла, а не к полному пути. 
Пример: "foo.*\.txt$", который будет соответствовать файлу с именем foo23.txt, но не bar.txt или foo23.png.


* `recursive` - *Необязательно*. Либо True, либо False. По умолчанию установлено значение False. Указывает, должны ли 
быть включены все подкаталоги `path`.


* `allow_files` - *Необязательно*. Либо True, либо False. По умолчанию установлено значение True. Указывает, следует ли 
включать файлы в указанном месте. Либо это, либо `allow_folders` должно быть True.


* `allow_folders` - *Необязательно*. Либо True, либо False. По умолчанию установлено значение False. Указывает, следует 
ли включать папки в указанном месте. Либо это, либо `allow_files` должно быть True.


3. `ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)` - Наследует все атрибуты 
и методы из FileField, но также проверяет, что загруженный объект является допустимым изображением. 
В дополнение к специальным атрибутам, которые доступны для `FileField`, `ImageField` также имеет атрибуты height и width.

`ImageField` имеет следующие дополнительные аргументы:

* `height_field` - *Необязательно*. Имя поля модели, которое будет автоматически заполняться высотой изображения при 
каждом сохранении экземпляра модели.


* `width_field` - *Необязательно*. Имя поля модели, которое будет автоматически заполняться шириной изображения при 
каждом сохранении экземпляра модели.

4. `JSONField(encoder=None, decoder=None, **options)` - Поле для хранения данных в кодировке JSON. 
В Python данные представляются в родном для Python формате: словари, списки, строки, числа, булевы и None.
JSONField поддерживается на MariaDB, MySQL 5.7.8+, Oracle, PostgreSQL и SQLite (с JSON1 extension enabled).

`JSONField` имеет следующие дополнительные аргументы:

* `encoder` - *Необязательно*. Необязательный подкласс `json.JSONEncoder` для сериализации типов данных, не поддерживаемых 
стандартным сериализатором JSON (например, datetime.datetime или UUID). Например, вы можете использовать класс `DjangoJSONEncoder`.
По умолчанию используется json.JSONEncoder.


* `decoder` - *Необязательно*. Необязательный подкласс `json.JSONDecoder` для десериализации значения, полученного из базы данных. 
Значение будет в формате, выбранном пользовательским кодировщиком (чаще всего это строка). 
Ваша десериализация, возможно, должна учитывать тот факт, что вы не можете быть уверены в типе ввода. 
Например, вы рискуете вернуть datetime, который на самом деле был строкой в том же формате, который выбран для datetime.
По умолчанию используется `json.JSONDencoder`.

# 2. Общие параметры поля

Общие передаваемые параметры в поля, будут обозначаться `**options` и включают в себя:
1. `primary_key` (тип: bool): Указывает, является ли поле первичным ключом модели. 
По умолчанию, первичным ключом является AutoField, но вы можете использовать этот параметр, чтобы явно указать поле 
в качестве первичного ключа. Например:
```python
id = models.AutoField(primary_key=True)
```
2. `verbose_name` (тип: str): Определяет человекочитаемое имя поля. Это имя будет использовано в административной панели Django 
или в других местах, где требуется представление поля для пользователя. Например:
```python
id = models.AutoField(primary_key=True, verbose_name='ID')
```
3. `auto_created` (тип: bool): Указывает, является ли поле автоматически созданным. Этот параметр полезен, когда вы имеете связь 
"многое ко многим" (**ManyToManyField**) и хотите указать, что поле было автоматически создано. Например:
```python
authors = models.ManyToManyField(Author, auto_created=True)
```
4. `db_column` (тип: str): Указывает название столбца в базе данных, к которому привязано поле. 
Если параметр не указан, Django будет использовать имя поля в качестве названия столбца.


5. `db_index` (тип: bool): Определяет, должен ли быть создан индекс для данного поля в базе данных. 
По умолчанию, значение False.


6. `db_tablespace` (тип: str): Указывает таблицевое пространство базы данных, в котором должно храниться поле. 
Если параметр не указан, Django будет использовать значение по умолчанию для базы данных.


7. `serialize` (тип: bool): Определяет, будет ли поле сериализовано при сохранении объекта модели. 
Если установлено значение False, поле будет исключено из сериализации. 
По умолчанию, значение True.


8. `null` (тип: bool): Определяет, может ли поле принимать значение NULL. 
По умолчанию, значение False.


9. `blank` (тип: bool): Определяет, может ли поле быть пустым
По умолчанию, значение False.


10. `editable` (тип: bool): Определяет, может ли поле быть изменено в формах
По умолчанию, значение False.


11. `unique` (тип: bool): Определяет, должно ли поле содержать уникальные значения. 
По умолчанию, значение False.


12. `unique_for_date`, `unique_for_month` и `unique_for_year` (тип: obj): Используются в Django для добавления дополнительных 
ограничений на уникальность значений поля в сочетании с датой.
  * `unique_for_date`: Параметр unique_for_date позволяет задать, что значение поля должно быть уникальным для каждой даты. 
Например, если у вас есть модель Event с полем event_date и вы установите unique_for_date="event_date", это означает, 
что каждая дата должна иметь уникальное значение для поля, т.е. в один день может быть только одно событие с определенным 
значением поля.

  * `unique_for_month`: Параметр unique_for_month позволяет задать, что значение поля должно быть уникальным для каждого месяца. 
Если вы установите unique_for_month="event_date", то значение поля должно быть уникальным в пределах каждого месяца.

  * `unique_for_year`: Параметр unique_for_year позволяет задать, что значение поля должно быть уникальным для каждого года. 
Если вы установите unique_for_year="event_date", то значение поля должно быть уникальным в пределах каждого года.

Пример использования параметра `unique_for_date`:
```python
class Event(models.Model):
    event_date = models.DateField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique_for_date="event_date")
```
В этом примере поле slug должно быть уникальным для каждой даты события, что позволяет создавать уникальные URL-адреса 
для каждого события в рамках определенной даты.

13. `default` (тип: Any): Устанавливает значение по умолчанию для поля(если создавать объект базы данных и не передать
значение полю, то в него запишется значение по умолчанию).
Значение может быть указано в виде конкретного значения или в виде вызова функции. Например:
```python
id = models.AutoField(primary_key=True, default=0)
```

14. `choices` (тип: список): Позволяет ограничить список допустимых значений, которые могут быть присвоены определенному полю. 
Он используется для создания поля с предопределенным набором вариантов выбора. Параметр `choices` принимает список кортежей, 
где каждый кортеж содержит два элемента: значение и человекочитаемое представление значения. Например:
```python
STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
        ('archived', 'В архиве'),
    ]

status = models.CharField(max_length=20, choices=STATUS_CHOICES)
```
В этом примере поле status будет иметь ограниченный набор значений: 'draft', 'published' и 'archived'. 
При создании формы или административного интерфейса Django будет отображать пользователю человекочитаемые представления 
значений, указанные во втором элементе каждого кортежа.


15. `help_text` (тип: str): Предоставляет вспомогательный текст или инструкции для поля. 
Этот текст отображается при использовании формы или в административной панели Django. Например:
```python
id = models.AutoField(primary_key=True, help_text='Уникальный идентификатор записи')
```

16. `error_messages` (тип: dict): Позволяет определить пользовательские сообщения об ошибках для поля. 
Вы можете переопределить предопределенные сообщения об ошибках, такие как null, blank, invalid, и другие. Например:
```python
id = models.AutoField(primary_key=True, error_messages={
    'null': 'Поле ID не может быть пустым.',
    'invalid': 'Недопустимое значение для поля ID.'
})
```
17. `validators` (тип: список функций или вызываемых объектов): Позволяет определить пользовательские валидаторы для поля. 
Валидаторы используются для проверки вводимых данных и обеспечения их соответствия определенным условиям. Например:
```python
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value <= 0:
        raise ValidationError('Значение должно быть положительным числом.')

id = models.AutoField(primary_key=True, validators=[validate_positive])
```