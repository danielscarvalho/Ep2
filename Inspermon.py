import pickle
import random
import time
insperdex={
	"Pikaxu":{
		"Ataque":50, "Defesa":30, "Vida":200, "Exp":10, "Chance":10, "Evo":20
	},
	"Kapuznakara":{
		"Ataque":50, "Defesa":30, "Vida":200, "Exp":20, "Chance":7, "Evo":25
	}, 
	"Xanaina":{
		"Ataque":105, "Defesa":10, "Vida":230, "Exp":30, "Chance":2, "Evo":30
	},
	"Kingnaldo":{
		"Ataque":120, "Defesa":15, "Vida":180, "Exp":35, "Chance":2, "Evo":30   #mudar a evolucao do kingnaldo
	},
	"Douglas":{
		"Ataque":90, "Defesa":25, "Vida":210, "Exp":30, "Chance":2, "Evo":35
	},
	"Cetaxu":{
		"Ataque":70, "Defesa":50, "Vida":220, "Exp":30, "Chance":0, "Evo":1000
	},
	"Bonenakara":{
		"Ataque":70, "Defesa":50, "Vida":220, "Exp":30, "Chance":0, "Evo":1000
	}, 
	"Xanalna":{
		"Ataque":120, "Defesa":30, "Vida":240, "Exp":30, "Chance":0, "Evo":1000
	},
	"Godnaldo":{
		"Ataque":140, "Defesa":35, "Vida":200, "Exp":30, "Chance":0, "Evo":1000
	},
	"Showglas":{
		"Ataque":110, "Defesa":45, "Vida":230, "Exp":30, "Chance":0, "Evo":1000
	}
}	#Dicionários dos Inspermons

dexjog={} #InsperDex
seus_inspermons=[] #Lista com seus inspermons


def save(arquivo):
	dados= open(arquivo,'wb') 
	pickle.dump({"dados" : [dexjog, exp, jogador,seus_inspermons]}, dados)
	dados.close()


def load(arquivo):
	dado=pickle.load(open(arquivo,"rb"))
	return dado


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


def captura(oponente,vidaopo): #Função captura
	if random.randint(1,100) >=int(round((vidaopo/insperdex[oponente]["Vida"])*85+10)):
		return True
	else:
		return False


lista_evo=[]
lista_chance=[] #Lista de chance de encontro no passeio
for i in insperdex:
	if insperdex[i]["Chance"]>0:
		x=0
		while x<insperdex[i]["Chance"]:
			lista_chance.append(i)
			x=x+1
	elif insperdex[i]["Chance"]<=0:
		lista_evo.append(i)


def roll(): #Randomizador
 	poke= random.randint(0, len(lista_chance))
 	aleatorio=lista_chance[poke]
 	return aleatorio


def experiencia(xp):
	expganha=insperdex[oponente]["Exp"]
	xp=xp+expganha
	return xp


def evolucao(jogador):
	if jogador == "Pikaxu":
		return "Cetaxu"
	if jogador == "Kapuznakara":
		return "Bonenakara"
	if jogador == "Xanaina":
		return "Xanalna"
	if jogador == "Kingnaldo":
		return "Godnaldo"
	if jogador == "Douglas":
		return "Showglas"


def batalha(jogador,oponente): #Função Batalha
	vidajog=insperdex[jogador]["Vida"]+10*niveljog
	vidaopo=insperdex[oponente]["Vida"]
	print("Você encontrou um {} selvagem!".format(oponente))
	time.sleep(1.0)
	print("O seu oponente tem: ")
	print("Ataque: {}".format(insperdex[oponente]["Ataque"]))
	print("Defesa: {}".format(insperdex[oponente]["Defesa"]))
	print("Vida: {}".format(insperdex[oponente]["Vida"]))
	print("E da {} de experiência".format(insperdex[oponente]["Exp"]))
	
	if oponente not in dexjog:
		dexjog[oponente]=insperdex[oponente]
	time.sleep(1.5)
	
	while vidajog>0 and vidaopo>0:
		
		if jogador == oponente or oponente in seus_inspermons:
			acao=str(input("Qual o seu comando? (Lutar(L) ou Fugir(F))")).lower() #Escolha de comando

		else:
			acao=str(input("Qual o seu comando? (Lutar(L), Fugir(F) ou Capturar(C))")).lower() #Escolha de comando
		
		if acao == "lutar" or acao == "l": 
			time.sleep(1.0)
			
			if ((insperdex[jogador]["Ataque"]+10*niveljog)-insperdex[oponente]["Defesa"])>0:
				
				if vidajog>0: #Ataque Jogador
					
					if critico()==True:
						vidaopo=vidaopo-((insperdex[jogador]["Ataque"]+10*niveljog)-insperdex[oponente]["Defesa"])*1.5
						
						if vidaopo>0:
							print("O {} leva um ataque CRÍTICO e fica com {} de vida".format(oponente,vidaopo))
							time.sleep(1.0)
						
						elif vidaopo<=0:
							print("O {} leva um ataque CRÍTICO e desmaia!".format(oponente))
							time.sleep(1.0)
					
					else:
						vidaopo=vidaopo-((insperdex[jogador]["Ataque"]+10*niveljog)-insperdex[oponente]["Defesa"])
						
						if vidaopo>0:
							print("O {} leva o ataque e fica com {} de vida".format(oponente,vidaopo))
							time.sleep(1.0)
						
						elif vidaopo<=0:
							print("O {} leva o ataque e desmaia!".format(oponente))
							time.sleep(1.0)
			
			elif ((insperdex[jogador]["Ataque"]+10*niveljog)-insperdex[oponente]["Defesa"])<=0:
				print("O seu ataque não deu dano!")
			
			
			if (insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))>0:
				
				if vidaopo>0: #Ataque Oponente
					print("O {} selvagem se prepara para atacar!".format(oponente))
					time.sleep(1)
					
					if critico()==True:
						vidajog=vidajog-(insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))*1.5
						
						if vidajog>0:
							print("O seu {} é atacado CRITICAMENTE e fica com {} de vida".format(jogador,vidajog))
							time.sleep(1.0)
						
						elif vidajog<=0:
							print("O seu {} é atacado CRITICAMENTE e desmaia!".format(jogador))
							time.sleep(0.5)
							print("O seu Inspermon foi levado ao InsperCenter!")
							time.sleep(1.0)
					
					else:
						vidajog=vidajog-(insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))
						
						if vidajog>0:
							print("O seu {} é atacado e fica com {} de vida".format(jogador,vidajog))
							time.sleep(1.0)
						
						elif vidajog<=0:
							print("O seu {} é atacado e desmaia!".format(jogador))
							time.sleep(1.0)
			
			elif (insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))<=0:
				print("O ataque do {} não deu dano!".format(oponente))
			
			if vidaopo<=0: #Resultado Batalha
				print(("Você venceu! Seu {} ganhou {} de exp!").format(jogador,insperdex[oponente]["Exp"]))
				time.sleep(1.0)
				return True
			
			elif vidajog<=0:
				print("Você perdeu e seu Inspèrmon foi levado ao InsperCenter!")
				time.sleep(1.0)
				return False
		
		if acao == "fugir" or acao == "f": #Tentativa de Fuga
			time.sleep(1.0)
			
			if luta()==True:
				print("Fuga Falhou!")
				time.sleep(1.0)
				
				if (insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))>0:
				
					if vidaopo>0: #Ataque Oponente
						print("O {} selvagem se prepara para atacar!".format(oponente))
						time.sleep(1)
						
						if critico()==True:
							vidajog=vidajog-(insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))*1.5
							
							if vidajog>0:
								print("O seu {} é atacado CRITICAMENTE e fica com {} de vida".format(jogador,vidajog))
								time.sleep(1.0)
							
							elif vidajog<=0:
								print("O seu {} é atacado CRITICAMENTE e desmaia!".format(jogador))
								time.sleep(1.0)
						
						else:
							vidajog=vidajog-(insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))
							
							if vidajog>0:
								print("O seu {} é atacado e fica com {} de vida".format(jogador,vidajog))
								time.sleep(1.0)
							
							elif vidajog<=0:
								print("O seu {} é atacado e desmaia!".format(jogador))
								time.sleep(1.0)
				
				elif (insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))<=0:
					print("O ataque do {} não deu dano!".format(oponente))
			else:
				print("Fuga Sucedida")
				time.sleep(1.0)
				break

		if acao == "capturar" or acao == "c":
			time.sleep(1.0)
			
			if jogador != oponente:
				cc= captura(oponente,vidaopo)
				
				if cc == True:
					seus_inspermons.append(oponente)
					print("Parabéns! Você agora possui {} como um de seus inspermons!".format(oponente))
					break
			
				if cc == False:
					print("Foi por pouco! {} se recusa a ter sua liberdade retirada!".format(oponente))
					
					if (insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))>0:
				
						if vidaopo>0: #Ataque Oponente
							print("O {} selvagem se prepara para atacar!".format(oponente))
							time.sleep(1)
					
							if critico()==True:
								vidajog=vidajog-(insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))*1.5
						
								if vidajog>0:
									print("O seu {} é atacado CRITICAMENTE e fica com {} de vida".format(jogador,vidajog))
									time.sleep(1.0)
						
								elif vidajog<=0:
									print("O seu {} é atacado CRITICAMENTE e desmaia!".format(jogador))
									time.sleep(1.0)
					
							else:
								vidajog=vidajog-(insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))
						
								if vidajog>0:
									print("O seu {} é atacado e fica com {} de vida".format(jogador,vidajog))
									time.sleep(1.0)
						
								elif vidajog<=0:
									print("O seu {} é atacado e desmaia!".format(jogador))
									time.sleep(1.0)
			
					elif (insperdex[oponente]["Ataque"]-(insperdex[jogador]["Defesa"]+10*niveljog))<=0:
						print("O ataque do {} não deu dano!".format(oponente))

			else:
				print("Você já possui esse inspermon!")


				
niveljog=1
exp=0
lista_saves=[]
print("Bem Vindo ao Mundo de Inspermon!")
time.sleep(0.5)
while True:
	inicio=str(input("New Game(N) ou Load Game(L)? ")).lower()
	
	if inicio=="new game" or inicio=="n":
		jogador=str(input("Qual seu Inspermon inicial? (Xanaina, Kingnaldo ou Douglas) ")).title()
		dexjog[jogador]=insperdex[jogador]
		seus_inspermons.append(jogador)
		time.sleep(0.5)
		break
	
	if inicio=="load game" or inicio=="l":
		try:
			lista_saves=pickle.load(open("lista","rb"))
			if len(lista_saves)>0:
				print("Os saves disponíveis são: {}".format(lista_saves))
				time.sleep(1)
				file=str(input("Qual save deseja carregar? "))
				dado=load(file)
				dexjog=dado["dados"][0]
				exp=dado["dados"][1]
				jogador=dado["dados"][2]
				seus_inspermons=dado["dados"][3]
				print("Carregando....")
				time.sleep(2)
				print("Sucesso!")
				time.sleep(0.5)
				print("O seu inspermon é o: {}".format(jogador))
				break
		except:
			print("Não há saves ainda!")


while True:
	fazer=str(input("O que você vai fazer? (Passear(P), Dormir(D), Insperdex(I), Salvar(S), Load(L) ou Trocar Inspermon(T)? ")).lower() #Escolha de ação
	time.sleep(1.0)
	
	if fazer == "passear" or fazer == "p": #Caso Passeie
		print("Passeando...")
		time.sleep(1.5) 
		oponente=roll()
		
		if batalha(jogador,oponente)==True:
			exp=experiencia(exp)
		print("Seu {} possui {} de experiência".format(jogador,exp))
		time.sleep(0.5)
		
		if exp >=insperdex[jogador]["Evo"]:
			seus_inspermons.remove(jogador)
			jogador=evolucao(jogador)
			print(".")
			time.sleep(0.2)
			print(".")
			time.sleep(0.2)
			print(".")
			time.sleep(0.2)
			print("O seu pokemon evolui para...")
			time.sleep(0.5)
			print(("{} !!".format(jogador)).upper())
			time.sleep(2.0)
			print("Os stats do {} são:".format(jogador))
			print("Ataque: {}".format(insperdex[jogador]["Ataque"]))
			print("Defesa: {}".format(insperdex[jogador]["Defesa"]))
			print("Vida: {}".format(insperdex[jogador]["Vida"]))
	
			dexjog[jogador]=insperdex[jogador]
			seus_inspermons.append(jogador)
		

	if fazer == "dormir" or fazer == "d": #Caso durma
		print("Bons Sonhos!")
		break 
	
	if fazer == "insperdex" or fazer == "i": #Caso cheque Insperdex
		print("Este são os Inspèrmons que você já encontrou: {}".format(dexjog))
		time.sleep(0.5)

	if fazer == "trocar inspermon" or fazer == "t":
		print("Seus inspermons atuais são:")
		for h in range(0,len(seus_inspermons)):
			print("{}({})".format(seus_inspermons[h],h+1))
			time.sleep(0.5)
		hh=int(input("Insira o numero do inspermon desejado :"))
		jogador=seus_inspermons[hh-1]
		time.sleep(1.5)
		print("Seu inspermon agora é {}".format(jogador))
	
	if fazer == "salvar" or fazer == "s":
		print("Os saves disponíveis são: {}".format(lista_saves))
		arquivo=str(input("Deseja salvar com que nome? "))
		lista_saves.append(arquivo)
		save(arquivo)
		saves=open("lista", "wb" )
		pickle.dump(lista_saves, saves)
		saves.close()
		print("Salvando....")
		time.sleep(2)
		print("Sucesso!")
		time.sleep(0.5)
	
	if fazer == "load" or fazer == "l":
		try:
			lista_saves=pickle.load(open("lista","rb"))
			if len(lista_saves)>0:
				print("Os saves disponíveis são: {}".format(lista_saves))
				time.sleep(1)
				file=str(input("Qual save deseja carregar? "))
				dado=load(file)
				dexjog=dado["dados"][0]
				exp=dado["dados"][1]
				jogador=dado["dados"][2]
				seus_inspermons=dado["dados"][3]
				print("Carregando....")
				time.sleep(2)
				print("Sucesso!")
				time.sleep(0.5)
		except:
			print("Não há saves ainda!")



