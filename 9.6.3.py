# Protsay Solomia, Chapter 9, Exercise 3

import nltk
fs1 = nltk.FeatStruct(Category="Chas")
fs2 = nltk.FeatStruct(Category="Chas", Other_Category='Misce')# Defining the features
print fs1.subsumes(fs2) # Subsuming the features
