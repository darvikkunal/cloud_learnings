'''
import json
import pandas as pd

def lambda_handler(event, context):

    d = {"column1" : ["a", "b", "c"], "column2": [1,2,3]}
    df = pd.DataFrame(data=d)
    print(df)
    print(f"The version of pandas is = {pd.__version__}")
    return{
        "statusCode": 200,
        "body": json.dumps({
            "message": "pandas successfully imported",
        }),
    }
'''