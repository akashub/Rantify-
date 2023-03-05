import spacy
nlp = spacy.load("en_core_sci_lg")
text = "I think I should not be doing engineering and open a small pastry shop in france."
doc = nlp(text)
print(doc.ents)
