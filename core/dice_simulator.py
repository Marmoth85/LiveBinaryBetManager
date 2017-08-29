from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot

from gen_files import ui_dice_simulator
from . import gambling


class DiceSimulator(QWidget, gambling.Gambling, ui_dice_simulator.Ui_DiceSimulator):
    
    def __init__(self, parent=None):
        
        print("DiceSimulator : On entre dans le constructeur")
        super(DiceSimulator, self).__init__(parent)
        self.setupUi(self)
        print("DiceSimulator : On sort du le constructeur")
    
    @pyqtSlot('QString')
    def currency_changed(self):
        """Ce SLOT est activé lorsque l'utilisateur change de monnaie dans le combobox.
        Il s'agit alors d'ajuster la précision des double_spin_box de la trésorerie et des paris, de façon à ce que les
        incréments correspondent à la "force" des monnaies choisies"""
        
        print("DiceSimulator: On entre dans le SLOT currency_changed")
        print("DiceSimulator: On sort du SLOT currency_changed")
    
    @pyqtSlot()
    @pyqtSlot(int)
    def precision_changed(self):
        """Ce SLOT est déclenché lorsque l'un des spinBox de précision est modifié. Il sert à modifier les incréments
        par défaut des spinbox d'entrée, de façon à pouvoir cliquer sur up et down un nombre restreint de fois."""
        
        print("DiceSimulator: On entre dans le SLOT precision_changed")
        print("DiceSimulator: On sort du SLOT precision_changed")
    
    @pyqtSlot()
    def compute_expectation(self):
        """Cette méthode est un SLOT déclenché par le bouton "Calculer".
        On calcule les paramètres théoriques souhaités ainsi que ceux, pragmatiques, quand la trésorerie réelle ne
        correspond pas à ce que nous voudrions sur un plan purement théorique."""
        
        print("DiceSimulator: On entre dans le SLOT compute_expectation")
        print("DiceSimulator: On sort du SLOT compute_expectation")
        
    @pyqtSlot()
    def bet_clicked(self):
        """Ce SLOT est déclenché par un des radioButton liés à la stratégie des mises lors de paris gagnés ou perdus.
        Ici, on s'assure qu'un seul radioButton ne peut être activé pour un pari gagnant et pour un pari perdant."""

        print("DiceSimulator: On entre dans le SLOT bet_clicked")
        print("DiceSimulator: On sort du SLOT bet_clicked")
    
    def load_input_data(self):
        """Cette méthode récupère les informations depuis l'IHM pour les stocker dans les attributs d'objets,
                afin de pouvoir les exploiter facilement dans les calculs qui suivront."""

        print("DiceSimulator: On entre dans le SLOT load_input_data")
        print("DiceSimulator: On sort du SLOT load_input_data")

    def update_result_data(self):
        """Cette méthode récupère les résultats des calculs effectués pour les afficher dans l'IHM"""

        print("DiceSimulator: On entre dans le SLOT update_result_data")
        print("DiceSimulator: On sort du SLOT update_result_data")

    def check_inputs(self):
        """Cette méthode a pour objet de vérifier que les inputs soient cohérents.
                Aucun calcul ne doit être lancé sans être assuré de la bonne forme des paramètres d'entrée"""

        print("DiceSimulator: On entre dans le SLOT check_inputs")
        print("DiceSimulator: On sort du SLOT check_inputs")
