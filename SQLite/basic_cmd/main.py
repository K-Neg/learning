import sqlite3

while True:
    print(
        "Escolha uma opção:\n"
        "[1] incluir produto:\n"
        "[2] Alterar produto\n"
        "[3] Excluir produto\n"
        "[4] Localizar produto\n"
        "[5] Listar produto\n"
        "[6] Sair produto\n"
    )
    op = int(input())
    if op == 1:
        inserir_produtos()
    elif op == 2:
        alterar_produto()
    elif op == 3:
        excluir_produto()
    elif op == 4:
        localizar_produto()
    elif op == 5:
        consultar_produtos()
    elif op == 6:
        print("Saindo")
        break
    else:
        print("Escolha não existente")
