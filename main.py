import argparse

from style_transfer import get_device, get_vgg19, run_style_transfer
from image_preparation import get_content_image_size, image_loader, save_image

def main():

    parser = argparse.ArgumentParser(description='Neural Style Transfer')

    parser.add_argument('--content', type=str, required=True, help='Path to content image')
    parser.add_argument('--style', type=str, required=True, help='Path to style image')
    parser.add_argument('--output', type=str, default='output/input.jpg' ,help='Path to save stylized image')
    parser.add_argument('--steps', type=int, default=500, help='Number of optimization steps')
    parser.add_argument('--style-weight', type=float, default=1e5, help='Style weight')
    parser.add_argument('--content-weight', type=float, default=1, help='Content weight')
    parser.add_argument('--imsize', type=int, default=512, help='Size of images used for training (imsize * imsize)')

    args = parser.parse_args()

    width, height = get_content_image_size(args.content)

    device = get_device()

    content_img = image_loader(args.content, args.imsize, device)
    style_img = image_loader(args.style, args.imsize, device)
    input_img = image_loader(args.output, args.imsize, device)

    cnn = get_vgg19()

    output = run_style_transfer(cnn, content_img, style_img, input_img,
                                num_steps=args.steps,
                                style_weight=args.style_weight,
                                content_weight=args.content_weight) 

    save_image(output, width, height, args.output)
    print(f"[INFO] Стилизованное изображение сохранено в: {args.output}") 
    
if __name__ == "__main__":
    main()