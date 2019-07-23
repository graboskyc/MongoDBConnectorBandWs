from gskymongofactory import gskymongofactory
import pickle

def p(r):
    for doc in r:
        print(doc)

print("===CONNECT===")
gmc = gskymongofactory("mongodb+srv://atlasroot:password@beta-v9iwf.mongodb.net/test?retryWrites=true&w=majority&maxPoolSize=10")

print("===AGG===")
r = gmc.doAgg('sample_mflix','movies',[{"$sample":{"size":1}}], appAutoRetry=30)
p(r)

print("===FINDONE===")
r = gmc.doFindOne('sample_mflix','movies', {})
print(r)
print("===FINDONE===")
r = gmc.doFindOne('sample_mflix','movies', {}, projection={"_id":0})
print(r)
#print("===FINDONE===")
#r = gmc.doFindOne('baddbname','movies', {})
#print(r)

print("===INSONE===")
r = gmc.doInsertOne('sample_mflix','movies', {"title":"My great movie"})
print(r)