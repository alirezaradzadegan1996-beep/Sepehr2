
class DomainKnowledge:

    domains = {

        "hospital":[
            "patients",
            "doctors",
            "appointments",
            "medical_records",
            "database"
        ],

        "pharmacy":[
            "medicines",
            "inventory",
            "expiration",
            "users",
            "orders",
            "database"
        ],

        "car_market":[
            "products",
            "brands",
            "inventory",
            "orders",
            "customers"
        ],

        "restaurant":[
            "menu",
            "orders",
            "customers",
            "inventory"
        ],

        "farm":[
            "plants",
            "animals",
            "inventory",
            "weather",
            "database"
        ],

        "photo_editor":[
            "upload",
            "filters",
            "processing",
            "export"
        ],

        "video_editor":[
            "upload",
            "timeline",
            "effects",
            "export"
        ]
    }


    def detect(self,text):

        for domain,features in self.domains.items():

            if domain in text:
                return domain,features

        mapping={

            "بیمارستان":"hospital",
            "دارو":"pharmacy",
            "دارویی":"pharmacy",
            "داروخانه":"pharmacy",
            "خودرو":"car_market",
            "قطعات":"car_market",
            "رستوران":"restaurant",
            "غذا":"restaurant",
            "مزرعه":"farm",
            "کشاورزی":"farm",
            "عکس":"photo_editor",
            "فیلم":"video_editor",
            "ویدیو":"video_editor"
        }


        for k,v in mapping.items():

            if k in text:
                return v,self.domains[v]


        return "general",[
            "database",
            "users",
            "interface"
        ]


domain_knowledge=DomainKnowledge()
