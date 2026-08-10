import sys; sys.path.insert(0, "src")
from clm_common.config import settings, credential
from azure.search.documents import SearchClient
sc = SearchClient(settings.search_endpoint, settings.search_index, credential())
print("docs:", sc.get_document_count())
for r in sc.search("standard payment terms Net 60", top=3):
    txt = r.get("content") or ""
    print(f"* {r.get('title')}  score={r['@search.score']:.2f}  hasNet60={'Net 60' in txt}")
