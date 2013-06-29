# python

import os
import errno
import random

# create folder if it does not exist
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

# create file if it does not exist
def touch(path):
	if not os.path.exists(path):
		open(path, 'w').close()

# main
if __name__ == '__main__':
	random.seed()
	pathTest = os.path.join(os.getcwd(),'Test')
	pathMovie = os.path.join(pathTest,'Movies')
	pathTVShow = os.path.join(pathTest,'TV Shows')

	extensions = ['mkv','mp4','avi','wma']

	movies = ["(500) Days of Summer (2009)","A Knight's Tale (2001)","Aladdin (1992)","Alien (1979)","Aliens (1986)","Almost Famous (2000)","An American Tail - Fievel Goes West (1991)","An American Tail (1986)","Anastasia (1997)","Anchorman - The Legend of Ron Burgundy (2004)","Beauty and the Beast (1991)","Byôsoku 5 senchimêtoru (2007)","Captain America - The First Avenger (2011)","Coraline (2009)","Despicable Me (2010)","District 9 (2009)","Donnie Darko (2001)","Dr. Horrible's Sing-Along Blog (2008)","Dragons - Gift of the Night Fury (2011)","Eternal Sunshine of the Spotless Mind (2004)","Fantastic Mr. Fox (2009)","Ferris Bueller's Day Off (1986)","Fight Club (1999)","Final Fantasy VII - Advent Children (2005)","Finding Nemo (2003)","Gake no ue no Ponyo (2008)","Harry Potter and the Chamber of Secrets (2002)","Harry Potter and the Deathly Hallows - Part 1 (2010)","Harry Potter and the Deathly Hallows - Part 2 (2011)","Harry Potter and the Goblet of Fire (2005)","Harry Potter and the Half-Blood Prince (2009)","Harry Potter and the Order of the Phoenix (2007)","Harry Potter and the Prisoner of Azkaban (2004)","Harry Potter and the Sorcerer's Stone (2001)","Hauru no ugoku shiro (2004)","Hercules (1997)","Horton Hears a Who! (2008)","Hot Fuzz (2007)","How to Train Your Dragon (2010)","Hugo (2011)","I Love You,Man (2009)","Inception (2010)","Inglourious Basterds (2009)","Iron Man (2008)","Kick-Ass (2010)","Kill Bill - Vol. 1 (2003)","Kill Bill - Vol. 2 (2004)","Mean Girls (2004)","Megamind (2010)","Mission - Impossible (1996)","Mononoke-hime (1997)","Moulin Rouge! (2001)","Mulan (1998)","Muppets from Space (1999)","Nick and Norah's Infinite Playlist (2008)","Ninja Assassin (2009)","Nowhere Boy (2009)","Peter Pan (2003)","Pirates of the Caribbean - At World's End (2007)","Pirates of the Caribbean - Dead Man's Chest (2006)","Pirates of the Caribbean - On Stranger Tides (2011)","Pirates of the Caribbean - The Curse of the Black Pearl (2003)","Pocahontas (1995)","Pooh's Grand Adventure - The Search for Christopher Robin (1997)","Pulp Fiction (1994)","Scott Pilgrim vs. the World (2010)","Sen to Chihiro no kamikakushi (2001)","Sherlock Holmes (2009)","Speed Racer (2008)","Star Wars - Episode IV - (Despecialized Edition) (1977)","Star Wars - Episode V - The Empire Strikes Back (Despecialized Edition) (1980)","Star Wars - Episode VI - Return of the Jedi (Despecialized Edition) (1983)","Stardust (2007)","Starkid Productions","Super Troopers (2001)","Sweeney Todd - The Demon Barber of Fleet Street (2007)","Tangled (2010)","Tarzan (1999)","That Thing You Do! (1996)","The Adventures of Tintin (2011)","The Bourne Identity (2002)","The Bourne Supremacy (2004)","The Bourne Ultimatum (2007)","The Chronicles of Narnia - The Lion,the Witch and the Wardrobe (2005)","The Dark Knight (2008)","The Emperor's New Groove (2000)","The Hangover (2009)","The Hunchback of Notre Dame (1996)","The Incredible Hulk (2008)","The Incredibles (2004)","The Land Before Time (1988)","The Lion King (1994)","The Little Mermaid (1989)","The Muppet Christmas Carol (1992)","The Muppets Take Manhattan (1984)","The Nightmare Before Christmas (1993)","The Phantom of the Opera (2004)","The Producers (2005)","The Room (2003)","The Secret of Kells (2009)","The Social Network (2010)","Thor (2011)","Titanic (1997)","Tonari no Totoro (1988)","Toy Story 3 (2010)","Treasure Planet (2002)","TRON - Legacy (2010)","Up (2009)","V for Vendetta (2005)","WALL·E (2008)","Watchmen (2009)","Where the Wild Things Are (2009)","Winnie the Pooh (2011)","Zombieland (2009)"]
	tvshows = ["Adventure Time with Finn and Jake","Angel Beats!","Archer (2009)","Arrested Development","Avatar - The Last Airbender","Buffy the Vampire Slayer","Burn Notice","Castle (2009)","Code Geass","Community","Death Note","Dexter","Doctor Who (2005)","Ergo Proxy","Eureka Seven","FLCL","Fringe","Fullmetal Alchemist","Fullmetal Alchemist Brotherhood","Game of Thrones","Gravity Falls","How I Met Your Mother","Invader Zim","Lost","My Little Pony- Friendship is Magic","Neon Genesis Evangelion","Once Upon A Time (2011)","Sherlock","Soul Eater","Tengen Toppa Gurren Lagann","The Big Bang Theory","The Legend of Korra","The Walking Dead","Toradora"]

	# Test Path
	make_sure_path_exists(pathTest)
	for movie in movies:
		# Movies
		movieDir = os.path.join(pathMovie, movie)
		make_sure_path_exists(movieDir)
		if not os.path.exists(movieDir):
			# movieName = movie + '.' + extensions[random.randrange(0,len(extensions))]
			touch(os.path.join(movieDir, movie + '.' + extensions[random.randrange(0,len(extensions))]))
		pass
	for tvshow in tvshows:
		# TV Shows
		
		make_sure_path_exists(os.path.join(pathTVShow, tvshow))
		pass
	
	

