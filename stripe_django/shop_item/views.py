from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import stripe
from .models import Item
from django.shortcuts import get_object_or_404
import os

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


@require_http_methods(['GET'])
def get_session_stripe(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    session = stripe.checkout.Session.create(
        paymount_method_types=['card'],
        line_items
    )
