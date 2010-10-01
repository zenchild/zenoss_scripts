#!/usr/bin/env python
import Globals
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from transaction import commit

dmd = ZenScriptBase(connect=True).dmd
devices = dmd.Devices

templContainer = devices.Server.Windows.WMI.MSSQLServer.rrdTemplates
base_template = templContainer.MSSQLServer
base_name = 'MSSQLServer'
old_inst = '\\SQLServer:'
inst_name = 'PG3A'
new_inst = '\\MSSQL$' + inst_name + ':'

new_templ = templContainer.manage_clone(base_template, (base_name + "_" + inst_name))
commit()

# The viewName must be changed because if you have multiple templates with the same
# datasource viewName only one value will be recorded.
for dsrc in new_templ.datasources():
  dsrc.counter = dsrc.counter.replace(old_inst, new_inst, 1)
  dsrc.rename(dsrc.viewName() + '_' + inst_name)


commit()

for gdef in new_templ.graphDefs():
	gdef.rename(gdef.viewName() + ' (' + inst_name + ')')


commit()
