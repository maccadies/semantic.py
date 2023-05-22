# semantic.py

Word Similarity Analyzer

Overview
This Python script utilizes Spacy's Natural Language Processing (NLP) capabilities to analyze and compare the similarity between words and sentences. The script calculates and prints out similarity scores between a set of chosen words and sentences, using two different Spacy language models: 'en_core_web_md' (medium) and 'en_core_web_sm' (small).

Installation
To run this project, you need to have Python and Spacy installed. Additionally, you need to download both 'en_core_web_md' and 'en_core_web_sm' language models.

How It Works
The script first loads the Spacy language model and assigns different words to variables. It then prints out the similarity scores between these words.

The second part of the script creates a set of tokens and calculates the similarity score for each pair of tokens.

The third part compares a chosen sentence to a set of other sentences, generating a similarity score for each pair.

The process is then repeated with the 'en_core_web_sm' model for comparison.

Usage
The script can be run as is. The words and sentences to compare are hard-coded into the script, but can be easily changed to suit your needs.

python
Copy code
word1 = nlp("your_word_here")
sentence_to_compare = "Your sentence here"
sentences = ["Your", "list", "of", "sentences", "to", "compare"]

Insights
This script provides an opportunity to understand how Spacy's different language models might give different results for the same similarity comparisons. By comparing these outputs, users can gain insights into the characteristics and performance of each model.

Limitations and Future Work
Please note that the words and sentences currently included in the script are placeholders. For more meaningful results, users should replace these with their data. Future enhancements could include a more interactive interface, allowing users to input their words or sentences to compare.
