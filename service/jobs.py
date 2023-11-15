from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone


from service.const import CREATED, READY, COMPLETED, LAUNCHED, NO_ACTIVE, START
from service.models import Mailing

scheduler = BackgroundScheduler()


def job_rady_check():
    mailing = Mailing.objects.all()
    print('началась проверка')
    now = datetime.now()
    now = timezone.make_aware(now, timezone.get_current_timezone())
    print(now)
    for mail in mailing:
        if not mail.is_active:
            mail.status = NO_ACTIVE
        else:
            mail.status = CREATED
            if not mail.stop > now:
                mail.status = COMPLETED
            else:
                mailing_clients = mail.clients.all()
                if not mail.massage in [None, ''] and mailing_clients.exists():

                    if not mail.start < now:
                        mail.status = READY
                    else:
                        mail.status = LAUNCHED
                        mail.start = START + timedelta(minutes=mail.periodic)
                        for client in mailing_clients:
                            send_mail(
                                subject=mail.massage.title,
                                message=mail.massage.text,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list=[client.email]
                            )
        mail.save()
