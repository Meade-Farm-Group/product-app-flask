from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Product)
def product_notification(sender, instance, created, **kwargs):
    if created:
        # send email of new product created
        pass
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
