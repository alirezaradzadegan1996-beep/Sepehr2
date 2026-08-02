import os
import shutil
from datetime import datetime

print("""
====================================
SEPEHR2 SELF CAPABILITY CREATOR
AUTO UPGRADE
====================================
""")

# backup
backup="backup_self_capability_"+datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(backup,exist_ok=True)

for f in [
    "core/self_completion",
    "core/capabilities/registry/capability_registry.py"
]:
    if os.path.exists(f):
        if os.path.isdir(f):
            shutil.copytree(f,backup+"/"+os.path.basename(f),dirs_exist_ok=True)
        else:
            shutil.copy2(f,backup)

print("[✓] Backup created")


# directories
os.makedirs(
    "core/self_completion/evolution",
    exist_ok=True
)


# creator
with open(
"core/self_completion/evolution/capability_creator.py",
"w",
encoding="utf-8"
) as f:

    f.write(r'''
import os


class CapabilityCreator:

    def create(self,name):

        path=f"core/capabilities/{name}.py"

        if os.path.exists(path):
            return {
                "status":"exists",
                "file":path
            }


        code=f'''
from core.capabilities.base.capability import Capability


class {name.title().replace("_","")}Capability(Capability):

    name="{name}"

    keywords=[
        "{name}",
        "debug",
        "خطا",
        "اشکال"
    ]

    def run(self,text):
        return {{
            "status":"active",
            "capability":"{name}"
        }}


capability={name.title().replace("_","")}Capability()
'''


        with open(path,"w",encoding="utf-8") as f:
            f.write(code)


        return {
            "status":"created",
            "file":path
        }


capability_creator=CapabilityCreator()
''')


print("[✓] Capability Creator created")


# executor integration
with open(
"core/self_completion/evolution/auto_builder.py",
"w",
encoding="utf-8"
) as f:

    f.write(r'''
from core.self_completion.evolution.capability_creator import capability_creator
from core.capabilities.registry import registry


class AutoBuilder:


    def build(self,target):

        result=capability_creator.create(target)

        try:
            registry.load()
        except:
            pass

        return {
            "target":target,
            "creator":result,
            "registered":target in registry.list()
        }


auto_builder=AutoBuilder()
''')


print("[✓] Auto Builder created")


# test creator
from core.self_completion.evolution.auto_builder import auto_builder

result=auto_builder.build("debugger")

print()
print("=== RESULT ===")
print(result)


print()
print("=== CAPABILITIES ===")

from core.capabilities.registry import registry

print(registry.list())


print("""
====================================
SELF CAPABILITY CREATOR COMPLETE
====================================
""")
