import sys
import os
import pprint

lista = {
	"fs13":"D:/Programas/Farming Simulator 2013/FarmingSimulator2013.exe",
	"teste":"D:/Programas/SpeedAutoClicker.exe",
	"csgo":"D:/Programas/Counter-Strike Global Offensive/Run_CSGO.exe",
	"ets2":"D:/Programas/EuroTruck Simulator 2/bin/win_x86/eurotrucks2.exe",
	"cs16":'"D:/Programas/CounterStrike 1.6/hl.exe" -game cstrike',
	"pb":"D:/Programas/Pointblank/PBLauncher.exe",
	"gtavc":"D:/Programas/GTA Vice City/gta-vc.exe",
	"gtasa":"D:/Programas/GTA San Andreas/GTA San Andreas/gta_sa.exe",
	"pinball":"D:/Programas/Pinball/pinball.exe",
	"samp":"D:/Programas/GTA San Andreas/GTA San Andreas/samp.exe",
	"woshaulin":"D:/Programas/18 Wheels of Steel Haulin/haulin.exe",
	"mc":"C:/Users/User/Desktop/Minecraft.exe",
	"stk":"D:/Programas/SuperTuxKart/supertuxkart.exe"
    }

def rungame(name):
	os.system(lista[name])

try:
	rungame(sys.argv[1])
except IndexError:
	print("Lista de comandos disponíveis")
	pprint.pprint(lista)	
