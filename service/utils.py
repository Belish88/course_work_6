from django.utils.timezone import localtime


def start():
    result = localtime().now()
    return result
