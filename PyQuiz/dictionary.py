import random
from Track import Track


class DJ:
    # put song variables here in this format: trackName = Track("string of song to be displayed", 'music/filename.ogg')
    trackRickAstleyNever = Track("Never gonna give you up", 'music/rick.ogg')
    trackShootingStars = Track("Shooting Stars", 'music/shoot.ogg')
    trackBanksGeminiFeed = Track("Gemini Feed", 'music/banks.ogg')
    trackChrisRayGun = Track("Aint No Rest Triggered", 'music/chris.ogg')
    trackArcticMonkeys = Track("Do I Wanna Know", 'music/AM.ogg')

    dictSongs = {
        # put songs here like this: 'name': varName,
        'nevergonnagiveyouup': trackRickAstleyNever,
        'shootingstars': trackShootingStars,
        'geminifeed': trackBanksGeminiFeed,
        'aintnorest': trackChrisRayGun,
        'doiwannaknow': trackArcticMonkeys,
    }
    """
    arrayRandomized = [
        # Put future songs here in this format: songs['name'],
    ]
    """
    arrayChosen = []
    trackChosen = ""

    def chooseListing(self):
        for i in xrange(4):
            randomsong = random.choice(self.dictSongs.keys())
            while not randomsong == any(self.arrayChosen):
                self.arrayChosen.append(randomsong)

    def chooseTrack(self):
        self.trackChosen = random.choice(self.arrayChosen)
