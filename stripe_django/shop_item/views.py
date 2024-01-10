from django.shortcuts import reverse

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import stripe
from .models import Order, Item
from django.shortcuts import get_object_or_404
import os

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


@require_http_methods(['GET'])
def get_session_stripe(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success_view')),
        cancel_url=request.build_absolute_uri(reverse('cancel_view')),
    )
    return JsonResponse({'session_id': session.id})


def success_view(request):
    return render(request, 'success.html')


def cancel_view(request):
    return render(request, 'cancel.html')
