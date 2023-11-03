import numpy as np

list = [0,1,2,3,4,5,6,7,8]

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  
  arr = np.array(list).reshape((3,3))
  
  operations = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
  np_operations = [np.mean, np.var, np.std, np.max, np.min, np.sum]
  
  calculations = {}
  
  for operation, np_operation in zip(operations, np_operations):
    calculations[operation] = [
      np_operation(arr, axis=0).tolist(),
      np_operation(arr, axis=1).tolist(),
      np_operation(arr, axis=None).tolist()
    ]
  
  return calculations