from validate_docbr import CPF

class ValidaCpf:
    def format_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()