

class SepehrOSGenesisActivator:


    def activate(self, components):

        return {

            "components":
                components,

            "mode":
                "GENESIS",

            "status":
                "SEPEHR_OS_GENESIS_ACTIVE"

        }



sepehr_os_genesis_activator = SepehrOSGenesisActivator()

