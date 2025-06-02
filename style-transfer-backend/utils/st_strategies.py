from abc import ABC, abstractmethod
from typing import List
import torchvision.models as models
import torch.nn as nn

class StyleModelStrategy(ABC):
    @abstractmethod
    def get_model(self) -> nn.Sequential:
        pass

    @abstractmethod
    def get_content_layers(self) -> List[str]:
        pass

    @abstractmethod
    def get_style_layers(self) -> List[str]:
        pass

class VGG19Strategy(StyleModelStrategy):
    def __init__(self, weights=models.VGG19_Weights.DEFAULT):
        self.weights=weights

    def get_model(self) -> nn.Sequential:
        return models.vgg19(weights=self.weights).features.eval()
    
    def get_content_layers(self) -> List[str]:
        return ['conv_4']  
    
    def get_style_layers(self) -> List[str]:
        return ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']  
    
    def name (self) -> str:
        return "VGG19"

class VGG16Strategy(StyleModelStrategy):
    def __init__(self, weights=models.VGG16_Weights.DEFAULT):
        self.weights=weights

    def get_model(self) -> nn.Sequential:
        return models.vgg16(weights=self.weights).features.eval()
    
    def get_content_layers(self) -> List[str]:
        return ['conv_3']
    
    def get_style_layers(self) -> List[str]:
        return ['conv_1', 'conv_2', 'conv_3', 'conv_4']
    
    def name (self) -> str:
        return "VGG16"

def get_strategy(name: str) -> StyleModelStrategy:
    
    name = name.lower()
    strategies = {
        "vgg19": VGG19Strategy,
        "vgg16": VGG16Strategy,
        # "resnet": ResNetStrategy, и т.д.
    }
    if name not in strategies:
        raise ValueError(f"Unknown model strategy: {name}")
    return strategies[name]()