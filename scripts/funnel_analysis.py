import pandas as pd

# Read data
users = pd.read_csv('../data/users.csv', parse_dates=['signup_date'])
events = pd.read_csv('../data/events.csv', parse_dates=['event_time'])

# First, what events did each user perform?
pivot = events.pivot_table(
    index='user_id',
    columns='event_name',
    values='event_time',
    aggfunc='min'  # First time
)

# Let's count the stages that users have reached in the funnel.
funnel_steps = ['app_open', 'level_complete', 'purchase']
funnel_counts = []

for i, step in enumerate(funnel_steps):
    required_steps = funnel_steps[:i+1]
    users_in_step = pivot.dropna(subset=required_steps).shape[0]
    funnel_counts.append({'step': step, 'users': users_in_step})

funnel_df = pd.DataFrame(funnel_counts)

# Conversion rate
funnel_df['conversion_rate'] = funnel_df['users'] / funnel_df['users'].iloc[0]

# Save
funnel_df.to_csv('../data/funnel_analysis.csv', index=False)

print("Funnel analysis completed. Funnel_analysis.csv file created.")
