import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

def setup_spotify_client():
    """
    Set up and return an authenticated Spotify client
    """
    scope = 'user-library-modify user-library-read'
    
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri='http://localhost:8888/callback',
        # You'll need to fill these in from your Spotify Developer Dashboard
        client_id='INSERT YOUR SPOTIFY DEVELOPER CLIENT ID HERE',
        client_secret='INSERT YOUR SPOTIFY DEVELOPER CLIENT SECRET HERE',
    ))

def get_all_saved_albums(sp):
    """
    Retrieve all saved albums from the user's library
    """
    albums = []
    offset = 0
    limit = 50  # Maximum allowed by Spotify API
    
    while True:
        results = sp.current_user_saved_albums(limit=limit, offset=offset)
        if not results['items']:
            break
            
        albums.extend([item['album']['id'] for item in results['items']])
        offset += limit
        
        # Respect rate limiting
        time.sleep(0.1)
    
    return albums

def remove_saved_albums(sp, album_ids):
    """
    Remove albums from the user's library in batches
    """
    batch_size = 20  # Maximum allowed by Spotify API
    total_albums = len(album_ids)
    
    for i in range(0, total_albums, batch_size):
        batch = album_ids[i:i + batch_size]
        try:
            sp.current_user_saved_albums_delete(batch)
            print(f"Removed albums {i + 1}-{min(i + batch_size, total_albums)} of {total_albums}")
            
            # Rate limiting
            time.sleep(0.1)
            
        except Exception as e:
            print(f"Error removing batch starting at index {i}: {str(e)}")
            continue

def main():
    try:
        # Set up the Spotify client
        sp = setup_spotify_client()
        
        # Get all saved albums
        print("Fetching saved albums...")
        albums = get_all_saved_albums(sp)
        
        if not albums:
            print("No saved albums found in your library.")
            return
            
        # Confirm with user
        total_albums = len(albums)
        confirm = input(f"Found {total_albums} saved albums. Are you sure you want to remove them all? (yes/no): ")
        
        if confirm.lower() != 'yes':
            print("Operation cancelled.")
            return
            
        # Remove the albums
        print("Starting album removal...")
        remove_saved_albums(sp, albums)
        
        print("Successfully removed all saved albums from your library!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
