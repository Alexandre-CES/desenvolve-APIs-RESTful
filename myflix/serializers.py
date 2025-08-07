from rest_framework import serializers
from myflix.models import user, stream

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

class streamSerializer(serializers.ModelSerializer):
    class Meta:
        model = stream
        fields = '__all__'
