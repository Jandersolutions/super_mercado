import random
import csv
from faker import Faker
from datetime import datetime

fake = Faker("pt_BR")

# Solicitar informações do usuário
num_records = int(input("Digite a quantidade de registros a serem gerados: "))
mes = int(input("Digite o número do mês desejado: "))
ano = int(input("Digite o ano desejado: "))
num_cpf = int(input("Digite a quantidade de clientes: "))
num_op = int(input("Digite a quantidade de operadoras: "))
mes_ano = f"{mes:02d}-{ano:04d}"  # Usar hífen em vez de barra

# Dados para o dataset
start_hour = 8
end_hour = 22
product_dict = {
    "Arroz": 21.70,
    "Feijão": 15.50,
    "Açúcar": 25.50,
    "Óleo de cozinha": 8.90,
    "Farinha": 2.70,
    "Sabonete": 3.50,
    "File de frango": 19.20,
    "Sal": 2.30,
    "Ovos": 18.20,
    "Cafe": 9.50,
    "Detergente liquido": 2.50,
    "Esponja de aço": 5.50,
    "Escova dental": 15.50,
    "Tomate": 8.20,
    "Cenoura": 7.10,
    "Morango": 7.50,
    "Gelatina": 2.40,
    "Refrigerante lata": 4.70,
    "Cerveja": 7.50,
    "Vinho": 17.70,
    "Picanha": 50.40,
    "Alcatra": 45.70,
    "Linguiça frango": 9.70,
    # ... Adicione mais produtos aqui
}
operators = [fake.first_name_female() for _ in range(num_op)]
operations = ["pix", "cartão_credito", "cartão_debito", "dinheiro"]

# Variáveis de controle
min_cpf_percentage = 0.05
max_cpf_percentage = 0.3

# Calcula a quantidade de CPFs com base na porcentagem definida
min_cpf = int(num_cpf * min_cpf_percentage)
max_cpf = int(num_cpf * max_cpf_percentage)
num_cpfs = random.randint(min_cpf, max_cpf)

# Gera CPFs aleatórios
all_cpfs = [fake.cpf() for _ in range(num_cpfs)]

# Gera os registros do dataset
dataset = []
for _ in range(num_records):
    cpf = random.choice(all_cpfs)
    hora = f"{random.randint(start_hour, end_hour):02d}:{random.randint(0, 59):02d}"  # Formatação da hora
    dia = random.randint(1, 30)
    data = datetime(year=ano, month=mes, day=dia).strftime("%d/%m/%Y")
    produto = random.choice(list(product_dict.keys()))
    preço = product_dict[produto]
    quantidade = random.randint(1, 10)
    pdv = random.randint(1, 21)
    operadora = random.choice(operators)
    operação = random.choice(operations)
    total = round(preço * quantidade, 2)
    dataset.append([cpf, hora, data, produto, preço, quantidade, pdv, operadora, operação, total])

# Escreve os registros no arquivo CSV
filename = f"venda_{mes_ano}.csv"
with open(filename, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["cpf", "hora", "data", "produto", "preço", "quantidade", "pdv","operadora", "operação", "total"])
    csvwriter.writerows(dataset)

print(f"Dataset gerado e salvo como {filename}")
