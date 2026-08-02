

class SemanticRetrieval:

    def search(self,query):
        return {
            "query":query,
            "match":"found",
            "status":"SEMANTIC_RETRIEVAL_ACTIVE"
        }


semantic_retrieval=SemanticRetrieval()

