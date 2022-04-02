import math

def sell_out(list):
  running_total = 0
  for item in list:
    running_total += item.net() * item.stock
  return f'Your sell-out payout is ${round(running_total, 2)}.'

def challenge(list, profit):
  def iteration(same_list):
    iteration_total = 0
    for item in same_list:
      iteration_total += item.net() * math.ceil(item.stock * 0.1)
    return iteration_total
  num_of_iterations = (profit + 100) / iteration(list)
  return f'You\'ll need to sell {round(num_of_iterations * 10, 2)}% of your stock to earn the desired profit'