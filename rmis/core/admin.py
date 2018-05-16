from django.contrib import admin

from rmis.core.models import District
from rmis.core.models import Subdistrict
from rmis.core.models import Contractor
from rmis.core.models import Typeworks
from rmis.core.models import Fundsource
from rmis.core.models import Contract


admin.site.register(District)
admin.site.register(Subdistrict)
admin.site.register(Contractor)
admin.site.register(Typeworks)
admin.site.register(Fundsource)
admin.site.register(Contract)
