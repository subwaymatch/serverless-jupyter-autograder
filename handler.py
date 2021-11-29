try:
  import unzip_requirements
except ImportError:
  pass

import json
import pandas as pd
import numpy as np
import plotly
import statsmodels

def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
        "pandas_version": pd.__version__,
        "numpy_version": np.__version__,
        "plotly_version": plotly.__version__,
        "statsmodels_version": statsmodels.__version__
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """