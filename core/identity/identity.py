class IdentityManager:

    def __init__(self):

        self.face = False
        self.voice = False
        self.password = False

    def face_ok(self):
        self.face = True

    def voice_ok(self):
        self.voice = True

    def password_ok(self):
        self.password = True

    def reset(self):
        self.face = False
        self.voice = False
        self.password = False

    def trusted(self):

        if self.face and self.voice:
            return True

        if self.face and self.password:
            return True

        if self.voice and self.password:
            return True

        return False
