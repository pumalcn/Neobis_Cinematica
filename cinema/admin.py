from django.contrib import admin

from cinema.models import (
    Cinema, Hall, MovieScreening,
    Movie, Reserve, Ticket,
    Seat, Row, Discount,
    Feedback, PurchaseHistory
)

admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.register(Row)
admin.site.register(Seat)
admin.site.register(Movie)
admin.site.register(MovieScreening)
admin.site.register(Reserve)
admin.site.register(Ticket)
admin.site.register(Discount)
admin.site.register(Feedback)
admin.site.register(PurchaseHistory)