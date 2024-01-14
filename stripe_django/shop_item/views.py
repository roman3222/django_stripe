from django.shortcuts import reverse

from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
import stripe
from .models import Order, Item
from django.shortcuts import get_object_or_404
import os

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


def get_public_key() -> str:
    stripe_public_key = os.getenv('STRIPE_PUBLISHABLE_KEY')
    return stripe_public_key


@require_http_methods(['GET'])
def get_session_stripe(request, item_id: int) -> JsonResponse:
    item = get_object_or_404(Item, pk=item_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success_view')),
        cancel_url=request.build_absolute_uri(reverse('cancel_view')),
    )
    return JsonResponse({'session_id': session.id})


def success_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'success.html')


def cancel_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'cancel.html')


def pay_items(request: HttpRequest, item_id: int) -> HttpResponse:
    item = Item.objects.get(pk=item_id)
    stripe_public_key = get_public_key()
    context = {'item': item, 'stripe_public_key': stripe_public_key}
    return render(request, 'buy.html', context)


def create_payment_intent(request, user_id: int) -> JsonResponse:
    try:
        orders = Order.objects.filter(user=user_id)
        total_amount = sum(order.total_price() for order in orders)
        intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),
            currency=orders[0].items.first().currency if orders else 'usd',
        )
        return JsonResponse({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({'error': str(e)})


def pay_order(request: HttpRequest, user_id: int) -> HttpResponse:
    order = Order.objects.filter(user=user_id)
    total_amount = sum(order.total_price() for order in order)
    discount = order.first().discount
    tax = order.first().tax
    all_items = [item for order in order for item in order.items.all()]
    client_secret = create_payment_intent(request, user_id)
    stripe_public_key = get_public_key()
    context = {
        'client_secret': client_secret,
        'stripe_public_key': stripe_public_key,
        'order': order,
        'total_amount': total_amount,
        'all_items': all_items,
        'discount': discount,
        'tax': tax,
    }
    return render(request, 'buy_order.html', context)
