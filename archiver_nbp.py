import os
import datetime

dt = str(datetime.datetime.now().strftime('%Y_%m_%d %H.%M'))
name = str(os.path.join(os.path.expanduser("~"), "Desktop")+'\data '+dt+'.xml')
file = str(os.path.join(os.path.expanduser("~"), "Desktop")+'\data.xml')


os.rename(file,name)
