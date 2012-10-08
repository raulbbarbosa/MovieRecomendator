
actual = {}

movies = []

def main() :
    #read...
    fileName = ""
    movies = [{}]*17771           #movies[0] = NULL
    avgs = [0]*17771
    for movie_id in range(1,17771) :
        fileName = "/u/downing/cs/netflix/training_set/mv_" + str(movie_id).zfill(7) +".txt"
        #r = StringIO.StringIO()
        f = open(fileName)
        
        s = f.readline()
        movie_id = int(s.split(":")[0])

        movies[movie_id] = {}
        sum = 0
        counter = 0            
        for line in f :  
            row = line.split(",")    
            
            user_id = int(row[0])
            rating = row[1]
            rating_date = row[2]    
            
            movies[movie_id][user_id] = rating
            sum +=int(rating)
            counter+=1
            #print user_id +"\t"+rating+"\t"+rating_date        
        result = sum/counter
        avgs[movie_id] = str(result)
        f.close()
        
            
    print "movie_avg =  [",
    for i in avgs[1:]:
        print i, ",",
    print "]"



main() 
    

