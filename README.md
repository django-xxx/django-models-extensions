# django-models-extensions
Django Models Extensions

## Installation
```shell
pip install django-models-ext
```

## Usage
```python
from models_ext import upload_path

class MyModel(models.Model):
    upload = models.FileField(upload_to=upload_path)
```
