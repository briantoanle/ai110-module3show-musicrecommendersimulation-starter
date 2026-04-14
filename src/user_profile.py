"""
Defines a unique user profile dictionary for the music recommender simulation.
This profile represents a specific type of listener used as a baseline for comparisons.
"""

# 1. The High-Energy Pop Enthusiast
# Loves upbeat, danceable, and mainstream energy.
POP_ENTHUSIAST = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.85,
    "target_tempo": 125,
    "target_valence": 0.8,
    "target_danceability": 0.85,
    "likes_acoustic": False,
    "target_acousticness": 0.15
}

# 2. The Chill Lofi Student
# Prefers low-energy, focused, and acoustic beats for studying.
CHILL_LOFI_LISTENER = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.35,
    "target_tempo": 75,
    "target_valence": 0.5,
    "target_danceability": 0.4,
    "likes_acoustic": True,
    "target_acousticness": 0.8
}

# 3. The Metal Head
# Craves high-intensity, aggressive, and non-acoustic sounds.
METAL_HEAD = {
    "favorite_genre": "metal",
    "favorite_mood": "intense",
    "target_energy": 0.95,
    "target_tempo": 150,
    "target_valence": 0.2,
    "target_danceability": 0.4,
    "likes_acoustic": False,
    "target_acousticness": 0.05
}

# 4. The EDM Enthusiast
# High energy, heavy dance beats, and purely electronic.
EDM_ENTHUSIAST = {
    "favorite_genre": "edm",
    "favorite_mood": "party",
    "target_energy": 0.95,
    "target_tempo": 128,
    "target_valence": 0.7,
    "target_danceability": 0.9,
    "likes_acoustic": False,
    "target_acousticness": 0.05
}

# 5. The Acoustic Folk Fan
# Low energy, high acousticness, and relaxed storytelling.
ACOUSTIC_FAN = {
    "favorite_genre": "folk",
    "favorite_mood": "relaxed",
    "target_energy": 0.25,
    "target_tempo": 80,
    "target_valence": 0.7,
    "target_danceability": 0.5,
    "likes_acoustic": True,
    "target_acousticness": 0.95
}

# Keeping UNIQUE_USER_PROFILE for backward compatibility with main.py
UNIQUE_USER_PROFILE = CHILL_LOFI_LISTENER

