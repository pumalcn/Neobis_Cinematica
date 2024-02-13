from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Cinema, Hall, Movie, MovieScreening, Reserve, Ticket, Row, Seat, Discount, Feedback, PurchaseHistory
from .serializers import (
    CinemaSerializer,
    HallSerializer,
    MovieSerializer,
    MovieScreeningSerializer,
    ReserveSerializer,
    TicketSerializer,
    RowSerializer,
    SeatSerializer,
    DiscountSerializer,
    FeedbackSerializer,
    PurchaseHistorySerializer
)


class CinemaListView(generics.ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaCreateView(generics.CreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [IsAdminUser]


class CinemaUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [IsAdminUser]


class HallListCreateView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsAdminUser]


class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]


class MovieScreeningListView(generics.ListAPIView):
    queryset = MovieScreening.objects.all()
    serializer_class = MovieScreeningSerializer


class MovieScreeningCreateView(generics.CreateAPIView):
    queryset = MovieScreening.objects.all()
    serializer_class = MovieScreeningSerializer
    permission_classes = [IsAdminUser]


class MovieScreeningUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieScreening.objects.all()
    serializer_class = MovieScreeningSerializer


class RowListCreateView(generics.ListCreateAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer
    permission_classes = [IsAdminUser]


class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAdminUser]


class ReserveListCreateView(generics.ListCreateAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [IsAuthenticated]


class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [IsAdminUser]


class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        discount, created = Discount.objects.get_or_create(user=user)
        serializer.save(user=user, discount=discount)


class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminUser]


class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class FeedbackListView(generics.ListAPIView):
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer
    permission_classes = [IsAdminUser]


class PurchaseHistoryView(generics.ListAPIView):
    queryset = PurchaseHistory.objects.all().order_by('-id')
    serializer_class = PurchaseHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PurchaseHistory.objects.filter(user=self.request.user)
