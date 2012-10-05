#Reads actual

actual = {}

movies = []

def main() :
    #read...
    fileName = ""
    movies = [{}]*17771           #movies[0] = NULL

    for movie_id in range(1,2) :
        fileName = "/u/downing/cs/netflix/training_set/mv_" + str(movie_id).zfill(7) +".txt"
        #r = StringIO.StringIO()
        f = open(fileName)
        
        s = f.readline()
        movie_id = int(s.split(":")[0])

        movies[movie_id] = {}
            
        for line in f :  
            row = line.split(",")    
            
            user_id = int(row[0])
            rating = row[1]
            rating_date = row[2]    
   
            movies[movie_id][user_id] = rating

            #print user_id +"\t"+rating+"\t"+rating_date        

        f.close()
        #print str(movies[1][946102])
main() 
    



