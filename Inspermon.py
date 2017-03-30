import random
import time
insperdex={"Pikaxu":{"Ataque":50, "Defesa":30, "Vida":200, "Exp":10, "Chance":10},
           "Kapuznakara":{"Ataque":50, "Defesa":30, "Vida":200, "Exp":20, "Chance":5}, 
           "Xanaina":{"Ataque":100, "Defesa":10, "Vida":220, "Exp":30, "Chance":2}}  #Dicionários dos Inspermons
dexjog={} #InsperDex

def critico(): #Função Critico
	if random.randint(1,100)<= 20:
		return True
	else:
		return False 


def luta(): #Função Fuga
	if random.randint(1,10) <=3:
		return True
	else:
		return False


lista_chance=[] #Lista de chance de encontro no passeio
for i in insperdex:
	x=0
	while x<insperdex[i]["Chance"]:
		lista_chance.append(i)
		x=x+1


def roll(): #Randomizador
 	poke= random.randint(0, len(lista_chance))
 	aleatorio=lista_chance[poke]
 	return aleatorio


def batalha(jogador,oponente): #Função Batalha
	vidajog=insperdex[jogador]["Vida"]
	vidaopo=insperdex[oponente]["Vida"]
	print("Você encontrou um {} selvagem!".format(oponente))
	time.sleep(1.0)
	print("Os atributos do {} são: {}".format(oponente,insperdex[oponente]))
	if oponente not in dexjog:
		dexjog[oponente]=insperdex[oponente]
	time.sleep(1.5)
	while vidajog>0 and vidaopo>0:
		acao=str(input("Qual o seu comando? (Lutar(L) ou Fugir(F))")).lower() #Escolha de comando
		if acao == "lutar" or acao == "l": 
			time.sleep(1.0)
			if vidajog>0: #Ataque Jogador
				if critico()==True:
					vidaopo=vidaopo-(insperdex[jogador]["Ataque"]-insperdex[oponente]["Defesa"])*1.5
					if vidaopo>0:
						print("O {} leva um ataque CRÍTICO e fica com {} de vida".format(oponente,vidaopo))
						time.sleep(1.0)
					elif vidaopo<=0:
						print("O {} leva um ataque CRÍTICO e desmaia!".format(oponente))
						time.sleep(1.0)
				else:
					vidaopo=vidaopo-(insperdex[jogador]["Ataque"]-insperdex[oponente]["Defesa"])
					if vidaopo>0:
						print("O {} leva o ataque e fica com {} de vida".format(oponente,vidaopo))
						time.sleep(1.0)
					elif vidaopo<=0:
						print("O {} leva o ataque e desmaia!".format(oponente))
						time.sleep(1.0)
			print("O {} selvagem se prepara para atacar!".format(oponente))
			time.sleep(1.0)
			if vidaopo>0: #Ataque Oponente
				if critico()==True:
					vidajog=vidajog-(insperdex[oponente]["Ataque"]-insperdex[jogador]["Defesa"])*1.5
					if vidajog>0:
						print("O seu {} é atacado CRITICAMENTE e fica com {} de vida".format(jogador,vidajog))
						time.sleep(1.0)
					elif vidajog<=0:
						print("O seu {} é atacado CRITICAMENTE e desmaia!".format(jogador))
						time.sleep(1.0)
				else:
					vidajog=vidajog-(insperdex[oponente]["Ataque"]-insperdex[jogador]["Defesa"])
					if vidajog>0:
						print("O seu {} é atacado e fica com {} de vida".format(jogador,vidajog))
						time.sleep(1.0)
					elif vidajog<=0:
						print("O seu {} é atacado e desmaia!".format(jogador))
						time.sleep(1.0)
			
			if vidaopo<=0: #Resultado Batalha
				print(("Você venceu! Seu {} ganhou {} de exp!").format(jogador,insperdex[oponente]["Exp"]))
				time.sleep(1.0)
			elif vidajog<=0:
				print("Você perdeu e seu Inspèrmon foi levado ao InsperCenter!")
				time.sleep(1.0)
		
		if acao == "fugir" or acao == "f": #Tentativa de Fuga
			time.sleep(1.0)
			if luta()==True:
				print("Fuga Falhou!")
				time.sleep(1.0)
				if critico()==True:
					vidajog=vidajog-(insperdex[oponente]["Ataque"]-insperdex[jogador]["Defesa"])*1.5
					if vidajog>0:
						print("O seu {} é atacado CRITICAMENTE e fica com {} de vida".format(jogador,vidajog))
						time.sleep(1.0)
					elif vidajog<=0:
						print("O seu {} é atacado CRITICAMENTE e desmaia!".format(jogador))
						time.sleep(1.0)
				else:
					vidajog=vidajog-(insperdex[oponente]["Ataque"]-insperdex[jogador]["Defesa"])
					if vidajog>0:
						print("O seu {} é atacado e fica com {} de vida".format(jogador,vidajog))
						time.sleep(1.0)
					elif vidajog<=0:
						print("O seu {} é atacado e desmaia!".format(jogador))
						time.sleep(1.0)
			else:
				print("Fuga Sucedida")
				time.sleep(1.0)
				break


print("Bem Vindo ao Mundo de Inspermon!") #Introdução
time.sleep(0.5)
jogador=str(input("Qual seu Inspermon inicial? (Pikaxu, Kapuznakara ou Xanaina) ")).title() #Escolha de Inicial
dexjog[jogador]=insperdex[jogador]
time.sleep(0.5)
while True:
	fazer=str(input("O que você vai fazer? (Passear(P), Dormir(D) ou Insperdex(I)?) ")).lower() #Escolha de ação
	time.sleep(1.0)
	if fazer == "passear" or fazer == "p": #Caso Passeie
		print("Passeando...")
		time.sleep(1.5) 
		oponente=roll()
		batalha(jogador,oponente)
	if fazer == "dormir" or fazer == "d": #Caso Durma
		print("Bons Sonhos!")
		break
	if fazer == "insperdex" or fazer == "i": #Caso cheque InsperDex
		print("Este são os Inspèrmons que você já encontrou: {}".format(dexjog))
		time.sleep(0.5)