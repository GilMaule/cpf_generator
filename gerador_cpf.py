import random
import os

os.system('cls')
"""Gera os 9 digitos do cpf"""
def gerar_cpf_base():

  return ''.join(str(random.randint(0,9))for _ in range(9))


"""Calcula os digitos verificadores do cpf"""
def calculo_digito(cpf_parcial, peso_inicial):
  soma = 0
  peso = peso_inicial

  for digito in cpf_parcial:
    soma +=int(digito) * peso
    peso -=1

  resto = 11 - (soma% 11)
  return 0 if resto > 9 else resto

"""Gerar um cpf valido"""
def gerar_cpf():
  while True:
    cpf_base = gerar_cpf_base()

    primeiro_dv = calculo_digito(cpf_base, 10)
    cpf_com_primeiro_dv =cpf_base + str(primeiro_dv)

    segundo_dv = calculo_digito(cpf_com_primeiro_dv, 11)
    cpf = cpf_com_primeiro_dv + str(segundo_dv)

    return cpf

def formatar_cpf(cpf):
  return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

cpf_gerado = gerar_cpf()
cpf_formatado = formatar_cpf(cpf_gerado)

print(cpf_formatado)
print('CPF válido')