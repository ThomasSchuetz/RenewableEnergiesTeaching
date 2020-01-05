import sys
import json
import numpy as np

if len(sys.argv) < 2:
    print("Transform a given CSV file to JSON format.")
    print("Usage: python to_json.py MY_FILENAME.csv")
    print("Will create a new file named MY_FILENAME.json")
else:
    filename = sys.argv[1]
    if not ".csv" in filename:
        print("Please provide a valid CSV file as input")
    else:

        json_file = filename.replace(".csv", ".js")

        data = np.loadtxt(filename, delimiter=";", skiprows=1, usecols=(3,))

        with open(json_file, "w") as fout:
            fout.write("var " + json_file.split(".")[0] + " = " + json.dumps(data.tolist()) + ";")