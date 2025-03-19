import torch
import train

def main():
    opt = train.parse_opt()
    # Override torch.load to disable weights_only
    original_load = torch.load
    torch.load = lambda *args, **kwargs: original_load(*args, **kwargs, weights_only=False)
    train.main(opt)

if __name__ == '__main__':
    main() 