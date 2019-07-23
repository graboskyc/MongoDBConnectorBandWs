from gskymongofactory import gskymongofactory
import pickle

def p(r):
    for doc in r:
        print(doc)

print("===CONNECT===")
gmf = gskymongofactory("mongodb+srv://atlasroot:password@beta-v9iwf.mongodb.net/test?retryWrites=true&w=majority")

print("===AGG===")
r = gmf.doAgg('sample_mflix','movies',[{"$sample":{"size":1}}], appAutoRetry=30)
p(r)

print("===FINDONE===")
r = gmf.doFindOne('sample_mflix','movies', {})
print(r)
print("===FINDONE===")
r = gmf.doFindOne('sample_mflix','movies', {}, projection={"_id":0})
print(r)
#print("===FINDONE===")
#r = gmf.doFindOne('baddbname','movies', {})
#print(r)

print("===INSONE===")
r = gmf.doInsertOne('sample_mflix','movies', {"title":"My great movie"})
print(r)