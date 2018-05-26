from django.core.management.base import NoArgsCommand
from tracker.models import Notification
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

class Command(NoArgsCommand):
    help = 'Process pending notifications'
    
    def handle_noargs(self, **options):
        subject_text = get_template('notification/notification_subject.txt').render()
        body_template = get_template('notification/notification_text.txt')
        html_template = get_template('notification/notification_html.html')
        for user in User.objects.all():
            ack_notifs = Notification.objects.filter(target_user=user, notification_type="ack")
            ticket_notifs = Notification.objects.filter(target_user=user, notification_type="ticket")
            comment_notifs = Notification.objects.filter(target_user=user, notification_type="comment")

            if len(ack_notifs) > 0 or len(ticket_notifs) > 0 or len(comment_notifs) > 0:
                c_dict = {u"ack_notifs": ack_notifs, u"ticket_notifs": ticket_notifs, u"comment_notifs": comment_notifs, u"ABSOLUTE_URL": settings.ABSOLUTE_URL}
                c = Context(c_dict)
                user.email_user(subject_text, body_template.render(c), html_message=html_template.render(c))
            for notification in Notification.objects.filter(target_user=user):
                #notification.delete()
                print 'sending'