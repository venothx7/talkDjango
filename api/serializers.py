from rest_framework import  serializers

from talkApp.models import Talk


class TalkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talk
        fields = ('id','name','speaker','venue','duration')