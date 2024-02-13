import decimal

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Cinema(models.Model):
    cinema_name = models.CharField(max_length=100)
    cinema_address = models.CharField(max_length=100)
    start_work = models.TimeField(verbose_name='Начало работы')
    end_work = models.TimeField(verbose_name='Конец работы')

    def __str__(self):
        return f"{self.cinema_name} - {self.cinema_address}"


class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    hall_type = models.CharField(max_length=100, verbose_name='Hall Type')
    hall_name = models.CharField(max_length=255, verbose_name='Hall Name')

    def __str__(self):
        return f"{self.cinema.cinema_name} - {self.hall_name} - {self.hall_type}"


class Row(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row_number = models.PositiveIntegerField(verbose_name='Row Number')

    def __str__(self):
        return f"Row: {self.row_number}"


class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField(verbose_name='Seat Number')

    def __str__(self):
        return f"Hall Name: {self.hall.hall_name} - Row Number: {self.row.row_number} Seat Number: {self.seat_number}"


class Movie(models.Model):
    title = models.CharField(max_length=150, verbose_name='Movie Title')
    genres = models.CharField(max_length=150)
    description = models.TextField(max_length=1500, verbose_name='Movie Description')
    duration = models.CharField(max_length=20, verbose_name='Movie Duration')
    poster = models.ImageField(verbose_name='Movie Poster')
    is_active = models.BooleanField(default=True)
    release_day = models.DateField(verbose_name="Upcoming Day")
    end_day = models.DateField(verbose_name="Distribution Off Day")

    def __str__(self):
        return self.title


class MovieScreening(models.Model):
    show_time = models.DateTimeField(verbose_name='Movie Showing', default=timezone.now)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    cinema_hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Movie Price')

    def __str__(self):
        return f'{self.movie.title}-{self.show_time}-{self.price}'


class Reserve(models.Model):
    room = models.ForeignKey(Hall, on_delete=models.CASCADE)
    screening = models.ForeignKey(MovieScreening, on_delete=models.CASCADE)
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.screening.movie.title}-{self.screening.show_time}-{self.room.hall_name}" \
               f"-Ряд {self.row.row_number}, Место {self.seat.seat_number}"


class Discount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    have_discount = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Ticket(models.Model):
    PAY_METHODS = (
        ('card', 'Картой'),
        ('cash', 'Наличные')

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screening = models.ForeignKey(MovieScreening, on_delete=models.CASCADE)
    seat = models.ManyToManyField(Seat)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAY_METHODS, verbose_name='Payment Method')
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ticket_amount = models.PositiveIntegerField(default=1)
    purchase_time = models.DateTimeField(auto_now=True, verbose_name='Purchase Time')

    def save(self, *args, **kwargs):
        bill = self.screening.price * self.ticket_amount
        if self.discount.have_discount:
            bill *= decimal.Decimal(0.97)
        self.total_bill = bill
        super().save(*args, **kwargs)
        purchase_history, created = PurchaseHistory.objects.get_or_create(user=self.user)
        purchase_history.total_bill += self.total_bill
        purchase_history.movies_info.add(self)
        purchase_history.save()

    def __str__(self):
        return f'{self.total_bill}-{self.ticket_amount}'


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    movies_info = models.ManyToManyField(Ticket, related_name='purchase_history', blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.total_bill}"


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.cinema.cinema_name} - {self.created_at}"
