
movies = []

def main() :
    #read...
    fileName = ""
    years = [""]*17771 
                     
    print "movie_year =  [",

    fileName = "/u/downing/cs/netflix/movie_titles.txt"
    #r = StringIO.StringIO()
    f = open(fileName)
    s = f.readline()     
    for line in f :  
        row = line.split(",")    
        movie_id = int(row[0])
        year = row[1]
        years[movie_id] = year
        print year, ",",
        #avgs[movie_id] = str(result)
    f.close()
   
    print "]"



main() 
    

