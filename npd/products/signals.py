import os

from django.db.models.signals import post_save, post_delete, m2m_changed
from django.shortcuts import reverse
from django.db.models import Q
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.sites.models import Site

from .views import product_details
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
            A new product has been created on the Meade NPD App.
            <h3><b>Customer:</b> {product.customer}</h3>
            <h3><b>Department:</b> {product.department}</h3>
            <h3><b>Start Date:</b> {product.start_date}</h3>
            <h3><b>Link:</b> http://{str(Site.objects.get_current()) + link}</h3>
        """
    )


def signoff_email(user_list, product, link):
    send_mail(
        subject=f'Ready For Signoff: {product.product_name}',
        message=f'',
        recipient_list=user_list,
        from_email=os.environ.get('EMAIL_HOST_USER', ''),
        html_message=f"""
            <h1>Product: {product.product_name}</h1>
            A product is ready for signoff on the Meade NPD App.
            <h3><b>Customer:</b> {product.customer}</h3>
            <h3><b>Department:</b> {product.department}</h3>
            <h3><b>Start Date:</b> {product.start_date}</h3>
            <h3><b>Link:</b> http://{str(Site.objects.get_current()) + link}</h3>
        """
    )


def ready_email(user_list, product, link):
    send_mail(
        subject=f'Production Ready: {product.product_name}',
        message=f'',
        recipient_list=user_list,
        from_email=os.environ.get('EMAIL_HOST_USER', ''),
        html_message=f"""
            <h1>Product: {product.product_name}</h1>
            A product is complete and production ready on the Meade NPD App.
            <h3><b>Customer:</b> {product.customer}</h3>
            <h3><b>Department:</b> {product.department}</h3>
            <h3><b>Start Date:</b> {product.start_date}</h3>
            <h3><b>Link:</b> http://{str(Site.objects.get_current()) + link}</h3>
        """
    )


@receiver(post_save, sender=Product)
def product_notification(sender, instance, created, **kwargs):
    if created:
        user_list = User.objects.values_list('email', flat=True)
        created_email(user_list, instance, reverse(product_details, args=[instance.id]))
    
    if instance.is_ready():
        user_list = User.objects.values_list('email', flat=True)
        ready_email(user_list, instance, reverse(product_details, args=[instance.id]))


    # update product status to final confirmation status
    # if prerequisites met
    if instance.is_ready_for_signoff():
        instance.status = ProductStatus.objects.get(
            status="Pending - Awaiting Final Confirmation"
        )
        instance.save()
        user_list = User.objects.filter(groups__name__in=['Commercial', 'Admin']).values_list('email', flat=True)
        print(user_list)
        signoff_email(user_list, instance, reverse(product_details, args=[instance.id]))


@receiver(post_save, sender=CommercialModel)
@receiver(post_save, sender=ApprovedOrigin)
@receiver(post_save, sender=ApprovedVariety)
@receiver(post_save, sender=ApprovedSupplier)
@receiver(post_save, sender=InnerPackaging)
@receiver(post_save, sender=OuterPackaging)
@receiver(post_save, sender=Palletisation)
@receiver(post_save, sender=OperationsModel)
@receiver(post_save, sender=DefectSpecification)
@receiver(post_save, sender=FinishedProduct)
@receiver(post_save, sender=ProphetModel)
def commercial_notification(sender, instance, created, **kwargs):
    # update product status to final confirmation status
    # if prerequisites met
    if instance.product.is_ready_for_signoff():
        instance.product.status = ProductStatus.objects.get(
            status="Pending - Awaiting Final Confirmation"
        )
        instance.product.save()
        user_list = User.objects.filter(
            groups__name__in=['Commercial', 'Admin']).values_list('email', flat=True)
        print(user_list)
        signoff_email(
            user_list, 
            instance.product, 
            reverse(product_details, args=[instance.product.id]))