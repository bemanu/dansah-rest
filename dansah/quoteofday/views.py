from rest_framework import status, generics
from rest_framework.response import Response

from .models import QuoteOfTheDay
from .serializers import QuoteOfTheDaySerializer


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

    def get_quote_of_day(self, pk):
        try:
            return QuoteOfTheDay.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        quote_of_day = self.get_quote_of_day(pk=pk)
        if quote_of_day is None:
            return Response({"status": "fail", "message": f"Quote of the day with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(quote_of_day)
        return Response({"status": "success", "quote_of_Day": serializer.data})


