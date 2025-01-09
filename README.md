# Spotify-Mass-Delete
A useful little Python script which uses Spotify's web API to mass delete all saved albums from your library.

## Usage Instructions

1. Install the required package:
`pip install spotipy`

2. Set up a Spotify Developer account:

  Go to the [Spotify developer dashboard](https://developer.spotify.com/dashboard) and sign in
  Create a new application, fill out the required details
  Get your Client ID and Client Secret
  Add `http://localhost:8888/callback` to your application's Redirect URIs

3. Replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET in the script with your actual credentials

These credentials are specifically for your app to communicate with Spotify's API. The script will still prompt you to log in with your regular Spotify account when you run it, but it needs these developer credentials to access the API.

When you run the script, it will:

- Authenticate with Spotify (opening a browser window for authorization)
- Fetch all your saved albums
- Ask for confirmation before proceeding
- Remove the albums in batches, respecting Spotify's API rate limits

The script includes error handling and rate limiting to ensure reliable operation.
