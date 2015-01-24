class FizzBuzz:

  def fizzbuzz(self, value):
    if type(value) is int:
      if(value % 15 == 0):
        return 'Fizzbuzz'
      elif(value % 3 == 0):
        return 'Fizz'
      elif(value % 5 == 0):
        return 'Buzz'
      else:
        return int(value)
    else:
      raise TypeError('This method only handles integers.')

