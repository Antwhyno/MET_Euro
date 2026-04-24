import requests
import json

res = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&hasImages=true&q=paintings")
data = res.json()
object_ids = data['objectIDs'][:20]

artworks = []
for oid in object_ids:
    resp = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}")
    obj = resp.json()
    artworks.append({
        'title': obj.get('title', ''),
        'artist': obj.get('artistDisplayName', 'Unknown Artist'),
        'date': obj.get('objectDate', ''),
        'medium': obj.get('medium', ''),
        'image': obj.get('primaryImageSmall', obj.get('primaryImage', ''))
    })

print(json.dumps(artworks, indent=2))
