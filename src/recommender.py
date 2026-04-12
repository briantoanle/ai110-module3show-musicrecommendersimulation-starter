from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_tempo: float
    target_valence: float
    target_danceability: float
    likes_acoustic: bool
    target_acousticness: float

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """
        Generates list of song recommendations using the score_song function logic.
        """
        # Convert dataclass to dict to reuse functional score_song logic
        user_dict = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "target_tempo": user.target_tempo,
            "target_valence": user.target_valence,
            "target_danceability": user.target_danceability,
            "likes_acoustic": user.likes_acoustic,
            "target_acousticness": user.target_acousticness
        }

        scored = []
        for s in self.songs:
            # Convert Song dataclass to dict
            s_dict = vars(s)
            score, explanation = score_song(user_dict, s_dict)
            scored.append((s, score))

        # Sort by score descending
        scored.sort(key=lambda x: x[1], reverse=True)
        return [item[0] for item in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """
        Provides a detailed explanation for why a song was recommended.
        """
        user_dict = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "target_tempo": user.target_tempo,
            "target_valence": user.target_valence,
            "target_danceability": user.target_danceability,
            "likes_acoustic": user.likes_acoustic,
            "target_acousticness": user.target_acousticness
        }
        s_dict = vars(song)
        _, explanation = score_song(user_dict, s_dict)
        return explanation

import csv

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numerical strings to floats/ints
                song = {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"])
                }
                songs.append(song)
    except FileNotFoundError:
        print(f"Error: Could not find songs file at {csv_path}")
    except Exception as e:
        print(f"Error loading songs: {e}")
    
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """
    Calculates a similarity score using a point-based weighting system (Strategy C - Balanced).
    Total potential points: ~27
    """
    score = 0.0
    reasons = []

    # Weights
    W_GENRE = 7.0
    W_MOOD = 5.0
    W_ENERGY = 4.0
    W_ACOUSTIC = 4.0
    W_TEMPO = 3.0
    W_VALENCE = 2.0
    W_DANCE = 2.0

    # 1. Genre match
    if song["genre"].lower() == user_prefs.get("favorite_genre", "").lower():
        score += W_GENRE
        reasons.append(f"genre match ({song['genre']})")

    # 2. Mood match
    if song["mood"].lower() == user_prefs.get("favorite_mood", "").lower():
        score += W_MOOD
        reasons.append(f"mood match ({song['mood']})")

    # 3. Energy similarity
    target_energy = user_prefs.get("target_energy", 0.5)
    energy_diff = abs(song["energy"] - target_energy)
    score += max(0, W_ENERGY * (1 - energy_diff))
    if energy_diff < 0.15:
        reasons.append("perfect energy")
    elif energy_diff < 0.3:
        reasons.append("good energy")

    # 4. Acousticness & Preferences
    target_acoustic = user_prefs.get("target_acousticness", 0.5)
    acoustic_diff = abs(song["acousticness"] - target_acoustic)
    likes_acoustic = user_prefs.get("likes_acoustic", False)
    is_acoustic = song["acousticness"] > 0.5
    
    acoustic_score = max(0, W_ACOUSTIC * (1 - acoustic_diff))
    # Bonus for matching the boolean preference
    if likes_acoustic == is_acoustic:
        acoustic_score += 1.0 
    
    score += acoustic_score
    if acoustic_diff < 0.2:
        reasons.append("ideal acousticness")

    # 5. Tempo similarity (Normalized by 60 BPM range)
    target_tempo = user_prefs.get("target_tempo", 120)
    tempo_diff = abs(song["tempo_bpm"] - target_tempo)
    tempo_score = max(0, W_TEMPO * (1 - (tempo_diff / 60)))
    score += tempo_score
    if tempo_diff < 15:
        reasons.append("matching tempo")

    # 6. Valence & Danceability
    v_diff = abs(song["valence"] - user_prefs.get("target_valence", 0.5))
    d_diff = abs(song["danceability"] - user_prefs.get("target_danceability", 0.5))
    score += max(0, W_VALENCE * (1 - v_diff))
    score += max(0, W_DANCE * (1 - d_diff))

    explanation = "Points earned for: " + ", ".join(reasons) + "." if reasons else "General recommendation."
    return round(score, 2), explanation

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        scored_songs.append((song, score, explanation))

    # Sort by score descending
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    
    return scored_songs[:k]
