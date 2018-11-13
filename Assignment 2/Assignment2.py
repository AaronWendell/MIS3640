import urllib.request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

def get_text_from_web(url):
    """*Pulls any UTF-8 encoded text back from the internet*
    
    url (string): The url at which the text is located
    
    Returns a string containing the source text found at the provided URL
    """

    response = urllib.request.urlopen(url)
    data = response.read()
    return data.decode('utf-8')

def remove_characters(source, characters):
    """*Removes characters in a play from source text*
    
    source (string): The original text to remove characters from
    characters (list): The list of characters to remove from the source text
    
    Returns a string containing the source text, having removed the character names at the beginning of each of their lines
    """

    for character in characters:
        source = source.replace('\n' + character + '.', '')
    return source

def adapt_text_to_TIOBE(source):
    """*Trims and formats basic elements of a Project Gutenberg's version of Oscar Wilde's "The Importance of Being Earnest" to be more easily processed*
    
    source (string): The original text to format
    
    Returns a string containing the source text reformatted for processing
    """

    source = source.split("FIRST ACT")[1].split("***END OF THE PROJECT GUTENBERG EBOOK THE IMPORTANCE OF BEING EARNEST***")[0]
    TIOBE_characters = ['Lane','Algernon','Lady Bracknell','Gwendolen','Jack','Miss Prism','Cecily','Chasuble','Merriman']
    return remove_characters(source, TIOBE_characters)

def get_TIOBE_samples(source):
    """*Assembles a list of pre-chosen samples for Oscar Wilde's "The Importance of Being Earnest"*
    
    source (string): The formatted book
    
    Returns a list of strings containing a set of samples from the play to analyze
    """

    samples = []

    allsentences = tokenize.sent_tokenize(source)    

    samples.append(allsentences[750])
    samples.append(allsentences[1037] + allsentences[1038])
    samples.append(allsentences[1038])
    samples.append(allsentences[1287] + allsentences[1288])
    samples.append(allsentences[1288])
    samples.append(allsentences[2371])
    samples.append(source)
    return samples

def print_sample_sentiments(samples):
    """*Processes sentiment analysis for a list of samples and prints the results*
    
    samples (list): A list of strings to process
    """

    sample_sentiments = []
    counter = 0
    
    for sample in samples:
        score= SentimentIntensityAnalyzer().polarity_scores(sample)
        counter += 1
        sample_sentiments.append([counter,score.get('neg'), score.get('neu'), score.get('pos'), score.get('compound'),sample])
        print(counter,score.get('neg'), score.get('neu'), score.get('pos'), score.get('compound'),sample)



book = get_text_from_web('http://www.gutenberg.org/cache/epub/844/pg844.txt')
book = adapt_text_to_TIOBE(book)
sample_set = get_TIOBE_samples(book)
print_sample_sentiments(sample_set)

