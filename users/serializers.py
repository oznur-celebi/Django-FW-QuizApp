from asyncore import write
from dataclasses import fields
from wsgiref import validate
from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    #Email zorunlu olsun diye, normal user modelinde burasi zorunlu degil, suan overwrite yapiyoruz.
    email =serializers.EmailField(
    required =True,
    validatiors =[validators.UniqueValidator(queryset=User.objects.all())] #Email uniqe olsun diye, 2 kullanici ayni email i kullanamasin diye
    )

    password =serializers.CharField(
        write_only =True,# Burdada kwargs da da yaziyoruz, 2. yol!!!!
        required =True,
        validatiors =[validate_password] # önce import ediyoruz.. sonra burda belirtiyoruz, validation icin
    )
    password2 =serializers.CharField(
        write_only =True,
        required =True,
       # validatiors =[validate_password]# buna gerek yok zaten password validationdan gecmek zorunda 
    )

    class Meta:
        model =User
    fields =['username', 'first_name', 'last_name', 'email', 'password', 'password2']
  # User basarili olarak login oldugunda biz ueserinfolari response olarak frontende e dönmek istiyoruz 
  # ama passwordlarin dönmemesi gererki. Yani read olmayacak, yani ön tarafa gitmeyecek, Sadece kullanicidan write only ile alinacak
    extra_kwargs ={
        'password' :{'write_only' : True},
        'password2' :{'write_only' : True}
    }
   #Benim user tablomda password2 yok, frontendin gönderdigi bu datayi ayiriyoruz.. Dtabese ime kaydedemedigim icin
   # Create methodunu overwrite yapiyoruz
    def create(self, validated_data):
        password=validated_data.get('password')# passwordumu direk kaydedemem, hacklenmis bir bicimde database imi kaydetmem gerekiyor..!!
        validated_data.pop('password2')
        user =User.objects.create(**validated_data)# degerleri eslestiriyor name =name gibi
        user.set_password(password) # adatabese e isleyip kaydediyor
        return user

   #We are  writing a Validation , to control password = ?Password2
   # Object level validation----->we are calling here  the complete data

    def validate(self, data):
        if data['password']!=data['password2']:
            raise serializers.ValidationError(
                { "password" : "Password fields didn't match."}
            )
            return data





