
movies = []

def main() :
    #read...
    fileName = ""
    avg_users = [0.0]*2649430 
                      
    counter_users = [1]*2649430
    print "avg_user =  [",
    for movie_id in range(1,17771) :
        fileName = "/u/downing/cs/netflix/training_set/mv_" + str(movie_id).zfill(7) +".txt"
        #r = StringIO.StringIO()
        f = open(fileName)
        
        s = f.readline()
        movie_id = int(s.split(":")[0])           
        for line in f :  
            row = line.split(",")    
            
            user_id = int(row[0])
            rating = row[1]
            rating_date = row[2]    
            

            avg_users[user_id] += float(rating) 
            counter_users[user_id] += 1
        #avgs[movie_id] = str(result)
        f.close()
        
    n = 1
    for i in avg_users[1:]:
        result = i / counter_users[n]
        n+=1        
        print result, ",",
    print "]"



main() 
    

