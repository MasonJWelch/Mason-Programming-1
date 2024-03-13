import math
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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei UI", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Red
		self._label1.Location = System.Drawing.Point(35, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Speed limit: "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei UI", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Red
		self._label2.Location = System.Drawing.Point(35, 177)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Fine:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei UI", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Red
		self._label3.Location = System.Drawing.Point(34, 106)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Vehicle speed:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.ForeColor = System.Drawing.Color.Red
		self._textBox1.Location = System.Drawing.Point(165, 32)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.ForeColor = System.Drawing.Color.Red
		self._textBox2.Location = System.Drawing.Point(165, 106)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.Control
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.ForeColor = System.Drawing.Color.Red
		self._label4.Location = System.Drawing.Point(165, 177)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 5
		self._label4.Click += self.Label4Click
		# 
		# button1
		# 
		self._button1.ForeColor = System.Drawing.Color.Red
		self._button1.Location = System.Drawing.Point(12, 318)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.ForeColor = System.Drawing.Color.Red
		self._button2.Location = System.Drawing.Point(322, 318)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(165, 318)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(409, 425)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.ForeColor = System.Drawing.Color.Red
		self.Name = "MainForm"
		self.Text = "P 82a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		limit = float(self._textBox1.Text)
		vehicle = float(self._textBox2.Text)
		fine = 20 + (vehicle - limit) * 5
		self._label4.Text = str(fine)

	def Label4Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button3Click(self, sender, e):
		self._label4.Text = ""
		self._textBox2.Text = ""
		self._textBox1.Text = ""
		