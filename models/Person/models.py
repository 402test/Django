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
#  DateField == datetime.date  class DateField(auto_now=False, auto_now_add=False, **options)
# DateTimeField  == datetime.datetime class DateTimeField(auto_now=False, auto_now_add=False, **options)
# TimeField  class TimeField(auto_now=False, auto_now_add=False, **options)  ==   datetime.time
#  auto_now 大多用于修改日期   在调用Model.save(). 后 会自动更新    。  auto_now_add  大多用于创建时间
# auto_now 或 auto_now_add被设置为True后，这样做会导致字段成为editable=False和blank=True的状态。editable=False将导致字段不会被呈现在admin中，blank=Ture表示允许在表单中不输入值。
# EmailField
#  FileField  文件上传字段    upload_to  案例如下
class MyModel(models.Model):
	# file will be uploaded to MEDIA_ROOT/uploads
	upload = models.FileField(upload_to='uploads/')  #记得设置 MEDIA_ROOT
	# or...
	# file will be saved to MEDIA_ROOT/uploads/2015/01/30
	upload_t = models.FileField(upload_to='uploads/%Y/%m/%d/')
#  upload_to  也可以自定义
def user_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModelss(models.Model):
	upload = models.FileField(upload_to=user_directory_path)

# IntegerField
# GenericIPAddressField
# SlugField


# 关联关系字段