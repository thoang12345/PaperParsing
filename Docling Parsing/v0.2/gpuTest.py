import torch
import torch.nn as nn

conv = nn.Conv2d(3, 16, 3, padding=1).cuda()
x = torch.randn(1, 3, 224, 224, device="cuda")
conv(x)

print("Success")