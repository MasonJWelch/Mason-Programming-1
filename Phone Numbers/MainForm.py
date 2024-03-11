import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(146, 206)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._label1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label1.Location = System.Drawing.Point(360, 47)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 110)
		self._label1.TabIndex = 1
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(370, 206)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(621, 206)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self.ClientSize = System.Drawing.Size(817, 313)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Phone Numbers"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "List: \n (608) 554-3712 \n (715) 384-3326 \n (608) 754-5015 \n (608) 758-9410 \n (608) 563-0801 "


	def Label1Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()