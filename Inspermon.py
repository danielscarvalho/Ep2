import random
insperdex={"Pikaxu":{"ataque":50, "defesa":30, "vida":200, "exp":10, "chance":10}, "Kapuznakara":{"ataque":50, "defesa":30, "vida":200, "exp":20, "chance":5}, "Xanaina":{"ataque":100, "defesa":10, "vida":220, "exp":30, "chance":2}}


def critico():
	if random.randint(1,100)<= 50:
		return True
	else:
		return False 


def luta():
	if random.randint(0,9) <= 3:
		return True
	else:
		return False


lista_chance=[]
for i in insperdex:
	x=0
	while x<insperdex[i]["chance"]:
		lista_chance.append(i)
		x=x+1


def roll():
 	poke= random.randint(0, len(lista_chance))
 	aleatorio=lista_chance[poke]
 	return aleatorio


def batalha(jogador,oponente):
	vidajog=insperdex[jogador]["vida"]
	vidaopo=insperdex[oponente]["vida"]
	print("Você encontrou um {} selvagem!".format(oponente))
	while vidajog>0 and vidaopo>0:
		acao=str(input("Qual o seu comando? (Lutar ou Fugir)"))
		acao=acao.lower()
		if acao == "lutar": 
			
			if vidajog>0:
				if critico()==True:
					vidaopo=vidaopo-(insperdex[jogador]["ataque"]-insperdex[oponente]["defesa"])*1.5
					if vidaopo>0:
						print("O {} leva um ataque CRÍTICO e fica com {} de vida".format(oponente,vidaopo))
					elif vidaopo<=0:
						print("O {} leva um ataque CRÍTICO e desmaia!".format(oponente))
				else:
					vidaopo=vidaopo-(insperdex[jogador]["ataque"]-insperdex[oponente]["defesa"])
					if vidaopo>0:
						print("O {} leva o ataque e fica com {} de vida".format(oponente,vidaopo))
					elif vidaopo<=0:
						print("O {} leva o ataque e desmaia!".format(oponente))
			if vidaopo>0:
				if critico()==True:
					vidajog=vidajog-(insperdex[oponente]["ataque"]-insperdex[jogador]["defesa"])*1.5
					if vidajog>0:
						print("O seu {} é atacado CRITICAMENTE e fica com {} de vida".format(jogador,vidajog))
					elif vidajog<=0:
						print("O seu {} é atacado CRITICAMENTE e desmaia!".format(jogador))
				else:
					vidajog=vidajog-(insperdex[oponente]["ataque"]-insperdex[jogador]["defesa"])
					if vidajog>0:
						print("O seu {} é atacado e fica com {} de vida".format(jogador,vidajog))
					elif vidajog<=0:
						print("O seu {} é atacado e desmaia!".format(jogador))
			

			if vidaopo<=0:
				print(("Você venceu! Seu {} ganhou {} de exp!").format(jogador,insperdex[oponente]["exp"]))
			elif vidajog<=0:
				print("Você perdeu!")
		if acao == "fugir":
			if luta()==True:
				print("Fuga Falhou!")
				vidajog=vidajog-(insperdex[oponente]["ataque"]-insperdex[jogador]["defesa"])
				print("O seu {} é atacado e fica com {} de vida".format(jogador,vidajog))
			else:
				print("Fuga Sucedida")
				break


jogador=str(input("Qual seu Inspermon inicial? (Pikaxu, Kapuznakara ou Xanaina) ")).title()
while True:
	fazer=str(input("O que você vai fazer? (Passear ou Dormir) ")).lower()
	if fazer == "passear":
		oponente=roll()
		batalha(jogador,oponente)
	if fazer == "dormir":
		print("Bons Sonhos!")
		break
