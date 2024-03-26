import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._button1.Location = System.Drawing.Point(13, 166)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._button2.Location = System.Drawing.Point(94, 166)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._button3.Location = System.Drawing.Point(175, 166)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.InactiveCaptionText
		self._listBox1.ForeColor = System.Drawing.Color.Turquoise
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(24, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(204, 147)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Yellow
		self.ClientSize = System.Drawing.Size(285, 223)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "P 122d"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "x\t\ty"
		self._listBox1.Items.Add(heading)
		for num in range(-12, 16+1):
			nsqrd = num*4
			#y = num**6 - (3*num)**5 - (93 * num)**4 + (87 * num)**3 + (1596 * num)**2 - (1380 * num) - 2800
			y = num**6 - 3*num**5 - 93 * num**4 + 87 * num**3 + 1596 * num**2 - 1380 * num - 2800
			msg = str(num) + "\t\t" + str(y)  
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()