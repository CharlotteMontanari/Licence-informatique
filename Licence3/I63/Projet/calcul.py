def bresenham(P1, P2):
	dx = P2[0] - P1[0]
	dy = P2[1] - P1[1]
	if dy < 0:	#Moitié haute
		print("Moitié haute")
		if dx > 0:	#Quart droit
			print("Quart droit")
			
			if abs(dx) > abs(dy): #Octant 1
				print("Octant 1")
				x = P1[0]
				y = P1[1]
				dec = dx + 2*dy
				while x <= P2[0]:
					creer_point(x,y)
					if dec < 0:
						dec = dec + 2*dx
						y = y - 1
					dec = dec + 2*dy
					x = x + 1
				creer_point(P2[0],P2[1])
			
			else:	#Octant 2
				print("Octant 2")
				x = P1[0]
				y = P1[1]
				dec = dy - 2*dx
				while y > P2[1]:
					creer_point(x,y)
					if dec < 0:
						dec = dec - 2*dy
						x = x + 1
					dec = dec - 2*dx
					y = y - 1
				creer_point(P2[0],P2[1])
		
		else:	#Quart gauche
			print("Quart gauche")
			if abs(dx) <= abs(dy): #Octant 3
				print("Octant 3")
				x = P1[0]
				y = P1[1]
				dec = dy + 2*dx
				while y > P2[1]:
					creer_point(x,y)
					if dec < 0:
						dec = dec - 2*dy
						x = x - 1
					dec = dec + 2 * dx
					y = y - 1
				creer_point(P2[0],P2[1])
			
			else:	#Octant 4
				print("Octant 4")
				x = P1[0]
				y = P1[1]
				dec = dx - 2*dy
				while x > P2[0]:
					creer_point(x,y)
					if dec < 0:
						dec = dec - 2*dx
						y = y - 1
					dec = dec + 2*dy
					x = x - 1
				creer_point(P2[0],P2[1])
				
	else:	#Moitié basse
		print("Moitié basse")
		if dx > 0:	#Quart droit
			print("Quart droit")
			
			if abs(dx) > abs(dy): #Octant 8
				print("Octant 8")
				x = P1[0]
				y = P1[1]
				dec = dx - 2*dy
				while x < P2[0]:
					creer_point(x,y)
					if dec < 0:
						dec = dec + 2*dx
						y = y + 1
					dec = dec - 2*dy
					x = x + 1
				creer_point(P2[0],P2[1])
			
			else:	#Octant 7
				print("Octant 7")
				x = P1[0]
				y = P1[1]
				dec = dy - 2*dx
				while y < P2[1]:
					creer_point(x,y)
					if dec < 0:
						dec = dec + 2*dy
						x = x + 1
					dec = dec - 2*dx
					y = y + 1
				creer_point(P2[0],P2[1])
		
		else:	#Quart gauche
			print("Quart gauche")
			if abs(dx) > abs(dy): #Octant 5
				print("Octant 5")
				x = P1[0]
				y = P1[1]
				dec = dx - 2*dy
				while x > P2[0]:
					creer_point(x,y)
					if dec < 0:
						dec = dec - 2*dx
						y = y - 1
					dec = dec + 2*dy
					x = x - 1
				creer_point(P2[0],P2[1])
			
			else:	#Octant 6
				print("Octant 6")
				x = P1[0]
				y = P1[1]
				dec = dy + 2*dx
				while y < P2[1]:
					creer_point(x,y)
					if dec < 0:
						dec = dec + 2*dy
						x = x - 1
					dec = dec + 2 * dx
					y = y + 1
				creer_point(P2[0],P2[1])

