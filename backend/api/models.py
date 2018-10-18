from django.db import models


class Risk(models.Model):
    """
    Risk Model
    Defines the attributes of a Risk
    """
    risk_type = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.risk_type

    def get_risk(self):
        return self.risk_type + ' belongs to ' + self.risk_type + ' Risk Type.'


class Field(models.Model):
    FTChoices = (
        ('Text', 'Text'),
        ('Number', 'Number'),
        ('Date', 'Date'),
        ('Enum', 'Enum'),
    )
    risk = models.ForeignKey(Risk, related_name='fieldz',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=6, choices=FTChoices)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class Field_Risk(models.Model):
#     field_id = models.ForeignKey(Field, on_delete=models.CASCADE)
#     risk_id = models.ForeignKey(Risk, on_delete=models.CASCADE)
