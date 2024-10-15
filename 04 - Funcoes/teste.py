anos = (datetime.now() - data_nascimento).days // 365
meses = floor(((datetime.now() - data_nascimento).days / 365) * 12)
dias = (datetime.now() - data_nascimento).days
if anos == 1:
            return f'Voce tem: {anos} ano de idade, {meses} meses e {dias} dias vividos.'
else:
return f'Voce tem: {anos} anos de idade, {meses} meses e {dias} dias vividos.'


data_nascimento = datetime.strptime(
  input('Informe a data de nascimento (formato dd/mm/AAAA): '), "%d/%m/%Y")


print(calcula_idade(data_nascimento))


data_nascimento = datetime.strptime(
 input('Informe a data de nascimento (formato dd/mm/AAAA): '), "%d/%m/%Y")

print(calcula_idade(data_nascimento))