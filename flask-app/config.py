import json
import torch

with open('resources/config.json') as f:
    configs = json.load(f)

model_state = torch.load('resources/nn_model', map_location=torch.device('cpu'))
