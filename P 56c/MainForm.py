import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.SlateBlue
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(25, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(213, 53)
		self._label1.TabIndex = 0
		self._label1.Text = "Radius:"
		self._label1.Click += self.Label1Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(255, 20)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(254, 38)
		self._textBox1.TabIndex = 2
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SlateBlue
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(25, 240)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(213, 51)
		self._label3.TabIndex = 4
		self._label3.Text = "Area:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.SlateBlue
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(25, 324)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(213, 51)
		self._label4.TabIndex = 5
		self._label4.Text = "Circumference"
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(255, 240)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(254, 51)
		self._label5.TabIndex = 7
		self._label5.Text = " "
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(255, 324)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(254, 51)
		self._label6.TabIndex = 6
		self._label6.Text = " "
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(12, 418)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(234, 92)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(252, 418)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(125, 92)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(384, 418)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(125, 92)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Indigo
		self.ClientSize = System.Drawing.Size(524, 528)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		radius = float(self._textBox1.Text)
		pi = 3.14159
		area   = pi * radius**2
		perim  = 2 * pi * radius 
		self._label5.Text = str(area)
		self._label6.Text = str(perim)
		# + - * / %     ** pow     // divide & round down
		# int (Integer): a whole number, pos/neg
		# float (Floating-Point Number): any number w/ a decimal
		# str (String): a string of text

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label1Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass