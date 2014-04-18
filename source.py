import chooseOption
import game

menu=chooseOption.Menu()
menu.show()

ddr=game.Game()
ddr.initiate()
ddr.play()
