class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.dtext = {}
        self.ltext = []

    def calculate_word(self):
        self.dtext = {}
        self.ltext = []
        self.stext = self.text.split()  
        for word in self.stext:
            self.dtext[word] = self.dtext.get(word, 0) + 1

        for k, v in self.dtext.items():
            self.ltext.append((v, k))

        return sorted(self.ltext, reverse=True)[0] 

    def calculate_sentence(self):
        self.dtext = {}
        self.ltext = []
        self.sentenc_text = self.text.split('.')  
        for sentence in self.sentenc_text:
            sentence = sentence.strip()
            if sentence: 
                self.dtext[sentence] = self.dtext.get(sentence, 0) + 1

        for k, v in self.dtext.items():
            self.ltext.append((v, k))

        for v,k in sorted(self.ltext,reverse=True) :

            return v,k



text1 = TextAnalyzer(input("Enter your text: "))
print("Most frequent word:", text1.calculate_word())
print("Most frequent sentence:", text1.calculate_sentence())
