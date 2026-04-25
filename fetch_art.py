import urllib.request
import json

req = urllib.request.Request("https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&hasImages=true&q=paintings", headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode('utf-8'))

object_ids = data['objectIDs'][:20]

artworks = []
for oid in object_ids:
    req2 = urllib.request.Request(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}", headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req2) as r2:
            obj = json.loads(r2.read().decode('utf-8'))
            artworks.append({
                'title': obj.get('title', ''),
                'artist': obj.get('artistDisplayName', 'Unknown Artist'),
                'date': obj.get('objectDate', ''),
                'medium': obj.get('medium', ''),
                'image': obj.get('primaryImageSmall', obj.get('primaryImage', ''))
            })
    except Exception as e:
        print(f"Failed {oid}")

print(json.dumps(artworks, indent=2))
