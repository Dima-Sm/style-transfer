import torch
from utils.style_transfer import run_style_transfer
from st_config import TransferConfig

class StyleTransferFacade:
    def __init__(self, config: TransferConfig):
        self.config = config
        self.strategy = config.strategy
        self.device = config.device 
        
    def transfer_style(self, 
                       content_img: torch.Tensor, 
                       style_img: torch.Tensor):
        
        model = self.strategy.get_model().to(self.device)

        normalization_mean = self.config.normalization_mean
        normalization_std = self.config.normalization_std
        
        output_img = run_style_transfer(
            cnn=model,
            content_img=content_img,
            style_img=style_img,
            input_img=content_img.clone(),
            normalization_mean=normalization_mean,
            normalization_std=normalization_std,
            num_steps=self.config.steps,
            style_weight=self.config.style_weight,
            content_weight=self.config.content_weight,
            content_layers=self.strategy.get_content_layers(),
            style_layers=self.strategy.get_style_layers(),
        )
        
        return output_img