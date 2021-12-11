from django.db import models
from django.db.models.deletion import CASCADE


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'ipl/media/documents/{0}_{1}'.format(instance.name, filename)

class DriverModel(models.Model):
    name = models.CharField(max_length=45)
    contact_number = models.BigIntegerField(default=None)
    alternate_contact = models.BigIntegerField(default=None)
    family_contact = models.BigIntegerField(default=None)
    date_of_joining = models.DateField(null=True, default=None)
    license_number = models.CharField(max_length=45)
    license_document = models.FileField(upload_to=user_directory_path)
    address_permanent = models.CharField(max_length=300, default=None)
    address_temporary = models.CharField(max_length=300, default=None)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Driver'
        get_latest_by = 'created_dtm'
        ordering = ['name']


class ConsigneeModel(models.Model):
    name = models.CharField(max_length=45)
    contact = models.BigIntegerField()
    gstin = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    pincode = models.CharField(max_length=10)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Consignee'
        get_latest_by = 'created_dtm'


class ConsignorModel(models.Model):
    name = models.CharField(max_length=45)
    contact = models.BigIntegerField()
    gstin = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    pincode = models.CharField(max_length=10)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Consignor'
        get_latest_by = 'created_dtm'


class ShippingOrdersModel(models.Model):
    class TaxPayable(models.TextChoices):
        Male = 'Consignee', ('Consignee')
        Female = 'Consignor', ('Consignor')
        Transgender = 'IPL', ('IPL')

    class PaymentStatus(models.TextChoices):
        to_pay = 'to_pay', ('To Pay')
        tbb = 'tbb', ('To be Billed')
        paid = 'paid', ('PAID')

    class ConsigneePlaces(models.TextChoices):
        indore = 'indore', ('Indore')
        ahmedabad = 'ahmedabad', ('Ahmedabad')

    consignor = models.CharField(max_length=15)
    consignor_gst = models.CharField(max_length=15)
    consignor_place = models.CharField(max_length=15, default="Coimbatore")
    consignee = models.ForeignKey(ConsigneeModel, on_delete=CASCADE)
    consignee_gst = models.CharField(max_length=15)
    consignee_place = models.CharField(max_length=15, choices=ConsigneePlaces.choices, default=None)
    no_of_packages = models.CharField(max_length=15)
    package_value = models.IntegerField()
    package_description = models.CharField(max_length=115)
    actual_weight = models.IntegerField()
    charged_weight = models.IntegerField()
    freight_charges = models.IntegerField(default=0)
    lr_charges = models.IntegerField(default=0)
    hamali_charges = models.IntegerField(default=0)
    door_collection = models.IntegerField(default=0)
    door_delivery = models.IntegerField(default=0)
    other_charges  = models.IntegerField(default=0)
    total_charges  = models.IntegerField(default=0)
    paid_amount  = models.IntegerField(default=0)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=None)
    invoice_no = models.IntegerField(default=0)
    invoice_date = models.DateField(null=True, default=None)
    billing_date = models.DateField(null=True, default=None)
    gs_tax_payable = models.CharField(max_length=20, choices=TaxPayable.choices, default=None)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'LandingPage'
        get_latest_by = 'created_dtm'
