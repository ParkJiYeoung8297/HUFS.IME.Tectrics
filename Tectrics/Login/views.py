from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response

# Create your views here.
class UserLogin(APIView):
    def get (self,request):
        return render(request,"Login/userlogin.html")
    
    def post(self, request):
        user_id = request.data.get('user_id', None)
        password = request.data.get('password', None)
        
        
        if user_id is None:
            return Response(status=400, data=dict(message='아이디를 입력해주세요'))

        if password is None:
            return Response(status=400, data=dict(message='비밀번호를 입력해주세요'))

        user = User.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(status=401, data=dict(message='입력정보가 잘못되었습니다.'))

        if check_password(password, user.password) is False:
            return Response(status=401, data=dict(message='입력정보가 잘못되었습니다.'))

        request.session['loginCheck'] = True
        request.session['user_id'] = user_id
        
        return Response(status=200, data=dict(message='로그인에 성공했습니다.'))
    
class Join(APIView):
    def get (self,request):
        return render(request,"Login/join.html")
    
    def post(self, request):
        # 회원가입
        dev_name = request.data.get('dev_name', None)
        dev_phone = request.data.get('dev_phone', None)
        user_id = request.data.get('user_id', None)
        password = request.data.get('password', None)
        dev_ok = 0
        work_ok = 0
        
        if User.objects.filter(user_id=user_id).exists() : 
            return Response(status=500, data=dict(message='사용자 아이디 "' + user_id + '"이(가) 존재합니다.'))

        User.objects.create(dev_name=dev_name,
                            dev_phone=dev_phone,
                            user_id=user_id, 
                            password=make_password(password),
                            dev_ok=dev_ok,
                            work_ok=work_ok
                            )
        
        return Response(status=200, data=dict(message="가입 완료"))
    