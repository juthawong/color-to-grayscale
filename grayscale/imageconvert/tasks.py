from __future__ import absolute_import

from django.conf import settings
from django.core.files import File

from celery import shared_task
from subprocess import call
import os

from .models import Image


def handle_upload(object):
    task = convert_to_gray.delay(object.pk, object.color_file.path)
    return task.id


@shared_task
def convert_to_gray(pk, path):
    output_name = "%s.gray%s" % (os.path.splitext(path))
    command = [
        'convert',
        path,
        '-set', 'colorspace', 'Gray',
        '-separate',
        '-average',
        output_name]
    call(command)

    f = File(open(output_name, 'r'))
    o = Image.objects.get(pk=pk)
    o.gray_file = f
    o.save()

    url = settings.MEDIA_URL + os.path.basename(output_name)
    return url
