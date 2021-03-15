from random import randint
#lists and varibles
loggedIN = False
password = 'Carguy_2008'
EXLVL = 0
INLVL = 0
TURLVL = 0
ENLVL = 0
FILVL = 0
GASLVL = 0
FPLVL = 0
NITLVL = 0
money = 100
hp = 80
run = True
results = []
Emin = [None, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200,  1300,  1400,  1500,  1600,  1700,  1800,  1900]
Emax = [None, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200,  1300,  1400,  1500,  1600,  1700,  1800,  1900, 2000] 
#funcions
def enemy(hp, Emin, eMax):
	if hp >  Emin[1] and hp < eMax[1]:
		enemyHp = randint(Emin[1], eMax[1])
		return enemyHp
	if hp >  Emin[2] and hp < eMax[2]:
		enemyHp = randint(Emin[2], eMax[2])
		return enemyHp
	if hp >  Emin[3] and hp < eMax[3]:
		enemyHp = randint(Emin[3], eMax[3])
		return enemyHp
	if hp >  Emin[4] and hp < eMax[4]:
		enemyHp = randint(Emin[4], eMax[4])
		return enemyHp
	if hp >  Emin[5] and hp < eMax[5]:
		enemyHp = randint(Emin[5], eMax[5])
		return enemyHp
	if hp >  Emin[6] and hp < eMax[6]:
		enemyHp = randint(Emin[6], eMax[6])
		return enemyHp
	if hp >  Emin[7] and hp < eMax[7]:
		enemyHp = randint(Emin[7], eMax[7])
		return enemyHp
	if hp >  Emin[8] and hp < eMax[8]:
		enemyHp = randint(Emin[8], eMax[8])
		return enemyHp
	if hp >  Emin[9] and hp < eMax[9]:
		enemyHp = randint(Emin[9], eMax[9])
		return enemyHp
	if hp >  Emin[10] and hp < eMax[10]:
		enemyHp = randint(Emin[10], eMax[10])
		return enemyHp


	if hp >  Emin[11] and hp < eMax[11]:
		enemyHp = randint(Emin[11], eMax[11])
		return enemyHp
	if hp >  Emin[12] and hp < eMax[12]:
		enemyHp = randint(Emin[12], eMax[12])
		return enemyHp
	if hp >  Emin[13] and hp < eMax[13]:
		enemyHp = randint(Emin[13], eMax[13])
		return enemyHp
	if hp >  Emin[14] and hp < eMax[14]:
		enemyHp = randint(Emin[14], eMax[14])
		return enemyHp
	if hp >  Emin[15] and hp < eMax[15]:
		enemyHp = randint(Emin[15], eMax[15])
		return enemyHp
	if hp >  Emin[16] and hp < eMax[16]:
		enemyHp = randint(Emin[16], eMax[16])
		return enemyHp
	if hp >  Emin[17] and hp < eMax[17]:
		enemyHp = randint(Emin[17], eMax[17])
		return enemyHp
	if hp >  Emin[18] and hp < eMax[18]:
		enemyHp = randint(Emin[18], eMax[18])
		return enemyHp
	if hp >  Emin[19] and hp < eMax[19]:
		enemyHp = randint(Emin[19], eMax[19])
		return enemyHp
	if hp >  Emin[20] and hp < eMax[20]:
		enemyHp = randint(Emin[20], eMax[20])
		return enemyHp
	




while run:
	action = input(f'£{money} | {hp}hp \nAction:\n>').lower()
	if action == 'race':
		enemy_hp = enemy(hp, Emin, Emax)
		try:
			bet = int(input('Bet:\n>'))
		except ValueError:
			bet = 0
		if bet <= money:
			if hp >= enemy_hp:
				print('you won!')
				money += bet
				results.append('win')
			else:
				print('you lost')
				money -= bet
				results.append('lost')
		else:
			print('That bet is more money that you have!')
	if action == 'info':
		wins = 0
		loses = 0
		for result in results:
			if result == 'win':
				wins += 1
			if result == 'lost':
				loses += 1
		try:
			WTL = wins / loses
		except:
			WTL = 0
		print(f'wins: {wins} | loses: {loses} \nWins to Loses: {WTL}')
	if action == 'quit' or money <= 0:
		print('Bye!')
		run = False

	if action == 'mod':
		mRun = True
		while mRun:
			print(f'	/MOD SHOP/')
			print(f'	Engine - +400hp -£10,000 lv{ENLVL}/1')
			print(f'	Nitros - +250hp -£6,750 lv{NITLVL}/3')
			print(f'	Fuel - +200hp -£5,400 {GASLVL}/1')
			print(f'	Turbo - +60hp -£1,850 lv{TURLVL}/2' )
			print(f'	Intake - +40hp -£1400 lv{INLVL}/5')
			print(f'	Fuel Pump - +50hp -£1,750 lv{FPLVL}/1')
			print(f'	Exhaust - +40hp -£1,400 lv{EXLVL}/5')
			print(f'	Quit - to leave the program')
			modSel = input('	Mod:\n	>').lower()
			if modSel == 'engine' and money >= 10000 and ENLVL < 1:
				money -= 10000
				hp += 400
				print('You bought an engine!')
				ENLVL += 1
			if modSel == 'turbo' and money >= 1850 and TURLVL < 2:
				money -= 1850
				hp += 60
				TURLVL += 1
				print('You bought an Turbo!')
			if modSel == 'intake' and money >= 1400 and INLVL < 5:
				money -= 1400
				hp += 40
				INLVL += 1
				print('You bought an Intake!')
			if modSel == 'exhaust'  and money >= 1400 and EXLVL < 5:				
				money -= 1400
				hp += 40
				EXLVL += 1
				print('You bought an Exhaust!')
			if modSel == 'nitros' and money >= 6750 and NITLVL < 3:
				money -= 6750
				hp += 250
				NITLVL += 1
				print('You bought a nitros Kit upgrade.')
			if modSel == 'fuel' and money >= 5400 and GASLVL < 1:
				hp += 200
				money -= 5400
				GASLVL += 1
				print('You upgraded your fuel.')
			if modSel == 'fuel pump' and money >= 1750 and FPLVL > 1:
				hp += 50
				money -= 1750
				FPLVL += 1
				print('You got a better fuel pump.')

			
			if modSel == 'quit':
				mRun = False
	if action == 'admin':
		if loggedIN == False:
			aPassword = input('Password:\n>')
			if aPassword == password:
				loggedIN = True
		if loggedIN:
			adIn = input('Admin:\n>')
			adOp = adIn.split('=')[0]
			adVal = adIn.split('=')[1]
			if adOp == 'hp':
				if int(adVal) <= 1000:
					hp = int(adVal)
				else:
					hp = 1000
			if adOp == 'money':
				money = adVal
			if adOp == 'all_mod':
				if adVal == 'True':
					ENLVL = 1
					TURLVL = 2
					INLVL = 5
					EXLVL = 5
					GASLVL = 1
					NITLVL = 3
					FPLVL = 1
					hp = 2000

