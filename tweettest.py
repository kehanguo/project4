import twitter_analyzer as analyzer

def test_wrongkey():

  # Define the search term
  search_words = "#BU"
  # Define the date_since date
  date_since = "2020-12-10"
  # Define the date_since date
  max_number =10
  
  # get all tweets into a list
  # tweets_list = search_tweet(search_words, date_since, max_number)
  
  assert len(analyzer,search_tweet(search_words, date_since, max_number)) == 10
  
  max_number = 5
  
  assert len(analyzer.search_tweet(search_words, date_since, max_number)) == 5
  
  # analyze all tweets
  # analyze(tweets_list)

test_wrongkey()
run