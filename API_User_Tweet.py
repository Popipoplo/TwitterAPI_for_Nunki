from ast import main
import tweepy
from flask import Flask

### Connection à L'API de Twitter ###

### Remplacez les etoiles ###
auth = tweepy.OAuthHandler("****" , "****")
auth.set_access_token("****" , "****")

api = tweepy.API(auth)

### Test De L'API Twitter ###

try : 
    api.verify_credentials()
    print("API : Connected")
except : 
    print("API : Not connected")


### Initialisation de l'app ###

app = Flask(__name__) 

### Route pour mon getTweet ###

@app.route("/search=<keyword>/media=<boolean>", methods = ['GET'])

### Fonction me permettant de rechercher le dernier tweet posté, comportant mon keyword. De plus cette fonction permet de filtrer les tweets avec ou sans média grace à boolean ###

def getTweet(keyword, boolean):

    ### Permet de filtrer les Retweets ce qui nous permet d'avoir uniquement des vrais tweets ###
    keyword_filterRT = keyword + " -filter:retweets"
    max_tweets = 1
    include_entities = boolean

    tweets = tweepy.Cursor(api.search_tweets, q = keyword_filterRT, tweet_mode = 'extended', include_entities = include_entities).items(max_tweets)

    for tweet in tweets :

        tweet_text = str(tweet.full_text)


    return tweet_text


### Route pour mon getUser ###

@app.route("/user=<userId>", methods = ['GET'])

### Fonction me permettant d'obtenir les infos d'un utilisateur grace à son user_id ###

def getUser(userId):

    user = api.get_user(user_id = userId)

    return str(user)


if __name__ == '__main__' :
    app.run(debug = True)
    print ("API START")
