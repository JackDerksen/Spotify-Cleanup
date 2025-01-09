import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

def setup_spotify_client():
    """
    Set up and return an authenticated Spotify client
    """
    scope = 'user-library-modify user-library-read playlist-modify-public playlist-modify-private'
    
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri='http://localhost:8888/callback',
        client_id='INSERT YOUR CLIENT ID HERE',
        client_secret='INSERT YOUR CLIENT SECRET HERE'
    ))

def get_all_saved_albums(sp):
    """
    Retrieve all saved albums from the user's library
    """
    albums = []
    offset = 0
    limit = 50
    
    while True:
        results = sp.current_user_saved_albums(limit=limit, offset=offset)
        if not results['items']:
            break
            
        albums.extend([item['album']['id'] for item in results['items']])
        offset += limit
        time.sleep(0.1)
    
    return albums

def get_all_playlists(sp):
    """
    Retrieve all playlists owned by the user
    """
    playlists = []
    offset = 0
    limit = 50
    
    while True:
        results = sp.current_user_playlists(limit=limit, offset=offset)
        if not results['items']:
            break
            
        # Only include playlists owned by the user
        user_id = sp.current_user()['id']
        playlists.extend([
            {
                'id': item['id'],
                'name': item['name']
            }
            for item in results['items']
            if item['owner']['id'] == user_id
        ])
        
        offset += limit
        time.sleep(0.1)
    
    return playlists

def get_all_liked_songs(sp):
    """
    Retrieve all liked songs from the user's library
    """
    tracks = []
    offset = 0
    limit = 50
    
    while True:
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        if not results['items']:
            break
            
        tracks.extend([item['track']['id'] for item in results['items']])
        offset += limit
        time.sleep(0.1)
    
    return tracks

def remove_saved_albums(sp, album_ids):
    """
    Remove albums from the user's library in batches
    """
    batch_size = 20
    total_albums = len(album_ids)
    
    for i in range(0, total_albums, batch_size):
        batch = album_ids[i:i + batch_size]
        try:
            sp.current_user_saved_albums_delete(batch)
            print(f"Removed albums {i + 1}-{min(i + batch_size, total_albums)} of {total_albums}")
            time.sleep(0.1)
        except Exception as e:
            print(f"Error removing batch starting at index {i}: {str(e)}")
            continue

def remove_playlists(sp, playlists):
    """
    Remove user's playlists
    """
    for i, playlist in enumerate(playlists, 1):
        try:
            sp.current_user_unfollow_playlist(playlist['id'])
            print(f"Removed playlist {i} of {len(playlists)}: {playlist['name']}")
            time.sleep(0.1)
        except Exception as e:
            print(f"Error removing playlist {playlist['name']}: {str(e)}")
            continue

def remove_liked_songs(sp, track_ids):
    """
    Remove liked songs from the user's library in batches
    """
    batch_size = 20
    total_tracks = len(track_ids)
    
    for i in range(0, total_tracks, batch_size):
        batch = track_ids[i:i + batch_size]
        try:
            sp.current_user_saved_tracks_delete(batch)
            print(f"Removed tracks {i + 1}-{min(i + batch_size, total_tracks)} of {total_tracks}")
            time.sleep(0.1)
        except Exception as e:
            print(f"Error removing batch starting at index {i}: {str(e)}")
            continue

def display_menu():
    """
    Display the main menu and get user choice
    """
    print("\nSpotify Library Cleanup Tool")
    print("1. Remove all saved albums")
    print("2. Remove all owned playlists")
    print("3. Remove all liked songs")
    print("4. Remove everything")
    print("5. Exit")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")

def confirm_action(item_type, count):
    """
    Get user confirmation before proceeding with deletion
    """
    confirm = input(f"\nFound {count} {item_type}. Are you sure you want to remove them all? (yes/no): ")
    return confirm.lower() == 'yes'

def main():
    try:
        sp = setup_spotify_client()
        
        while True:
            choice = display_menu()
            
            if choice == 5:
                print("Goodbye!")
                break
                
            if choice in [1, 4]:
                albums = get_all_saved_albums(sp)
                if albums and confirm_action("saved albums", len(albums)):
                    remove_saved_albums(sp, albums)
                    
            if choice in [2, 4]:
                playlists = get_all_playlists(sp)
                if playlists and confirm_action("owned playlists", len(playlists)):
                    remove_playlists(sp, playlists)
                    
            if choice in [3, 4]:
                tracks = get_all_liked_songs(sp)
                if tracks and confirm_action("liked songs", len(tracks)):
                    remove_liked_songs(sp, tracks)
                    
            input("\nPress Enter to continue...")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
