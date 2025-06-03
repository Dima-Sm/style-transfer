import torch
from typing import Optional
from dataclasses import dataclass, field
from utils.st_strategies import StyleModelStrategy, VGG19Strategy 

@dataclass
class TransferConfig:
    steps: int = 300
    imsize: int = 512
    style_weight: float = 1e5
    content_weight: float = 1.0
    strategy: StyleModelStrategy = field(default_factory=VGG19Strategy)
    device: torch.device = field(default_factory=lambda:torch.device("cuda" if torch.cuda.is_available() else "cpu"))
    normalization_mean: Optional[torch.Tensor] = None
    normalization_std: Optional[torch.Tensor] = None

class TransferConfigBuilder:
    def __init__(self):
        self.config = TransferConfig()

    def with_steps(self, steps: int) -> 'TransferConfigBuilder':
        if steps is not None:
            if steps <= 0:
                raise ValueError("Steps must be positive")
            self.config.steps = steps
        return self
    
    def with_imsize(self, imsize: int) -> 'TransferConfigBuilder':
        if imsize is not None:
            if imsize <= 0:
                raise ValueError("Imsize must be positive")
            self.config.imsize = imsize
        return self

    def with_style_weight(self, weight: float) -> 'TransferConfigBuilder':
        if weight is not None:
            if weight <= 0:
                raise ValueError("Style weight must be positive")
            self.config.style_weight = weight
        return self

    def with_content_weight(self, weight: float) -> 'TransferConfigBuilder':
        if weight is not None:
            if weight <= 0:
                raise ValueError("Content weight must be positive")
            self.config.content_weight = weight
        return self

    def with_strategy(self, strategy: StyleModelStrategy) -> 'TransferConfigBuilder':
        self.config.strategy = strategy
        return self

    def with_device(self, device: torch.device) -> 'TransferConfigBuilder':
        self.config.device = device
        return self

    def with_normalization(self, mean: list[float], std: list[float]) -> 'TransferConfigBuilder':
        self.config.normalization_mean = torch.tensor(mean).to(self.config.device)
        self.config.normalization_std = torch.tensor(std).to(self.config.device)
        return self

    def build(self) -> TransferConfig:

        if self.config.normalization_mean is None:
            self.config.normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(self.config.device)
        if self.config.normalization_std is None:
            self.config.normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(self.config.device)
        return self.config