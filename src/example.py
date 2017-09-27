import tool

data = tool.loadData("/home/changuk/data/MovieLens/movielens.dat")
from recommender import UserBased

ubcf = UserBased()
ubcf.loadData(data)
import similarity

simMeasure = similarity.cosine_intersection
#set numbers of users with recommendations to display
# display = 0 -> all 
display = 10
c=0
if (display == 0):
    for user in data.keys():
            recommendation = ubcf.Recommendation(user, simMeasure=simMeasure,
                                            nNeighbors=30)
            print('usuario: %s , recomendacion %s',str(user), str(recommendation))
else:
    for user in data.keys():
            c+=1
            if c != display:
                recommendation = ubcf.Recommendation(user, simMeasure=simMeasure,
                                                nNeighbors=30)
                print('usuario: %s , recomendacion %s',str(user), str(recommendation))
            else:
                break