from django.core.mail import  send_mail,EmailMessage
from django.conf import settings
from django.conf import  settings
# For normal email send

filepath=f"{settings.BASE_DIR}/data.csv"
def send_email_client(x,y):
    print("ldpldp")
    subject="User Created!!"
    message="Hi,{0} \n".format(str(x).upper())+"This Is system generated don't replay in this email.User has succcessfully created.\n"+"Regards,\n"+"Admin Team"
    from_email=settings.EMAIL_HOST_USER
    recipient_user=[y]
    send_mail(subject,message,from_email,recipient_user)

# normal emal with attachment
def send_email_with_attachemt(x,y):
    subject = "User Created!!"
    message = "Hi,{0} \n".format(
        str(x).upper()) + "This Is system generated don't replay in this email.User has succcessfully created.\n" + "Regards,\n" + "Admin Team"
    from_email = settings.EMAIL_HOST_USER
    recipient_user = [y]
    email=EmailMessage(subject=subject,body=message,from_email=from_email,to=recipient_user)
    email.attach_file(filepath)
    email.send()


