from datetime import datetime


class IdentityModel:

    def __init__(self):
        self.identity = {
            "name":"Sepehr",
            "type":"digital_agent"
        }

    def get(self):
        return self.identity



class PersonalityTraits:

    def __init__(self):
        self.traits = {}

    def set(self,key,value):
        self.traits[key]=value

        return {
            "status":"trait_added",
            "trait":key
        }



class ValueSystem:

    def __init__(self):
        self.values=[]

    def add(self,value):
        self.values.append(value)

        return {
            "status":"value_added",
            "values":self.values
        }



class PreferenceLearning:

    def __init__(self):
        self.preferences={}

    def learn(self,item,choice):

        self.preferences[item]=choice

        return {
            "status":"preference_learned",
            "item":item
        }



class SelfReflection:

    def reflect(self,experience):

        return {
            "experience":experience,
            "insight":"learned_from_experience",
            "time":str(datetime.now())
        }



class SelfAwarenessEngine:

    def analyze(self):

        return {
            "self_awareness":"active",
            "understanding":"self_model_available"
        }



identity_model = IdentityModel()
personality_traits = PersonalityTraits()
value_system = ValueSystem()
preference_learning = PreferenceLearning()
self_reflection = SelfReflection()
self_awareness = SelfAwarenessEngine()



print("Personality & Self Awareness Active")

print(identity_model.get())

print(
personality_traits.set(
"curiosity",
"high"
)
)

print(
value_system.add(
"learning"
)
)

print(
preference_learning.learn(
"communication",
"friendly"
)
)

print(
self_reflection.reflect(
"completed cognitive layer"
)
)

print(
self_awareness.analyze()
)

