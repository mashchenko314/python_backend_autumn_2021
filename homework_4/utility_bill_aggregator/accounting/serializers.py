from accounting.models import Account, Service
from rest_framework import serializers
import datetime


class AccountSerializer(serializers.ModelSerializer):
    service_type = serializers.PrimaryKeyRelatedField(read_only=False, label="Тип услуги", queryset=Service.objects.all())

    class Meta:
        model = Account
        fields = ['id', 'personal_account', 'year',  'month', 'payment_amount', 'indications', 'electronic_receipt_filename', 'address', 'is_paid', 'service_type',  ]
        
    def validate_year(self, value):
        current_year = datetime.datetime.now().year
        if int(value) > current_year:
            raise serializers.ValidationError("Этот год еще не наступил.")
        return value

    def validate_payment_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Сумма платежа не может быть отрицательной.")
        return value

    