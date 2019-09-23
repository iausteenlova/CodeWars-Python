

# >> Even or Odd



def even_or_odd(number):
  return 'Odd' if number % 2 else 'Even'



def even_or_odd(number):
  return 'Even' if number % 2 == 0 else 'Odd'




def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"




def even_or_odd1(number):
  return ["Even", "Odd"][number % 2]




def even_or_odd(number):
  # number % 2 will return 0 for even numbers and 1 for odd ones.
  # 0 evaluates to False and 1 to True, so we can do it with one line
  return "Odd" if number % 2 else "Even"




#Lambda function
even_or_odd = lambda number: "Odd" if number % 2 else "Even"




def even_or_odd(number):
  if number%2 == 0: return 'Even'
  return 'Odd'





def even_or_odd2(number):
  return number % 2 and 'Odd' or 'Even'


