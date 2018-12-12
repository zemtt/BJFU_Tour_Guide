# coding:utf-8
import sys
from tour_guide_system.main import app

reload(sys)
sys.setdefaultencoding('utf-8')

app.run(debug=True)