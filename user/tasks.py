from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from massage import settings
from django.template.loader import render_to_string
from celery import Celery


@shared_task
def mail(verify_id, email_user):
    email_host = settings.EMAIL_HOST
    massage = render_to_string('user/verify.html', {'verify_id': verify_id})
    return send_mail('verify', massage, email_host, [email_user])
