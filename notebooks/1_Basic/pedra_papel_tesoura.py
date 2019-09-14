# -*- coding: utf-8 -*-
""" Created on Fri Sep 13 22:16:26 2019
    @author: kaw """

import random 

# Mostra instruções
print("Regras do jogo Pedra, papel e tesoura: \n"
	  + "Pedra X Papel   -> Papel vence\n"
	  + "Pedra X Tesoura -> Pedra vence\n"
  	  + "Papel X Tesoura -> Tesoura vence\n") 

while True: 
	print("Escolha:\n 1. Pedra\n 2. Papel\n 3. Tesoura\n") 
	escolha = int(input("Usuário: ")) 

	while escolha > 3 or escolha < 1: 
		escolha = int(input("Escolha um objeto válido: ")) 
	if escolha == 1: 
		objeto_escolhido = 'Pedra'
	elif escolha == 2: 
		objeto_escolhido = 'Papel'
	else: 
		objeto_escolhido = 'Tesoura'
		
	print("Escolha do usuário: " + objeto_escolhido) 
	print("\nAgora eu escolho...") 

	# Computador escolhe randomicamente um número
	# entre 1 , 2 e 3. Usando o método 'randint' do módulo 'random'
	escolha_comp = random.randint(1, 3) 
	
	# busca nova escolha se o objeto escolhido pelo computador
	# for o mesmo escolhido pelo usuário
	while escolha_comp == escolha: 
		escolha_comp = random.randint(1, 3) 

	if escolha_comp == 1: 
		objeto_escolhido_comp = 'Pedra'
	elif escolha_comp == 2: 
		objeto_escolhido_comp = 'Papel'
	else: 
		objeto_escolhido_comp = 'Tesoura'
		
	print("Escolha do computador: " + objeto_escolhido_comp) 
	print(objeto_escolhido + " X " + objeto_escolhido_comp) 

	if((escolha == 1 and escolha_comp == 2) or
	   (escolha == 2 and escolha_comp == 1)): 
		print("Papel vence => ", end = "") 
		result = "Papel"
	elif((escolha == 1 and escolha_comp == 3) or
	   (escolha == 3 and escolha_comp == 1)): 
		print("Pedra vence => ", end = "") 
		result = "Pedra"
	else: 
		print("Tesoura vence => ", end = "") 
		result = "Tesoura"

	if result == objeto_escolhido: 
		print(">>> Usuário venceu <<<") 
	else: 
		print(">>> Computador venceu <<<") 
		
#	print() 
	resp = input("\n\nQuer jogar novamente? ( /N) ") 
	if resp == 'n' or resp == 'N': 
		break
	
print("\nObrigado por jogar!") 
