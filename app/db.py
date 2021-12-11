from deta import Deta

from app.settings import setting

deta = Deta(setting.DETA_PROJECT_KEY)
db = deta.Base(setting.DETA_BASE_NAME)
