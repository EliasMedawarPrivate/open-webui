from open_webui.config import VECTOR_DB
from open_webui.utils.chat_context import temporarychatenabled, temporray_user_id

def get_vector_db_client():
    if temporarychatenabled.get("false") == "true":
        from open_webui.retrieval.vector.dbs.chroma import ChromaClient
        VECTOR_DB_CLIENT = ChromaClient(user_temporary_client=True,userId=temporray_user_id.get(""))
    elif VECTOR_DB == "milvus":
        from open_webui.retrieval.vector.dbs.milvus import MilvusClient

        VECTOR_DB_CLIENT = MilvusClient()
    elif VECTOR_DB == "qdrant":
        from open_webui.retrieval.vector.dbs.qdrant import QdrantClient

        VECTOR_DB_CLIENT = QdrantClient()
    elif VECTOR_DB == "opensearch":
        from open_webui.retrieval.vector.dbs.opensearch import OpenSearchClient

        VECTOR_DB_CLIENT = OpenSearchClient()
    elif VECTOR_DB == "pgvector":
        from open_webui.retrieval.vector.dbs.pgvector import PgvectorClient

        VECTOR_DB_CLIENT = PgvectorClient()
    elif VECTOR_DB == "elasticsearch":
        from open_webui.retrieval.vector.dbs.elasticsearch import ElasticsearchClient

        VECTOR_DB_CLIENT = ElasticsearchClient()
    elif VECTOR_DB == "pinecone":
        from open_webui.retrieval.vector.dbs.pinecone import PineconeClient

        VECTOR_DB_CLIENT = PineconeClient()
    else:
        from open_webui.retrieval.vector.dbs.chroma import ChromaClient

        VECTOR_DB_CLIENT = ChromaClient()

    return VECTOR_DB_CLIENT