def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def words(someString):
  result = {}
  someList = someString.split()
  
  for i in someList:
    if representsInt(i):
      i = int(i)
    if i not in result:
      result[i] = 1
    else:
      result[i] += 1
      
  return result
  
