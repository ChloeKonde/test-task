import os
from twilio.rest import Client


account_sid = 'ACca5a7f6c10411889563d7b39af291704'
auth_token = '9c80ca0a7df2d5ec0872fd816a026d9b'
client = Client(account_sid, auth_token)

"""creating domain"""
# domain = client.sip.domains.create(domain_name='astfgl.sip.twilio.com')
# print(domain.sid)  # "SD19edea24ea258aaeabd98f6f17381a19" result


"""fetching my domain from twilio"""
sid = "SD19edea24ea258aaeabd98f6f17381a19"
# domain = client.sip.domains(sid).fetch()
# print(domain.domain_name)

"""creating cred list"""
# credential_list = client.sip.credential_lists.create(
#                                                   friendly_name='credential_list'
#                                               )

# print(credential_list.sid) # CLc69d93a2561f77d9b30bba6b7579ca3d

"""fetching cred list from twilio"""

cred_sid = "CLc69d93a2561f77d9b30bba6b7579ca3d"
# credential_list = client.sip \
#     .credential_lists(cred_sid) \
#     .fetch()

# print(credential_list.friendly_name)

"""mappimg sid with creds"""
# auth_calls_credential_list_mapping = client.sip \
#     .domains(sid) \
#     .auth \
#     .calls \
#     .credential_list_mappings \
#     .create(credential_list_sid=cred_sid)

# print(auth_calls_credential_list_mapping.sid) #CLc69d93a2561f77d9b30bba6b7579ca3d

"""adding creds to cred list"""
# credential = client.sip.credential_lists(cred_sid) \
#                        .credentials \
#                        .create(username='login', password='passwordPA33')

# print(credential.sid) #CR5fe906ec4300c41fc34e2f2224c5bc96


call = client.calls \
    .create(
         twiml='<Response><Say>Hello and thanks for connecting to your SIP network!</Say></Response>',
         to='sip:login@astfgl.sip.twilio.com',
         from_='+14154834991'
     )

print(call.sid)