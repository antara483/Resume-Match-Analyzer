
# import re
# import nltk
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from collections import Counter
# import string

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt') 

# class ResumeMatcher:
#     def __init__(self):
#         self.stop_words = set(nltk.corpus.stopwords.words('english'))
#         self.lemmatizer = nltk.stem.WordNetLemmatizer()
#         self.punctuation = set(string.punctuation)
        
#     def tokenize(self, text):
#         # More sophisticated tokenization
#         tokens = []
#         for word in nltk.word_tokenize(text.lower()):
#             if word in self.stop_words or word in self.punctuation:
#                 continue
#             if word.isdigit():
#                 continue
#             lemma = self.lemmatizer.lemmatize(word)
#             if len(lemma) > 2:  # Ignore very short words
#                 tokens.append(lemma)
#         return tokens
    
#     def calculate_match_score(self, resume_text, job_text):
#         # Enhanced preprocessing
#         resume_tokens = self.tokenize(resume_text)
#         job_tokens = self.tokenize(job_text)
        
#         # Combine for vectorization
#         documents = [' '.join(resume_tokens), ' '.join(job_tokens)]
        
#         # Improved vectorizer with better parameters
#         vectorizer = TfidfVectorizer(
#             ngram_range=(1, 3),
#             min_df=2,
#             max_df=0.8,
#             sublinear_tf=True,
#             use_idf=True
#         )
        
#         try:
#             tfidf_matrix = vectorizer.fit_transform(documents)
#             similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
#             return min(round(similarity * 115, 2), 100)  # Slightly boosted score
#         except ValueError:
#             return 0.0  # Fallback for empty texts
# # deep


import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

# Ensure required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

class ResumeMatcher:
    def __init__(self):
        self.stop_words = set(nltk.corpus.stopwords.words('english'))
        self.lemmatizer = nltk.stem.WordNetLemmatizer()
        self.punctuation = set(string.punctuation)
        
    def tokenize(self, text):
        # Tokenization with filtering
        tokens = []
        for word in nltk.word_tokenize(text.lower()):
            if word in self.stop_words or word in self.punctuation:
                continue
            if word.isdigit():
                continue
            lemma = self.lemmatizer.lemmatize(word)
            # if len(lemma) > 2:
            #     tokens.append(lemma)
            if len(lemma) > 1:
                tokens.append(lemma)

        return tokens
    
    # def calculate_match_score(self, resume_text, job_text):
    #     resume_tokens = self.tokenize(resume_text)
    #     job_tokens = self.tokenize(job_text)
    #     # add
    #     print("\n--- Resume Tokens ---")
    #     print(resume_tokens[:50])
    
    #     print("\n--- Job Tokens ---")
    #     print(job_tokens[:50])
    #     # add
    #     documents = [' '.join(resume_tokens), ' '.join(job_tokens)]
        
    #     vectorizer = TfidfVectorizer(
    #         ngram_range=(1, 3),
    #         min_df=1,
    #         max_df=0.9,
    #         sublinear_tf=True,
    #         use_idf=True
    #     )
        
    #     try:
    #         tfidf_matrix = vectorizer.fit_transform(documents)
    #         similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    #         return min(round(similarity * 115, 2), 100)  # Boosted slightly
    #     except ValueError:
    #         return 0.0

    def calculate_match_score(self, resume_text, job_text):
        resume_tokens = set(self.tokenize(resume_text))
        job_tokens = set(self.tokenize(job_text))
    
        if not resume_tokens or not job_tokens:
            return 0.0
    
        common = resume_tokens.intersection(job_tokens)
        score = len(common) / len(job_tokens) * 100
    
        print(f"Overlap: {len(common)} / {len(job_tokens)} → {score}%")
    
        return round(score, 2)
