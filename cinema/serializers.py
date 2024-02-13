from rest_framework import serializers
from .models import Cinema, Hall, Movie, MovieScreening, Reserve, Ticket, Row, Seat, Discount, Feedback, PurchaseHistory


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieScreening
        fields = '__all__'


class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['user', 'have_discount']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['user', 'cinema', 'hall', 'movie', 'screening', 'seat', 'payment_method', 'ticket_amount', 'discount',
                  'total_bill', 'purchase_time']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class PurchaseHistorySerializer(serializers.ModelSerializer):
    movies_info = TicketSerializer(read_only=True, many=True)

    class Meta:
        model = PurchaseHistory
        fields = ['user', 'total_bill', 'movies_info']