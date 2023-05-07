from django.db import models

# Create your models here.

class Material(models.Model):
    cod = models.CharField(primary_key=True, max_length=3, help_text='Código do Material')
    descricao = models.CharField(max_length=50, help_text='Descrição do Material em Estoque')
    peso = models.DecimalField(max_digits=6, decimal_places=2, help_text='Peso do Material em Estoque em Kg')
    def __str__(self):
        return self.descricao

class Caixa(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now=True, auto_now_add=False)
    entrada = models.DecimalField(max_digits=6, decimal_places=2, help_text='Recebimento em R$')
    saida = models.DecimalField(max_digits=6, decimal_places=2, help_text='Pagamentos em R$')
    def __str__(self):
        return str(self.id)

class Coletor(models.Model):
    cpf = models.CharField(primary_key=True, max_length=11, help_text='CPF dos Coletores de Material Reciclado')
    nome = models.CharField(max_length=50, help_text='Nome do Coletor')
    sobrenome = models.CharField(max_length=50, help_text='Sobrenome do Coletor')
    pagamento = models.ForeignKey('Caixa',on_delete=models.PROTECT, default=1, help_text='Id da Transação')
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Compra(models.Model):
    material = models.ForeignKey('Material',on_delete=models.PROTECT, help_text='Código Material que Será Comprado')
    coletor = models.ForeignKey('Coletor',on_delete=models.PROTECT, help_text='CPF do Coletor')
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    peso = models.DecimalField(max_digits=4, decimal_places=2, help_text='Peso do Material Comprado Kg')
    prensado = models.DecimalField(max_digits=4, decimal_places=2, help_text='Peso do Material Prensado Kg')
    valor = models.DecimalField(max_digits=6, decimal_places=2, help_text='Valor Pago ao Coletor')
    def __str__(self):
        return str(self.id)

class Funcionario(models.Model):
    FUNCAO = (('v', 'Vendedor'), ('c', 'Comprador'), ('e', 'Estoquista'), ('g', 'Gestor'))
    cpf = models.CharField(primary_key=True, max_length=11, help_text='CPF dos Funcionarios')
    nome = models.CharField(max_length=50, help_text='Nome do Funcionario')
    sobrenome = models.CharField(max_length=50, help_text='Sobrenome do Funcionario')
    funcao = models.CharField(max_length=1, choices=FUNCAO, default='v', help_text='Função do Funcionario')
    pagamento = models.ForeignKey('Caixa',on_delete=models.PROTECT, default=1, help_text='Id da Transação')
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Cliente(models.Model):
    cnpj = models.CharField(primary_key=True, max_length=14, help_text='CNPJ do Cliente')
    razao_social = models.CharField(max_length=50, help_text='Razão Social do Cliente')
    nome_fantasia = models.CharField(max_length=50, help_text='Nome Fantasia do Cliente')
    pagamento = models.ForeignKey('Caixa',on_delete=models.PROTECT,default=1, help_text='Id da Transação')
    def __str__(self):
        return self.razao_social

class Venda(models.Model):
    cliente = models.ForeignKey('Cliente',on_delete=models.PROTECT, help_text='CNPJ do Cliente')
    material = models.ForeignKey('Material',on_delete=models.PROTECT, help_text='Código do Material')
    vendedor = models.ForeignKey('Funcionario',on_delete=models.PROTECT, help_text='CPF do Vendedor')
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, help_text='Peso do Material Comprado Kg')
    valor = models.DecimalField(max_digits=6, decimal_places=2, help_text='Valor Pago ao Coletor')
    def __str__(self):
        return str(self.id)

class Preco_compra(models.Model):
    cod = models.ForeignKey('Material',on_delete=models.PROTECT, help_text='Código Material que Será Comprado')
    data = models.DateField(auto_now=False, auto_now_add=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return str(self.cod)

class Preco_venda(models.Model):
    cod = models.ForeignKey('Material',on_delete=models.PROTECT, help_text='Código Material que Será Vendido')
    data = models.DateField(auto_now=False, auto_now_add=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return str(self.cod)
