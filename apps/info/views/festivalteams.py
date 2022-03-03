from rest_framework.generics import ListAPIView

from apps.info.models import FestivalTeamMember
from apps.info.serializers import FestivalTeamsSerializer


class FestivalTeamsAPIView(ListAPIView):
    queryset = FestivalTeamMember.objects.all()
    serializer_class = FestivalTeamsSerializer
    filterset_fields = ("team",)
    pagination_class = None
