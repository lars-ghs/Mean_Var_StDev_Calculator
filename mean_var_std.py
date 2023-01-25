import numpy as np

def calculate(list_1):

  # needs 9 digits: 
  if len(list_1) != 9:
    raise ValueError("List must contain nine numbers.")

  # convert to array, and convert 1D to 2D array: 
  mat = np.array(list_1).reshape((3,3))
  
  # create dict: 
  calculations = dict()

  # mean: 
  calculations['mean'] = [
        np.mean(mat,axis=0).tolist(),
        np.mean(mat,axis=1).tolist(),
        np.mean(mat).tolist()
    ]

  # variance: 
  calculations['variance'] = [
        np.var(mat,axis=0).tolist(),
        np.var(mat,axis=1).tolist(),
        np.var(mat).tolist()
    ]

  # standard dev: 
  calculations['standard deviation'] = [
        np.std(mat,axis=0).tolist(),
        np.std(mat,axis=1).tolist(),
        np.std(mat).tolist()
    ]

  # maximum values: 
  calculations['max'] = [
        np.max(mat,axis=0).tolist(),
        np.max(mat,axis=1).tolist(),
        np.max(mat).tolist()
    ]

  # minimum values: 
  calculations['min'] = [
        np.min(mat,axis=0).tolist(),
        np.min(mat,axis=1).tolist(),
        np.min(mat).tolist()
    ]

  # sum: 
  calculations['sum'] = [
        np.sum(mat,axis=0).tolist(),
        np.sum(mat,axis=1).tolist(),
        np.sum(mat).tolist()
    ]


  return calculations