import json
import sys

class TraitementJson:
    def __init__(self, fileName):
        self.fileName = fileName

    def upjson(self, bouton_ID):
        try:
            a_file = open(self.fileName, "r")
            json_object = json.load(a_file)
            a_file.close()
            json_object[bouton_ID]['clicks'] = json_object[bouton_ID]['clicks'] + 1
            a_file = open(self.fileName, "w")
            json.dump(json_object, a_file)
            a_file.close()
        except Exception as e:
            print(e)
            sys.exit(1)
