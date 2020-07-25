import torch

# Verifica se o CUDA está presente no respectivo computador. Caso sim atribui ao devide. Caso não atribui o cpu, apresentando uma mensagem ao usuário
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)