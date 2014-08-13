from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
from user_place.token_generator import *
from django.http import HttpResponse
from django.utils.translation import ugettext as _


def mail_sender(email):
        plaintext = get_template('email/email_content.html')
        subject, from_email = 'hello',\
                              'surveydck@gmail.com'
        if email:
            to = email

            hash_key_example = activation_key_generator(to)
            transmitted_key = Context(
                {'hash_key': hash_key_example})

            # text_content = plaintext.render(d)
            text_content = render_to_string('email/email_content.html',
                                            transmitted_key)

            msg = EmailMultiAlternatives(subject,
                                         text_content,
                                         from_email,
                                         [to])
            msg.send()
            return HttpResponse(_("mailiniz gonderildi"))

        else:
            return HttpResponse(_("Gondereceginiz kisinin"
                                "email adresi belli olmalidir."))