from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.urls import reverse

@receiver(user_signed_up)
def redirect_to_complete_profile(request, user, **kwargs):
    request.session['next'] = reverse('complete_profile')