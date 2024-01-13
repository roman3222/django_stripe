from django.urls import path
from .views import get_session_stripe, success_view, cancel_view, pay_items, create_payment_intent, pay_order
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('buy/<int:item_id>/', get_session_stripe, name='get-session'),
    path('success/', success_view, name='success_view'),
    path('cancel/', cancel_view, name='cancel_view'),
    path('item/<int:item_id>/', pay_items, name='pay_items'),
    path('payment/<int:user_id>/', create_payment_intent, name='payment-view'),
    path('buy/order/<int:user_id>/', pay_order, name='pay_order')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

