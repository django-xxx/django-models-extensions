========================
django-models-extensions
========================

Django Models Extensions

Installation
============

::

    pip install django-models-ext


Usage
=====

::

    from models_ext import upload_path

    class MyModel(models.Model):
        upload = models.FileField(upload_to=upload_path)

