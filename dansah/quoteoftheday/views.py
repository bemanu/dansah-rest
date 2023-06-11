from datetime import date

from rest_framework import status, generics
from rest_framework.response import Response

from .models import QuoteOfTheDay
from .quoteofthedayserializers import QuoteOfTheDaySerializer


class QuoteOfTheDayView(generics.GenericAPIView):
    serializer_class = QuoteOfTheDaySerializer
    queryset = QuoteOfTheDay.objects.all()

    def get(self, request):
        quote_of_the_day = QuoteOfTheDay.objects.all()
        if not quote_of_the_day:
            return Response({"status": "No quote of the day available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(quote_of_the_day, many=True)
        return Response({
            "status": "success",
            "quote_of_the_day": serializer.data
        })


class QuoteOfTheDayDetailView(generics.GenericAPIView):
    serializer_class = QuoteOfTheDaySerializer
    queryset = QuoteOfTheDay.objects.all()

    def get_quote_of_day(self, pk, date_param):
        try:
            return QuoteOfTheDay.objects.filter(pk=pk, date=date_param)
        except:
            return None

    def get(self, request, pk):
        quote_of_day = self.get_quote_of_the_day_for_date(pk, request)
        if quote_of_day is None:
            return Response({"status": "fail", "message": f"Quote of the day with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(quote_of_day)
        return Response({"status": "success", "quote_of_Day": serializer.data})

    def get_quote_of_the_day_for_date(self, pk, request):
        date_of_quote_of_the_day = request.query_params.get('date')
        if date_of_quote_of_the_day is None:
            date_of_quote_of_the_day = date.today()
        quote_of_day = self.get_quote_of_day(pk=pk, date_param=date_of_quote_of_the_day)
        return quote_of_day
