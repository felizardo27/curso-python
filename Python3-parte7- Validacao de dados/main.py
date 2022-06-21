from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

# objeto_cpf = Cpf(49820387833)
# print(objeto_cpf)

cnpj = 63537056000108
objeto_cnpj = CpfCnpj(cnpj, 'cnpj')
print(objeto_cnpj)

cpf = 25863868090
objeto_cpf = CpfCnpj(cpf, 'cpf')
print(objeto_cpf)