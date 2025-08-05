'''
Atividade 8 

Ana está cadastrando clientes em um sistema. Para seguir com o cadastro,
o CPF precisa ter exatamente 11 dígitos numéricos.

Crie uma função cpf_valido(cpf) que recebe uma string e retorna se o CPF é
válido ou não (apenas pela contagem de dígitos e se são numéricos).

'''
print("=== Verificação de CPF ===\n")

def cpf_valido(cpf):
    
    if len(cpf) == 11 and cpf.isdigit():
        print(f"Seu CPF é {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    else:
        print("CPF inválido!")

pessoa = input("Digite seu CPF: ")
cpf_valido(pessoa)