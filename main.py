from cpf_cnpj import Documento

exemplo_cnpj = "21647634000100"
exemplo_cpf = "07387151903"
documento = Documento.cria_documento(exemplo_cpf)

print(documento)