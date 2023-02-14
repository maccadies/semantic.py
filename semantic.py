import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

'''Similarities - Cats and monkey's are both furry, on the odd exception of the hairless animals. Both Cats and monkeys
can be the same colour. Both are animals and they have the same basic genetics, of eyes, noses and mouths. 

Bananas and monkeys make sense because monkeys eat bananas. Cats do not eat bananas. 

Both Cats and monkeys can be pets. You can also have a pet banana if you really wanted. 

All three things will degrade over time and die. All 3 things have skin, an outer layer and an inside.
'''

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity


nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity

'''After carefukky comparing the differences between web_sm and web_md. It seems that the few entries are similar with the
swap of apple cat on the 4th entry. All of the numbers on the far right have changed and are in different formats. 
Again bar the exception of some pairs including 1.0's. 
The order of Cat, Apple, Monkey, Banana is still the same. 

The second words in the phrases in the first code it is Cat Apple Monkey Banana, in the second code it becomes cat monkey bananacat apple monkey banana

Finally, after some researching I can see that md is for medium and sm is for small. 

'''