movies = []

def main() :
    fileName = "/u/downing/cs/netflix/movie_titles.txt"
    f = open(fileName)    
    s = f.readline()
    movies = [None]*17771
    for line in f :  
        row = line.split(",")    
            
        movie_id = int(row[0])
        year = row[1]
        title = ""
        for i in row[2:]:
            title += row[2]    
   
        movies[movie_id] = (year,title)

        print str(movie_id) + "\t %s" % (movies[movie_id],)        

    f.close()
        #print str(movies[1][946102])
main() 
    



