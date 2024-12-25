import spacy

class CommandParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def parse(self, input_text):
        doc = self.nlp(input_text)
        #extract verbs and nouns
        action = None
        target = None
        for token in doc:
            if token.pos_ == "VERB":
                action = token.lemma_  #form of the verb
            elif token.pos_ == "NOUN":
                target = token.text
        return action, target

# use
# parser = CommandParser()
# action, target = parser.parse("attack the goblin")
# print(f"Action: {action}, Target: {target}")  #out: Action: attack, Target: goblin
