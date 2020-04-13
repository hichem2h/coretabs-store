from django.template.loader import render_to_string


def send_order_email(user, order):

    subject = 'Your Order Details'
    message = render_to_string('orders/order_email.html', {
        'user': user,
        'order': order,
    })

    user.email_user(subject, message)
