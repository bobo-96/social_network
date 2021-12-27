from rest_framework import serializers

from apps.users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "id",
            "email",
            "password",
            'last_activity',
        )
        read_only_fields = ("id", 'last_activity')

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.set_password(instance.password)
        instance.save()
        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255)
    password_repeat = serializers.CharField(max_length=255)

    class Meta:
        model = models.User
        fields = (
            "id",
            "email",
            "password",
            "password_repeat",
        )

    def create(self, validated_data):
        password = validated_data["password"]
        password_repeat = validated_data["password_repeat"]
        if password == password_repeat:
            user = models.User.objects.create(
                email=validated_data["email"],
            )
            user.is_active = True
            user.set_password(password)
            user.set_password(password_repeat)
            user.save()
            return user
        raise serializers.ValidationError({"password": "Ваши пароли не совпадают."})


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'first_name', 'last_name']
