from core.templates.brain.template_memory import template_memory


class TemplateEvolutionEngine:


    def improve(self,name,result):

        template_memory.remember(
            name,
            result.get(
                "features",
                []
            )
        )


        return {
            "template":name,
            "status":"evolved"
        }



template_evolution=TemplateEvolutionEngine()
