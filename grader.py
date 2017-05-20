""""Grader.

Best practices xcthulu & others

def grader(x):
  if 0.9 <= x <= 1: return "A"
  elif 0.8 <= x < 0.9: return "B"
  elif 0.7 <= x < 0.8: return "C"
  elif 0.6 <= x < 0.7: return "D"
  else: return "F"
"""


def grader(score):
    if score < 0.6 or score > 1:
        return 'F'
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return score