import pickle

with open( modelseq + '.json', 'r') as f:
        model = model_from_json(f.read())