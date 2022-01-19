import os
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.shortcuts import reverse
from .views import product_details
from django.db.models import Q
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import *
from users.models import Profile


def created_email(user_list, product, link):
    send_mail(
        subject=f'New Product Created: {product.product_name}',
        message=f'',
        recipient_list=user_list,
        from_email=os.environ.get('EMAIL_HOST_USER', ''),
        html_message=f"""
            <h1>New Product: {product.product_name}</h1>
            <h3><b>Customer:</b> {product.customer}</h3>
            <h3><b>Department:</b> {product.department}</h3>
            <h3><b>Start Date:</b> {product.start_date}</h3>
            <h3><b>Link:</b> {link}</h3>
        """
    )


@receiver(post_save, sender=Product)
def product_notification(sender, instance, created, **kwargs):
    if created:
        user_list = User.objects.values_list('email', flat=True)
        created_email(user_list, instance, reverse(product_details, args=[instance.id]))
    else:
        # send email of product updated
        pass

    # update product status to final confirmation status
    # if prerequisites met
    if instance.is_ready_for_signoff():
        instance.status = ProductStatus.objects.get(
            status="Pending - Awaiting Final Confirmation"
        )
        instance.save()
