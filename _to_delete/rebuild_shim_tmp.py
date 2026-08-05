import sys, pathlib, tempfile, subprocess
ROOT = pathlib.Path('.').resolve()
sys.path.insert(0, str(ROOT/'tools')); sys.path.insert(0, str(ROOT/'pipeline'/'scripts'))
NEW = pathlib.Path(tempfile.mktemp(prefix='rpdb_', suffix='.db', dir='/tmp'))
print('temp db:', NEW)
import build_db; build_db.DB_FALLBACK = NEW; build_db.build_db()
import export_json; export_json.DB_CANDIDATES = [NEW]; export_json.main()
