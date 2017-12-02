def dictator(keys, values):
  """
  DOCUMENTATION DOWN BELOW
  Функция, которая создаёт словарь ключей и значений из списков разной длины.

  Если ключу не хватило значения, то присваивается значение None. 

  Значения, которым не хватило ключей, игнорируются.
  """
  assert(type(keys) == list), "keys-argument is not a list"
  assert(type(values) == list), "values-argument is not a list"
  
  res = dict.fromkeys(keys, None)
  
  for i, k in enumerate(keys):
    if i < len(values):
      res.update({k : values[i]})
    else:
      break
  
  return res

#ASSERTIONS  
#if __name__ == "__main__":
  #assert(dictator([1], ['haha']) == {1:'haha'})
  #assert(dictator([], []) == {})
  #assert(dictator([1,2], []) == {1:None,2:None})
  #assert(dictator([1,2,3,4], ['a','b']) == {1:'a',2:'b',3:None,4:None})
  #assert(dictator([1,2], ['w','o','w']) == {1:'w',2:'o'})


#EXAMPLES  
#print('\n',dictator([1, 2, 3, 4, 6], ['m','e','o','w'])) # {1: 'm', 2: 'e', 3: 'o', 4: 'w', 6: None}
#print('\n',dictator(['k','e','y'],['v','a','l','u','e'])) # {'k': 'v', 'e': 'a', 'y': 'l'}
#print('\n',dictator(['k','e','y','s'],['v','a','l']),'\n') # {'k': 'v', 'e': 'a', 'y': 'l', 's': None}