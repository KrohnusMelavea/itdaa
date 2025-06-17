import csv
import json
import time
import uuid
import datetime
import functools
import matplotlib.pyplot as plt

class Point:
 x: float
 y: float

 def __init__(self, x: float, y: float):
  self.x = x
  self.y = y

class Line:
 label: str
 points: list[Point]

 def __init__(self, label: str, points: list[Point]):
  self.label = label
  self.points = points

def create_line_graph(lines: list[Line], file_path: str):
    plt.clf()
    for line in lines:
        xs = [point.x for point in line.points]
        ys = [point.y for point in line.points]
        plt.plot(xs, ys, label = line.label)
    plt.legend(bbox_to_anchor=(0.5, -0.1), loc='upper center')
    plt.savefig(file_path, bbox_inches="tight")


class SentimentKeywordLookup:
    POSITIVE = [
        "excellent", 
        "amazing", 
        "outstanding", 
        "impressive", 
        "superb", 
        "brilliant", 
        "happy", 
        "delightful", 
        "cheerful", 
        "joyful", 
        "content", 
        "satisfied",
        "recommended", 
        "appreciated", 
        "valuable", 
        "useful", 
        "worth", 
        "beneficial",
        "strong",
        "efficient",
        "fast",
        "reliable",
        "responsive",
        "stable",
        "perfect",
        "flawless",
        "smooth",
        "clean",
        "neat",
        "elegant",
        "good",
        "awesome",
        "helpful",
        "expedient",
        "nice",
        "cool",
        "fantastic",
        "wow",
        "best",
        "great",
        "dope",
        "op",
        "noice",
        "super",
        "funtastic",
        "love",
        "incredible",
        "like",
        "phenomenal",
        "exceptional",
        "excellent",
        "wonderful",
        "sweet",
        "accurate",
        "excelente",
        "goat",
        "sigma",
        "grear",
        "works well",
        "legit",
        "gut",
        "thank",
        "helped",
        "amezing",
        "gud",
        "awaysome",
        "addicted",
        "assignment",
        "epic",
        "prefect",
        "beautiful",
        "groundbreaking",
        "exeptional",
        "supportive",
        "helping",
        "goood",
        "gooood",
        "goooood",
        "gooooood",
        "goooooood",
        "extraordinary",
        "it's gd",
        "gnarly",
        "peak",
        "genuine",
        "sastifying",
        "incradible",
        "parfect",
        "future",
        "woow",
        "wooow",
        "woooow",
        "wooooow",
        "woooooow",
        "wooooooow",
        "waw",
        "friendly",
        "perfekt",
        "lifesaver",
        "exilent",
        "awsame",
        "expert application",
        "effective",
        "loving",
        "supar",
        "awasome",
        "dankie",
        "tremendous",
        "helps",
        "very convenient",
        "fun",
        "factual",
        "quick",
        "awsome",
        "genius",
        "magnificent",
        "exelent",
        "game changer",
        "fabulous",
        "well done",
        "sexy",
        "astounding",
        "time saving",
        "thumbs up",
        "goid",
        "amzing",
        "revolutionary",
        "interesting",
        "fascinating",
        "spectagular",
        "ultimate",
        "life saver",
        "informative",
        "life changing",
        "amazed",
        "owsome",
        "exelnte",
        "increible",
        "goog",
        "suprb",
        "extra ordinary",
        "favourite",
        "favorite",
        "understanding",
        "intelligent",
        "better",
        "powerful",
        "exciting",
        "knowledgeable",
        "transformative",
        "excellant",
        "delicious",
        "resourceful",
        "mind blowing",
        "very goo",
        "banger",
        "godd",
        "amzaing",
        "elite",
        "solid",
        "amsome",
        "authentic",
        "recommendable",
        "remarkable",
        "legendary",
        "5/5",
        "4/5",
        "brillant",
        "handy",
        "awosome",
        "execllent",
        "exllent",
        "amaze",
        "xcellent",
        "sick",
        "execellent",
        "lit",
        "sharp",
        "gooooooooood",
        "goooooooood",
        "gooooooood",
        "goooooood",
        "gooooood",
        "goooood",
        "gooood",
        "goood",
        "accuracy",
        "geat"
    ]
    NEGATIVE = [
        "terrible",
        "awful",
        "poor",
        "bad",
        "disappointing",
        "subpar",
        "angry",
        "annoyed",
        "irritated",
        "frustrated",
        "furious",
        "weak",
        "slow",
        "buggy",
        "broken",
        "faulty",
        "unstable",
        "hate",
        "regret",
        "waste",
        "failure",
        "useless",
        "problematic",
        "sad",
        "upset",
        "waste",
        "failure",
        "useless",
        "problematic",
        "sad",
        "upset",
        "depressing",
        "painful",
        "unhappy",
        "not work",
        "trash",
        "worst",
        "stupid",
        "didnt work",
        "dogshit",
        "crash",
        "outdated",
        "false information",
        "lag",
        "never work",
        "cant login",
        "not impartial",
        "no bueno",
        "unexpected",
        "not god",
        "boo",
        "booo",
        "rubbish",
        "1/5",
        "2/5",
        "garbage",
        "fake",
        "lazy",
        "overhyped",
        "lame",
        "worse",
        "all wrong",
        "goof"
    ]
class Sentiment:
    POSITIVE = 0
    NEGATIVE = 1
    NEUTRAL = 2

def timing(function):
    @functools.wraps(function)
    def wrap(*args, **kw):
        start_time = time.time()
        result = function(*args, **kw)
        end_time = time.time()
        print(f"Function: {function.__name__} Took {end_time - start_time}s")
        return result
    return wrap

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return f"{obj}"
        return json.JSONEncoder.default(self, obj)

class ChatGPTRating:
    pass

class ChatGPTRating:
    id:uuid.uuid4
    username:str
    content: str
    score:int
    likes:int
    created_version:str
    created_on:datetime.datetime
    current_version:str
    sentiment: int
    
    def __init__(self, id:uuid.uuid4, username:str, content:str, score:int, likes:int, created_version:str, created_on:str, current_version:str, sentiment:str):
        self.id = id
        self.username = username
        self.content = content
        self.score = score
        self.likes = likes
        self.created_version = created_version
        self.created_on = created_on
        self.current_version = current_version
        self.sentiment = sentiment
    
    def analyse_positive_sentiment(content: str) -> int:
        return sum(content.count(sentimental_word) for sentimental_word in SentimentKeywordLookup.POSITIVE)
    def analyse_negative_sentiment(content: str) -> int:
        return sum(content.count(sentimental_word) for sentimental_word in SentimentKeywordLookup.NEGATIVE)
    def analyse_sentiment(content: str) -> float:
        #Don't have time for proper unbiased analysis (this one's weighted in favour of positive)
        positive_sentiment = ChatGPTRating.analyse_positive_sentiment(content)
        negative_sentiment = ChatGPTRating.analyse_negative_sentiment(content)
        if negative_sentiment == 0:
            if positive_sentiment == 0:
                return Sentiment.NEUTRAL
            else:
                return Sentiment.POSITIVE
        else:
            if positive_sentiment / negative_sentiment > 1.25:
                return Sentiment.POSITIVE
            elif positive_sentiment / negative_sentiment < 0.75:
                return Sentiment.NEGATIVE
            else:
                return Sentiment.NEUTRAL
    
    def from_row(row) -> ChatGPTRating:
        return ChatGPTRating(
            id = uuid.UUID(row[0]),
            username = row[1],
            content = row[2],
            score = int(row[3]),
            likes = int(row[4]),
            created_version = row[5],
            created_on = datetime.datetime.strptime(row[6], "%m/%d/%Y %H:%M"),
            current_version = row[7],
            sentiment = ChatGPTRating.analyse_sentiment(row[2].lower())
        )

@timing
def setup_reader(file_handler):
    reader = csv.reader(file_handler)
    next(reader)
    return reader

@timing
def read_ratings(file_path:str) -> list[ChatGPTRating]:
    with open(file_path, "r", encoding="utf-8") as file_handler:
        return list(map(ChatGPTRating.from_row, setup_reader(file_handler)))
    
@timing
def convert_ratings(ratings:list[ChatGPTRating]) -> str:
    return json.dumps([rating.__dict__ for rating in ratings], cls=UUIDEncoder, indent=4)

def get_sentiment_by_month(data: list[ChatGPTRating]) -> list[list[int, int, int]]:
    grouped_by_month = dict()
    for entry in data:
        if (entry.created_on.year, entry.created_on.month) in grouped_by_month:
            grouped_by_month[(entry.created_on.year, entry.created_on.month)][entry.sentiment] += 1
        else:
            grouped_by_month[(entry.created_on.year, entry.created_on.month)] = [0, 0, 0]
            grouped_by_month[(entry.created_on.year, entry.created_on.month)][entry.sentiment] = 1
    return grouped_by_month
data = read_ratings("data/chatgpt_reviews.csv")
                
#neutral = [entry.content for entry in data if ChatGPTRating.analyse_positive_sentiment(entry.content.lower()) == 0 and ChatGPTRating.analyse_negative_sentiment(entry.content.lower()) == 0]
#print("\n".join(entry for entry in neutral))

#print(len(neutral))
#print([entry.created_on for entry in data])

print(sorted(list(get_sentiment_by_month(data).items()), key=lambda x: x[0]))

sentiment_by_month = sorted(list(get_sentiment_by_month(data).items()), key=lambda x: x[0])
create_line_graph(
    [
        Line(("Positive", "Negative", "Neutral")[sentiment], [Point(index, entry[1][sentiment]) for index, entry in enumerate(sentiment_by_month)])
        for sentiment in (Sentiment.POSITIVE, Sentiment.NEGATIVE, Sentiment.NEUTRAL)
    ],
    "graphs/3.3.png"
)