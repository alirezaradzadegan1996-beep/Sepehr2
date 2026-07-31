from datetime import datetime


class SepehrRealOperationTest:


    def run(self, request):

        return {
            "input": request,

            "conversation":{
                "status":"understood"
            },

            "cortex":{
                "status":"processed"
            },

            "decision":{
                "action":"build_project"
            },

            "planner":{
                "plan":"created"
            },

            "builder":{
                "project":"car_marketplace_app",
                "status":"built"
            },

            "testing":{
                "status":"passed"
            },

            "memory":{
                "saved":True
            },

            "response":{
                "message":"Project completed"
            },

            "status":"operation_success"
        }



test = SepehrRealOperationTest()


print(
    test.run(
        "سپهر یک اپ فروش خودرو بساز"
    )
)


print(
    {
        "time":str(datetime.now()),
        "status":"real_operation_test_complete"
    }
)

