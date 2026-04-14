# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Rhymer**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---
Personalized song suggestions by matching a user's stylistic preferences (genre, mood) and technical attributes (BPM, energy, acousticness) against a library.
It assumes users can define their taste across seven specific dimensions: genre, mood, energy, tempo, valence, danceability, and acousticness.
Classroom exploration and simulation to understand how weighting and scoring algorithms influence content discovery.
## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---
- It looks at everything from the song's "vibe" (mood and energy) to its technical specs (how fast it is and how much it uses real instruments vs. electronics).
- It takes your favorite genre/mood and compares it to your target "goals", like how much energy you want in a song or if you’re looking for something positive (valence).
- Every time a song matches a part of your profile, it earns "points." High-priority features like Energy and Tempo carry more weight than simple labels. It even uses "fuzzy matching," so if you like Pop, it knows to give partial credit for related styles like Synthwave or Disco.
- I rebalanced the weights to prioritize the "feel" of a song (Energy/Acousticness) over strict genre labels to help break users out of "filter bubbles" and find related music they might otherwise miss.
## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
50 Songs catalog.
It covers a wide range of genres (Pop, Metal, Lofi, Jazz, Reggae, EDM, etc.) and moods (Chill, Intense, Happy, Sad, Moody).
The dataset is a static snapshot, so it lacks real-time popularity data, lyrics, or niche sub-genres that haven't been manually categorized yet.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---
It works exceptionally well for users with "extreme" tastes, like those who only want super high-energy Metal or very low-energy Lofi study beats.
It's great at identifying the "acoustic signature" of a user's taste, consistently surfacing songs with the right instrument-to-electronic ratio.
The fuzzy matching feels natural; a Pop fan stays within a "mainstream" vibe without being trapped in just one genre label.
## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---
It doesn't know anything about the lyrics, the artist's reputation, or how recent the song is.
Some genres like Flamenco or Grunge have very few entries, making them harder for the system to recommend frequently
Pop is the most common genre in the dataset, which may unintentionally lead to "Pop-leaning" results for general profiles.
The high weight on Energy at 6.0 means the system might ignore a perfect genre/mood match if the energy level is slightly outside the user's target.



## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---
The prfoiles tested are "High-energy Pop Enthusiast", "Chill Lofi Student," and "Metal Head."
I looked for whether the top 5 results felt cohesive. I was surprised by how much the "Fuzzy Matching" helped high-energy pop fans discover EDM and Synthwave tracks.
I ran the same profile multiple times to ensure the tie-breaking logic (sorting by artist/title) kept the results stable and predictable.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---
I can add a feature to show the exact point breakdown for every recommendation like (+6 for Energy).
Implement a "diversity penalty" to ensure the top 5 results aren't all by the same artist.
Allow users to specify genres they hate to explicitly filter them out

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that recommendation systems are a delicate balance of math and psychology; changing a single weight can completely change the personality of the app.

I was surprised by how difficult it is to quantify vibe using just numerical data, sometimes two songs have the same stats but feel very different. 
