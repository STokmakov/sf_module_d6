from django.db.models.signals import m2m_changed, post_save
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory, Post


def send_notifications(preview, pk, title, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@receiver(post_save, sender=Post)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['actions'] == 'post_create':
#         categories = instance.category.all()
#         subscribers: list[str] = []
#
#         for category in categories:
#             subscribers += category.subscribers.all()
#
#         subscribers = [s.email for s in subscribers]
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers)

def test_signal(sender, instance, **kwargs):
    print(f'I am signal!!!')