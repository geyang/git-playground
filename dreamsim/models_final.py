import torch.nn as nn

class MLP(nn.Sequential):
    def __init__():
        super().__init__(
            nn.Linear(10, 200),
            nn.Sin(),
            nn.Linear(200, 200),
            nn.Sin(),
            nn.Linear(200, 200),
            nn.Sin(),
            nn.Linear(200, 10),
        )



