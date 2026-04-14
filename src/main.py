"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs
from user_profile import POP_ENTHUSIAST, CHILL_LOFI_LISTENER, METAL_HEAD


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Define the target profiles to test
    profiles = [
        ("High-Energy Pop Enthusiast", POP_ENTHUSIAST),
        ("Chill Lofi Student", CHILL_LOFI_LISTENER),
        ("Metal Head", METAL_HEAD)
    ]

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "═" * 65)
        print(f"{f'🎵  RECOMMENDATIONS FOR: {profile_name.upper()}  🎵':^65}")
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
