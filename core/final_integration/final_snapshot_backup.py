

class FinalSnapshotBackup:


    def save(self):

        return {

            "snapshot":
                "saved",

            "backup":
                "completed",

            "status":
                "FINAL_SNAPSHOT_ACTIVE"

        }


final_snapshot_backup = FinalSnapshotBackup()

