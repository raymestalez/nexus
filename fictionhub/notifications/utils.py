from django.core.mail import send_mail # for email
from notifications.models import Message

def send_comment_email(from_username,to_email,story_url,comment_body):
    if comment.post.author.email_comments:

        try:
            email = to_email
            send_mail(topic, body, 'raymestalez@gmail.com', [email], fail_silently=False)
        except:
            pass



        

def send_notification_email(message):
    from_username = message.from_user.username
    to_user = message.to_user
    send_email = False

    if message.message_type == "upvote" and to_user.email_upvotes:
        send_email = True
        story_url = message.story.get_absolute_url()
        story_title = message.story.title
        
        topic = "fictionhub: " + from_username + " upvoted your story "  + story_title
        body = from_username + " upvoted your story\n" +\
               "http://fictionhub.io"+story_url
        body += "\n\nYou can manage your email notifications in preferences:\n" +\
                "http://fictionhub.io/preferences/"
    elif message.message_type == "subscriber"  and to_user.email_subscribers:
        send_email = True

        topic = "fictionhub: " + from_username + " subscribed to your stories!"
        body = from_username + " subscribed to your stories!"
        body += "\n\nYou can manage your email notifications in preferences:\n" +\
                "http://fictionhub.io/preferences/"
    elif message.message_type == "comment" and to_user.email_comments:
        send_email = True
        story_url = message.story.get_absolute_url()
        comment_body = message.comment.body

        topic = "fictionhub: " + from_username + " has commented on your story "
        body = from_username + " has left a comment on your story\n" +\
               "http://fictionhub.io"+story_url+ "\n" +\
               "'" + comment_body[:64] + "...'"
        body += "\n\nYou can manage your email notifications in preferences:\n" +\
                "http://fictionhub.io/preferences/"        
    elif message.message_type == "message" and to_user.email_comments:
        send_email = True

        topic = "fictionhub: " + from_username + " has sent you a message "
        body = from_username + " has  sent you a message:\n" +\
               "'" + message.subject.title + "'\n" + \
               message.body + "\n" + \
               "http://fictionhub.io/subject/" + str(message.subject.pk) + "/"
        body += "\n\nYou can manage your email notifications in preferences:\n" +\
                "http://fictionhub.io/preferences/"        

    if send_email == True:
        try:
            email = "raymestalez@gmail.com" # to_user.email
            send_mail(topic, body, 'raymestalez@gmail.com', [email], fail_silently=False)
        except:
            pass

    message.email_sent = True
    message.save()

            
def send_email_notifications():
    messages = Message.objects.filter(email_sent=False, isread=False)
    teststring = ""
    for message in messages:
        send_notification_email(message)
        teststring += str(message) + "</br>"

    return teststring
