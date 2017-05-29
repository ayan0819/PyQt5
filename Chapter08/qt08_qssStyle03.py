# -*- coding: utf-8 -*-

'''
    【简介】
	 QSS样式
    
'''

from PyQt5.QtWidgets import *
import sys  
    
class WindowDemo(QWidget):  
	def __init__(self):
		super(WindowDemo, self).__init__();
		self.InitUI();

	def InitUI(self):                   	
		combo = QComboBox(self)
		combo.addItem('Window')
		combo.addItem('Ubuntu')
		combo.addItem('Red Hat')
		combo.move(50,50)  	
		self.setGeometry(250,200,350,250)
		self.setWindowTitle('QComboBox')
  
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	win = WindowDemo()  
	qssStyle = '''      			  			
			QComboBox::drop-down { 
                 image: url( ./images/dropdown.png)
            }
				
		'''
	win.setStyleSheet( qssStyle ) 				
	win.show()  
	sys.exit(app.exec_())
