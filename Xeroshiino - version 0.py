"""
GAME : Xeroshiino village
"""

"""
Aouthor : ABDIRIZAK ABDULLAHI HUSEEIN
DATE : 6/7/2022 
INSTEGRAM : Abdirizak_8899
GITHUB : github.com/AbdirizaK8899
					
"""	
#------------------------------------------
import pygame , sys,os,random,time
#------------------------------------------
from pygame.locals import *
#-------------------------------------------

# HABEYNTA SHAASHADA SIDA CABIRKA/ DHIRIR IYO BALLAC

ballaca_shaashada = 750
dhirirka_shaashada = 490

pygame.init()
pygame.display.set_caption("Xeroshiino village")
shaashada = pygame.display.set_mode([ballaca_shaashada,dhirirka_shaashada])

# kalarada --waxaa jiro kalaro badan balse hadda waxaa u baahanay kaliya saddex ama kayar saa filaayo sababto ah waxaa isticmaalayaa sawiro
madow = pygame.Color(0,0,0)
caddaan = pygame.Color(255,255,255)

#sawirada  backroundka
bg_list = [None]*4
for bg in range(1,5):
	bg_list[bg-1] = pygame.image.load(os.path.join('bg' + str(bg) + '.png'))
	bg += 1


# sawiraanta ciyaryahanka
#--------------------------------------------------------------------------------------------
#sawiraanta dhanka bidix waa kuwaan
dhaqaajinta_bidix = [None]*10 #inta waxaa kujiro sagaal sawir dhanka bidix
for sawir in range(1,10):
	dhaqaajinta_bidix[sawir-1] = pygame.image.load(os.path.join('L' + str(sawir) + '.png'))
	sawir +=1
#--------------------------------------------------------------------------------------------
#sawiraanta dhanka idig waa kuwaan
dhaqaajinta_midig = [None]*10# intana sidoo kle
for sawir in range(1,10):
	dhaqaajinta_midig[sawir-1] = pygame.image.load(os.path.join('R' + str(sawir) + '.png'))
	sawir +=1
#sawirkaan waxaa loogu talagalay marka uu san meelna u dhaqaaqin sawir taaganlee soo baxaayo
#------------------------------------------------------------------
standing = pygame.image.load('standing.png')
#------------------------------------------------------------------
# madoorsoomayaa sha gameka
fps = pygame.time.Clock() #fps waxaa lagasoo gaabiyey frame per second yacnii inta u qaadanayo inuu shayga kusoo sawiro shashashada
ciyaarta_waa_play = True
global i 
i = 0 # i daan waxaa ugu talagalay ine backgroundka dhan=[midig/bidix] u dhaqaajiso 
RIGHT = False
LEFT = False
askari_x = ballaca_shaashada//3-50+100
askari_y = dhirirka_shaashada//2+148


#madoorsoomayaasha boodida
karaarinta = 20
dhirirka_labooday = karaarinta
cufasjiidadka = 1
#_______________________________________



"""
faahfaahin yar aa kaa siiyo classkan hero waxaa ugu magacaaabay sawirka player 
wuxuu u egyahay geesi
classkan waxaa ku jiro methods badan sida dhaqaajinta playerka , sawirdida lagu sawirayo shaashada markuu u dhaqaaqayo
[midig/bidix], 
"""
class hero:
	def __init__(self,askari_x,askari_y):
		
	#--------------------------------------------	
		self.askari_x = askari_x
		self.askari_y = askari_y
		self.tirin = 0
		self.RIGHT = False
		self.LEFT = False
		self.ero = 0
		self.ballaca_shaashada = 750
		self.boodid = False
		self.karaarinta = 20
		self.dhirirka_labooday = karaarinta
		self.cufasjiidadka = 1
	#---------------------------------------------
	def bg(self):
		shaashada.blit(bg_list[0],[self.ero,0])
		shaashada.blit(bg_list[1],[self.ballaca_shaashada+self.ero,0])
		shaashada.blit(bg_list[2],[self.ballaca_shaashada+self.ballaca_shaashada+self.ero,0])
		shaashada.blit(bg_list[3],[self.ballaca_shaashada+self.ballaca_shaashada+self.ballaca_shaashada+self.ero,0])

	def dhaqaaji(self,FALKADHACAY):
		if FALKADHACAY[K_RIGHT]:
			self.RIGHT = True
			self.LEFT = False
		elif FALKADHACAY[K_LEFT]:
			self.RIGHT = False
			self.LEFT = True
		else:
			self.LEFT = False
			self.RIGHT = False
	def sawirid(self):
		if self.tirin >=9:
			self.tirin = 0
		if self.askari_x <= 0:
			self.LEFT = False
		if askari_x >= ballaca_shaashada-100:
			RIGHT = False
		if self.RIGHT and self.askari_x <= self.ballaca_shaashada-60:
			if self.ero != -2270:
				self.ero -= 5
			else:
				self.askari_x +=3
			if self.askari_x < self.ballaca_shaashada//3 :
				self.askari_x +=3
				
			shaashada.blit(dhaqaajinta_midig[self.tirin],[self.askari_x,self.askari_y])
			self.tirin +=1
		elif self.LEFT:
			#------------------------------------------------
			if self.ero < 0:
				self.ero +=5

			if self.askari_x >  self.ballaca_shaashada//2:
				self.askari_x -= 3
			if self.askari_x > 0 and self.ero == 0:
				self.askari_x -= 3
			#--------------------------------------------------
			shaashada.blit(dhaqaajinta_bidix[self.tirin] , [self.askari_x,self.askari_y])
			self.tirin += 1

		

		else:
			shaashada.blit(standing,[self.askari_x,self.askari_y])
	
	def kor_uboodid(self,FALKADHACAY):
		if FALKADHACAY[K_UP] and self.boodid == False:
			self.boodid = True

		if self.boodid:
			self.askari_y -= self.karaarinta
			self.karaarinta -= self.cufasjiidadka
		if self.karaarinta <-20:
			self.karaarinta = 20
			self.boodid= False

player = hero(askari_x,askari_y)
ciyaarta_waa_play = True	


#main loop 'main logic'
while ciyaarta_waa_play:
	shaashada.fill([0,0,0])
	player.bg()
	fps.tick(30)
	for event in pygame.event.get():
		if event.type == QUIT:
			ciyaarta_waa_play = False

	FALKADHACAY = pygame.key.get_pressed()
	player.sawirid()

	player.dhaqaaji(FALKADHACAY)
	player.kor_uboodid(FALKADHACAY)
	if FALKADHACAY[K_ESCAPE]:
		ciyaarta_waa_play = False

	pygame.display.update()



pygame.quit()

