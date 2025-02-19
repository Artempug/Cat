from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SpyCat, Mission, Target
from .serializers import SpyCatSerializer, MissionSerializer, TargetSerializer

#ViewSet for SpyCat model
class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

#ViewSet for Mission model
class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    #Prevent deletion if mission has an assigned spy cat
    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.spy_cat:
            return Response({"error": "Cannot delete a mission assigned to a spy cat"}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

    #Mark the mission as complete if all targets are complete
    @action(detail=True, methods=['patch'], url_path='complete')
    def complete_mission(self, request, pk=None):
        mission = self.get_object()
        if all(target.is_complete for target in mission.targets.all()):
            mission.is_complete = True
            mission.save()
            return Response({"status": "Mission completed"})
        return Response({"error": "Not all targets are completed"}, status=status.HTTP_400_BAD_REQUEST)

#ViewSet for Target model
class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    #Mark the target as complete
    @action(detail=True, methods=['patch'], url_path='mark-complete')
    def mark_complete(self, request, pk=None):
        target = self.get_object()
        if target.is_complete:
            return Response({"error": "Target is already completed"}, status=status.HTTP_400_BAD_REQUEST)
        target.is_complete = True
        target.save()
        return Response({"status": "Target marked as complete"})
