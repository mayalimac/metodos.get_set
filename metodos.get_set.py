from funcionario import Funcionario

func = Funcionario ('Pedro','Lima', 30, 'Rua Crominia')
print(f'Nome: {func.get_nome()}')
print(f'Sobrenome: {func.get_sobrenome()}')
print(f'Idade: {func.get_idade()}')
print(f'Endereço: {func.get_endereço()}')

func.set_endereço('Rua Paraisopolis')
print(f'\n\nNovo endereço:{func.get_endereço()}')