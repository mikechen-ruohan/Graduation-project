import torch

# 加载模型
model = torch.load('model1.pt', map_location=torch.device('cpu'))

# 打印模型结构
print(model)