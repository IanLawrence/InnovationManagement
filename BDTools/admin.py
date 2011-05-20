# Copyright (C) 2008 Instituto Nokia de Tecnologia. All rights reserved.
# Contact: Ian Lawrence root@ianlawrence.info
#
# This software, including documentation, is protected by copyright
# controlled by Instituto Nokia de Tecnologia. All rights are reserved.
# Copying, including reproducing, storing, adapting or translating, any
# or all of this material requires the prior written consent of
# Instituto Nokia de Tecnologia. This material also contains
# confidential information which may not be disclosed to others without
# the prior written consent of Instituto Nokia de Tecnologia.
#
#===========================================================================
#
# Django Framework views the work horse of the app root@ianlawrence.info
#
#===========================================================================


from InnovationManagement.BDTools.models import Spreadsheet, BusinessCase

from django.contrib import admin


admin.site.register(BusinessCase)
admin.site.register(Spreadsheet)

