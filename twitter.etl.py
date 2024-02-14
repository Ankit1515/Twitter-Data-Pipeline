import tweepy
import os
import pandas as pd             #to work with data 
import json                     #to transfer data as text that can be sent over a network
from datetime import datetime   
import s3fs                     #to store, retrive data from S3 Bucket
from zipfile import ZipFile

#access_token = ""
#access_token_secret = ""
#consumer_key = ""
#consumer_secret = ""

def run_twitter_etl():
    df = pd.read_csv("C:/Users/ANKIT/Desktop/Airflow_Project/TweetsFile.csv")
    df.to_csv("s3://ankit-twitter-airflow-bucket/TweetsFiles.csv")
    