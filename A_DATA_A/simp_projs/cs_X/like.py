import tweepy

#necessary keys & tokens
access_token = "1750929024883564546-vwgJW5mWw8VgF4WmjAEjIcOlHofjor"
access_token_secret = "1PIwKKJUU1cHWd2tCZ2j9v2EQrrtroebbx5pb0mSAyGm7"
api_key="4AceyJkR87OEzfW4ss6lt3mcc"
api_secret="nbT1JnCI6jc4q9Mx5YBEDMi3NKk08Cz4gsBPdChDOI2m3J7hvt"
bearer_token="AAAAAAAAAAAAAAAAAAAAAE9msAEAAAAADJoOHfjkK3t2IMJcV%2BT4AvKx72E%3DWlnVGLqkenEnyLU3ZEa7iErqHymVExKqzLNr3qeMcVS4vM1uy8"
consumer_key = "V2tTSnE3V1R4aVplT2RobS1fc2s6MTpjaQ"
consumer_secret = "lDpEvC-Yh5KRMlH8rglLftwRmqKxPbSYXPZQTWFjzEjYNIosvD"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
client = tweepy.Client(auth)



    # Post a tweet
client.get_tweet("1751248539626422370")

   
print("Successfully connected!")