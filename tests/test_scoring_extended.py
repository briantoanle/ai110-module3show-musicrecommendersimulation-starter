import pytest
from src.recommender import score_song

def test_perfect_match():
    user = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.5,
        "target_tempo": 120,
        "target_valence": 0.5,
        "target_danceability": 0.5,
        "likes_acoustic": True,
        "target_acousticness": 0.5
    }
    song = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.5,
        "tempo_bpm": 120,
        "valence": 0.5,
        "danceability": 0.5,
        "acousticness": 0.6
    }
    score, _ = score_song(user, song)
    # 3.5(G) + 2.5(M) + 6(E) + (4 * (1 - 0.1))(A) + 4(T) + 3(V) + 3(D)
    # 3.5 + 2.5 + 6 + 3.6 + 4 + 3 + 3 = 25.6
    assert score == 25.6

def test_mismatch_penalties():
    user = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.0,
        "target_tempo": 60,
        "target_valence": 0.0,
        "target_danceability": 0.0,
        "likes_acoustic": False,
        "target_acousticness": 0.0
    }
    song = {
        "genre": "rock",
        "mood": "angry",
        "energy": 1.0, # -4 points
        "tempo_bpm": 180, # -3 points (diff is 120, 1 - 2 = -1, max(0, -1) = 0)
        "valence": 1.0, # -2 points
        "danceability": 1.0, # -2 points
        "acousticness": 1.0 # -4 points
    }
    score, _ = score_song(user, song)
    # No matches, all numerical diffs are 1.0 or more (resulting in 0 points)
    assert score == 0.0

def test_genre_vs_mood_weighting():
    user = {
        "favorite_genre": "jazz",
        "favorite_mood": "relaxed",
        "target_energy": 0.5,
        "target_tempo": 100,
        "target_valence": 0.5,
        "target_danceability": 0.5,
        "likes_acoustic": True,
        "target_acousticness": 0.5
    }
    
    # Song A matches genre but not mood
    song_a = {
        "genre": "jazz",
        "mood": "party",
        "energy": 0.5,
        "tempo_bpm": 100,
        "valence": 0.5,
        "danceability": 0.5,
        "acousticness": 0.5
    }
    
    # Song B matches mood but not genre
    song_b = {
        "genre": "pop",
        "mood": "relaxed",
        "energy": 0.5,
        "tempo_bpm": 100,
        "valence": 0.5,
        "danceability": 0.5,
        "acousticness": 0.5
    }
    
    score_a, _ = score_song(user, song_a)
    score_b, _ = score_song(user, song_b)
    
    # Song A should score higher because Genre (3.5) > Mood (2.5)
    assert score_a > score_b
    assert round(score_a - score_b, 1) == 1.0
