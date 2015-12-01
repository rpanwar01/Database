import sqlite3
import datetime

database = sqlite3.connect('Chinook_Sqlite.sqlite', **{})
c = database.cursor()

#c.execute("CREATE INDEX IOK_Track ON Track(Name, Composer)");
#c.execute("DROP INDEX IOK_Track");

startTime = datetime.datetime.now()
c.execute("SELECT Album.Title FROM Album INNER JOIN Track ON Album.AlbumId = Track.AlbumId WHERE Track.Name = 'Overdose' AND Track.Composer = 'AC/DC'");
Titles = c.fetchall()

endTime = datetime.datetime.now() 
executionTime = endTime - startTime;
print ("start Time : ", startTime)
print ("end Time : ", endTime)
print ("Execution Time : ", executionTime)

for Title in Titles:
		print("Album Title: ", Title)

#c.execute("SELECT COUNT(Album.Title) FROM Album INNER JOIN Track ON Album.AlbumId = Track.AlbumId");
#Count = c.fetchone()
#print("Total Number of Records (After Join): ", Count)

#c.execute("SELECT COUNT(Album.Title) FROM Album INNER JOIN Track ON Album.AlbumId = Track.AlbumId WHERE Track.Name = 'Overdose' AND Track.Composer = 'AC/DC'");
#Counts = c.fetchall()

#for Count in Counts:
#		print("Number of Records After Filteration: ", Count)

#c.execute("explain query plan SELECT Album.Title FROM Album INNER JOIN Track ON Album.AlbumId = Track.AlbumId WHERE Track.Name = 'Overdose' AND Track.Composer = 'AC/DC'");
#Values = c.fetchall()

#for value in Values:
#		print("Explain Query Plan Result: ", value)
		
c.close()

