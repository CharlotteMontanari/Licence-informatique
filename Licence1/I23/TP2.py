def Lecture(nomfichier):
   fichier = open(nomfichier, 'r')
   liste = fichier.readlines()
   X = set()
   G = {}
   Y = set()
   for chaine in liste:
      couple = chaine.rstrip().split('>')
      if couple[0] != '':
         X = X | {couple[0]}
      if couple[1] != '':
         Y = Y | {couple[1]}
      if couple[0] != '' and couple[1] != '':
         if couple[0] in G.keys():
            G[couple[0]] = G[couple[0]] | {couple[1]}
         else:
            G[couple[0]] = {couple[1]}
   return (X, G, Y)
# print(Lecture('TP2.txt'))

def Reciproque(c):
   X, G, Y = c[2], c[1], c[0]
   G_recip = {}
   for cle_g in G.keys():
      for val in G[cle_g]:
         if val in G_recip.keys():
            G_recip[val] = G_recip[val] | {cle_g}
         else:
            G_recip[val] = {cle}
   return (X, G_recip, Y)
# print(Reciproque(Lecture('TP2.txt')))

def Imagedirect(c, a):
   X, G, Y = c[0], c[1], c[2]
   image_direct = {}
   for cle_g in G.keys():
      for j in a:
         if cle_g == j:
            for e in G[j]:
               if j in image_direct:
                  image_direct[j] = image_direct[j] | {e}
               else:
                  image_direct[j] = {e}
   return image_direct
# print(Imagedirect(Lecture('TP2.txt'), {'c','a'}))

def Imagereciproque(c, a):
   G = c[1]
   image_recip = {}
   for i in G.keys():
      for j in a:
         if i == j:
            for e in G[j]:
               if j in image_recip:
                  image_recip[j] = image_recip[j] | {e}
               else:
                  image_recip[j] = {e}
   return image_recip
# print(Imagereciproque(Reciproque(Lecture('TP2.txt')), {'1', '2'})) 

def Composer(g, f):
   gof = {}
   Gg = g[1]
   G = f[1]
   for i in G.keys():
      for e in G[i]:
         if e in Gg.keys():
            if i in gof.keys():
               gof[e] = gof[e] | {i}
            else:
               gof[e] = {i}
   return (gof)
# print(Composer(Reciproque(Lecture('TP2.txt')), Lecture('TP2.txt')))

def Estfonction(c):
   X, G, Y = c[0], c[1], c[2]
   fonction = True
   for i in G.keys():
      if len(G[i]) > 1:
         fonction = False
      else:
         fonction = True
   return fonction
# print(Estfonction(Lecture('TP2.txt')))

def Estapplication(c):
   X, G, Y = c[0], c[1], c[2]
   application = True
   for i in X:
      if not (i in G.keys()) or (len(G[i]) > 1):
         application = False
      else:
         application = True
   return application
# print(Estapplication(Lecture('TP2.txt')))