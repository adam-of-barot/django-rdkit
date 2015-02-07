from __future__ import unicode_literals

from django_rdkit.db import models

class MoleculeModel(models.Model):

    molecule = models.MolField()


class SfpModel(models.Model):

    sfp = models.SfpField(null=True)


class BfpModel(models.Model):

    bfp = models.BfpField(null=True)


#class TestModel(models.Model):#
#
#    molecule = models.MolField()
#    sfp = models.SfpField()
#    bfb = models.BfpField()


