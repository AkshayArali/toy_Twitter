import random, csv, time
from datetime import datetime, timedelta

random.seed(42)

NUM_USERS = 200          # total users
NUM_TWEETS = 1500        # total tweets
IN_NET_SHARE = 0.50      # 50% in-network authors

# Define a target user and their in-network (followed) users
TARGET_USER = 0
IN_NET_USERS = set(range(1, 1 + int(NUM_USERS * 0.2)))  # 20% of users as follows
OUT_NET_USERS = set(range(1 + len(IN_NET_USERS), NUM_USERS))

# Assign authors: 50% from in-network, 50% from out-of-network
# Use random.choices to allow repetition (population < requested sample)
in_net_count = int(NUM_TWEETS * IN_NET_SHARE)
out_net_count = NUM_TWEETS - in_net_count
in_net_authors = random.choices(list(IN_NET_USERS), k=in_net_count)
out_net_authors = random.choices(list(OUT_NET_USERS), k=out_net_count)
authors = in_net_authors + out_net_authors
random.shuffle(authors)

# Generate tweets with timestamps
now = datetime.utcnow()
tweets = []
for tid, author in enumerate(authors, start=1):
    age_days = random.randint(0, 7)  # last week
    ts = now - timedelta(days=age_days, seconds=random.randint(0, 86400))
    tweets.append({
        "tweet_id": tid,
        "author_id": author,
        "created_at": ts.isoformat() + "Z",
        "text": f"Synthetic tweet {tid} by user {author}"
    })

# Generate engagements: likes/retweets/replies from random users
engagement_types = ["like", "retweet", "reply"]
engagements = []
for tw in tweets:
    # more likely engagements if in-network
    base_p = 0.6 if tw["author_id"] in IN_NET_USERS else 0.25
    num_eng = sum(random.random() < base_p for _ in range(5))  # up to ~5 Bernoulli trials
    engaged_users = random.sample(range(NUM_USERS), k=min(num_eng, NUM_USERS))
    for u in engaged_users:
        if u == tw["author_id"]:
            continue
        engagements.append({
            "tweet_id": tw["tweet_id"],
            "user_id": u,
            "engagement": random.choice(engagement_types),
            "timestamp": (now - timedelta(days=random.randint(0, 7),
                                          seconds=random.randint(0, 86400))).isoformat() + "Z"
        })

# Save to CSVs
with open("tweets.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["tweet_id", "author_id", "created_at", "text", "in_network"])
    w.writeheader()
    for tw in tweets:
        w.writerow({
            **tw,
            "in_network": int(tw["author_id"] in IN_NET_USERS)
        })

with open("engagements.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["tweet_id", "user_id", "engagement", "timestamp"])
    w.writeheader()
    w.writerows(engagements)

print("Done. tweets.csv and engagements.csv written.")