import numpy as np
import datetime
from utils import Trade

def front_running_score(trades):
  """
  Calculates a score for each trade that indicates the likelihood of front-running.

  Args:
    trades: A list of trades.

  Returns:
    A list of scores, one for each trade.
  """

  # Calculate the time difference between each trade and the previous trade.
  time_deltas = [trades[i].timestamp - trades[i - 1].timestamp for i in range(1, len(trades))]

  # Calculate the average time difference between trades.
  average_time_delta = np.mean(time_deltas)

  # Calculate the score for each trade.
  scores = [
      time_delta / average_time_delta
      for time_delta in time_deltas
  ]

  return scores


# Sample trade data
trade_data = [
    Trade(datetime.datetime(2023, 5, 20, 9, 0, 0)),
    Trade(datetime.datetime(2023, 5, 20, 10, 15, 16)),
    Trade(datetime.datetime(2023, 5, 20, 11, 47, 8)),
    Trade(datetime.datetime(2023, 5, 20, 13, 3, 45)),
    Trade(datetime.datetime(2023, 5, 20, 18, 4, 15)),
    Trade(datetime.datetime(2023, 5, 20, 18, 5, 0)),
    Trade(datetime.datetime(2023, 5, 20, 18, 5, 35)),
    Trade(datetime.datetime(2023, 5, 20, 18, 6, 10)),
    Trade(datetime.datetime(2023, 5, 20, 18, 6, 23)),
    Trade(datetime.datetime(2023, 5, 20, 18, 6, 51))
]

# Test the front_running_score function
scores = front_running_score(trade_data)

# Print the trades and their corresponding scores
for trade, score in zip(trade_data[1:], scores):
    print(f"Trade: {trade.timestamp}, Score: {score}")
 