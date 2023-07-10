from rest_framework import status, generics
from rest_framework.response import Response

from .models import Media, SocialMedia
from .socialmediaserializers import MediaSerializer, SocialMediaSerializer


class MediaView(generics.GenericAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

    def get(self, request):
        media = Media.objects.all()
        if not media:
            return Response(
                {"status": "No social media available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(media, many=True)
        return Response({"status": "success", "result": serializer.data})


class MediaDetailView(generics.GenericAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

    def get_media(self, pk):
        try:
            return Media.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        media = self.get_home_ministries_material(pk=pk)
        if media is None:
            return Response(
                {"status": "fail", "message": f"Media data with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(media)
        return Response({"status": "success", "media": serializer.data})


class SocialMediaView(generics.GenericAPIView):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

    def get(self, request):
        social_media = SocialMedia.objects.all()
        if not social_media:
            return Response(
                {"status": "No social media data available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(social_media, many=True)
        return Response({"status": "success", "social_media": serializer.data})


class SocialMediaDetailView(generics.GenericAPIView):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

    def get_social_media(self, pk):
        try:
            return SocialMedia.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        social_media = self.get_ministries_material(pk=pk)
        if social_media is None:
            return Response(
                {"status": "fail", "message": f"Social media with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(social_media)
        return Response({"status": "success", "social_media": serializer.data})
