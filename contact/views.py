from rest_framework import generics, status
from rest_framework.response import Response

from .models import Contact
from .contactserializers import ContactSerializer


class ContactView(generics.GenericAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get(self, request):
        contact = Contact.objects.all()
        if not contact:
            return Response(
                {"status": "No contact available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(contact, many=True)
        return Response({"status": "success", "result": serializer.data})
