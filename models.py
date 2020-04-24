
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class AgeDescriptors(models.Model):
    age_descriptor = models.CharField(db_column='Age_Descriptor', primary_key=True, max_length=45)  # Field name made lowercase.
    def __str__(self):
        return self.age_descriptor
    class Meta:
        managed = False
        db_table = 'age_descriptors'

class Genders(models.Model):
    gender = models.CharField(db_column='Gender', primary_key=True, max_length=15)  # Field name made lowercase.
    def __str__(self):
        return self.gender
    class Meta:
        managed = False
        db_table = 'genders'

class MaritalStatus(models.Model):
   
    marital_status = models.CharField(db_column='marital_status',primary_key=True,  max_length=20)
    def __str__(self):
        return self.marital_status
    class Meta:
        managed = False
        db_table = 'marital_status'

class Physicians(models.Model):
    physician = models.CharField(db_column='Physician', primary_key=True, max_length=45)  # Field name made lowercase.
    def __str__(self):
        return self.physician
    class Meta:
        managed = False
        db_table = 'physicians'

class Relations(models.Model):
    relation = models.CharField(db_column='Relation', primary_key=True, max_length=45)  # Field name made lowercase.
    def __str__(self):
        return self.relation
    class Meta:
        managed = False
        db_table = 'relations'

class Seeds(models.Model):
    counter = models.AutoField(primary_key=True)
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prefix = models.CharField(max_length=45, blank=True, null=True)
    month = models.SmallIntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    month_seed = models.SmallIntegerField(blank=True, null=True)
    year_seed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seeds'

class Units(models.Model):
    unit = models.CharField(db_column='Unit', primary_key=True, max_length=10)  # Field name made lowercase.
    def __str__(self):
        return self.unit
    class Meta:
        managed = False
        db_table = 'units'

class BillingCategories(models.Model):
    billing_category = models.CharField(primary_key=True, max_length=45)
    def __str__(self):
        return self.billing_category
    class Meta:
        managed = False
        db_table = 'billing_categories'

class Departments(models.Model):
    department = models.CharField(db_column='Department', primary_key=True, max_length=45)  # Field name made lowercase.
    def __str__(self):
        return self.department
    class Meta:
        managed = False
        db_table = 'departments'
    



class OpdRegister(models.Model):

    #-------------------------------------------------------------------
# creating a validator function 
#def validate_for_number(self): 
#	    if  self.isnumeric(): 
#		    pass
#	    else: 
#		    raise ValidationError("Hello Dear, number only") 
#-------------------------------------------------------------------


    counter = models.AutoField(db_column='Counter', primary_key=True)  # Field name made lowercase.
    opno = models.CharField(db_column='OPNo', unique=True, max_length=20)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    middle_name = models.CharField(db_column='Middle_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age',max_length=2,blank=False,null=False)  # Field name made lowercase.
    age_descriptor = models.ForeignKey(AgeDescriptors, models.DO_NOTHING, db_column='Age_Descriptor', blank=True, null=True)  # Field name made lowercase.
    gender = models.ForeignKey(Genders, models.DO_NOTHING, db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    #mobile = models.CharField(db_column='Mobile', max_length=10, blank=True, null=True,validators=[RegexValidator(regex=r'[0-9]+',message="hello")] )  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=10, blank=False, null=False)  # Field name made lowercase.
    address_1 = models.CharField(db_column='Address_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address_2 = models.CharField(db_column='Address_2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address_3 = models.CharField(db_column='Address_3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    native_place = models.CharField(db_column='Native_Place', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taluka = models.CharField(db_column='Taluka', max_length=20, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pin = models.CharField(db_column='PIN', max_length=6, blank=False, null=False,error_messages={'required':'PIN is 6 digits number'})  # Field name made lowercase.
    nextofkin = models.CharField(db_column='NextOfKin', max_length=45, blank=True, null=True)  # Field name made lowercase.
    relation = models.ForeignKey('Relations', models.DO_NOTHING, db_column='Relation', blank=True, null=True)  # Field name made lowercase.
    refered_by = models.CharField(db_column='Refered_by', max_length=45, blank=True, null=True)  # Field name made lowercase.
    department = models.ForeignKey('Departments', models.DO_NOTHING, db_column='Department', blank=True, null=True)  # Field name made lowercase.
    unit = models.ForeignKey('Units', models.DO_NOTHING, db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    physician = models.ForeignKey('Physicians', models.DO_NOTHING, db_column='Physician', blank=True, null=True)  # Field name made lowercase.
    billing_category = models.ForeignKey('BillingCategories', models.DO_NOTHING, db_column='Billing_category', blank=True, null=True)  # Field name made lowercase.
    doa = models.DateField(db_column='DOA', blank=True, null=True,help_text='TODAY')  # Field name made lowercase.
    dod = models.DateField(db_column='DOD', blank=True, null=True)  # Field name made lowercase.
    bed_no = models.CharField(db_column='Bed_No', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mlc = models.BooleanField(db_column='MLC', blank=True, null=False)  # Field name made lowercase.
    age_in_days = models.IntegerField(db_column='age_In_Days', blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(max_length=30, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    marital_status = models.ForeignKey('MaritalStatus', models.DO_NOTHING, db_column='Marital_Status', blank=True, null=True)  # Field name made lowercase.
    photo=models.ImageField(db_column='photo',upload_to="HMS/static/images", default="HMS/static/images")#file is saved in images folder
    class Meta:
        managed = False
        db_table = 'opd_register'




class IpdRegister(models.Model):
    counter = models.AutoField(db_column='Counter', primary_key=True)  # Field name made lowercase.
    ipno = models.CharField(db_column='IPNo', unique=True, max_length=20)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=45, blank=False, null=False)  # Field name made lowercase.
    middle_name = models.CharField(db_column='Middle_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=2, blank=True, null=True)  # Field name made lowercase.
    age_descriptor = models.ForeignKey(AgeDescriptors, models.DO_NOTHING, db_column='Age_Descriptor', blank=True, null=True)  # Field name made lowercase.
    gender = models.ForeignKey(Genders, models.DO_NOTHING, db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address_1 = models.CharField(db_column='Address_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address_2 = models.CharField(db_column='Address_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address_3 = models.CharField(db_column='Address_3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    native_place = models.CharField(db_column='Native_Place', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taluka = models.CharField(db_column='Taluka', max_length=20, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pin = models.CharField(db_column='PIN', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nextofkin = models.CharField(db_column='NextOfKin', max_length=45, blank=True, null=True)  # Field name made lowercase.
    relation = models.ForeignKey('Relations', models.DO_NOTHING, db_column='Relation', blank=True, null=True)  # Field name made lowercase.
    refered_by = models.CharField(db_column='Refered_by', max_length=45, blank=True, null=True)  # Field name made lowercase.
    department = models.ForeignKey('Departments', models.DO_NOTHING, db_column='Department', blank=True, null=True)  # Field name made lowercase.
    unit = models.ForeignKey('Units', models.DO_NOTHING, db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    physician = models.ForeignKey('Physicians', models.DO_NOTHING, db_column='Physician', blank=True, null=True)  # Field name made lowercase.
    billing_category = models.ForeignKey('BillingCategories', models.DO_NOTHING, db_column='Billing_category', blank=True, null=True)  # Field name made lowercase.
    doa = models.DateField(db_column='DOA', blank=True, null=True)  # Field name made lowercase.
    dod = models.DateField(db_column='DOD', blank=True, null=True)  # Field name made lowercase.
    bed_no = models.CharField(db_column='Bed_No', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mlc = models.IntegerField(db_column='MLC', blank=True, null=True)  # Field name made lowercase.
    age_in_days = models.IntegerField(db_column='age_In_Days', blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(max_length=30, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    mother = models.CharField(db_column='Mother', max_length=20, blank=True, null=True)  # Field name made lowercase.
    father = models.CharField(db_column='Father', max_length=20, blank=True, null=True)  # Field name made lowercase.
    husband = models.CharField(db_column='Husband', max_length=20, blank=True, null=True)  # Field name made lowercase.
    marital_status = models.ForeignKey('MaritalStatus', models.DO_NOTHING, db_column='Marital_Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ipd_register'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

