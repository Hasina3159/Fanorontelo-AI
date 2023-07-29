
def ajouter(liste, var):
	nwLst = [0]*(len(liste)+1)
	for i in range(0, len(liste)):
		nwLst[i] = liste[i]
	nwLst[(len(nwLst))-1] = var
	return nwLst 

def valeurAbs(chiffre):
	if chiffre < 0:
		chiffre = chiffre*(-1)
	return chiffre

def posToCoord(pos):
	ligne = 0
	colonne = 0
	if pos%3 == 0:
		colonne = 2
	else:
		colonne = (pos % 3)-1
	ligne = (pos - (colonne+1))//3
	return ligne, colonne

def afficher(grille):
	import os
	os.system("cls")
	print("*********")
	for ligne in grille:
		print("* ", end = "")
		for colonne in ligne:
			print(colonne, end = " ")
		print("*")
	print("*********")

def poserPieces(grille, piece, pos, vide):
	ligne, colonne = posToCoord(pos)
	if grille[ligne][colonne] == vide:
		grille[ligne][colonne] = piece
		return 1
	else:
		return 0

def deplacerPieces(grille, piece, depart, dest, vide):
	ligneDp, colonneDp = posToCoord(depart)
	ligneDst, colonneDst = posToCoord(dest)
	if depart != dest:
		if grille[ligneDst][colonneDst] == vide:
			if valeurAbs(ligneDp - ligneDst) <= 1 and valeurAbs(colonneDp - colonneDst) <= 1:
				if grille[ligneDp][colonneDp] == piece:
					if depart %2 != 0 or dest %2 != 0:
						grille[ligneDp][colonneDp] = vide
						poserPieces(grille, piece, dest, vide)
						return True
	return False

def grilleTolist(grille):
	liste = []
	for element in grille:
		for e in element:
			liste = ajouter(liste, e)
	return liste

def gagner(grille, piece1):
	g = grilleTolist(grille)
	gagne = (g[0] == g[1] == g[2] == piece1 or
			g[3] == g[4] == g[5] == piece1 or
			g[6] == g[7] == g[8] == piece1 or
			g[0] == g[3] == g[6] == piece1 or
			g[1] == g[4] == g[7] == piece1 or
			g[2] == g[5] == g[8] == piece1 or
			g[0] == g[4] == g[8] == piece1 or
			g[6] == g[4] == g[2] == piece1)
	return gagne

def debuter(grille, piece1, piece2, vide):
	i = 0
	afficher(grille)
	pp1 = 0
	pp2 = 0
	while i < 3:
		pp1 = 0
		while not pp1:
			try:
				pp1 = poserPieces(grille, piece1, int(input("J1 >>> ")), vide)
				afficher(grille)
			except:
				afficher(grille)
				print("Avereno!", end=" ")
		print(gagner(grille, piece1))
		if gagner(grille, piece1):
			print ("!!! Nandresy ny Mpilalao J1 !!!")
			return 1
		pp2 = 0
		while not pp2:
			try:
				pp2 = poserPieces(grille, piece2, int(input("J2 >>> ")), vide)
				afficher(grille)
			except:
				afficher(grille)
				print("Avereno!", end=" ")
				pass
		print(gagner(grille, piece2))
		if gagner(grille, piece2):
			print ("!!! Nandresy ny Mpilalao J2 !!!")
			return 1
		i = i+1
	return 0

def jouer(grille, piece1, piece2, vide):
	i = 0
	afficher(grille)
	pp1 = 0
	pp2 = 0
	while i < 3:
		pp1 = 0

		while not pp1:
			try:
				pp1 = deplacerPieces(grille, piece1, int(input("J1 Dp >>> ")),int(input("J1 Dst >>> ")), vide)
				afficher(grille)
			except:
				afficher(grille)
				print("Avereno!", end=" ")
		print(gagner(grille, piece1))
		if gagner(grille, piece1):
			print ("!!! Nandresy ny Mpilalao J1 !!!")
			return 1
		pp2 = 0
		while not pp2:
			try:
				pp2 = deplacerPieces(grille, piece2, int(input("J2 Dp >>> ")),int(input("J2 Dst >>> ")), vide)
				afficher(grille)
			except:
				afficher(grille)
				print("Avereno!", end=" ")
				pass
		print(gagner(grille, piece2))
		if gagner(grille, piece2):
			print ("!!! Nandresy ny Mpilalao J2 !!!")
			return 1
		i = i+1
	return 0

def afficherSimple(grille):
	for x in grille:
		print(x)

def indexerPiece(grille, piecebot):
	fl = grilleTolist(grille)
	placePieceBot = []
	for i in range(len(fl)):
		if fl[i] == piecebot:
			placePieceBot.append(i+1)
	return placePieceBot

def coupsPossible(grille, piece, vide):
	cpsPossible = []
	placePiece = indexerPiece(grille, piece)
	for depart in placePiece:
		for destination in range(1, 10):
			estDeplace = deplacerPieces(grille, piece, depart, destination, vide)
			if estDeplace:
				cpsPossible.append([depart, destination])
				deplacerPieces(grille, piece, destination, depart, vide)
	return cpsPossible

def trouverCaseVide(grille, vide):
	g = grilleTolist(grille)
	liste = []
	for i in range(len(g)):
		if g[i] == vide:
			liste.append(i+1)
	return liste

def poserPiecesBot(grille, piecebot, pieceJoueur, vide):
	import random
	caseVide = trouverCaseVide(grille, vide)

	#Maka laka
	pp = poserPieces(grille, piecebot, 5, vide)
	if pp:
		return True

	#gagner	
	for i in caseVide:
		poserPieces(grille, piecebot, i, vide)
		if gagner(grille, piecebot):
			return True
		else:
			poserPieces(grille, vide, i, piecebot)
	
	#parer
	for i in caseVide:
		poserPieces(grille, pieceJoueur, i, vide)
		if gagner(grille, pieceJoueur):
			poserPieces(grille, vide, i, pieceJoueur)
			poserPieces(grille, piecebot, i, vide)
			return True
		else:
			poserPieces(grille, vide, i, pieceJoueur)

	#eviter domination
	hasard = caseVide[random.randint(0, len(caseVide)-1)]
	poserPieces(grille, piecebot, hasard, vide)

	return

def meilleurCoupJr(grille, pieceJoueur, vide):
	cpsJr = coupsPossible(grille, pieceJoueur, vide)
	dep = 0
	dst = 1
	for moveJ in cpsJr:
		deplacerPieces(grille, pieceJoueur, moveJ[dep], moveJ[dst], vide)
		if gagner(grille, pieceJoueur):
			deplacerPieces(grille, pieceJoueur, moveJ[dst], moveJ[dep], vide)
			return moveJ
		deplacerPieces(grille, pieceJoueur, moveJ[dst], moveJ[dep], vide)
	return False

def meilleurCoupGagne(grille, piecebot, vide):
	cpsPossible = coupsPossible(grille, piecebot, vide)
	dep = 0
	dst = 1
	for move in cpsPossible:	
		deplacerPieces(grille, piecebot, move[dep], move[dst], vide)
		if gagner(grille, piecebot):
			return True
		deplacerPieces(grille, piecebot, move[dst], move[dep], vide)
	return False

def meilleurCoupParer(grille, piecebot, pieceJoueur, vide):
	cpsPossibleBot = coupsPossible(grille, piecebot, vide)
	dep = 0
	dst = 1
	bestCpJr = meilleurCoupJr(grille, pieceJoueur, vide)

	if bestCpJr == False:
		return False

	for moveB in cpsPossibleBot:
		if moveB[dst] == bestCpJr[dst]:
			deplacerPieces(grille, piecebot, moveB[dep], moveB[dst], vide)
			return True

def moveRandomBot(grille, piecebot, pieceJoueur, vide):
	import random
	cpsBot = coupsPossible(grille, piecebot, vide)
	tester = False
	while not tester:
		rnd = random.randint(0, len(cpsBot)-1)
		dep = cpsBot[rnd][0]
		dst = cpsBot[rnd][1]
		deplacerPieces(grille, piecebot, dep, dst, vide)
		bestCpJr = meilleurCoupJr(grille, pieceJoueur, vide)
		if bestCpJr != False:
			deplacerPieces(grille, piecebot, dst, dep, vide)
		else:
			return True

def deplacerInteligemment(grille, piecebot, pieceJoueur, vide):
	if not meilleurCoupGagne(grille, piecebot, vide):
		if not meilleurCoupParer(grille, piecebot, pieceJoueur, vide):
			moveRandomBot(grille, piecebot, pieceJoueur, vide)
			print("moverandom")
	if gagner(grille, piecebot):
		return True
	return False

def debut_contre_bot(grille, piecebot, pieceJoueur, vide):
	import time
	i = 0
	pj = False
	afficher(grille)
	while i < 3:
		while not pj:
			j = input("Joueur > ")
			j = int(j)
			pj = poserPieces(grille, pieceJoueur, j, vide)
			afficher(grille)
			if gagner(grille, pieceJoueur):
				print("Nandresy Joueur!!!")
				return True
		time.sleep(1)
		poserPiecesBot(grille, piecebot, pieceJoueur, vide)
		afficher(grille)
		pj = False
		i += 1

	if gagner(grille, piecebot):
		print("Nandresy Bot!!!")
		return True
	return False

def finale_contre_bot(grille, piecebot, pieceJoueur, vide):
	import time
	i = 0
	mj = False
	afficher(grille)
	while i < 3:
		while not mj:
			mj = deplacerPieces(grille, pieceJoueur, int(input("Depart > ")), int(input("Dest > ")), vide)
			afficher(grille)
			if gagner(grille, pieceJoueur):
				print("Nandresy Joueur!!!")
				return True
		time.sleep(1)
		if deplacerInteligemment(grille, piecebot, pieceJoueur, vide):
			afficher(grille)
			print("Nandresy ny Bot!!!")
			return True
		else:
			mj = False
			afficher(grille)

def jouerContreBot():
	t = [["-", "-", "-"],
	["-", "-", "-"],
	["-", "-", "-"]]
	if not debut_contre_bot(t, "o", "x", "-"):
		finale_contre_bot(t, "o", "x", "-")

jouerContreBot()
