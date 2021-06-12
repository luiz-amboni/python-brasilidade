# ------------------------------------------------------ #

# VALIDAÇÃO CPF/CNPJ #

# from cpf_cnpj import Documento
#
# exemplo_cnpj = "21647634000100"
# exemplo_cpf = "07387151903"
# documento = Documento.cria_documento(exemplo_cpf)
#
# print(documento)

# ------------------------------------------------------ #

# VALIDAÇÃO NÚMERO DE TELEFONE

# from TelefoneBr import TelefoneBr
#
# telefone = "554899175148"
#
# telefone_objeto = TelefoneBr(telefone)
# print(telefone_objeto)

# ------------------------------------------------------ #

from datas_br import DatasBr

cadastro = DatasBr()
print(cadastro)
print(cadastro.tempo_cadastro())
