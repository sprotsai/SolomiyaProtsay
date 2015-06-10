# Protsay Solomia, Chapter 5, Excercise 21
import nltk
from nltk.corpus import brown
verbs=['adore', 'love', 'like', 'prefer']#list of verbs in the task
text=nltk.corpus.brown.tagged_words(categories='news')#zminniy text prusvoila vsi slova z katehorii news
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V')]#made a condition for variety kk that prints list of bigrams sliv+tag
kk
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V') and w[1][0] in verbs]#checking for kk the condition if words from the list of verbs present
kk
#checking if the same condition is used for other categories
text=nltk.corpus.brown.tagged_words(categories='romance')
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V') and w[1][0] in verbs]
text=nltk.corpus.brown.tagged_words(categories='religion')
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V') and w[1][0] in verbs]
#checking whether we need other words present in this category
text=nltk.corpus.brown.tagged_words(categories='news')
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V') and w[1][0]=='operated']
print kk
#there is no verbs in the category
