# https://www.ibm.com/think/topics/stemming-lemmatization#:~:text=The%20practical%20distinction%20between%20stemming,be%20found%20in%20the%20dictionary.
import re as re
import nltk as nltk

from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('words')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def lemmatize_passage(text):
    words = custom_tokenize(text)
    pos_tags = pos_tag(words)
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
    return lemmatized_words


def custom_tokenize(text):
    return re.split(r'([\s,"\[\]\(\)]|[^\d]\.[^\d])', text)


if __name__ == '__main__':
    # text = ("after looking at the change \"history provided\", we found that the issue occurred because the user was "
    #         "able to approve a batch with $340 that was already approved, which should not be allowed.")
    # print(f'{lemmatize_passage(text)}')
    # passage = lemmatize_passage(
    #     """,we have processed 18 inward cheques in  ph_user  and none of them received ‘ pay replied”""")
    # print(f'{len(passage)} -> {passage}')
    print(lemmatize_passage("""application current tls  ph_user  tlsv1.2 ecci tlsv1.2 onus tlsv1.2  ph_user  tlsv1.2 .  ph_user  i tlsv1.2 cda tlsv1.2 rdc tlsv1.2"""))
    print(lemmatize_passage("""v10.10 test new page v1.8.0 from  ph_user  side only v1.8.0,hello"""))
    print(WordNetLemmatizer().lemmatize('thinking', wordnet.VERB))
    print(WordNetLemmatizer().lemmatize('thinking', wordnet.ADJ))

    version_regex = re.compile(r'\b[vV][\d\.]+\b')
    print(re.sub(version_regex, 'ph_version', "v10.10 test new page v1.8.0 from  ph_user  side only v1.8.0."))
