import random
import time
insperdex={"Pikaxu":{"Ataque":50, "Defesa":30, "Vida":200, "Exp":10, "Chance":10}, "Kapuznakara":{"Ataque":50, "Defesa":30, "Vida":200, "Exp":20, "Chance":5}, "Xanaina":{"Ataque":100, "Defesa":10, "Vida":220, "Exp":30, "Chance":2}}
dexjog={}

def critico():
	if random.randint(1,100)<= 20:
		return True
	else:
		return False 


def luta():
	if random.randint(1,10) <=3:
		return True
	else:
		return False


lista_chance=[]
for i in insperdex:
	x=0
	while x<insperdex[i]["Chance"]:
		lista_chance.append(i)
		x=x+1


def roll():
 	poke= random.randint(0, len(lista_chance))
 	aleatorio=lista_chance[poke]
 	return aleatorio


def batalha(jogador,oponente):
	vidajog=insperdex[jogador]["Vida"]
	vidaopo=insperdex[oponente]["Vida"]
	print("Você encontrou um {} selvagem!".format(oponente))
	if oponente not in dexjog:
		dexjog[oponente]=insperdex[oponente]
	time.sleep(1.5)
	while vidajog>0 and vidaopo>0:
		acao=str(input("Qual o seu comando? (Lutar(L) ou Fugir(F))")).lower()
		if acao == "lutar" or acao == "l": 
			time.sleep(1.0)
			if vidajog>0:
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
			if vidaopo>0:
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
			
			if vidaopo<=0:
				print(("Você venceu! Seu {} ganhou {} de exp!").format(jogador,insperdex[oponente]["Exp"]))
				time.sleep(1.0)
			elif vidajog<=0:
				print("Você perdeu e seus Inspèrmon foi levado ao InsperCenter!")
				time.sleep(1.0)
		
		if acao == "fugir" or acao == "f":
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


print("Bem Vindo ao Mundo de Inspermon!")
time.sleep(1.0)
jogador=str(input("Qual seu Inspermon inicial? (Pikaxu, Kapuznakara ou Xanaina) ")).title()
dexjog[jogador]=insperdex[jogador]
time.sleep(1.0)
while True:
	fazer=str(input("O que você vai fazer? (Passear(P), Dormir(D) ou Insperdex(I)?) ")).lower()
	time.sleep(1.0)
	if fazer == "passear" or fazer == "p":
		print("Passeando...")
		time.sleep(1.5) 
		oponente=roll()
		batalha(jogador,oponente)
	if fazer == "dormir" or fazer == "d":
		time.sleep(1.0)
		print("Bons Sonhos!")
		break
	if fazer == "insperdex" or fazer == "i":
		time.sleep(1.0)
		print("Este são os Inspèrmons que você já encontrou: {}".format(dexjog))