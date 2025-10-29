import pandas as pd 

def get_data_from_file(file):
    if not file.filename.endswith('.xlsx'):
        return None

    df = pd.read_excel(file)
    data = df.to_dict(orient='records')
    
    return data
    