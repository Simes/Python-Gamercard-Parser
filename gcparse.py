from xml.etree import ElementTree
import urllib

class GamerCard:
	pass
	
def parse_gamercard(gamertag):
	gcurl = "http://gamercard.xbox.com/" + urllib.quote(gamertag) + ".card"
	
	remote = urllib.urlopen(gcurl)
	
	html = remote.read()
	html, tmp, tmp = html.partition("</body>")
	tmp, tmp, html = html.rpartition("<body>")
	xml = ElementTree.fromstring("<xml>" + html + "</xml>")
	
	card = GamerCard()
	card.url = gcurl
	card.tag = gamertag;

	# Gamer picture	
	node = xml.find('.//img[@id="Gamerpic"]')
	card.gamer_picture_url = node.get("src")
	
	# Gamerscore
	node = xml.find('.//div[@id="Gamerscore"]')
	card.score = node.text

	# Recently played games list
	recent_games = []
	rg_nodeset = xml.findall('.//ol[@id="PlayedGames"]//img')
	for node in rg_nodeset:
		recent_games.append((node.get("title"), node.get("src")))

	card.recent_games = recent_games
	return card


if __name__ == "__main__":
    import sys
    gc = parse_gamercard(sys.argv[1])
    
    print gc.__dict__
    