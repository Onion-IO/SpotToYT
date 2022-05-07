from distutils.command.upload import upload
from urllib.error import HTTPError
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from urllib.error import HTTPError

#SET VARIABLES
path_to_secret_json = "client_sercret_json.json" #path to YouTube oauth client secret.json. 
DEV_KEY = '[EDIT THIS]' #YouTube API key
SPT_client_ID = '[EDIT THIS]'  #Spotify API Client ID
SPT_client_secret = '[EDIT THIS]'  #Spotify API client secret



#GUI-VARIABLES (Do not edit)
state_check = True
username = 'placeholder' #spotify username
playlist_link = 'placeholder' #spotify playlist ID
final_URL = 'placeholder'
scopes = ["https://www.googleapis.com/auth/youtube"]

#Verifies spotify client id using the 'client credentials' flow
client_credentials_manager = SpotifyClientCredentials(client_id=SPT_client_ID,client_secret=SPT_client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = path_to_secret_json

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    #Creates playlist
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": "Created for " + username,
            "description": "Reminder: Due to API Quota limits, the maximum playlist size is 100 songs :)",
          },
          "status": {
            "privacyStatus": "public"
          }
        }
    )
    
    try:
      response = request.execute()
      print('response executed')
    except:
      e = sys.exc_info()[0]
      print("Error occured. Most likely, this is a rate-limiting error on YouTube's side. Simply try again in a few minutes.")
      print( "<p>Error: %s</p>" % e )
      sys.exit("Program stopped; refer to above error message")


    #filters response, and prints created playlist ID
    for i in range(1):
        YTlistID = response['id']
        print('youtube playlist ID: ' + YTlistID)


    #gets SPOTIFY playlist indicated by above variables
    sp_playlist = sp.user_playlist_tracks(username, playlist_id=playlist_link)

    #For every item in the spotify playlist, does the following:
    for item in sp_playlist['tracks']['items']:
      #gets song name
      tosearch = item['track']['name'] + ' ' + item['track']['artists'][0]['name']
      print('searching for ' + tosearch)

      #searches for var 'tosearch'
      searchrequest = youtube.search().list(
        part="snippet",
        maxResults=1,
        q= tosearch
      )
      searchresponse = searchrequest.execute()
      global final_URL
      final_URL = 'https://www.youtube.com/playlist?list=' + YTlistID

      
      #gets vid ID for searched video, and adds to playlist
      for item in searchresponse['items']:
        addthis = item['id']['videoId']
        print('youtube search result ID: ' + addthis)
        #adds to playlist
        ListAdd = youtube.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": YTlistID,
            "position": 0,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": addthis
            }
          }
        }
    )
        ListAdd.execute()
        
    final_URL = 'https://www.youtube.com/playlist?list=' + YTlistID
    print(final_URL)
    if __name__ == "__main__":
      main()

print('this should run before main')