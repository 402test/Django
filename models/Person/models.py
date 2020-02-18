from django.db import models

# Create your models here.

class Person(models.Model):
	"""
	docstring for Person
	 记得修改 INSTALLED_APPS 
	表名是 app_name + Person
	会自动 为表格添加上 id 字段  id = models.AutoField(primary_key=True)
	自己设置 一个字段 为 primary_key=True   将不会自动在表（模型）中添加 id 列
	"""
	first_name = models.CharField(max_length=30,verbose_name="first name ") #  默认 NOT NULL
	last_name = models.CharField(max_length=30)
	#  字段选项
	# null  blank  这两个 通常是在设置该字段可以为空的时候使用   null=True， blank=False
    #  choices     如下   Student

	#  db_column   定义 字段在 数据库的 名称
	#  db_index  如果设置为 True 则 会为该字段创建一个数据库索引
	#   editable 如果设置为 false  那么这个字段 就不会出现在 admin  或者  其它 modelform 里面  也会跳过模型验证
	#    自定义错误提示   如下  null, blank, invalid, invalid_choice, unique, and unique_for_date  等等
    #    email = forms.EmailField(error_messages={'required':'邮箱不能为空','invalid':"邮箱格式不对"})
	# unique  唯一
class Student(models.Model):
	FRESHMAN = 'FR'
	SOPHOMORE = 'SO'
	JUNIOR = 'JR'
	SENIOR = 'SR'
	YEAR_IN_SCHOOL_CHOICES = [
		(FRESHMAN, 'Freshman'),
		(SOPHOMORE, 'Sophomore'),
		(JUNIOR, 'Junior'),
		(SENIOR, 'Senior'),
	]
	year_in_school = models.CharField(
		max_length=2,
		choices=YEAR_IN_SCHOOL_CHOICES,
		default=FRESHMAN,
	)

	def is_upperclass(self):
		return self.year_in_school in (self.JUNIOR, self.SENIOR)

	'''
	s = Student(YEAR_IN_SCHOOL_CHOICES="FR")
	 s.save()
	 s.YEAR_IN_SCHOOL_CHOICES  ---->   FR
	 s.get_YEAR_IN_SCHOOL_CHOICES_display()   ---->Freshman
	'''

#  字段类型

#  AutoField   IntegerField 型  自增    还有类似的  BigAutoField BigIntegerField
# BigIntegerField  长整型
# BooleanField  布尔型  默认true
# CharField 字符串类型   长度不够的时候  用 TextField.