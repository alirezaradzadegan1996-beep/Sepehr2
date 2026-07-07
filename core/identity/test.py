from identity import IdentityManager

idm = IdentityManager()

print("===== Identity Test =====")

print("Trust:", idm.trusted())

idm.face_ok()

print("Trust:", idm.trusted())

idm.password_ok()

print("Trust:", idm.trusted())
