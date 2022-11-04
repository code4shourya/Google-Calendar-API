# Google-Calendar-API
API to get the events from the users calendar

# TASK

Assignments for Python
## Problem: In this assignment you have to implement google calendar integration using
django rest api.

You need to use the OAuth2 mechanism to get users calendar access.
Below are detail of API endpoint and corresponding views which you need to implement
/rest/v1/calendar/init/ -> GoogleCalendarInitView() This view should start

step 1 of the OAuth. Which will prompt user for his/her credentials
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()

This view will do two things
1. Handle redirect request sent by google with code for token. You need to implement
mechanism to get access token from given code

2. Once got the access_token get list of events in users calendar You need to write the
code in Django. You are not supposed to use any existing third-party library other then
google’s provided standard libraries Please create a GitHub repo and upload code
there.

Looking forward to your submission. Have a great day

## Procedure followed for the Assignment :

### 1 . Looked for the Documentation of Google Calendar API and I got these referenced materials :
  > https://developers.google.com/calendar/api/v3/reference
  
  > https://developers.google.com/identity/protocols/oauth2/web-server#protectauthcode
  
  > https://developers.google.com/identity/protocols/oauth2/web-server#exchange-authorization-codee


### 2 . Learned about OAuth 2.0 for Web Server Applications and Implemented it in Python in GoogelCalendarRedirectView()


### 3 . Learned about how to call Google Calendar API , and get the events of users from Calendar 


### 4 . Mapping of the Urls  


## Results

### responses are as follows 

### Json Responce for both the API's

Google Calendar Init
This view will prompt / show user for his/her credentials to get events from his email

GET /rest/v1/calendar/init/
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "authorization_url": "https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=62991435137-7i2kujmvd2372jgtilooej6ut4q58ti0.apps.googleusercontent.com&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Frest%2Fv1%2Fcalendar%2Fredirect&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalendar&state=7jZ62MTwQuQx3qwcQOEZKrOMTSsz5U&access_type=offline&include_granted_scopes=true"
    
}


Google Calendar Redirect
Handles redirect request sent by google with code for token
Then it provides the events in User Calendar in Json Format

GET /rest/v1/calendar/redirect/?state=Zec8fjUlNsLzgGu8aUlfBdk4RTuopK&code=4/0ARtbsJopGfie99KpTwJi6S2fD6diYLxSMOgUjVPzYrA8NCOsyvIrKX75LZBRXz42b52pqw&scope=https://www.googleapis.com/auth/calendar
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "events": [
        {
            "kind": "calendar#event",
            "etag": "\"3307094072452000\"",
            "id": "_60q30c1g60o30e1i60o4ac1g60rj8gpl88rj2c1h84s34h9g60s30c1g60o30c1g60s44dhp88oj8gq66krk8dpg64o30c1g60o30c1g60o30c1g60o32c1g60o30c1g8ksk8dhi8krj8c1g8kpj4cpk710jidhj6orj6gq28kpk2h1o84p68d3274omac1h5lij0dj45kq3ep345ksmcohm5lj34p1n69j3ecb460q3a",
            "status": "confirmed",
            "htmlLink": "https://www.google.com/calendar/event?eid=XzYwcTMwYzFnNjBvMzBlMWk2MG80YWMxZzYwcmo4Z3BsODhyajJjMWg4NHMzNGg5ZzYwczMwYzFnNjBvMzBjMWc2MHM0NGRocDg4b2o4Z3E2NmtyazhkcGc2NG8zMGMxZzYwbzMwYzFnNjBvMzBjMWc2MG8zMmMxZzYwbzMwYzFnOGtzazhkaGk4a3JqOGMxZzhrcGo0Y3BrNzamlkaGo2b3JqNmdxMjhrcGsyaDFvODRwNjhkMzI3NG9tYWMxaDVsaWowZGo0NWtxM2VwMzQ1a3NtY29obTVsajM0cDFuNjlqM2VjYjQ2MHEzYSBzaG91cnlhMjQzNkBt",
            "created": "2022-05-25T07:19:55.000Z",
            "updated": "2022-05-26T06:37:16.226Z",
            "summary": "HackWithInfy 2021: Interview Invite",
            "description": "HackWithInfy 2021: Interview Invite",
            "location": "https://teams.microsoft.com/l/meetup-join/19%3ameeting_OWNhMmZhYzUtYjUyNi00ZDljLWE2OTUtMjhiZWJkOGY2NTlj%40thread.v2/0?context=%7b%22Tid%22%3a%2263ce7d59-2f3e-42cd-a8cc-be764cff5eb62c%22Oid%22%3a%2238fa374e-3aa3-40d7-8bdb-05b7e9192072%22%7d",
            "creator": {
                "email": "shourya2436@gmail.com",
                "self": true
            },
            "organizer": {
                "email": "hackwithinfy@infosys.com",
                "displayName": "Infosys Talent Acquisition"
            },
            "start": {
                "dateTime": "2022-05-26T08:00:00Z",
                "timeZone": "UTC"
            },
            "end": {
                "dateTime": "2022-05-26T09:00:00Z",
                "timeZone": "UTC"
            },
            "iCalUID": "040000008200E00074C5B7101A82E0080000000008B69B14CF57D701000000000000000010000000E9D62E7400E32348A963673CBE3AD8A2d4b91e01-e06d-47dd-9fb6-f2d72f71d045",
            "sequence": 0,
            "attendees": [
                {
                    "email": "shourya2436@gmail.com",
                    "self": true,
                    "responseStatus": "accepted"
                }
            ],
            "guestsCanInviteOthers": false,
            "privateCopy": true,
            "reminders": {
                "useDefault": true
            },
            "eventType": "default"
        }
    ]
}



