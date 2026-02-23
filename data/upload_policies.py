from elasticsearch import Elasticsearch,helpers
from dotenv import load_dotenv
import os
import json
load_dotenv()  # Load environment variables from .env file

client = Elasticsearch(
    os.getenv("INDEX_URL"),
    api_key=os.getenv("API_KEY")
)

index_name = os.getenv("INDEX_NAME_POLICY")

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
      "jurisdiction": {
        "type": "semantic_text",
        "inference_id": ".elser-2-elastic"
      },
      "data_type": {
        "type": "semantic_text",
        "inference_id": ".elser-2-elastic"
      },
      "reason": {
        "type": "text"
      },
      "action": {
        "type": "keyword"
      }
    }
  }
    mapping_response = client.indices.put_mapping(index=index_name, body=mappings)
    print(mapping_response)

    # Timeout to allow machine learning model loading and semantic ingestion to complete
    ingestion_timeout=300

    bulk_response = helpers.bulk(
        client.options(request_timeout=ingestion_timeout),
        data,
        index=index_name
    )
    print(bulk_response)

if __name__ == "__main__":

    # Usage
    data = load_local_data(os.getenv("POLICY_DATA_FILE"))

    upload_policies_to_elasticsearch(data)
