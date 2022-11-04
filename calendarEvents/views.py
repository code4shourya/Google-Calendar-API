from django.shortcuts import render , redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


import google.oauth2.credentials
import google_auth_oauthlib.flow

import googleapiclient.discovery


import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


SCOPES = ['https://www.googleapis.com/auth/calendar']
REDIRECT_URL = 'http://127.0.0.1:8000/rest/v1/calendar/redirect'
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

@api_view(['GET'])
def GoogleCalendarInitView(request):
    """
    This view will prompt / show user for his/her credentials to get events from his email 
    """
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        "client_secret.json", scopes=SCOPES)

    flow.redirect_uri = REDIRECT_URL

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    request.session['state'] = state

    return Response({"authorization_url": authorization_url})

@api_view(['GET'])
def GoogleCalendarRedirectView(request):
    """
    Handles redirect request sent by google with code for token
    Then it provides the events in User Calendar in Json Format
    """

    state = request.session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        "client_secret.json", scopes=SCOPES, state=state)
    flow.redirect_uri = REDIRECT_URL

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = request.get_full_path()
    flow.fetch_token(authorization_response=authorization_response)


    credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(credentials)

    # Check if credentials are in session
    if 'credentials' not in request.session:
        return redirect('v1/calendar/init')

    # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
        **request.session['credentials'])

    service = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

    calendar_list = service.calendarList().list().execute()

    calendar_id = calendar_list['items'][0]['id']

    events  = service.events().list(calendarId=calendar_id).execute()

    events_list_append = []
    if not events['items']:
        print('No data found.')
        return Response({"message": "No data found or user credentials invalid."})
    else:
        for events_list in events['items']:
            events_list_append.append(events_list)
            return Response({"events": events_list_append})
    return Response({"error": "calendar event aren't here"})


def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}