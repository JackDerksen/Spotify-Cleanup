# Spotify Library Cleanup Tool
A useful little Python script which uses Spotify's web API to clean your library.

**CAUTION: THE EFFECTS OF USING THIS PROGRAM ARE PERMANENT AND IRREVERSIBLE AS FAR AS I KNOW. I'M NOT RESPONSIBLE IF YOU DELETE YOUR WHOLE LIBRARY BY ACCIDENT. USE AT YOUR OWN RISK.** Please read and understand all the instructions in the README prior to use.

This tool can help you remove:
- Saved albums
- Playlists you own
- Liked songs
- All of the above at once

## Prerequisites

- Python 3.6 or higher
- A Spotify account
- Spotify Developer credentials

## Installation

1. Clone this repository or download the script file (main.py).
2. Install the required package using pip:
```bash
pip install spotipy
```

## Setting Up Spotify Developer Credentials

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click "Create App"
4. Fill out the application details:
   - App name: Choose any name (e.g., "Library Cleanup Tool")
   - App description: Optional
   - Redirect URI: Set this to `http://localhost:8888/callback`
5. Accept the terms of service
6. After creation, you'll see your Client ID
7. Click "View Client Secret" to reveal your Client Secret
8. Open the script in a text editor and replace:
   - `YOUR_CLIENT_ID_HERE!` string with your actual Client ID
   - `YOUR_CLIENT_SECRET_HERE!` string with your actual Client Secret

## Usage

1. Run the script:
```bash
python3 spotify_cleanup.py
```

2. On first run, your browser will open asking you to log in to Spotify and authorize the application.

3. Once authorized, you'll see the main menu with these options:
```
Spotify Library Cleanup Tool
1. Remove all saved albums
2. Remove all owned playlists
3. Remove all liked songs
4. Remove everything
5. Exit
```

4. Choose an option by entering the corresponding number (1-5)

5. For each action:
   - The script will first tell you how many items will be removed by your selected action
   - **You'll be asked to confirm before deletion begins**
   - Type 'yes' to proceed or 'no' to cancel
   - Progress will be displayed as items are removed

## Important Notes

- This tool only removes playlists that you own, not playlists you follow
- Deletions are permanent and cannot be undone
- The script includes rate limiting to comply with Spotify's API guidelines
- You can safely cancel the script at any time by pressing Ctrl+C

## Troubleshooting

### Common Issues:

1. **Invalid Client Credentials:**
   - Double-check that you've correctly copied your Client ID and Client Secret
   - Ensure there are no extra spaces in the credentials

2. **Authorization Failed:**
   - Make sure the redirect URI in your Spotify Developer Dashboard matches exactly: `http://localhost:8888/callback`
   - Try clearing your browser cookies and cache

3. **Rate Limiting:**
   - The script includes built-in rate limiting
   - If you still encounter rate limit errors, wait a few minutes before trying again

### Error Messages:

- `Invalid Client Secret`: Check your developer dashboard for the correct secret
- `Invalid Redirect URI`: Verify the URI in your dashboard settings
- `Access Denied`: Re-authorize the application in your browser

## Safety Features

- Confirmation prompts before any deletion
- Rate limiting to prevent API abuse
- Error handling for failed operations
- Progress tracking during deletion

## Contributing

Feel free to submit issues and enhancement requests!
