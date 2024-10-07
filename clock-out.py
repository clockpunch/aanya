import requests
from fake_useragent import UserAgent
import json
import datetime
import holidays

ua = UserAgent()

session = requests.session()

ph_holidays = holidays.PH()

if datetime.datetime.today() in ph_holidays:
    # Today is a holiday Labor Day 2023-05-09 12:59
    print('Today is a holiday', ph_holidays.get(datetime.datetime.today().isoformat()), datetime.datetime.today().strftime('%Y-%m-%d %I:%M'))
else:
    headers1 = {
        'User-Agent': ua.google,
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer null',
        'Origin': 'https://app.aanyahr.com',
        'Connection': 'keep-alive',
        'Referer': 'https://app.aanyahr.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    json_data1 = {
        'username': '<username>',
        'password': '<password>',
        'company_code': '<company>',
        'remember': None,
        # ip addresses optional
        'ipv1': '<ip>',
        'ipv2': '<ip>',
    }

    response1 = session.post('https://v15.aanyahr.com:9000/api/AccountManagement/AuthenticateLogin', headers=headers1, json=json_data1)

    json_response1 = json.loads(response1.text)
    # json_response1['token']

    headers2 = {
        'User-Agent': ua.google,
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + json_response1['token'],
        'Origin': 'https://app.aanyahr.com',
        'Connection': 'keep-alive',
        'Referer': 'https://app.aanyahr.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    json_data2 = {
        'in_out': 1,
        'log_type_id': '1',
        'created_by': '<created_by>',
        'series_code': '<series_code>',
    }

    response2 = session.post(
        'https://v15.aanyahr.com:9000/api/AttendanceManagement/attendance_log_in',
        headers=headers2,
        json=json_data2,
    )

    # {"in_out":1,"log_type_id":1,"is_schedule":true,"created_by":30207}

    print('Clocked Out on', datetime.datetime.now().strftime('%a, %b %d, %Y at %H:%M:%S'))