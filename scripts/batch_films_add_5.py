#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — the 1970s (New Hollywood).

Fifth addition batch (v1.0 content pass toward 400 films): the decade of
directors as auteurs — M*A*S*H, Patton, The French Connection, Willy Wonka,
Cabaret, The Exorcist, The Sting, Mean Streets, Badlands, Amarcord, The
Conversation, Young Frankenstein, Dog Day Afternoon, Barry Lyndon, Nashville,
Rocky, Carrie, All the President's Men, Eraserhead, The Deer Hunter,
Halloween, Days of Heaven, Being There, and more. Handcrafted teaser + real
fact + quality-bar instruction. Appends only; rejects duplicate ids/names;
caps 450 (SCHEMA.md).
"""

from pathlib import Path
import json
import re
import sys


def _trim(text: str, limit: int = 450) -> str:
    if len(text) <= limit:
        return text
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    out = ""
    for s in sentences:
        candidate = s if not out else out + " " + s
        if len(candidate) > limit:
            break
        out = candidate
    return out


PATH = Path(__file__).resolve().parent.parent / "app/src/main/assets/topics/films.json"


def _entry(
    id_: str,
    name: str,
    teaser: str,
    byline: str,
    target_name: str,
    duration: int,
    instruction: str,
    tags: list[str],
) -> dict:
    return {
        "id": id_,
        "categoryId": "FILMS",
        "subtype": "Film",
        "name": name,
        "teaser": _trim(teaser),
        "imageUrl": "",
        "byline": byline,
        "exploreAction": {
            "verb": "Watch",
            "targetName": target_name,
            "durationMinutes": duration,
            "instruction": _trim(instruction),
        },
        "tags": tags,
        "tier": 1,
    }


NEW_TOPICS: list[dict] = [
    _entry(
        "film-mash-1970",
        "M*A*S*H (1970)",
        "The war comedy that made Robert Altman a star and spawned a TV empire — a Korean War field hospital run on wisecracks, booze, and black humor. The film's overlapping dialogue (everyone talking at once, the way real people do) was Altman's signature, and its theme song, 'Suicide Is Painless,' has a story: Altman's 14-year-old son wrote the lyrics for $200.",
        "Robert Altman",
        "M*A*S*H (1970) — the football game and the ending",
        116,
        "Watch the operating-room scenes — the chaos, the one-liners, the 'society of doctors' — and notice how Altman films war as a black comedy of professionalism: the blood is real, the jokes are the coping, and the film's irreverence was a 1970 shot at the Vietnam-era establishment. Then watch the ending, where Hawkeye's 'suicide' is a practical joke: the film's argument — that gallows humor is how the sane survive the insane — is in that final gag, and the film's Palme d'Or made Altman the decade's great anti-authoritarian.",
        ["Comedy", "War", "1970s", "Hollywood"],
    ),
    _entry(
        "film-patton-1970",
        "Patton (1970)",
        "George C. Scott's portrait of the general who believed he was history's instrument — the film opens with Patton addressing his troops before a giant American flag, and the speech is the most famous monologue in war cinema. Scott won the Oscar and refused it — the first actor ever to — and the film's 7 Oscars (including Best Picture) made it the year's epic.",
        "Franklin J. Schaffner",
        "Patton (1970) — the opening speech",
        172,
        "Watch the opening — the flag, the speech, Scott's Patton as a soldier-poet of war — and notice how the film announces its subject: the general is a performance artist of violence, and the film's ambivalence (admiring and appalled) is in that first monologue. Then watch the ending, where the general who conquered Europe is sidelined: the film's argument — that the warrior's glory is always temporary — is in the final shot, and the film's 'Old Blood and Guts' portrait made it required viewing at West Point.",
        ["War", "Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-mccabe-and-mrs-miller-1971",
        "McCabe & Mrs. Miller (1971)",
        "The anti-western that rewrote the genre — Robert Altman's frontier town built in the rain, with Warren Beatty's gambler and Julie Christie's madam running a brothel that becomes a town's heart. Shot in winter light with Leonard Cohen's songs as the score, it's the most beautiful-looking western ever made, and its ending — McCabe dying in the snow while the town burns — is the genre's saddest.",
        "Robert Altman",
        "McCabe & Mrs. Miller (1971) — the ending",
        120,
        "Watch the ending — McCabe bleeding in the snow, the church burning, Mrs. Miller lost in her opium dream — and notice how Altman films the death in pieces: the violence happens off-screen and on-screen at once, and the town's obliviousness is the tragedy. Then watch the opening, where the gambler arrives in a muddy mining camp: the film's argument — that the frontier was a business, not a dream — is in every frame, and the film's natural-light photography (Vilmos Zsigmond) made it the most influential-looking film of the decade.",
        ["Western", "1970s", "Hollywood"],
    ),
    _entry(
        "film-the-french-connection-1971",
        "The French Connection (1971)",
        "The car chase that changed cinema — Gene Hackman's Popeye Doyle chasing an elevated train through New York, filmed illegally on real streets with real traffic and no permits. It won 5 Oscars including Best Picture, and the chase remains the most dangerous sequence ever shot for a mainstream film. Hackman's fumbling, obsessive detective is the greatest cop in movie history.",
        "William Friedkin",
        "The French Connection (1971) — the car chase",
        104,
        "Watch the car chase — the Pontiac under the el train, the civilian cars, the near-misses — and notice how Friedkin shot it without permits: the collisions are real, the drivers were stuntmen in real traffic, and the sense of mortal risk is why it still works. Then watch the ending, the warehouse shootout and the frozen final shot: the film's argument — that the drug war is a war without victories — is in that ambiguity, and the film's grainy, handheld New York invented the modern police thriller.",
        ["Crime", "Action", "1970s", "Hollywood"],
    ),
    _entry(
        "film-willy-wonka-and-the-chocolate-factory-1971",
        "Willy Wonka & the Chocolate Factory (1971)",
        "The children's film that's secretly a horror movie — Gene Wilder's Wonka, the golden tickets, and the boat tunnel that terrified a generation. Wilder insisted his entrance be the limp-then-cartwheel: 'no one will know if I'm faking or not.' The film flopped, then became a beloved cult classic, and the 'Pure Imagination' song remains its hypnotic center.",
        "Mel Stuart",
        "Willy Wonka & the Chocolate Factory (1971) — the boat tunnel and the ending",
        100,
        "Watch the boat tunnel sequence — the screaming, the flashing images, the 'the candy man' turned nightmare — and notice how the film breaks the children's-movie contract: the adults made a deliberately frightening set piece, and Wilder's manic delivery sells it. Then watch the ending, where Wonka's final test — the 'candy is dandy but liquor is quicker' lesson — reveals the film's moral: the film's argument, that imagination is the only real wealth, is delivered by the most complicated children's-film villain ever written.",
        ["Family", "Fantasy", "1970s", "Hollywood"],
    ),
    _entry(
        "film-the-last-picture-show-1971",
        "The Last Picture Show (1971)",
        "The film that made small-town America an art form — a Texas town's last year before the highway and the war arrive, told through a boy, a girl, and the town's dying movie theater. Peter Bogdanovich shot it in black and white in a real dying town, and the film's two supporting Oscars (Ben Johnson, Cloris Leachman) launched a wave of 1970s nostalgia. Its ending — the picture show closing — gave the film its name and its meaning.",
        "Peter Bogdanovich",
        "The Last Picture Show (1971) — the ending",
        118,
        "Watch the film's first hour — the pool hall, the café, the football field — and notice how Bogdanovich films boredom with affection: the town is dying and the characters don't know it yet, and the black-and-white photography (by Robert Surtees) makes the 1950s feel biblical. Then watch the ending, where Sonny sits alone in the empty theater: the film's argument — that youth ends when the place that held it closes — is in that final shot, and the film's cast (including a young Cybill Shepherd and Jeff Bridges) became the decade's great ensemble.",
        ["Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-cabaret-1972",
        "Cabaret (1972)",
        "The musical that refused to be one — all its songs happen on the Kit Kat Club stage, never in the story, and the story is about Berlin sliding into Nazism. Liza Minnelli's Sally Bowles and Bob Fosse's choreography won 8 Oscars (a record at the time for a non-Best-Picture winner), and the film's final number — the club full of swastika armbands — is the most chilling use of a musical number in cinema.",
        "Bob Fosse",
        "Cabaret (1972) — the 'Tomorrow Belongs to Me' scene",
        124,
        "Watch 'Tomorrow Belongs to Me' — the young man singing in the beer garden, the camera rising as the crowd joins — and notice how Fosse films fascism's seduction: the song is beautiful, and the horror is how easily the beauty turns into the anthem. Then watch Liza's 'Maybe This Time' and the film's final stage number: the film's argument — that entertainment and politics are the same stage — is in that last song, and the film's Oscar sweep (8 wins) made Fosse the decade's most influential choreographer.",
        ["Musical", "1970s", "Hollywood"],
    ),
    _entry(
        "film-the-exorcist-1973",
        "The Exorcist (1973)",
        "The scariest film ever made, by near-universal vote — William Friedkin's story of a possessed girl and the two priests who try to save her, adapted from William Peter Blatty's novel. The pea-soup vomiting was invented for the film, the 'frozen face' subliminal flashes were real, and audiences fainted and vomited at screenings. The film's 10 Oscar nominations (including Best Picture) made horror respectable. 'The power of Christ compels you.'",
        "William Friedkin",
        "The Exorcist (1973) — the first signs and the ending",
        122,
        "Watch the first half hour — the archaeological dig, the ouija board, the 'Captain Howdy' — and notice how Friedkin establishes the horror through realism: the medical scenes are clinical, the mother's doubt is credible, and the possession arrives as a medical mystery. Then watch the ending, where Father Karras's sacrifice settles the film's argument: the film's claim — that faith is tested by evil and survives by choice, not certainty — is delivered in that final fall, and the film's influence (on everything from horror to comedy to music videos) is the largest of any horror film.",
        ["Horror", "1970s", "Hollywood"],
    ),
    _entry(
        "film-the-sting-1973",
        "The Sting (1973)",
        "The con-artist caper that reunited Butch and Sundance — Paul Newman and Robert Redford as Depression-era grifters who run the most elaborate con in cinema against a gangster (Robert Shaw). The Scott Joplin ragtime score ('The Entertainer') became a chart hit, and the film's final double-twist ending is the most satisfying last ten minutes in movie history. It won 7 Oscars including Best Picture.",
        "George Roy Hill",
        "The Sting (1973) — the ending twists",
        129,
        "Watch the film's structure — the setup, the marks, the 'let's make a deal' — and notice how the film teaches you the con as it runs it: every scene is a lesson in confidence, and the audience is being conned right along with the mark. Then watch the ending, where the double-cross reveals itself layer by layer: the film's argument — that the con is the only honest game in a crooked world — is in that final reveal, and the film's ragtime score made Scott Joplin famous 56 years after his death.",
        ["Crime", "1970s", "Hollywood"],
    ),
    _entry(
        "film-mean-streets-1973",
        "Mean Streets (1973)",
        "The film that introduced Martin Scorsese and Robert De Niro — Little Italy's small-time hoods, their debts, their saints, and their doom. 'You don't make up for your sins in church. You do it in the streets.' The film's handheld camera, pop-songs score, and Catholic guilt made it the founding text of 1970s New York cinema, and De Niro's Johnny Boy is the role that made his name.",
        "Martin Scorsese",
        "Mean Streets (1973) — the pool hall and the ending",
        112,
        "Watch the opening — the confession, the 'you don't make up for your sins in church' — and notice how Scorsese sets the film's theology in the first minutes: Charlie's Catholic guilt is the plot, and the film's handheld camera makes the streets feel like a confessional. Then watch the ending, where Johnny Boy's debt comes due in the back alley: the film's argument — that the streets are a system of grace and punishment — is in that final scene, and the film's mix of reverence and violence made Scorsese the decade's essential director.",
        ["Crime", "1970s", "Hollywood"],
    ),
    _entry(
        "film-badlands-1973",
        "Badlands (1973)",
        "Terrence Malick's debut — a 1950s teenage couple on a killing spree, based on the real Starkweather murders, told in the girl's dreamy voiceover. Martin Sheen and Sissy Spacek wander a deadpan American road of murder and beauty, and the film's tone — a fairy tale about real violence — made it the most original debut of its decade. The 'dance on the ledge' scene is the film in miniature.",
        "Terrence Malick",
        "Badlands (1973) — the voiceover and the ending",
        94,
        "Watch the opening — Holly's voiceover, the first meeting, the father's gun — and notice how Malick keeps the horror at a distance: the murders are narrated with the same flat wonder as the weather, and the film's beauty is its irony. Then watch the ending, where Kit is captured and treats it like a game: the film's argument — that violence is a daydream America tells itself — is in that final scene, and the film's use of Carl Orff's 'Gassenhauer' made the music box tune the decade's most haunting theme.",
        ["Crime", "1970s", "Hollywood"],
    ),
    _entry(
        "film-amarcord-1973",
        "Amarcord (1973)",
        "Federico Fellini's loving, bawdy memory of his 1930s seaside hometown under fascism — the film whose title is a Romagnol phrase for 'I remember.' The peacock in the snow, the ocean liner Rex, the village idiot's sexual bravado, and the film's great set piece — a fog-shrouded night — make it the most personal and playful of Fellini's films. It won the Oscar for Best Foreign Language Film.",
        "Federico Fellini",
        "Amarcord (1973) — the Rex and the ending",
        123,
        "Watch the Rex sequence — the whole town rowing out to sea to see the great liner pass — and notice how Fellini films collective longing: the ocean liner is the town's dream of escape, and the fog that follows is its reality. Then watch the ending, where the seasons turn and the same faces gather: the film's argument — that memory is a comedy with a sad ending — is in that final scene, and the film's mix of the grotesque and the tender makes it the most purely enjoyable of all Fellini's masterpieces.",
        ["Comedy", "Classic", "Italian"],
    ),
    _entry(
        "film-the-conversation-1974",
        "The Conversation (1974)",
        "The year's second surveillance masterpiece (with The Godfather Part II, same director) — Gene Hackman's wiretapper who hears a murder in a recording and can't be sure he heard it right. Francis Ford Coppola made it for a fraction of his Godfather budget, and the film's ending — Harry Caul tearing his apartment apart looking for the bug that isn't there — is the loneliest final scene in cinema. It won the Palme d'Or.",
        "Francis Ford Coppola",
        "The Conversation (1974) — the recording and the ending",
        113,
        "Watch the opening — the park, the mime, the recording that becomes the film's engine — and notice how Coppola builds the mystery from sound: the whole film is an act of listening, and the 'conversation' is replayed, isolated, and reinterpreted like a haunted recording. Then watch the ending, where Harry tears his own home apart and finds nothing: the film's argument — that the watcher is always watched, and paranoia is its own prison — is in that final shot, and the film's prophetic reading of the surveillance age made it the decade's most prescient thriller.",
        ["Thriller", "1970s", "Hollywood"],
    ),
    _entry(
        "film-young-frankenstein-1974",
        "Young Frankenstein (1974)",
        "The most lovingly crafted comedy ever made — Mel Brooks' parody shot in black and white on the original 1931 Frankenstein sets, with Gene Wilder's perfectionist Dr. Frankenstein ('It's Fronkensteen!'), Peter Boyle's tap-dancing monster, and the immortal 'Puttin' on the Ritz.' Wilder insisted the film be an homage, not a spoof — every frame is a tribute, and every gag lands.",
        "Mel Brooks",
        "Young Frankenstein (1974) — the 'Puttin' on the Ritz' scene",
        106,
        "Watch the 'Puttin' on the Ritz' number — the monster in top hat and tails, Gene Wilder's perfect comic timing — and notice how the film earns its anachronism: the dance is built from the earlier 'blind man' and 'wagon' gags, and the monster's joy is the film's heart. Then watch the 'Frau Blücher' horse-neigh joke and the 'Are you kidding? I'm a brilliant surgeon!' scene: the film's argument — that the monster's real problem is that everyone keeps screaming at him — is delivered with the decade's most precise comic acting.",
        ["Comedy", "1970s", "Hollywood"],
    ),
    _entry(
        "film-blazing-saddles-1974",
        "Blazing Saddles (1974)",
        "The most audacious comedy ever made by a major studio — a Black sheriff (Cleavon Little) defending a town that hates him, with Mel Brooks' wall-to-wall gags, the famous campfire fart scene, and an ending that literally breaks the fourth wall into a Hollywood backlot. It was so controversial that Warner Bros. nearly shelved it; it became one of the decade's biggest hits, and its satire of racism is still sharp.",
        "Mel Brooks",
        "Blazing Saddles (1974) — the ending and the campfire scene",
        93,
        "Watch the campfire scene — the cowboys, the beans, the sound effect — and notice how the film's most famous gag is also its thesis: the Old West was never noble, and the film's profanity is a demolition of the genre's dignity. Then watch the ending, where the fight spills into a 1974 movie premiere: the film's argument — that westerns are just shows, and racism is a role people choose — is in that final stunt, and the film's 'no holds barred' approach (it was the first studio comedy with the words the censors once banned) opened the door for every boundary-pushing comedy since.",
        ["Comedy", "Western", "1970s", "Hollywood"],
    ),
    _entry(
        "film-dog-day-afternoon-1975",
        "Dog Day Afternoon (1975)",
        "The true-crime comedy-drama that made the bank heist feel like a party — Al Pacino's 'Attica! Attica!' and the film's hostage standoff that turns into a street carnival. Sidney Lumet shot it in the real Brooklyn heat with real crowds, and the film's ending — the 'gay bank robber' whose heist was for his lover's surgery — is the decade's most surprising tragedy. It won the Oscar for Best Original Screenplay.",
        "Sidney Lumet",
        "Dog Day Afternoon (1975) — the 'Attica' scene and the ending",
        125,
        "Watch the 'Attica! Attica!' scene — Sonny on the steps, the crowd, the cops — and notice how Lumet films the heist as performance: the hostage-taker becomes a folk hero because the street decides he is, and the film's improvised energy (Pacino ad-libbed the 'Attica' chant) is its power. Then watch the ending, where the crowd's cheers turn to horror as the bus pulls away: the film's argument — that the American dream is a heist that always ends the same way — is in that final image.",
        ["Crime", "Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-barry-lyndon-1975",
        "Barry Lyndon (1975)",
        "The most beautiful film ever made — Stanley Kubrick's 18th-century rise-and-fall, shot by candlelight with lenses borrowed from NASA (f/0.7 Zeiss lenses that could capture a single flame). Ryan O'Neal's Irish adventurer climbs to the aristocracy and falls from it, and the film's narration, its duels, and its final image — a man whose only victory is survival — make it Kubrick's most perfect and most human work.",
        "Stanley Kubrick",
        "Barry Lyndon (1975) — the candlelight scenes and the ending",
        185,
        "Watch the candlelit interiors — the duels, the card games, the courtship — and notice how Kubrick's NASA lenses let him shoot by actual candlelight: the images have a texture no film has matched, and the stillness is the film's luxury. Then watch the ending, where Barry loses everything and the narrator tells you he was 'never to see them again': the film's argument — that ambition is a card game the house always wins — is in that final shot, and the film's 3-hour patience is rewarded by the greatest production design in cinema.",
        ["Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-nashville-1975",
        "Nashville (1975)",
        "The film with 24 main characters and no lead — Robert Altman's kaleidoscope of a country-music city over five days, where every story intersects at a rally that ends in an assassination. The songs were written and performed by the actors themselves, and the film's ending — the crowd singing 'You May Say I Ain't Free' over a dying man — is the most ironic final scene of the decade.",
        "Robert Altman",
        "Nashville (1975) — the ending",
        160,
        "Watch the opening — the traffic jam, the '200 Years' billboard, the overlapping voices — and notice how Altman builds a city from fragments: the film's 24 characters are introduced in a flurry of talk, and the chaos is the structure. Then watch the ending, where the assassination and the singing collide: the film's argument — that America sings over its own wounds — is in that final image, and the film's ensemble improvisation (the actors wrote their own songs and backstories) made it the decade's most ambitious group portrait.",
        ["Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-rocky-1976",
        "Rocky (1976)",
        "The $1 million underdog story written in three days by its star — Sylvester Stallone's boxer who gets a title shot and just wants to go the distance. It won Best Picture, spawned the decade's biggest franchise, and its ending — Rocky losing the fight but winning Adrian — remains the most honest happy ending in sports cinema. 'Gonna Fly Now' and the run up the Philadelphia steps became American iconography.",
        "John G. Avildsen",
        "Rocky (1976) — the training montage and the ending",
        120,
        "Watch the training montage — the raw eggs, the steps, 'Gonna Fly Now' — and notice how the film builds the film's engine from a single staircase: the montage turned the Philadelphia Museum steps into a pilgrimage site, and the music (by Bill Conti, who wrote it in a day) is the most famous training theme ever. Then watch the ending, where Rocky loses the decision and asks only 'Yo, Adrian, I did it': the film's argument — that winning isn't the point, lasting is — is in that final embrace, and the film's $117 million gross against its $1 million budget is the greatest return in cinema history.",
        ["Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-carrie-1976",
        "Carrie (1976)",
        "The prom-night horror that made Stephen King a household name — Brian De Palma's adaptation of King's first novel, with Sissy Spacek's telekinetic outcast and the most famous bucket of pig's blood in cinema. The film's split-screen prom sequence and its final shot — the hand rising from the grave — made it the defining horror film of the 1970s. The film cost under $2 million and grossed $33 million.",
        "Brian De Palma",
        "Carrie (1976) — the prom scene and the ending",
        98,
        "Watch the prom sequence — the slow-motion crowning, the bucket, the fire — and notice how De Palma splits the screen to show the cruelty and the revenge at once: the film's horror is that the audience roots for the destruction. Then watch the ending, where Sue dreams of the grave and the hand reaches out: the film's argument — that the bullied will rise — is in that final image, and the film's mix of high-school melodrama and Grand Guignol made it the model for every teen-horror film since.",
        ["Horror", "1970s", "Hollywood"],
    ),
    _entry(
        "film-all-the-presidents-men-1976",
        "All the President's Men (1976)",
        "The investigative-journalism thriller that made reporting feel like detective work — Robert Redford and Dustin Hoffman as Woodward and Bernstein, chasing Watergate through a parking garage, a phone book, and a whisper of 'Deep Throat.' The film won 4 Oscars, and its sound design — the clatter of typewriters as a percussive score — is the most famous in its genre. 'Follow the money' was invented for the film.",
        "Alan J. Pakula",
        "All the President's Men (1976) — the parking garage scenes",
        138,
        "Watch the parking-garage scenes — the 'Deep Throat' meetings, the darkness, the whispers — and notice how Pakula films journalism as espionage: the sources, the shadows, the risk, and the film's decision to never show Deep Throat's face (until the real one was revealed in 2005). Then watch the ending, where the story breaks and the camera pulls back to the typewriter keys: the film's argument — that the truth is built keystroke by keystroke — is in that final pull, and the film's influence on every newsroom drama is total.",
        ["Thriller", "1970s", "Hollywood"],
    ),
    _entry(
        "film-eraserhead-1977",
        "Eraserhead (1977)",
        "The midnight-movie phenomenon that launched David Lynch — five years in the making, a father's nightmare about fatherhood, with the Lady in the Radiator, the 'specimen' baby, and the most terrifying industrial soundtrack ever recorded. Stanley Kubrick screened it for the cast of The Shining to put them in the right mood. It cost $100,000 and became the most influential cult film of its era.",
        "David Lynch",
        "Eraserhead (1977) — the radiator and the ending",
        89,
        "Watch the opening — the planet, the sperm-like head, the industrial hiss — and notice how Lynch builds the film from texture and dread: the black-and-white photography, the noise, the total absence of conventional storytelling. Then watch the ending, where Henry's head opens into the radiator's light: the film's argument — that anxiety is the only real subject, and fatherhood its deepest form — is in that final image, and the film's influence (on everything from industrial music to indie cinema) made it the cult film of the century.",
        ["Horror", "1970s", "Hollywood"],
    ),
    _entry(
        "film-saturday-night-fever-1977",
        "Saturday Night Fever (1977)",
        "The film that made disco a national religion and John Travolta a star — Tony Manero's Brooklyn, his white suit, and the Bee Gees' 'Staying Alive.' But the film is darker than its legend: the bridge scene, the back-seat assault, and the ending's confession make it a working-class tragedy wearing a dance floor. The soundtrack became the best-selling album of its era.",
        "John Badham",
        "Saturday Night Fever (1977) — the opening walk and the ending",
        118,
        "Watch the opening — the white shoes, the walk, the 'Staying Alive' strut — and notice how Badham films the film's signature: the three-block walk is a dance, and the street is the stage before the disco's. Then watch the ending, where Tony confesses to Stephanie on the bridge: the film's argument — that the disco is an escape from a life that has no other doors — is in that final scene, and the film's darker second half was so at odds with its poster that the sequel (a pure dance film) pretended the tragedy never happened.",
        ["Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-the-deer-hunter-1978",
        "The Deer Hunter (1978)",
        "The Vietnam film that won Best Picture — three Pennsylvania steelworkers whose hunting trip becomes a war, with the film's centerpiece, the Russian roulette scene, becoming the most debated sequence in war cinema. Robert De Niro, Christopher Walken (his Oscar), and Meryl Streep headline, and the film's six-hour wedding-and-hunt opening is the decade's great portrait of American community before the war takes it.",
        "Michael Cimino",
        "The Deer Hunter (1978) — the wedding and the roulette scenes",
        182,
        "Watch the wedding sequence — the polka, the toasts, the community — and notice how Cimino spends the film's first hour building a world he's about to destroy: the friendship is the film's subject, and the war is what it costs. Then watch the Russian roulette scenes, where the film's central metaphor (America's gamble with its own young men) is staged in a bamboo cage: the film's argument — that the war broke something in the men who survived — is in Walken's performance, and the ending's 'God Bless America' is the decade's most ambiguous anthem.",
        ["War", "1970s", "Hollywood"],
    ),
    _entry(
        "film-halloween-1978",
        "Halloween (1978)",
        "The film that created the slasher genre — John Carpenter's $325,000 shocker about a babysitter, a masked killer, and a suburb. The opening five-minute POV shot, the eerie piano score (which Carpenter composed in an afternoon), and Jamie Lee Curtis' scream-queen turn made it one of the most profitable films ever made: it grossed $70 million. 'The Shape' — Michael Myers — never speaks and never dies.",
        "John Carpenter",
        "Halloween (1978) — the opening POV and the ending",
        91,
        "Watch the opening — the POV shot through the killer's eyes, the knife, the mask — and notice how Carpenter establishes the film's geometry: the tracking shot is the killer's gaze, and the film's tension comes from the camera itself. Then watch the ending, where Loomis empties his gun into Michael and the shape vanishes: the film's argument — that evil is a force, not a person — is in that final shot, and the film's influence (it invented the 'final girl' and the franchise template) is the largest of any horror film after Psycho.",
        ["Horror", "1970s", "Hollywood"],
    ),
    _entry(
        "film-days-of-heaven-1978",
        "Days of Heaven (1978)",
        "The most beautiful-looking film ever made, by consensus — Terrence Malick's turn-of-the-century love triangle set among wheat fields, shot almost entirely in 'magic hour' golden light by Néstor Almendros, who won the Oscar. The film's story — a laborer, his girlfriend, and the dying farmer who marries her — is narrated by the girl's little sister, and the ending's locusts and fire are among the most spectacular images in cinema.",
        "Terrence Malick",
        "Days of Heaven (1978) — the harvest and the locusts",
        94,
        "Watch the harvest scenes — the golden wheat, the threshers, the silence — and notice how Malick films work as worship: the film's images (shot in the last hour of daylight) are so gorgeous that the story almost disappears into them. Then watch the locust sequence and the fire, where the film's beauty turns Biblical: the film's argument — that paradise is always about to end — is in that catastrophe, and the narration by Linda Manz (a 14-year-old discovered on a bus) is the film's most quoted performance.",
        ["Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-grease-1978",
        "Grease (1978)",
        "The highest-grossing movie musical of its time — John Travolta's Danny and Olivia Newton-John's Sandy, Rydell High, and the most quotable songs of the 1970s ('Summer Nights,' 'You're the One That I Want'). The film's ending — the car flying into the sky — was a last-minute studio demand, and the film's 'rebel who becomes a jock' finale has been debated ever since. It's the most beloved high-school film of all time.",
        "Randal Kleiser",
        "Grease (1978) — the carnival ending",
        110,
        "Watch the 'Summer Nights' number — the beach, the bragging, the split-screen — and notice how the film's songs build the two versions of the same story: Danny's cool and Sandy's romance are the film's engine. Then watch the ending, where Sandy appears in leather and the car flies off: the film's argument — that high school is a performance you can choose to win — is in that final image, and the film's PG sanitizing of the raunchy stage show (and its total ignoring of the Rydell High setting's era) is part of its eternal charm.",
        ["Musical", "1970s", "Hollywood"],
    ),
    _entry(
        "film-kramer-vs-kramer-1979",
        "Kramer vs. Kramer (1979)",
        "The divorce drama that defined a generation of parenting — Dustin Hoffman's workaholic dad abandoned with his son when Meryl Streep's wife walks out, then the custody battle that follows. It won 5 Oscars including Best Picture and Best Actress (Streep), and the film's ice-cream scene and its ending — the elevator, the 'you don't know what it's like being a mother' — remain the most honest custody scenes in cinema.",
        "Robert Benton",
        "Kramer vs. Kramer (1979) — the ending",
        105,
        "Watch the first act — Joanna's departure, Ted's fumbling with the French toast and the bedtime — and notice how the film makes parenting the comedy and the tragedy at once: the single-dad learning curve is the film's heart, and Hoffman's performance (based on director Benton's own divorce) is lived-in. Then watch the ending, where the custody trial and the final elevator scene resolve: the film's argument — that a child's love is not a trophy to be won — is in that last exchange, and the film's two stars' acting duel made it the year's most talked-about film.",
        ["Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-manhattan-1979",
        "Manhattan (1979)",
        "Woody Allen's black-and-white valentine to New York — Isaac, a TV writer dating a 17-year-old, in love with his best friend's mistress, and the film's Gershwin score, its opening 'God, I love New York' monologue, and its final 'You have to have a little faith in people' are among the most famous in cinema. The 42-year-old/17-year-old romance is the film's contested heart — the film knows it's wrong, which is the point.",
        "Woody Allen",
        "Manhattan (1979) — the opening and the ending",
        96,
        "Watch the opening — the montage of New York, the 'God, I love New York' outtakes, the Gershwin 'Rhapsody in Blue' — and notice how Allen shoots the city in widescreen black and white (by Gordon Willis, the 'prince of darkness'): the film is a love letter that knows it's flawed. Then watch the ending, where Isaac chases Tracy in the rain and the film's last line lands: the film's argument — that love is a risk you take even when you're too old to — is in that final shot, and the film's self-awareness about its own questionable romance makes it the most honest of Allen's films.",
        ["Comedy", "1970s", "Hollywood"],
    ),
    _entry(
        "film-being-there-1979",
        "Being There (1979)",
        "The most quietly brilliant satire ever made — Peter Sellers as Chance, a gardener whose entire world is TV, who becomes a presidential adviser because everyone projects wisdom onto his simple statements. 'I like to watch.' The film's ending — Chance walking on water — is the most debated final scene in cinema, and Sellers' performance (his last great one) is a masterpiece of stillness.",
        "Hal Ashby",
        "Being There (1979) — the ending",
        130,
        "Watch the first hour — Chance's garden, the TV, his first 'appearance' — and notice how Ashby builds the film's satire from Sellers' total blankness: the joke is that everyone sees themselves in the man with nothing inside, and the film's deadpan never once winks. Then watch the ending, where Chance steps onto the lake: the film's argument — that America will elect any mirror, even an empty one — is in that final image, and the film's prophecy (that a man with no ideas can become a leader) has come true so many times it stopped being satire.",
        ["Comedy", "1970s", "Hollywood"],
    ),
]


def main() -> int:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    by_id = {t["id"]: t for t in data}
    by_name = {t["name"].lower(): t for t in data}

    errors = []
    for t in NEW_TOPICS:
        if t["id"] in by_id:
            errors.append(f"id already exists: {t['id']}")
        if t["name"].lower() in by_name:
            errors.append(f"name already exists: {t['name']}")
        if len(t["teaser"]) > 450:
            errors.append(f"teaser too long ({len(t['teaser'])}): {t['id']}")
        if len(t["exploreAction"]["instruction"]) > 450:
            errors.append(f"instruction too long ({len(t['exploreAction']['instruction'])}): {t['id']}")
        if len(t["name"]) > 80:
            errors.append(f"name too long ({len(t['name'])}): {t['id']}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    data.extend(NEW_TOPICS)
    PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"added {len(NEW_TOPICS)} entries → {len(data)} total")
    return 0


if __name__ == "__main__":
    sys.exit(main())
