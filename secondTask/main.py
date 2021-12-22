from twilio.rest import Client


account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

domain = client.sip.domains.create(domain_name='astfgl.sip.twilio.com')
print(domain.sid)  # "SD19edea24ea258aaeabd98f6f17381a19"


sid = 'SD19edea24ea258aaeabd98f6f17381a19'
domain = client.sip.domains(sid).fetch()
print(domain.domain_name)

credential_list = client.sip.credential_lists.create(
                                                  friendly_name='credential_list'
                                              )

print(credential_list.sid) # CLc69d93a2561f77d9b30bba6b7579ca3d


cred_sid = "CLc69d93a2561f77d9b30bba6b7579ca3d"
credential_list = client.sip \
    .credential_lists(cred_sid) \
    .fetch()

print(credential_list.friendly_name)


auth_calls_credential_list_mapping = client.sip \
    .domains(sid) \
    .auth \
    .calls \
    .credential_list_mappings \
    .create(credential_list_sid=cred_sid)

print(auth_calls_credential_list_mapping.sid) #CLc69d93a2561f77d9b30bba6b7579ca3d


credential = client.sip.credential_lists(cred_sid) \
                       .credentials \
                       .create(username='login', password='passwordPA33')

print(credential.sid) #CR5fe906ec4300c41fc34e2f2224c5bc96


call = client.calls \
    .create(
         twiml='<Response><Record timeout="10" transcribe="true" /><Say>Hello and thanks for connecting to your SIP network!</Say></Response>',
         to='sip:login@astfgl.sip.twilio.com',
         from_='+14154834991'
     )

print(call.sid)
print(call.subresource_uris['recordings'])
