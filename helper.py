import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')


def readAndCleanDoc(doc, language_analyzing):
    language_analyzing = language_analyzing
    with open(doc, 'r') as mydoc:
        document = mydoc.read()
        # documentSplit = document.splitlines()
    # Tokenize string
    tokenNoPunc = remove_punc(nltk.tokenize.word_tokenize(document))
    # Remove caps
    tokenLowerCase = list(map(lambda x: x.lower(), tokenNoPunc))
    stop_words = stopwords.words(language_analyzing)
    # Lemmatize
    lemmatized = WordNetLemmatizer()
    cleaned_tokens = [word for word in tokenLowerCase if word not in stop_words]
    lemmatized_words = [lemmatized.lemmatize(wordsToken) for wordsToken in cleaned_tokens]
    return lemmatized_words


def remove_punc(words):
    return [w for w in words if w not in string.punctuation]
