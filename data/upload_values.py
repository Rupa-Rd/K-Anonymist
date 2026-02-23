from elasticsearch import Elasticsearch,helpers
from dotenv import load_dotenv
import os
import json
load_dotenv()  # Load environment variables from .env file

client = Elasticsearch(
    os.getenv("INDEX_URL"),
    api_key=os.getenv("API_KEY")
)

index_name = os.getenv("INDEX_NAME_CONTEXT")

def load_local_data(filepath):
    try:
        with open(filepath, 'r') as file:
            # This converts the JSON array directly into a Python list
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []


def upload_policies_to_elasticsearch(data):

    mappings= { 
    "properties": {
      "date": {
        "type": "keyword"
        # "normalizer": "lowercase_normalizer"
      },
      "entity_type": {
        "type": "semantic_text",
        "inference_id": ".elser-2-elastic"
      },
      "entity_value": {
        "type": "semantic_text",
        "inference_id": ".elser-2-elastic"
      },
      "post_code": {
        "type": "keyword"
      },
      "risk_factor": {
        "type": "float"
      }
    }
  }
    mapping_response = client.indices.put_mapping(index=index_name, body=mappings)
    print(mapping_response)

    # Timeout to allow machine learning model loading and semantic ingestion to complete
    ingestion_timeout=900

    bulk_response = helpers.bulk(
        client.options(request_timeout=ingestion_timeout),
        data,
        index=index_name
    )
    print(bulk_response)

if __name__ == "__main__":

    # Usage
    data = load_local_data(os.getenv("VALUT_DATA_FILE"))

    upload_policies_to_elasticsearch(data)