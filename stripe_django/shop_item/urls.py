from django.urls import path
from .views import get_session_stripe, success_view, cancel_view, pay_items

urlpatterns = [
    path('buy/<int:item_id>/', get_session_stripe, name='get_session'),
    path('success/', success_view, name='success_view'),
    path('cancel/', cancel_view, name='cancel_view'),
    path('item/<int:item_id>/', pay_items, name='pay_items'),
]
