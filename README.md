# Toy Twitter Recommendation Engine

A simplified implementation of Twitter's recommendation algorithm pipeline built on synthetic data. This project demonstrates core concepts including bipartite graph construction, random walks (SALSA-style), and feature-based tweet scoring.

## Overview

This toy recommender mimics the high-level Twitter recommendation pipeline:

1. **Load Data**: Parse synthetic tweets and user engagements
2. **Build Graph**: Create a bipartite graph (users ↔ tweets) with engagement weights
3. **Random Walks**: Run SALSA-style random walks from a target user's recent engagements
4. **Score & Rank**: Rank tweets using walk scores, recency, and followed-author bonuses
5. **Output**: Write top-K recommendations to CSV

## Installation

### Requirements
- Python 3.9+
- pandas >= 1.5.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- networkx >= 3.0
- jupyter >= 1.0.0

### Setup

```bash
pip install -r requirements.txt
```

Or use Docker:

```bash
docker build -t toy-twitter .
docker run -p 8888:8888 toy-twitter
```

## Usage

### Generate Synthetic Data
```bash
python3 synthetic_tweets.py
```

### Generate Recommendations
```bash
python3 recommend.py --target_user 0 --top_k 50
```

**Arguments:**
- `--target_user`: User ID to generate recommendations for (default: 0)
- `--top_k`: Number of recommendations to return (default: 50)
- `--num_walks`: Number of random walks (default: 300)
- `--max_len`: Maximum walk length (default: 4)
- `--reset_p`: Reset probability for SALSA walks (default: 0.15)

### Explore Interactively
```bash
jupyter notebook demo.ipynb
```

## Project Structure

- `synthetic_tweets.py`: Generate synthetic tweet and engagement data
- `recommend.py`: Main recommendation engine
- `demo.ipynb`: Interactive Jupyter notebook for exploration
- `tweets.csv`: Tweet metadata (auto-generated)
- `engagements.csv`: User engagement data (auto-generated)
- `toy_recs.csv`: Output recommendations

## Features

- Bipartite graph-based recommendations
- SALSA-style random walk scoring
- Recency weighting
- In-network author bonuses
- Configurable walk parameters

## License

MIT
