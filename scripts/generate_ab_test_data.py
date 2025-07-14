import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Simulation parameters
n_users = 1000
user_ids = [f"user_{i}" for i in range(n_users)]

# Distribute equally to group A/B
ab_groups = np.random.choice(['A', 'B'], size=n_users)

# Let's assume that the app has opened
app_open = pd.DataFrame({
    'user_id': user_ids,
    'event_name': 'app_open',
    'event_time': pd.date_range(start='2025-06-01', periods=n_users, freq='T'),
    'ab_group': ab_groups
})

# Purchase events: 10% of group A buys, 15% of group B buys
purchase_probs = np.where(ab_groups == 'A', 0.10, 0.15)
did_purchase = np.random.binomial(1, purchase_probs)

purchase = app_open[did_purchase == 1].copy()
purchase['event_name'] = 'purchase'
purchase['value'] = np.random.randint(5, 30, size=len(purchase))
purchase['event_time'] = purchase['event_time'] + timedelta(minutes=5)

# Merge
events_ab = pd.concat([app_open, purchase], ignore_index=True)
events_ab = events_ab[['user_id', 'event_name', 'event_time', 'ab_group', 'value']]
events_ab['value'] = events_ab['value'].fillna(0)

# Save
events_ab.to_csv('../data/events_ab.csv', index=False)
print("A/B test data was created: events_ab.csv")
