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

# kalarada --waxaa jiro kalaro badan balse hadda waxaa u baahanay kaliya labo ama kayar saa filaayo sababto ah waxaa isticmaalayaa sawiro
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
	dhaqaajinta_bidix[sawir-1] = pygame.image.load(os.path.join('sawiro','L' + str(sawir) + '.png'))
	sawir +=1
#--------------------------------------------------------------------------------------------
#sawiraanta dhanka idig waa kuwaan
dhaqaajinta_midig = [None]*10# intana sidoo kle
for sawir in range(1,10):
	dhaqaajinta_midig[sawir-1] = pygame.image.load(os.path.join('sawiro','R' + str(sawir) + '.png'))
	sawir +=1
#sawirkaan waxaa loogu talagalay marka uu san meelna u dhaqaaqin sawir taaganlee soo baxaayo
#------------------------------------------------------------------
standing = pygame.image.load('sawiro/standing.png')
#------------------------------------------------------------------

#sawiraanta zombiyaha
zombbie_list = [None]*10
#-----------------------------

#sawirka xabada
xabad = pygame.transform.scale(pygame.image.load('sawiro/XABAD.png'),[10,10])

# sawirka diyaaradda
helicop = pygame.transform.scale(pygame.image.load('helicopter.png'),[200,100])
# madoorsoomayaa sha gameka
fps = pygame.time.Clock() #fps waxaa lagasoo gaabiyey frame per second yacnii inta u qaadanayo inuu shayga kusoo sawiro shashashada
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
[midig/bidix], backgrounka ------ IWM
"""
class hero:
	def __init__(self,askari_x,askari_y):
		
	#--------------------------------------------	
		self.askari_x = askari_x
		self.askari_y = askari_y
		self.tirin = 0
		self.RIGHT = False
		self.LEFT = False
		self.ero = 0 # ero waa variable dhaqaajinaayo backrounka
		self.ballaca_shaashada = 750
		self.boodid = False
		self.karaarinta = 20
		self.dhirirka_labooday = karaarinta
		self.cufasjiidadka = 1
		self.guns = []
		self.xabad_qaboojiye = 0
	#---------------------------------------------------
	def bg(self):
		shaashada.blit(bg_list[0],[self.ero,0])
		shaashada.blit(bg_list[1],[self.ballaca_shaashada+self.ero,0])
		shaashada.blit(bg_list[2],[self.ballaca_shaashada+self.ballaca_shaashada+self.ero,0])
		shaashada.blit(bg_list[3],[self.ballaca_shaashada+self.ballaca_shaashada+self.ballaca_shaashada+self.ero,0])
	#---------------------------------------------------
	def dhaqaaji(self,FALKADHACAY): #methodkaan wuxuu dhagesanaya keyboardka key ga lariixay kadibna soo celin xogta
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
			"""----------------------------------------------------------------------------------------------------------------------------
			kodka hoose waxaa uu sheegaya haddi ee dhammaanin afarta backgeound taas wexee la micno
			in backround dhimanyay waxaana ero laga jaraa -5 haddii kale wuu dhammaaday playerkana wuxuu joogaa outside of the village
			markaas waxaa socodsiinayaa player ilaa uu drbiga ka kaaro  
			----------------------------------------------------------------------------------------------------------------------------
			"""
			if self.ero != -2270:
				self.ero -= 5
			else:
				self.askari_x +=3
			"""-----------------------------------------------------------------
			koodkaanna wuxuu sheegayaa player markuu joogo darbiga dhanka bidix
			inuu midig u dhaqaaqi karo ilaa uu ka gaaro dhaxbartamaha sabtoo ah 
			markii backrounka scodo asna darbig ayuu  iska joogaya waa tijaabi kartaa xitaa

			"""
			#-------------------------------------------------------------------------
			if self.askari_x < self.ballaca_shaashada//3 :
				self.askari_x +=3
			#------------------------------------------------------------------------------	
			shaashada.blit(dhaqaajinta_midig[self.tirin],[self.askari_x,self.askari_y])
			self.tirin +=1
		elif self.LEFT:
			#------------------------------------------------
			if self.ero < 0:
				self.ero +=5
			"""
			intanna waa intii haddaye oo lagusameeye dhanka midig
			"""
			#---------------------------------------------------------
			if self.askari_x >  self.ballaca_shaashada//2:
				self.askari_x -= 3
			if self.askari_x > 0 and self.ero == 0:
				self.askari_x -= 3
			#--------------------------------------------------
			shaashada.blit(dhaqaajinta_bidix[self.tirin] , [self.askari_x,self.askari_y])
			self.tirin += 1

		
		else:
			shaashada.blit(standing,[self.askari_x,self.askari_y])
	"""
	methodka hoosena wuxuu ugu talagay boodida
	waxaa laga yaabaa inaa isweediiso maxaa funtionka dhaqaajinta ugu dari weresay 
	it doesn't matter iskumid lee waaye sida kuu roon yeel 
	"""
	def kor_uboodid(self,FALKADHACAY):
		if FALKADHACAY[K_UP] and self.boodid == False:
			self.boodid = True

		if self.boodid:
			self.askari_y -= self.karaarinta
			self.karaarinta -= self.cufasjiidadka
		if self.karaarinta <-20:
			self.karaarinta = 20
			self.boodid= False
	

	#xabadaynta
	# functionka hoose wuxuu hubinaya mesha uu player xabadeynayo kadib moving  functionka ee claska xabadaha xogta u gudbinayaa
	def direction(self):
		if self.RIGHT:
			return 1
		elif self.LEFT:
			return -1


	def shoot(self):
		if FALKADHACAY[K_SPACE]:
			dush.play()
			if self.RIGHT or self.LEFT:
				GUN = gun_machanic(self.askari_x,self.askari_y,self.direction())
				self.guns.append(GUN)
		for xabado in self.guns:
			xabado.move()
	def delete(self):
		self.guns.pop()
#---------------------------------------------------------------------
#claskaan wuxuu kusoo darayaa zombie
class zombie:
	pass
#---------------------------------------------------------------------------
#classkan waxa uu qaabilsanyaha xabada inuu habeeyo
class gun_machanic:
	def __init__(self,x,y,direction):
		self.x = x +15
		self.y = y + 30
		self.direction = direction
	def draw_guns(self):
		shaashada.blit(xabad,[self.x,self.y])
	def move(self):
		if self.direction == 1:
			self.x +=10
			if self.x >=ballaca_shaashada:
				player.delete()
		if self.direction == -1:
			self.x -= 10
			if self.x <=0:
				player.delete()


class helicopter:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def sawir_helicopter(self,shaashada):
		shaashada.blit(helicop,[self.x,self.y])
	def move_helicopter(self):
		self.x +=3
		if self.x == 3000:
			self.x = 100
		if self.x >= 0 and self.x <ballaca_shaashada:
			helicop_sound.play()
diyaarad = helicopter(0,dhirirka_shaashada-300-200)



player = hero(askari_x,askari_y)






ciyaarta_waa_play = True	


# codadka gameka 
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
dush = pygame.mixer.Sound('pop.ogg')
pygame.mixer.music.play()

helicop_sound = pygame.mixer.Sound('helicoptersound.wav')

#main loop 'main logic'
while ciyaarta_waa_play:
	shaashada.fill([0,0,0])
	#backrounka
	player.bg()

	for gun in player.guns:
		gun.draw_guns()
		

	fps.tick(30)
	for event in pygame.event.get():
		if event.type == QUIT:
			ciyaarta_waa_play = False

	FALKADHACAY = pygame.key.get_pressed()
	#kusoo sawirid playerka shaashada
	player.sawirid()
	
	diyaarad.sawir_helicopter(shaashada)
	diyaarad.move_helicopter()
	#---------------------------------

	#dhaqaajint player [midig/bidix]
	player.dhaqaaji(FALKADHACAY)
	#boodida
	player.kor_uboodid(FALKADHACAY)


	#xabadaynta
	player.shoot()

	#qofka haddu scape taabto ciyaarta waa u kabaxmayaa
	if FALKADHACAY[K_ESCAPE]:
		ciyaarta_waa_play = False

#-----------------------------------------
	#horor.sawiri_horor(shaashada)#-----------
#---------------------------------------------
	pygame.display.update()



pygame.quit()

"""
Hello i am Abdirizak i am the outhor of this game ,
this game is alittle bit fun game and it's super cool you can try it if u wanna,
i will call this game Xeroshiino village,
for particular reason hhhhhh if u intresting to tell you what it is, you can message me HEHE just kidding no big deal,

feel free to copy my code and use it 


HOPE U TO ENJOY!

SALAAAM '''''JAW'''BYE''

"""