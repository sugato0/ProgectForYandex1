import pathlib
import sys

from yandex1DBPrepare import Yandex1DB

script_dir = pathlib.Path(sys.argv[0]).parent
db_file = script_dir / 'models/ProgectDB.db'
model = Yandex1DB(db_file)