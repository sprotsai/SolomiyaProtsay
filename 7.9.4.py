# Protsay Solomia, Chapter 7, Exercise 4
import nltk
grammar = r"""
  NP:
  {<.*>+}
  }<VBD|IN>+{
  """
whole_sent = [("the", "DT"), ("shiny", "JJ"), ("hot", "JJ"), ("weather", "NN"), ("changes", "VBD"), ("into", "IN"), ("suffering", "NN"), ("for", "IN"), ("us", "PRP")]
single = nltk.RegexpParser(grammar)
print 'A single chunk:  ', single.parse(whole_sent)


