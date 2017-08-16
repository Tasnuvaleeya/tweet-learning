from django.core.exceptions import ValidationError


def validate_content(value):
    content = value
    if content=='':
        raise ValidationError('The Content can not be ABC ')
    return value
