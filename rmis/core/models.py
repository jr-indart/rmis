from django.db import models


class District(models.Model):
    district_name = models.CharField(max_length=100)
    district_code = models.CharField(max_length=3)

    class Meta:
        ordering = ['district_name']

    def __str__(self):
        return self.district_name


class Subdistrict(models.Model):
    subdistrict_name = models.CharField(max_length=100)
    subdistrict_code = models.CharField(max_length=3)
    district = models.ForeignKey(District, related_name='id_district', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sub District'
        ordering = ['district', 'subdistrict_name']

    def __str__(self):
        return u'%s - %s' % (self.subdistrict_name, self.district)


class Contractor(models.Model):
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=11)
    contractor_district = models.ForeignKey(District, related_name='contractor_district', on_delete=models.CASCADE)
    contractor_subdistrict = models.ForeignKey(Subdistrict, related_name='contractor_subdistrict',
                                               on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u'%s %s %s' % (self.name, self.director, self.telephone)


class Typeworks(models.Model):
    typeworks_description = models.CharField(max_length=100)
    typeworks_code = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Type of work'
        ordering = ['typeworks_description']

    def __str__(self):
        return self.typeworks_description


class Fundsource(models.Model):
    fundsource_description = models.CharField(max_length=100)
    fundsource_code = models.CharField(max_length=4)

    class Meta:
        verbose_name = 'Fund of source'
        ordering = ['fundsource_description']

    def __str__(self):
        return self.fundsource_description


class Contract(models.Model):
    contract_description = models.CharField(max_length=200)
    contract_year_cycle = models.IntegerField()
    contract_value = models.DecimalField(max_digits=9, decimal_places=2)
    contract_cost = models.DecimalField(max_digits=9, decimal_places=2)
    contract_code = models.CharField(max_length=20)
    contract_length_original = models.IntegerField()
    contract_length_actual = models.IntegerField()
    contractor = models.ForeignKey(Contractor, related_name='contract_id_contractor', on_delete=models.CASCADE)
    typeworks = models.ForeignKey(Typeworks, related_name='contract_id_typeworks', on_delete=models.CASCADE)
    fundsource = models.ForeignKey(Fundsource, related_name='contract_id_fundsource', on_delete=models.CASCADE)
    contract_district = models.ForeignKey(District, related_name='contract_district', on_delete=models.CASCADE)
    contract_subdistrict = models.ForeignKey(Subdistrict, related_name='contract_subdistrict', on_delete=models.CASCADE)

    class Meta:
        ordering = ['contractor']
#        ordering = ['contractor','contract_description']

    def __str__(self):
        return '%s %s %s %s'%(self.contract_code, self.contract_description, self.contractor, self.contract_value)