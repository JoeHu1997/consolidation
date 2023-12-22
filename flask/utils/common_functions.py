#建立共同函數

def convert_to_int(value_str):
    try:
       return int(value_str) if value_str is not None else None
    except ValueError:
        return None

def calculate_poreparameters(e, Gs, w, S):
    parameters = [e, Gs, w, S]
    provided_params = ['e', 'Gs', 'w', 'S']

    for param_name, param_value in zip(provided_params, parameters):
        if param_value is None or param_value == "":
            if param_name == 'e':
                e = Gs * w / S
                print(1)
            elif param_name == 'Gs':
                Gs = S * e / w
                print(2)
            elif param_name == 'w':
                w = S * e / Gs
                print(3)
            else:
                S = Gs * w / e
                print(4)
    return e, Gs, w, S
def calculate_gammamparameters(gammam, Gs, w, e):
    parameters = [gammam, Gs, w, e]
    provided_params = ['gammam', 'Gs', 'w', 'e']
#gammam = Gs* gammaw*(1+w)/(1+e)  
    gammaw = 1000
    for param_name, param_value in zip(provided_params, parameters):
        
        if param_value is None or param_value == "":
            if param_name == 'e':
                e = (Gs* gammaw*(1+w)/gammam)-1
                print(1)
            elif param_name == 'gammam':
                gammam = Gs* gammaw*(1+w)/(1+e)  
                print(2)
            elif param_name == 'w':
                w = (gammam*(1+e)/(Gs*gammaw))-1
                print(3)
            else:
                Gs = gammam/(gammaw*(1+w)/(1+e))
                print(4)

    return gammam, Gs, w, e

def calculate_gammadparameters(gammad, Gs, e):
    parameters = [gammad, Gs, e]
    provided_params = ['gammad', 'Gs', 'e']
    #gammad = Gs* gammaw/(1+e)
    for param_name, param_value in zip(provided_params, parameters):
        gammaw = 1000
        if param_value is None or param_value == "":
            if param_name == 'e':
                e = (Gs* gammaw/gammad)-1
                print(1)
            elif param_name == 'gammad':
                gammad = Gs* gammaw/(1+e)  
                print(2)
            elif param_name == 'Gs':
                Gs = gammad/(gammaw/(1+e))
                print(3)
            
    return gammad, Gs, e