import nltk
import math

stop_words = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
              "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
              "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
              "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",
              "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
              "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how",
              "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
              "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should",
              "now"}
ps = nltk.stem.PorterStemmer()


# tokenize text using nltk lib
def tokenize(text):
    return nltk.word_tokenize(text)


# stem word using provided stemmer
def stem(word, stemmer):
    return stemmer.stem(word)


# checks if word is appropriate - not a stop word and isalpha
def is_apt_word(word):
    return word not in stop_words and word.isalpha()


# combines all previous methods together
def preprocess(text):
    tokenized = tokenize(text.lower())
    return [stem(w, ps) for w in tokenized if is_apt_word(w)]


def ngram_generator(doc, n):
    tokens = preprocess(doc)
    text = ""
    for token in tokens:
        text += token

    ngrams = []
    for i in range(len(text) - (n - 1)):
        ngrams.append(text[i:i+n])

    return ngrams


def hash_generator(ngrams):
    result = []
    b = 41
    q = 997
    n = len(ngrams[0])
    for i in range(len(ngrams)):
        sum = 0
        if i == 0:
            for ch in ngrams[i]:
                sum += ord(ch)*math.pow(b, n - i + 1) % q
                result.append(sum)

        else:
            sum = (result[-1] - ord(ngrams[i-1][0])*math.pow(b, n - 1))*b + ord(ngrams[i][-1])
            sum = sum % q
            result.append(sum)
    return result


ngrams = ngram_generator("Hi my name is Anna Innopolis afgjjsldfokvfdj;jvfdddddddfbbbbbbbf", 4)
print(hash_generator(ngrams))
