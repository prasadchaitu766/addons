# -*- coding: utf-8 -*-
from datetime import datetime

import random
import string
import smtp
from random import randint

from odoo import models, fields, api

class StudentRegistaration(models.Model):
	_name = "student.register"


	s_id = fields.Char(string="Student-id" readonly=True)
	name = fields.Char(string="StudentName") 
	age = fields.Integer(string="Age",help="enter age")
	date_of_birth = fields.Date(string="Date-Of-Birth")
	gender = fields.Selection([("male","Male"),("female","Female"),("others","Others")],string="Gender")
	address =fields.Text(string="Address")
	image = fields.Binary()
	email = fields.Char(string="Email")
	contact = fields.Char(string="Contact")
	qualification = fields.Many2one("qualification.qualification",string="Qualification")
	username = fields.Char(string="Username")
	password = fields.Char(string="Password")

	@api.onchange('date_of_birth')
	def Calculate_age(self):
		if not self.date_of_birth:
			self.age=0
		else:
			today_date = datetime.now().year
			date_split = self.date_of_birth.split('-',1)
			birth_year = date_split[0]
			self.age = today_date-int(birth_year)


	@api.multi
	def generate_record_name(self):
		# self.username="prasad"
		f=({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})
		self.username=f["name"]

	@api.multi
	def generate_record_password(self):
		self.ensure_one()
		g=({'password': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(12,15)))
})		
		self.password=g["password"]
		

		
	@api.one

	def generate_student_id(self):
		if self.s_id ==False:
			next_id = self.env["ir.sequence"].next_by_code("test_seq_id")
			self.s_id =next_id
		else:
			pass
	def send_mail_template(self): 
        # Find the e-mail template
        template = self.env.ref('student.example_email_template1')
        # Send out the e-mail template to the user
        self.env['mail.template'].browse(template.id).send_mail(self.id, force_send=True)







class qualification(models.Model):
	_name ="qualification.qualification"

	name=fields.Char(string="Qualification_Name")



	
# 	@api.multi
# 	def generate_record_password(self):
# 		self.ensure_one()
# 		g=self.write({'password': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(12,15)))
# })		
# 		self.password=g
# 		return True

