from django.contrib import admin
from .models import *


class FrameAdmin(admin.ModelAdmin):
    pass


class SeatAdmin(admin.ModelAdmin):
    pass


class TireAdmin(admin.ModelAdmin):
    pass


class BasketAdmin(admin.ModelAdmin):
    pass


class BikeAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Frame, FrameAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Tire, TireAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Order, OrderAdmin)
