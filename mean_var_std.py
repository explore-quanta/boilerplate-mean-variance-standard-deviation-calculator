import numpy as np

def calculate(list):
    if len(list) == 9:
        list = np.array(list).reshape(-1, 3, 1)
        calculations = {'mean': [np.mean(list, axis=0).flatten().tolist(), 
                                np.mean(list, axis = 1).flatten().tolist(), 
                                np.mean(list).item()],
                        'variance':  [np.var(list, axis = 0).flatten().tolist(),
                                     np.var(list, axis = 1).flatten().tolist(),
                                     np.var(list).item()],
                        'standard deviation': [np.std(list, axis = 0).flatten().tolist(),
                                              np.std(list, axis = 1).flatten().tolist(),
                                              np.std(list).item()],    
                        'max': [np.max(list, axis = 0).flatten().tolist(),
                               np.max(list, axis = 1).flatten().tolist(),
                               np.max(list).item()],   
                        'min': [np.min(list, axis = 0).flatten().tolist(),
                               np.min(list, axis = 1).flatten().tolist(),
                               np.min(list).item()], 
                        'sum': [np.sum(list, axis = 0).flatten().tolist(),
                                np.sum(list, axis = 1).flatten().tolist(),
                                np.sum(list).item()] 
                    }
        return calculations
    else:
        raise ValueError("List must contain nine numbers.")
    