from rest_framework import serializers
from catalog.models import Catalog

class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = ('id','AM1','AM2','GAD','AN','MCM','ED','TP','AC','MS','EFM','ANA','AR','TSCO1','MDC','TLH','SDGD','TSCO2','AF','AS','FB','Cript','TAEFSS','EISS','TITC','CVAI','AL','Fr','TAPI','FPC','PC','POO','ASD','BD','TA','CO','PCO','AC','SO','RC','GID','PAW','PIM','FG','CG','FM','FC','EM','TDFS','RM','IO','MC','ET')