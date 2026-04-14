
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.recommender import score_song, Song

def run_test_case(name, user_prefs, song_data):
    score, explanation = score_song(user_prefs, song_data)
    print(f"--- {name} ---")
    print(f"User: {user_prefs}")
    print(f"Song: {song_data}")
    print(f"Score: {score}")
    print(f"Explanation: {explanation}")
    print("-" * (len(name) + 8))
    return score

if __name__ == "__main__":
    # Case 1: Conflicting Preferences (High energy vs Sad mood)
    user_conflict = {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.9,
        "target_tempo": 120,
        "target_valence": 0.5,
        "target_danceability": 0.5,
        "likes_acoustic": False,
        "target_acousticness": 0.2
    }
    
    # Song A: Sad but low energy
    song_a = {
        "genre": "pop",
        "mood": "sad",
        "energy": 0.2,
        "acousticness": 0.2,
        "tempo_bpm": 120,
        "valence": 0.5,
        "danceability": 0.5
    }
    
    # Song B: High energy but mood match "happy"
    song_b = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "acousticness": 0.2,
        "tempo_bpm": 120,
        "valence": 0.5,
        "danceability": 0.5
    }

    run_test_case("Conflicting: Sad/LowEnergy", user_conflict, song_a)
    run_test_case("Conflicting: Happy/HighEnergy", user_conflict, song_b)

    # Case 2: Extreme Out-of-Bounds (if possible)
    # The score_song function uses max(0, ...) so it should be safe, 
    # but let's see how much it penalizes.
    user_extreme = {
        "favorite_genre": "pop",
        "target_energy": 1.0,
        "target_acousticness": 1.0,
        "target_tempo": 120
    }
    song_extreme = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.0,
        "acousticness": 0.0,
        "tempo_bpm": 240, # 120 bpm diff
        "valence": 0.0,
        "danceability": 0.0
    }
    run_test_case("Extreme Mismatch", user_extreme, song_extreme)

    # Case 3: Missing Keys in user_prefs (testing defaults)
    user_minimal = {
        "favorite_genre": "pop"
    }
    song_pop = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.5,
        "acousticness": 0.5,
        "tempo_bpm": 120,
        "valence": 0.5,
        "danceability": 0.5
    }
    run_test_case("Minimal User Prefs", user_minimal, song_pop)

    # Case 4: Acoustic Logic (Unified)
    # likes_acoustic = True but target_acousticness = 0.1
    # Previously this got a +1.0 bonus even if far. Now it should only rely on diff.
    user_acoustic_weird = {
        "likes_acoustic": True,
        "target_acousticness": 0.1,
        "target_energy": 0.5
    }
    song_acoustic_mid = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.5,
        "acousticness": 0.6, 
        "tempo_bpm": 120,
        "valence": 0.5,
        "danceability": 0.5
    }
    run_test_case("Acoustic Conflict (Bool ignored)", user_acoustic_weird, song_acoustic_mid)

    # Case 5: Empty Matches
    user_empty = {"favorite_genre": "", "favorite_mood": ""}
    song_empty = {"genre": "", "mood": "", "energy": 0.5, "acousticness": 0.5, "tempo_bpm": 120, "valence": 0.5, "danceability": 0.5}
    run_test_case("Empty String Match (Should be lower)", user_empty, song_empty)

    # Case 6: Tie Breaking
    from src.recommender import recommend_songs
    songs_tied = {
        1: {"id": 1, "title": "B Track", "artist": "Z Artist", "genre": "pop", "mood": "happy", "energy": 0.5, "acousticness": 0.5, "tempo_bpm": 120, "valence": 0.5, "danceability": 0.5},
        2: {"id": 2, "title": "A Track", "artist": "A Artist", "genre": "pop", "mood": "happy", "energy": 0.5, "acousticness": 0.5, "tempo_bpm": 120, "valence": 0.5, "danceability": 0.5}
    }
    results = recommend_songs({"favorite_genre": "pop"}, songs_tied, k=2)
    print("\n--- Tie Breaking Test ---")
    for song, score, _ in results:
        print(f"Song: {song['title']} by {song['artist']}, Score: {score}")
