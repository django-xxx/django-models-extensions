# django-models-extensions
Django Models Extensions

## Installation
```shell
pip install django-models-ext
```

## Usage
```python
from django_models_ext import BaseModelMixin, upload_path, upload_file_url

class MyModel(BaseModelMixin):
    upload = models.FileField(upload_to=upload_path)

    @property
    def upload_url(self):
        return upload_file_url(self.upload)
```
