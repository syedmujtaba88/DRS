from django.db import models
from datetime import datetime

# Create your models here.


class NumberSync(models.Model):
    """Number sync job between CSS and CBCM"""
    msisdn = models.BigIntegerField(primary_key=True)
    status_in_css = models.IntegerField(null=False)
    status_in_cbcm = models.IntegerField(null=False)
    job_status = models.IntegerField(default=0)
    mismatch_identified_on = models.DateTimeField(default=datetime.now())
    failure_reason = models.TextField(null=True, blank=True)
    retry_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Human readable data return for Admin page"""
        return str(self.msisdn)


class DeviceSync(models.Model):
    """Device sync job between CSS and CBCM"""
    serial_number = models.CharField(
        primary_key=True, null=False, max_length=30)
    status_in_css = models.IntegerField(null=False)
    status_in_cbcm = models.IntegerField(null=False)
    job_status = models.IntegerField(default=0)
    mismatch_identified_on = models.DateTimeField(default=datetime.now())
    failure_reason = models.TextField(null=True, blank=True)
    retry_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Human readable data return for Admin page"""
        return str(self.serial_number)


class FixedNumberSync(models.Model):
    """Fixed Number sync job between CSS and CBCM"""
    fixed_number = models.IntegerField(primary_key=True)
    status_in_css = models.IntegerField(null=False)
    status_in_cbcm = models.IntegerField(null=False)
    job_status = models.IntegerField(default=0)
    mismatch_identified_on = models.DateTimeField(default=datetime.now())
    failure_reason = models.TextField(null=True, blank=True)
    retry_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Human readable data return for Admin page"""
        return str(self.fixed_number)


class Jobs(models.Model):
    """DRS Jobs"""
    job_name = models.CharField(null=False, max_length=20)
    job_status = models.IntegerField(default=0)
    src_system = models.CharField(null=False, max_length=20)
    target_system = models.CharField(null=False, max_length=20)
    pending_records = models.BooleanField(default=False)
    run_date = models.DateTimeField(default=datetime.now())
    failure_reason = models.TextField(null=True, blank=True)
    retry_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Human readable data return for Admin page"""
        return self.job_name
