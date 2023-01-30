from rest_framework import serializers
from transacoes.models import Transacoes

class TransacoesSerializers (serializers.Serializer):
    type = serializers.CharField(max_length=1)
    data = serializers.DateField()
    value= serializers.DecimalField(max_digits=10, decimal_places=2)
    cpf = serializers.CharField(max_length=11)
    card = serializers.CharField(max_length=12)
    hour = serializers.TimeField()
    owner = serializers.CharField(max_length=14)
    store = serializers.CharField(max_length=19)

    def create(self, validated_data):
        return Transacoes.objects.create(**validated_data)