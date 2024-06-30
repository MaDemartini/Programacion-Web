from decimal import Decimal
from django.conf import settings
from .models import Subscripcion

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, subscription):
        subscription_id = str(subscription.id)
        if subscription_id not in self.cart:
            self.cart[subscription_id] = {
                'id': subscription_id,
                'cantidad': 1,
            }
        else:
            self.cart[subscription_id]['cantidad'] += 1
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, item_id):
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def get_cart_items(self):
        subscription_ids = self.cart.keys()
        subscriptions = Subscripcion.objects.filter(id__in=subscription_ids)
        cart_items = []
        for subscription in subscriptions:
            cart_items.append({
                'subscription': subscription,
                'cantidad': self.cart[str(subscription.id)]['cantidad'],
            })
        return cart_items

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
