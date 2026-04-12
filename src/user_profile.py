"""
Defines a unique user profile dictionary for the music recommender simulation.
This profile represents a specific type of listener used as a baseline for comparisons.
"""

# Unique User Profile: "The Atmospheric Focus Listener"
# This listener enjoys mellow, acoustic, and chill vibes for deep work.
UNIQUE_USER_PROFILE = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.3,
    "target_tempo": 70,
    "target_valence": 0.5,
    "target_danceability": 0.4,
    "likes_acoustic": True,
    "target_acousticness": 0.85
}

# Another example: "The High-Energy Party Starter"
PARTY_USER_PROFILE = {
    "favorite_genre": "edm",
    "favorite_mood": "party",
    "target_energy": 0.9,
    "target_tempo": 128,
    "target_valence": 0.8,
    "target_danceability": 0.9,
    "likes_acoustic": False,
    "target_acousticness": 0.05
}
