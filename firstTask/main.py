import requests 
import time
import smtp
from datetime import datetime


def update_lead():
    timestamp = int(time.time())
    data = {"update": [
      {
         "id": "251041",
         "updated_at": f"{timestamp}",
         "status_id":"44859031"
         }]}
    r = requests.post(leads_url, headers={'Content-Type':'application/json', 'Authorization': f"Bearer {token}"}, json=data)
    # pipeline_url = "https://cleaningcompany1.amocrm.com/api/v2/pipelines"
    # r = requests.get(pipeline_url, headers={'Content-Type':'application/json', 'Authorization': f"Bearer {token}"})
    print(r.status_code)
    

def create_note(element_id, element_type, text, note_type):
    timestamp = int(time.time())
    data = {
        "add": [
      {
         "element_id": f"{element_id}",
         "element_type": f"{element_type}",
         "text": f"{text}",
         "note_type": f"{note_type}",
         "created_at": f"{timestamp}",
         "responsible_user_id": "7745563",
         "created_by": "7745563"
      }
   ]
    }
    notes_url = "https://cleaningcompany1.amocrm.com/api/v2/notes"
    r = requests.post(notes_url, headers={'Content-Type':'application/json', 'Authorization': f"Bearer {token}"}, json=data)
    print(r.status_code)


def get_client_info(id):
    r = requests.get(contacts_url+f"?id={id}", headers={'Content-Type':'application/json', 'Authorization': f"Bearer {token}"})
    data = r.json()
    # print(data["_embedded"]["items"][0]["custom_fields"][0]["values"][0]["value"]) #prints email
    return data["_embedded"]["items"][0]["custom_fields"][0]["values"][0]["value"]


def create_task(element_id, element_type, task_type, text):
    timestamp = int(time.time())
    task_url = "https://cleaningcompany1.amocrm.com/api/v2/tasks"
    data = {"add": [{
         "element_id": f"{element_id}",
         "element_type": f"{element_type}",
         "complete_till_at": f"{timestamp+86400}",
         "task_type": f"{task_type}",
         "text": f"{text}",
         "created_at": f"{timestamp}",
         "updated_at": f"{timestamp}",
         "responsible_user_id": "7745563",
         "is_completed":"false",
         "created_by": "7745563"
         }]}


    ts = datetime.utcfromtimestamp(timestamp+86400).strftime('%Y-%m-%d %H:%M:%S')
    r = requests.post(task_url, headers={'Content-Type':'application/json', 'Authorization': f"Bearer {token}"}, json=data)
    print(r.status_code)
    update_lead()
    create_note(464617, 1, f"meeting at {ts}", 4)
    smtp.sent_email(text, 'Meeting', f"data {ts}\nwhere -tbd link-")


sub_domain = "cleaningcompany1"
contacts_url = f"https://{sub_domain}.amocrm.com/api/v2/contacts"


token = ""

timestamp = int(time.time())

for i in range (0,10):
    data = {
      "add": [
         {
            "name": f"user{i}",
            "responsible_user_id": "7745563",
            "created_by": "7745563",
            "created_at": f"{timestamp}",
            "tags": "important, cleaning",
            "leads_id": "",
            "company_id": "444149",
            "custom_fields": [
               {
                  "id": "4396817",
                  "values": [
                     {
                        "value": "Cleaning Manager"
                     }
                  ]
               },
               {
                  "id": "4396818",
                  "values": [
                     {
                        "value": "+19990123456",
                        "enum": "WORK"
                     },
                     {
                        "value": "+19997894561",
                        "enum": "WORKDD"
                     },
                     {
                        "value": "+19991597532",
                        "enum": "MOB"
                     }
                  ]
               },
               {
                  "id": "4396819",
                  "values": [
                     {
                        "value": "konde.chloe@gmail.com",
                        "enum": "WORK"
                     }
                  ]
               },
               {
                  "id": "4396821",
                  "values": [
                     {
                        "value": "example.example",
                        "enum": "SKYPE"
                     }
                  ]},
   
               {
                  "id": "4400115",
                  "values": [
                     {
                        "value": "Madison st., 1",
                        "subtype": "address_line_1"
                     },
                     {
                        "value": "Washington",
                        "subtype": "city"
                     },
                     {
                        "value": "101010",
                        "subtype": "zip"
                     },
                     {
                        "value": "US",
                        "subtype": "country"
                     }
                  ]
               },
               {
                  "id": "4400116",
                     "values": [
                        "3692662",
                        "3692663"
                     ]
               }
            ]
         }
      ]
   }
    r = requests.post(contacts_url, headers={'Content-Type':'application/json', 'Authorization': f"Bearer {token}"}, json=data)
print(r.status_code)


r = requests.get(contacts_url, headers={'Content-Type':'application/json', 'Authorization': f"Bearer {token}"})
data = r.json()
contacts_ids = list(map(lambda x: x['id'], data["_embedded"]["items"]))
print(contacts_ids)


leads_url = f"https://{sub_domain}.amocrm.com/api/v2/leads"

for i in range (0,10):
    data = {"add": [{"name":f"lead{i}","created_at": "1508101200", "updated_at":"1508274000", "status_id":"", "responsible_user_id":"7745563", "sale":f"100{i}", "tags":"cleaning", "contacts_id":f"{contacts_ids[i]}"}]}
    r = requests.post(leads_url, headers={'Content-Type':'application/json', 'Authorization': f"Bearer {token}"}, json=data)

print(r.status_code)

create_task(251041, 2, 2, get_client_info(464617))