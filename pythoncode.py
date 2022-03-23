from flask import *
import json, time
import os
import pandas as pd
from configparser import ConfigParser
from tkinter import filedialog

try:

    config = ConfigParser()
    config.read('api_config.ini')
    smwlocation = config['apis']['sMWmasterlist']


    # START : Code by Arun
    Jsonfiles_FolderPath = filedialog.askdirectory()  # Select folder path with all json files
    ResultsList = list()
    for file in os.listdir(Jsonfiles_FolderPath):   # Loop through Json files for data and files names
        FilePath = str(os.path.join(Jsonfiles_FolderPath,str(file)))
        File = open (FilePath, "r")
        if file.endswith(".json"):
            ResultsList.append({"results": json.loads(File.read()), "filename": str(file) }) # Store files data

    '''
    JsonData = json.dumps(ResultsList)      # Convert whole data in List to json format
    JsonData = json.dumps(ResultsList[0])   # Convert 1st data in List to json format
    print(JsonData["results"])              # Access results of 1st Data
    print(JsonData["filename"])             # Access filename of 1st Data
    '''

    print(ResultsList)

    # END : Code by Arun
    dataToSend = json.dumps(ResultsList)


    smwmasterlist_csv_file = fr"{smwlocation}"
    sMWmasterlist_read = pd.read_csv(smwmasterlist_csv_file)


    omlo33_csv_file = r"/Users/johnlee/Desktop/Testing/Alinity_MW/Archive/Archive_20220129/aMW/a0_storg/A7_OMLO33/OMLO33.csv"
    omlo33_read = pd.read_csv(omlo33_csv_file )



    json_output = r"/Users/johnlee/Desktop/sMWmasterlist_UAT.json"
    smwoutput = sMWmasterlist_read.to_json(indent = 1, orient = 'records')
    omlo33output = omlo33_read.to_json(indent = 1, orient = 'records')



    # app = Flask(__name__)
    #
    # @app.route('/', methods=['GET'])
    #
    # def home_page():
    #     data_set = {'Page': 'Home', 'Message': 'Successfully loaded home page', 'Timestamp': time.time()}
    #     json_dump = json.dumps(data_set)
    #
    #     return json_dump
    #
    # @app.route('/smwResults', methods=['POST'])
    #
    # def smwmasterlist_results():
    #     # data_set = {'Page': 'smwResults', 'Message': 'Successfully loaded home page', 'Timestamp': time.time()}
    #     # json_dump = json.dumps(output)
    #     return smwoutput
    #
    # @app.route('/omlo33Results', methods=['GET'])
    #
    # def omlo33_results():
    #     return omlo33output
    #
    #
    #
    # if __name__ == '__main__':
    #     app.run(port=7777)


except Exception as error :
    print("Error Occurred : " ,error )