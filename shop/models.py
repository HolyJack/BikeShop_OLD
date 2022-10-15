from django.db import models


class Frame(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Seat(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Tire(models.Model):
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.type


class Basket(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return 'Basket'

    def is_available(self):
        if self.quantity > 0:
            return True
        return False


class Bike(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    has_basket = models.BooleanField(default=False)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_available(self):
        if self.frame.quantity < 1 or\
                self.tire.quantity < 2 or\
                self.seat.quantity < 1:
            return False

        if self.has_basket:
            basket = Basket.objects.filter().first()
            if not basket.is_available():
                return False

        return True

    def bought(self):
        self.frame.quantity -= 1
        self.seat.quantity -= 1
        self.tire.quantity -= 2
        self.frame.save()
        self.seat.save()
        self.tire.save()
        if self.has_basket:
            basket = Basket.objects.filter().first()
            basket.quantity -= 1
            basket.save()
        self.save()


class Order(models.Model):
    PENDING = 'P'
    READY = 'R'
    ORDER_STATUSES = [
        (PENDING, 'Pending'),
        (READY, 'Ready')
    ]
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=ORDER_STATUSES, default=PENDING)

    def __str__(self):
        return f'Order {self.pk}'
