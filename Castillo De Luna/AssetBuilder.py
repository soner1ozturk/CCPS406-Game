import json
assets="assetText.json"

def load_data():
  with open(assets, 'r') as assetFile:
    data=json.load(assetFile)
  return data