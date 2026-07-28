from pathlib import Path
import shutil

HOME = Path.home()

def ls(path="~"):
    p = Path(path).expanduser()
    if not p.exists():
        return {"error":"path not found"}
    return [x.name for x in p.iterdir()]

def mkdir(path):
    p = Path(path).expanduser()
    p.mkdir(parents=True, exist_ok=True)
    return {"status":"created","path":str(p)}

def rm(path):
    p = Path(path).expanduser()
    if not p.exists():
        return {"error":"not found"}

    if p.is_dir():
        shutil.rmtree(p)
    else:
        p.unlink()

    return {"status":"deleted"}

def info(path):
    p = Path(path).expanduser()

    if not p.exists():
        return {"error":"not found"}

    return {
        "name":p.name,
        "dir":p.is_dir(),
        "size":p.stat().st_size
    }
