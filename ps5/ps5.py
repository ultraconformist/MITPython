# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Morgan

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        '''
        Initializes a NewsStory object. Stores all relevant information to be 
        parsed from an RSS feed.
             
        guid (string): A globally unique identifier
        title (string): A news story title
        description (string): A news story description
        link (string): A link to more content
        pubdate (datetime): A datetime of a news story

        A NewsStory object has five attributes:
            self.guid (string, determined by input guid)
            self.title (string, determined by input title)
            self.description (string, determined by input string)
            self.link (string, determined by input link)
            self.pubdate (datetime, determined by input datetime)
        '''
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        '''
        Initializes a PhraseTrigger object. Inherits evaluate from Trigger 
        parent object. Takes in a string phrase.
        
        phrase (string): A phrase to be evaluated
        
        A PhraseTrigger has one attribute:
            self.phrase (string, determined by input phrase)
        
        PhraseTrigger implements one method:
            is_phrase_in(text): Returns True if self.phrase is present in text,
            and False otherwise
        '''
        self.phrase = phrase
        
    def is_phrase_in(self, text):
        
        # Processes text input by first stripping out all punctuation,
        # by replacing with whitespace, then splitting the text into substrings
        # on whitespace boundaries and rejoining with spaces, and then finally
        # reducing all characters in text to lowercase
        for char in string.punctuation:
            text = text.replace(char, ' ')
        text_list = text.split()
        text = ' '.join(text_list) + ' '
        text = text.lower()
       
        # Repeat for self.phrase
        cleaned_phrase = self.phrase
        for char in string.punctuation:
            cleaned_phrase = cleaned_phrase.replace(char, ' ')
        cleaned_phrase_list = cleaned_phrase.split()
        cleaned_phrase = ' '.join(cleaned_phrase_list) + ' '
        cleaned_phrase = cleaned_phrase.lower()

        # TODO: Refactor this to implement cleaning the inputs as a function

        # Check cleaned text for instance of phrase
        if cleaned_phrase in text:
            return True
        else:
            return False   

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        '''
        Initializes a TitleTrigger object. Inherits evaluate from Trigger 
        superclass and is_phrase_in function from PhraseTrigger.
        
        phrase (string): A phrase to be evaluated
        
        A TitleTrigger has one attribute:
            self.phrase (string, determined by input phrase)
        
        TitleTrigger inherits one method from PhraseTrigger:
            is_phrase_in(text): Returns True if self.phrase is present in text,
            and False otherwise
            
        TitleTrigger implements one method:
            evaluate(story): Takes a NewsStory object; Returns True if
            self.phrase is present in story's title, False otherwise
        '''
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())
    
# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        '''
        Initializes a DescriptionTrigger object. Inherits evaluate from Trigger 
        superclass and is_phrase_in function from PhraseTrigger.
        
        phrase (string): A phrase to be evaluated
        
        A DescriptionTrigger has one attribute:
            self.phrase (string, determined by input phrase)
        
        DescriptionTrigger inherits one method from PhraseTrigger:
            is_phrase_in(text): Returns True if self.phrase is present in text,
            and False otherwise
            
        DescriptionTrigger implements one method:
            evaluate(story): Takes a NewsStory object; Returns True if
            self.phrase is present in story's description, False otherwise
        '''
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, time):
        '''
        Initializes a TimeTrigger object. Inherits evaluate from Trigger parent
        class. Takes in time as a string. Abstract class.
        
        time (string): A time in EST in format '%d %b %Y %H:%M:%S'
        
        A TimeTrigger has one attribute:
            self.time (datetime, determined by input time string and converted 
            to datetime before saved as an attribute)
        '''
        self.time = datetime.strptime(time, '%d %b %Y %H:%M:%S')
        
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        '''
        Initializes a BeforeTrigger object, a subclass of TimeTrigger.
        Inherits self.time from TimeTrigger.
        
        time (string): A time in EST in format '%d %b %Y %H:%M:%S'
        
        A BeforeTrigger inherits one attribute from self.time:
            self.time (datetime, determined by input time string and converted 
            to datetime before saved as an attribute)
        
        A BeforeTrigger implements one method:
            evaluate(story): Takes a NewsStory object; returns True 
            if self.time occurs strictly before the story's time,
            and False otherwise
        '''
        TimeTrigger.__init__(self, time)
        
    def evaluate(self, story):
        # try-except to handle offset-naive/offset-aware mismatch case
        try:
            result = story.get_pubdate() < self.time
        except TypeError:
            corrected_time = self.time.replace(tzinfo=pytz.timezone("EST"))
            result = story.get_pubdate() < corrected_time
            
        if result:
            return True
        else:
            return False

class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        '''
        Initializes a AfterTrigger object, a subclass of TimeTrigger.
        Inherits self.time from TimeTrigger.
        
        time (string): A time in EST in format '%d %b %Y %H:%M:%S'
        
        An AfterTrigger inherits one attribute from self.time:
            self.time (datetime, determined by input time string and converted 
            to datetime before saved as an attribute)
        
        An AfterTrigger implements one method:
            evaluate(story): Takes a NewsStory object; returns True 
            if self.time occurs strictly after the story's time,
            and False otherwise
        '''
        TimeTrigger.__init__(self, time)
        
    def evaluate(self, story):
        # same as BeforeTrigger
        try:
            result = story.get_pubdate() > self.time
        except TypeError:
            corrected_time = self.time.replace(tzinfo=pytz.timezone("EST"))
            result = story.get_pubdate() > corrected_time
            
        if result:
            return True
        else:
            return False

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

# Problem 8
# TODO: AndTrigger

# Problem 9
# TODO: OrTrigger


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

