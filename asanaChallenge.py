import pandas as pd
import collections
import datetime


# A user table ("takehome_users") with data on 12,000 users who signed up for the product in the last two years. This table includes:
  # name: the user's name
  # object_id: the user's id
# email: email address
# creation_source: how their account was created. This takes on one of 5 values:
# PERSONAL_PROJECTS: invited to join another user's personal workspace
# GUEST_INVITE: invited to an organization as a guest (limited permissions)
# ORG_INVITE: invited to an organization (as a full member)
# SIGNUP: signed up via asana.com
# SIGNUP_GOOGLE_AUTH: signed up using Google Authentication (using a Google email account for their login id)
# creation_time: when they created their account
# last_session_creation_time: unix timestamp of last login
# opted_in_to_mailing_list: whether they have opted into receiving marketing emails
# enabled_for_marketing_drip: whether they are on the regular marketing email drip
# org_id: the organization (group of users) they belong to
# invited_by_user_id: which user invited them to join (if applicable).

 # A usage summary table ("takehome_user_engagement") that has a row for each day that a user logged into the product. Defining an "adopted user" as a user who has logged into the product on three separate days in at least one seven-day period, identify which factors predict future user adoption. You are free to alter the tables as needed and to create new tables in this database.

user=pd.read_csv('takehome_users.csv')
engage= pd.read_csv('takehome_user_engagement.csv')

#Extract yyyy-mm-dd from the time_stamp
engage['date']=engage['time_stamp'].str[0:10]

#Convert to datetime object
engage['time_stamp']=pd.to_datetime(engage['time_stamp'])
engage['date']=pd.to_datetime(engage['date'])

engage.sort_values('user_id')

# test=engage.groupby('user_id')
# count=collections.Counter(engage['user_id'])
is_adopted = engage.groupby(['user_id']).size().to_frame('size').reset_index()
engage=engage[engage['user_id'].isin(is_adopted[is_adopted['size']>=3]['user_id'])]


