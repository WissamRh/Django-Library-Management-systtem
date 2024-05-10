from rest_framework import serializers
from .models import Book, IssueLog, IssueRequest, User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'author', 'quantity', 'available']
        read_only_fields = ('id',)


class BookIssueLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueLog
        fields = ['id', 'book', 'borrower', 'issued_date',
                  'due_date', 'deposit_date', 'penalty']
        read_only_fields = ('id',)


class BookIssueRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueRequest
        fields = ['requester', 'book', 'request_status', 'request_date']
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
