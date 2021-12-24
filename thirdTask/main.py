import time
import requests 
from twilio.rest import Client
from twilio.rest.api.v2010.account import call

account_sid = 'ACca5a7f6c10411889563d7b39af291704'
auth_token = '23e2997c11cf7629c073f1b3b841422c'
client = Client(account_sid, auth_token)

sub_domain = "cleaningcompany1"

contacts_url = f"https://{sub_domain}.amocrm.com/api/v2/contacts"
leads_url = f"https://{sub_domain}.amocrm.com/api/v2/leads"

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjA1MmRlMDU2ZjljNzUwMGI4NTJjNWZhOTlhYzhlYTQwODY4MjFjYzZiNzg5ZmRiY2M3NGNjMjc1Mjk5YWJjMjVhZDJiMTEzNjFmNTQwZDU3In0.eyJhdWQiOiJkMjVlZjM5Yi0wMGM3LTRmZWUtYjg2ZS1mZDAyMGY3YzM0MjEiLCJqdGkiOiIwNTJkZTA1NmY5Yzc1MDBiODUyYzVmYTk5YWM4ZWE0MDg2ODIxY2M2Yjc4OWZkYmNjNzRjYzI3NTI5OWFiYzI1YWQyYjExMzYxZjU0MGQ1NyIsImlhdCI6MTY0MDMwMTYyOCwibmJmIjoxNjQwMzAxNjI4LCJleHAiOjE2NDAzODgwMjgsInN1YiI6Ijc3NDU1NjMiLCJhY2NvdW50X2lkIjoyOTg4ODI4NCwic2NvcGVzIjpbInB1c2hfbm90aWZpY2F0aW9ucyIsImNybSIsIm5vdGlmaWNhdGlvbnMiXX0.DuvA8n_08sB4ok6uDOFV4pCHeFRPnkx0JbjP2CNO7e-5dSDBhpU6yj5Xw3iiuyoZ4hF9eesrXOwQ1R974Vn9pmIwKO4B2MUUchsIvbQAaxLPOnqhjK9uHN6W7cK2Ma5YYXWthMHV7oIcmEDlCXcOXW45-10WVXBGlMcwMaqkxHECaYp_ObQTBfv4E-6CCcnP_qcCjGInuywhi0ayMeIBCI_n9NmAxgwj_YC7YcheuAAwnbJuqlwdUklRBEsoi3p_hN9bqpJR6mQ4Q-2asJ-OBIqQyuv454voP5LcS9QQJtPh8Itu33Kj6OR4UdgZg27hpKyji1Gk_cxa541clkDQtQ"


def make_call():
    call = client.calls \
    .create(
         twiml='<Response><Record timeout="10" transcribe="true" /><Say>Hello and thanks for connecting to your SIP network!</Say></Response>',
         to='sip:login@astfgl.sip.twilio.com',
         from_='+14154834991'
     )

    call_sid = call.sid
    call_status = call.status

    while call_status not in ['completed', 'busy', 'cancelled', 'failed', 'no-answer'] :
        call = client.calls(call_sid).fetch()
        call_status = call.status
        
    return {"sid" : call.sid, "duration" : call.duration}

def create_note(sid, duration):
    timestamp = int(time.time())

    data = {
        "add": [
        {
            "element_id": "251041",
            "element_type": "2",
            "note_type": "10",
            "params":[{
                "UNIQ": f"{sid}",
                "LINK": "https://api.twilio.com/cowbell.mp3",
                "PHONE": "+14154834991",
                "SRC": "amo_twilio6",
                "DURATION" : f"{duration}",
                "call_status": "4",
            }],
            "created_at": f"{timestamp}",
            "responsible_user_id": "7745563",
            "created_by": "7745563"
        }]
        }
    
    notes_url = "https://cleaningcompany1.amocrm.com/api/v2/notes"
    r = requests.post(notes_url, headers={'Content-Type':'application/json', 'Authorization': f"Bearer {token}"}, json=data)
    print(r.status_code)


call_info = make_call()
create_note(call_info["sid"], call_info["duration"])