import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(20, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Kilowatts Used"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(20, 58)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Base Rate"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(20, 81)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Surchage"
		self._label3.Click += self.Label3Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(20, 360)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 3
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(101, 360)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 4
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(182, 360)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 5
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(20, 104)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "City Tax"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(20, 127)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Pay this amount"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(20, 150)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 8
		self._label6.Text = "After May 20th Pay"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(213, 32)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 9
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(126, 58)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(187, 23)
		self._label7.TabIndex = 10
		self._label7.Text = "label7"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(213, 81)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 11
		self._label8.Text = "label8"
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(213, 104)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 12
		self._label9.Text = "label9"
		# 
		# label10
		# 
		self._label10.Location = System.Drawing.Point(213, 127)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 13
		self._label10.Text = "label10"
		# 
		# label11
		# 
		self._label11.Location = System.Drawing.Point(213, 150)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 14
		self._label11.Text = "label11"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(325, 469)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "P 93a"
		self.ResumeLayout(False)
		self.PerformLayout()

# 993 * 0.0475 + ((0.1) * 993 * 0.0475) + ((0.03) * 993 *0.0475)

	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		ku = float(self._textBox1.Text)
		br =  round(ku * 0.0475, 2) 
		self._label7.Text = "" +  str(ku) + " @ $0.0475 $" + str(br) 
		sc = 0.1 * ku * 0.0475
		rsc = round(sc, 2)
		self._label8.Text = "$" + str(rsc) 
		ct = round(0.03 * ku *0.0475, 2)
		self._label9.Text = "$" + str(ct)
		pta = br + rsc + ct
		self._label10.Text = "$" + str(pta)
		amtp = round(pta + pta * 0.04, 2)
		self._label11.Text = "$" + str(amtp)

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""