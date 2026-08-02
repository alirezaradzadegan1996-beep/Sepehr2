
class FileEnvironment:

    def manage(self,path):

        return {
            "path":path,
            "access":"granted",
            "operation":"ready",
            "status":"FILE_ENVIRONMENT_ACTIVE"
        }


file_environment = FileEnvironment()
