import catboost as cb
import pandas as pd
import numpy as np

from flask import Flask, jsonify, request

# Load the model
model = cb.CatBoostClassifier()
model.load_model("catboost_model_2023-10-18_raw_cat.dump")

# Init the app
app = Flask("default")

def preparation_data_for_catboost (df):
  df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
  selected_columns = ['bwd_psh_flags', 'bwd_urg_flags', 'fwd_avg_bytes/bulk',
       'fwd_avg_packets/bulk', 'fwd_avg_bulk_rate', 'bwd_avg_bytes/bulk',
       'bwd_avg_packets/bulk', 'bwd_avg_bulk_rate']
  df.drop(columns=selected_columns, inplace=True)
  max_value_flow_bytes_s = 1035500000
  max_value_flow_packets_s = 3000000
  df['flow_bytes/s'].replace([np.inf , -np.inf ], 2 * max_value_flow_bytes_s, inplace= True )
  df['flow_packets/s'].replace([np.inf , -np.inf ], 2 * max_value_flow_packets_s, inplace= True )
  return df

# Setup prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # Get the provided JSON
    X = request.get_json()
    # Perform a prediction
    X = pd.DataFrame(X, index=[0])
    X = preparation_data_for_catboost (X)

    preds = model.predict(X)
    print(preds[0][0])
    # Output json with prediction
    result = {"answer": preds[0][0]}
    return jsonify(result)


if __name__ == "__main__":
    # Run the app on local host and port 8989
    app.run(debug=True, host="0.0.0.0", port=8989)
