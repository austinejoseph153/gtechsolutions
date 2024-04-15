from django.core.mail import EmailMessage,BadHeaderError,get_connection
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.timezone import now

def send_email_message(from_email,message):

    admins = getattr(settings,"ADMIN",None)
    subject ="Gtechsolution -{}".format(_("Email Services"))
    message = message
    from_email= from_email
    if admins:
        for admin in admins:
            with get_connection(
                "django.core.mail.backends.console.EmailBackend"
            ) as connection:
                send_email = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=from_email,
                    to=[admin[1]],
                    connection=connection
                )
                send_email.send()
        return True
    else:
        return False

def send_email_when_account_is_created(user):
    subject ="User Account Creation"
    message = "".format(user)
    from_email= from_email
    to_email = settings.DEFAULT_FROM_EMAIL
    send_email = EmailMessage(
        subject=subject,
        body=message,
        from_email=from_email,
        to=[to_email]
    )