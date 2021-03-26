from django.db import models

# Create your models here.
class Catalog(models.Model):
    nume_student = models.CharField(max_length=50, blank=False, default='')

    AM1 = models.CharField(max_length=2, blank=True, default='')
    AL = models.CharField(max_length=2, blank=True, default='')
    FG = models.CharField(max_length=2, blank=True, default='')
    FPC = models.CharField(max_length=2, blank=True, default='')
    CG =  models.CharField(max_length=2, blank=True, default='')
    AM2 = models.CharField(max_length=2, blank=True, default='')
    GAD = models.CharField(max_length=2, blank=True, default='')
    AN = models.CharField(max_length=2, blank=True, default='')
    FM = models.CharField(max_length=2, blank=True, default='')
    PC = models.CharField(max_length=2, blank=True, default='')
    FC = models.CharField(max_length=2, blank=True, default='')
    MCM = models.CharField(max_length=2, blank=True, default='')

    ED = models.CharField(max_length=2, blank=True, default='')
    TP = models.CharField(max_length=2, blank=True, default='')
    AC = models.CharField(max_length=2, blank=True, default='')
    POO = models.CharField(max_length=2, blank=True, default='')
    EM = models.CharField(max_length=2, blank=True, default='')
    TDFS = models.CharField(max_length=2, blank=True, default='')
    RM = models.CharField(max_length=2, blank=True, default='')
    MS = models.CharField(max_length=2, blank=True, default='')
    EFM = models.CharField(max_length=2, blank=True, default='')
    IO = models.CharField(max_length=2, blank=True, default='')
    MC = models.CharField(max_length=2, blank=True, default='')
    ET = models.CharField(max_length=2, blank=True, default='')

    ANA = models.CharField(max_length=2, blank=True, default='')
    ASD = models.CharField(max_length=2, blank=True, default='')
    BD = models.CharField(max_length=2, blank=True, default='')
    AR = models.CharField(max_length=2, blank=True, default='')
    TSCO1 = models.CharField(max_length=2, blank=True, default='')
    MDC = models.CharField(max_length=2, blank=True, default='')
    TLH = models.CharField(max_length=2, blank=True, default='')
    SDGD= models.CharField(max_length=2, blank=True, default='')
    TSCO2 = models.CharField(max_length=2, blank=True, default='')
    AF = models.CharField(max_length=2, blank=True, default='')
    AS = models.CharField(max_length=2, blank=True, default='')
    TA = models.CharField(max_length=2, blank=True, default='')
    CO = models.CharField(max_length=2, blank=True, default='')
    PCO = models.CharField(max_length=2, blank=True, default='')
    FB = models.CharField(max_length=2, blank=True, default='')

    AC = models.CharField(max_length=2, blank=True, default='')
    SO= models.CharField(max_length=2, blank=True, default='')
    Fr = models.CharField(max_length=2, blank=True, default='')
    RC	 = models.CharField(max_length=2, blank=True, default='')
    TAPI = models.CharField(max_length=2, blank=True, default='')
    GID = models.CharField(max_length=2, blank=True, default='')
    PAW	= models.CharField(max_length=2, blank=True, default='')
    Cript = models.CharField(max_length=2, blank=True, default='')
    TAEFSS = models.CharField(max_length=2, blank=True, default='')
    EISS = models.CharField(max_length=2, blank=True, default='')
    TITC = models.CharField(max_length=2, blank=True, default='')
    CVAI = models.CharField(max_length=2, blank=True, default='')
    PIM =  models.CharField(max_length=2, blank=True, default='')


    def __str__(self):
        return self.nume_student

    class Meta:
        ordering = ('id', )

#mate = ['AM1','AM2','GAD','AN','MCM','ED','TP','AC','MS','EFM','ANA','AR','TSCO1','MDC','TLH','SDGD','TSCO2','AF','AS','FB','Cript','TAEFSS','EISS','TITC','CVAI','AL','Fr','TAPI']
#info = ['FPC','PC','POO','ASD','BD','TA','CO','PCO','AC','SO','RC','GID','PAW','PIM']
#fizica = ['FG','CG','FM','FC','EM','TDFS','RM','IO','MC','ET']
