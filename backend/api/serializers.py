from rest_framework import serializers
from .models import Risk, Field


class FieldSerializer(serializers.ModelSerializer):
    # field_type = serializers.CharField(source='get_field_type_display')

    class Meta:
        model = Field
        fields = ('name', 'field_type')


class RiskSerializer(serializers.ModelSerializer):
    fieldz = FieldSerializer(many=True)

    class Meta:
        model = Risk
        fields = ('risk_type', 'fieldz')

    def create(self, validated_data):
        fields_data = validated_data.pop('fieldz')
        risk = Risk.objects.create(**validated_data)
        for field_data in fields_data:
            Field.objects.create(risk=risk, **field_data)
        return risk
