#####################################################################
## /run.py will be used to launch the web server.
## Start flask by:
##    python run.py 
#####################################################################
from app import app
app.run(host='0.0.0.0', debug=True)
