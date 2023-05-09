import pandas as pd
import json


def main():
    df = pd.read_csv(r'../DSS_W23_Wilford_Woodruff_Papers/{file_link}')
    df_json = csv_to_json(df)
    csv_json = csv_to_json(r'../DSS_W23_Wilford_Woodruff_Papers/{file_link}')



    name_json = input("Put what you want the json file to be called here:\n")
    with open(r"../DSS_W23_Wilford_Woodruff_Papers/notebook/main.json", "w") as outfile:
        json.dump(csv_json, outfile)


def csv_to_json(csv_file):
    if isinstance(csv_file, str):
        df = pd.read_csv(csv_file)
    elif isinstance(csv_file, pd.DataFrame):
        df = csv_file
    else:
        raise ValueError("csv_file must be a string or a pandas DataFrame.")

    
    json_data = df.to_json(orient="records")

    
    json_list = json.loads(json_data)

    
    return json_list



if __name__ == '__main__':
    main()