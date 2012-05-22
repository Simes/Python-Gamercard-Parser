This simple little parser library, given a gamertag, will grab the HTML gamercard from `live.xbox.com` and extract the gamerscore and a few other salient details from it, returning a handy GamerCard object, which is just a data container for the gamercard information.

Usage is simple:

	from gcparse import parse_gamercard

	gcdata = parse_gamercard("MyGamertag")

This gives you a GamerCard object with the following properties:

`score`: Gamerscore
`url`: URL of the HTML gamercard
`tag`: The Gamertag you looked up
`gamer_picture_url`: URL to the gamer picture for the looked-up tag
`recent_games`: The recent games list, in the form of tuples containing the game title and the URL to the game's icon
