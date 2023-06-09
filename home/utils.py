import urllib.parse
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import time
def get_transcript(url):
    # Parse the query string parameters of the URL
    query_params = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)

    id = query_params['v'][0]
    ##id = 'Y8Tko2YC5hA'
    transcript = YouTubeTranscriptApi.get_transcript(id)
    script = ""

    for text in transcript:
        t = text["text"]
        if t != '[Music]':
            script += t + " "
    transcript, no_of_words = script, len(script.split())

    return transcript, no_of_words


# def clean(transcript):
#     from string import punctuation

#     stopwords = list(STOP_WORDS)
#     # %%
#     nlp = spacy.load('en_core_web_sm')
#     # %%
#     doc = nlp(transcript)
#     punctuated_text = ''
#     for token in doc:
#         # Add a space after each token
#         punctuated_text += token.text + ' '
#         # If the token ends a sentence, add a period
#         if token.is_sent_end:
#             punctuated_text = punctuated_text[:-1] + '. '

#     # Print the punctuated text
#     # print(punctuated_text)
#     tokens = [token.text for token in doc]
#     # print(tokens)
#     punctuation = punctuation + '\n'
#     word_frequencies = {}
#     for word in doc:
#         if word.text.lower() not in stopwords:
#             if word.text.lower() not in punctuation:
#                 if word.text not in word_frequencies.keys():
#                     word_frequencies[word.text] = 1
#                 else:
#                     word_frequencies[word.text] += 1
#     # print(word_frequencies)
#     max_frequency = max(word_frequencies.values())
#     for word in word_frequencies.keys():
#         word_frequencies[word] = word_frequencies[word] / max_frequency
#         # print(word_frequencies)
#     sentence_tokens = [sent for sent in doc.sents]
#     # print(sentence_tokens)
#     sentence_scores = {}
#     for sent in sentence_tokens:
#         for word in sent:
#             if word.text.lower() in word_frequencies.keys():
#                 if sent not in sentence_scores.keys():
#                     sentence_scores[sent] = word_frequencies[word.text.lower()]
#                 else:
#                     sentence_scores[sent] += word_frequencies[word.text.lower()]
#     select_length = int(len(sentence_tokens) * 0.3)
    
#     summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
#     final_summary = [word.text for word in summary]
#     summary = ' '.join(final_summary)

#     return summary


def get_summary(url):
    s = get_transcript(url)
    s = s[0]
    l=len(s)
 
    part1= str(s[:round(l/2)])
    part2 = str(s[round(l/2):])
    
    response1 = requests.post("https://sumit1614-summerization.hf.space/run/predict", json={
        "data": [
            part1,
        ]
    }).json()
    p1 = response1["data"]
    time.sleep(1)
    response2 = requests.post("https://sumit1614-summerization.hf.space/run/predict", json={
        "data": [
            part2,
        ]
    }).json()
    p2 = response2["data"]
    return "".join(p1+p2)

   


