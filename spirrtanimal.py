# import streamlit as st
# from fuzzywuzzy import fuzz

# # Define animal characteristics
# animal_traits = {
#     "Panda": ["calm", "lazy", "gentle", "sleeping", "climbing trees"],
#     "Lion": ["brave", "strong", "leader", "hunting", "roaring"],
#     "Dolphin": ["playful", "intelligent", "social", "swimming", "jumping"],
#     "Sloth": ["slow", "relaxed", "calm", "sleeping", "hanging"]
# }

# # Function to find spirit animal
# def find_spirit_animal(user_traits):
#     spirit_animal = ""
#     max_score = 0
#     for animal, traits in animal_traits.items():
#         score = 0
#         for trait in user_traits:
#             for t in traits:
#                 score += fuzz.ratio(trait.lower(), t.lower())
#         if score > max_score:
#             max_score = score
#             spirit_animal = animal
#     return spirit_animal

# # Streamlit app
# st.title("Spirit Animal Finder")

# # User input
# user_traits = st.multiselect("Select your traits and daily activities", 
#                              ["calm", "lazy", "gentle", "brave", "strong", "leader", 
#                               "playful", "intelligent", "social", "slow", "relaxed", 
#                               "sleeping", "climbing trees", "hunting", "roaring", 
#                               "swimming", "jumping", "hanging"])

# # Find and display spirit animal
# if st.button("Find my spirit animal"):
#     if user_traits:
#         spirit_animal = find_spirit_animal(user_traits)
#         st.write("Your spirit animal is:", spirit_animal)
#     else:
#         st.write("Please select at least one trait or activity.")

# Import necessary libraries
import streamlit as st
from operator import itemgetter

# Define Animal characteristics and store it in a list
animals = [
    {"name": "Panda", "traits": ["calm", "lazy", "gentle"], "activities": ["sleeping", "climbing trees"]},
    {"name": "Lion", "traits": ["brave", "strong", "leader"], "activities": ["hunting", "leading"]},
    {"name": "Dolphin", "traits": ["intelligent", "playful", "social"], "activities": ["swimming", "playing"]},
    {"name": "Sloth", "traits": ["relaxed", "slow", "solitary"], "activities": ["sleeping", "hanging upside down"]}
]

# Function to find spirit animal
def find_spirit_animal(traits, activities):
    scores = []
    for animal in animals:
        trait_score = sum(1 for trait in traits if trait in animal["traits"])
        activity_score = sum(1 for activity in activities if activity in animal["activities"])
        scores.append((animal["name"], trait_score + activity_score))
    return max(scores, key=itemgetter(1))[0]

# Create a user-friendly interface using streamlit
st.title("Spirit Animal Finder")
traits = st.multiselect("Choose your traits:", ["calm", "lazy", "gentle", "brave", "strong", "leader", "intelligent", "playful", "social", "relaxed", "slow", "solitary"])
activities = st.multiselect("Choose your daily activities:", ["sleeping", "climbing trees", "hunting", "leading", "swimming", "playing", "hanging upside down"])

# Display the spirit animal
if st.button("Find my spirit animal"):
    spirit_animal = find_spirit_animal(traits, activities)
    st.write(f"Your spirit animal is: **{spirit_animal}**")