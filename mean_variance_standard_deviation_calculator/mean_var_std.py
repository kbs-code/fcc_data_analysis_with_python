import numpy as np

list = [0,1,2,3,4,5,6,7,8]

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  arr = np.array(list)
  reshaped = arr.reshape((3,3))
  calculations = {
      'mean' :  [
        np.mean(reshaped, axis=0).tolist(), 
        np.mean(reshaped, axis=1).tolist(), 
        np.mean(reshaped, axis=None).tolist()],
      'variance' : [
        np.var(reshaped, axis=0).tolist(),
        np.var(reshaped, axis=1).tolist(),
        np.var(reshaped, axis=None).tolist()],
      'standard deviation': [
        np.std(reshaped, axis=0).tolist(),
        np.std(reshaped, axis=1).tolist(),
        np.std(reshaped, axis=None).tolist()],
      'max': [
        np.max(reshaped, axis=0).tolist(),
        np.max(reshaped, axis=1).tolist(),
        np.max(reshaped, axis=None).tolist()],
      'min': [
        np.min(reshaped, axis=0).tolist(),
        np.min(reshaped, axis=1).tolist(),
        np.min(reshaped, axis=None).tolist()],
      'sum': [
        np.sum(reshaped, axis=0).tolist(),
        np.sum(reshaped, axis=1).tolist(),
        np.sum(reshaped, axis=None).tolist()]
  }
  return calculations