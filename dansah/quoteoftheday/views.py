from datetime import datetime

from rest_framework import status, generics
from rest_framework.response import Response

from .models import QuoteOfTheDay
from .quoteofthedayserializers import QuoteOfTheDaySerializer


class QuoteOfTheDayView(generics.GenericAPIView):
    serializer_class = QuoteOfTheDaySerializer
    queryset = QuoteOfTheDay.objects.all()

    def get(self, request):
        parsed_date = self.get_date_query_param(request)
        if not parsed_date:
            quote_of_the_day = QuoteOfTheDay.objects.all()
        else:
            quote_of_the_day = QuoteOfTheDay.filter(quote_date=parsed_date)
        if not quote_of_the_day:
            return Response({"status": "No quote of the day available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(quote_of_the_day, many=True)
        return Response({
            "status": "success",
            "quote_of_the_day": serializer.data
        })

    def get_date_query_param(self,request):
        date_param = request.query_params.get('date')

        if date_param:
            try:
                # Perform any additional validation or parsing of the date parameter
                # For example, you can convert it to a datetime object
                parsed_date = datetime.datetime.strptime(date_param, '%Y-%m-%d').date()
                # ... do something with the parsed date ...

                return parsed_date
            except :
                return None



class QuoteOfTheDayDetailView(generics.GenericAPIView):
    serializer_class = QuoteOfTheDaySerializer
    queryset = QuoteOfTheDay.objects.all()

    def get_quote_of_day(self, pk):
        try:
            return QuoteOfTheDay.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        quote_of_day = self.get_quote_of_day(pk)
        if quote_of_day is None:
            return Response({"status": "fail", "message": f"Quote of the day with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(quote_of_day)
        return Response({"status": "success", "quote_of_Day": serializer.data})
