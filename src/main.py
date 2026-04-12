"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs
from user_profile import UNIQUE_USER_PROFILE


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Using the unique user profile for comparison
    user_prefs = UNIQUE_USER_PROFILE

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "═" * 65)
    print(f"{'🎵  TOP MUSIC RECOMMENDATIONS FOR YOU  🎵':^65}")
    print("═" * 65 + "\n")

    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        
        # Prepare display strings
        title_line = f" {i}. {song['title']} — {song['artist']}"
        score_line = f"    ⭐ Match Score: {score:.2f}"
        
        # Clean up and format reasons
        reasons = explanation.replace("Points earned for: ", "").replace(".", "")
        if "General recommendation" in reasons:
            reasons = "Fits your baseline preferences"
            
        print(title_line)
        print(score_line)
        print(f"    📝 Why: {reasons}")
        print("─" * 65)

    print("\n    🎧  Happy listening!  🎧\n")


if __name__ == "__main__":
    main()
