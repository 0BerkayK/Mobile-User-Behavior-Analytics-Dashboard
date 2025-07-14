import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta
import os

# Constants

NUM_USERS = 1000
START_DATE = datetime(2024, 1, 1)
COUNTRIES = ['US', 'UK', 'DE', 'TR']
PLATFORMS = ['iOS', 'Android']
CAMPAIGNS = [
    {'campaign_id': 'C01', 'channel': 'Facebook Ads', 'cost': 1200, 'start_date': '2024-01-01'},
    {'campaign_id': 'C02', 'channel': 'Google Ads', 'cost': 950, 'start_date': '2024-01-15'},
    {'campaign_id': 'C03', 'channel': 'TikTok Ads', 'cost': 700, 'start_date': '2024-02-01'}
]

EVENT_TYPES = ['app_open', 'level_complete', 'purchase']

# Indexing
os.makedirs('../data', exist_ok=True)

# Campaigns
campaigns_df = pd.DataFrame(CAMPAIGNS)
campaigns_df.to_csv('../data/campaigns.csv', index=False)

# Users
users = []
for i in range(NUM_USERS):
    user_id = f"U{i+1:04d}"
    signup_date = START_DATE + timedelta(days=random.randint(0, 60))
    country = random.choice(COUNTRIES)
    platform = random.choice(PLATFORMS)
    campaign = random.choice(CAMPAIGNS)['campaign_id']
    users.append([user_id, signup_date.strftime("%Y-%m-%d"), country, platform, campaign])

users_df = pd.DataFrame(users, columns=['user_id', 'signup_date', 'country', 'platform', 'campaign_id'])
users_df.to_csv('../data/users.csv', index=False)

# Events
events = []
for _, row in users_df.iterrows():
    user_id = row['user_id']
    signup = datetime.strptime(row['signup_date'], "%Y-%m-%d")
    num_events = random.randint(3, 10)
    for _ in range(num_events):
        event_time = signup + timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
        event_name = random.choices(EVENT_TYPES, weights=[0.5, 0.3, 0.2])[0]
        value = round(random.uniform(0.99, 19.99), 2) if event_name == 'purchase' else 0
        events.append([user_id, event_name, event_time.strftime("%Y-%m-%d %H:%M:%S"), value])

events_df = pd.DataFrame(events, columns=['user_id', 'event_name', 'event_time', 'value'])
events_df.to_csv('../data/events.csv', index=False)

print("Simulation data was created: users.csv, events.csv, campaigns.csv")
