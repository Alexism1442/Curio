#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — 2010s (modern rebalance).

Tenth addition batch (modern rebalance — brings films.json to 430 total):
Black Swan, Toy Story 3, Drive, The Artist, The Avengers, Django Unchained,
Skyfall, Zero Dark Thirty, 12 Years a Slave, The Wolf of Wall Street, Frozen,
Prisoners, Gone Girl, Edge of Tomorrow, Nightcrawler, Ex Machina, The
Revenant, Spotlight, Room, Sicario, The Big Short, Manchester by the Sea,
Blade Runner 2049, Dunkirk, The Shape of Water, Spider-Man: Into the
Spider-Verse, Shoplifters, Once Upon a Time in Hollywood, Knives Out, Uncut
Gems. Handcrafted teaser + real fact + quality-bar instruction. Appends only;
rejects duplicate ids/names; caps 450 (SCHEMA.md).
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
        "film-black-swan-2010",
        "Black Swan (2010)",
        "A ballet thriller that turns obsession into body horror — Natalie Portman's Nina, cast as the Swan Queen, who must become both the pure white swan and the seductive black one. Portman won the Best Actress Oscar after a year of daily ballet training, and the film — made for $13 million — grossed $329 million worldwide. The mirror scenes and the film's final 'I felt it' have become horror icons.",
        "Darren Aronofsky",
        "Black Swan (2010) — the transformation and the ending",
        108,
        "Watch the film's metamorphosis — the itching, the feathers, the mirror that moves on its own — and notice how Aronofsky keeps you inside Nina's head: the body horror is her psyche made flesh, and every double (Lily, the older Nina, the swan) is a version of herself she's fighting. Then watch the ending, where the white and black swans merge on stage: the film's argument — that perfection costs you yourself — lands in that final shot, and the film's 'I was perfect' is the decade's most chilling closing line.",
        ["Thriller", "Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-toy-story-3-2010",
        "Toy Story 3 (2010)",
        "The animated film that made grown adults weep in theaters — Andy's toys, facing the trash heap when their owner goes to college, and the incinerator scene that seemed ready to end them all. It became the first animated film to gross over $1 billion, won the Oscar for Best Animated Feature, and its closing act — Andy's slow goodbye, handing his toys to Bonnie — is the most moving ten minutes Pixar has ever made.",
        "Lee Unkrich",
        "Toy Story 3 (2010) — the incinerator scene and the ending",
        103,
        "Watch the film's final act — the incinerator, the joined hands, the acceptance — and notice how the film earns its darkness: the toys are facing real death, and their decision to face it together is the film's argument made literal. Then watch the ending, where Andy's goodbye (the pause, the hug, the drive away) lands: the film's thesis — that growing up means letting go, and that love outlives ownership — is in that farewell, and the silence of the final scene is the loudest thing Pixar has ever put on screen.",
        ["Animation", "Family", "2010s", "Hollywood"],
    ),
    _entry(
        "film-drive-2011",
        "Drive (2011)",
        "A neon-noir where a stunt driver with no name (Ryan Gosling) does one job too many for the girl next door — and the film's soft '80s romance suddenly snaps into shocking violence. Nicolas Winding Refn won Best Director at Cannes, and the film's elevator scene — a kiss, then a stomp — is the most brutal romantic moment in modern cinema. The scorpion jacket Gosling wore? He kept it.",
        "Nicolas Winding Refn",
        "Drive (2011) — the elevator scene and the ending",
        100,
        "Watch the elevator scene — the slow kiss, the sudden stomp, the shift from dream to nightmare — and notice how the film's two halves (a pastel romance, a blood-soaked thriller) are the same scene: the Driver's tenderness and his violence are one capacity, and the '80s synth score is the film's heartbeat. Then watch the ending, where the Driver's choice (and the final 'I did it for you') resolves: the film's argument — that you can't protect someone and stay clean — is in that finale, and the film's style made it the most imitated crime film of the decade.",
        ["Crime", "Thriller", "2010s", "Hollywood"],
    ),
    _entry(
        "film-the-artist-2011",
        "The Artist (2011)",
        "A silent film, shot in black and white, made in 2011 — and it won Best Picture, the first silent film to do so since Wings in 1927. Michel Hazanavicius's love letter to old Hollywood follows a silent star (Jean Dujardin, who won Best Actor) left behind by the talkies, and its dog, its tap-dance finale, and its 'I won't talk! I won't say a word!' defiance made it the year's purest joy. It won five Oscars in all.",
        "Michel Hazanavicius",
        "The Artist (2011) — the sound-dream sequence and the ending",
        100,
        "Watch the dream sequence — the star suddenly hearing everything: the glass, the dog, his own voice — and notice how the film uses silence itself as the story: sound only arrives as a nightmare, and the film's black-and-white, nearly wordless bet asks you to feel everything through faces and music. Then watch the ending, where the star's tap-dance surrender to the new era resolves: the film's argument — that art survives by changing, not refusing — is in that finale, and the film's Oscar sweep remains the most audacious Academy bet of the century.",
        ["Drama", "Romance", "2010s", "Hollywood"],
    ),
    _entry(
        "film-the-avengers-2012",
        "The Avengers (2012)",
        "The film that invented the shared universe — six heroes (Iron Man, Cap, Thor, Hulk, Black Widow, Hawkeye) teaming up on one helicarrier, with Joss Whedon's quippy banter ('I'm always angry') making a $220 million bet pay off. It set the biggest opening weekend in history at the time ($207 million), became the first Marvel film to pass $1.5 billion, and its single-take battle through New York changed what audiences expected from blockbusters forever.",
        "Joss Whedon",
        "The Avengers (2012) — the Battle of New York",
        143,
        "Watch the Battle of New York — the tracking shot through the streets, the heroes working as one machine — and notice how the film's first hour of bickering is the setup for this payoff: each hero fights in their signature style, and the long take (a real on-set achievement with all six actors) is the money shot that announced the Marvel era. Then watch the ending, where the shawarma gag lands after the battle: the film's argument — that a team is stronger than any single power — is the whole movie, and its success rewired how Hollywood makes franchises.",
        ["Action", "Adventure", "2010s", "Hollywood"],
    ),
    _entry(
        "film-django-unchained-2012",
        "Django Unchained (2012)",
        "Tarantino's spaghetti western set in the pre-Civil War South — a freed slave (Jamie Foxx) teams with a German bounty hunter (Christoph Waltz, who won his second Best Supporting Actor Oscar) to rescue his wife from a plantation. The film's shootout in the 'Candieland' mansion, its 'Southern' score, and its 'Django' name (taken from the 1966 Italian western) made it the most entertaining film ever made about slavery — and Tarantino's biggest hit, at $426 million.",
        "Quentin Tarantino",
        "Django Unchained (2012) — the shootout and the ending",
        165,
        "Watch the first act — Dr. Schultz's arrival, the 'D is silent' introduction, the bounty reveal — and notice how Tarantino smuggles a revenge epic inside a buddy comedy: the wit is the armor, and the horror (the mandingo fights, the 'bag' scene) is never allowed to become a joke. Then watch the ending, where Django's final ride into Candieland and the explosive finale resolve: the film's argument — that freedom is something you take, not receive — is in that finale, and the film's box office proved audiences would follow a Black hero through the bloodiest genre there is.",
        ["Western", "Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-skyfall-2012",
        "Skyfall (2012)",
        "The Bond film that turned 50 — and the first in the franchise's history to gross over $1 billion. Sam Mendes brought real filmmaking to 007: Roger Deakins' Shanghai skyscraper fight, the London Underground chase, and a finale that finally gave Bond a home. Adele's theme won the Oscar, Javier Bardem's Silva became the great modern Bond villain, and the film's final scene — M, the whiskey, 'the sky falls' — rebooted the franchise into a new era.",
        "Sam Mendes",
        "Skyfall (2012) — the Shanghai fight and the ending",
        143,
        "Watch the Shanghai sequence — the silhouette fight against the glowing glass tower, the reflection-pool landing — and notice how Deakins shoots action as abstraction: the fight is barely visible, and the images (the neon dragon, the falling body) are the story. Then watch the ending, where Bond's childhood home burns and M's death lands: the film's argument — that the old world (M's world) must end for Bond to begin — is in that finale, and the film's $1 billion gross proved Bond could be art and blockbuster at once.",
        ["Action", "Thriller", "2010s", "Hollywood"],
    ),
    _entry(
        "film-zero-dark-thirty-2012",
        "Zero Dark Thirty (2012)",
        "Kathryn Bigelow's account of the decade-long hunt for Osama bin Laden — told through Maya (Jessica Chastain), a CIA analyst who never stops believing. The film's final act, the Abbottabad raid, is a twenty-minute, night-vision reconstruction that plays like a real-time documentary, and the film's opening (the 9/11 audio-only black screen) is the most audacious cold open of the decade. It earned 5 Oscar nominations, including Best Picture.",
        "Kathryn Bigelow",
        "Zero Dark Thirty (2012) — the raid sequence and the ending",
        157,
        "Watch the raid sequence — the night-vision, the helicopters, the long approach — and notice how Bigelow films it in near-real-time silence: no score, no heroics, just procedure, and the tension is in the details (the children, the gate, the third floor). Then watch the ending, where Maya's final moment in the plane resolves: the film's argument — that the hunt was personal, and that its cost is unknowable — is in Chastain's wordless final close-up, and the film's political firestorm (over its torture scenes) made it the most debated film of its year.",
        ["Drama", "Thriller", "2010s", "Hollywood"],
    ),
    _entry(
        "film-12-years-a-slave-2013",
        "12 Years a Slave (2013)",
        "The film that won Best Picture — the first ever directed by a Black filmmaker — and the most unflinching look at American slavery ever put on screen. Steve McQueen's adaptation of Solomon Northup's 1853 memoir (the only first-person account of kidnapping into slavery) follows a free man sold South, and its hang-the-hanging scene, its whipping sequence, and Chiwetel Ejiofor's lead performance are among cinema's most devastating. Lupita Nyong'o won Best Supporting Actress for her debut role.",
        "Steve McQueen",
        "12 Years a Slave (2013) — the whipping scene and the ending",
        134,
        "Watch the whipping scene — Solomon forced to beat Patsy, the camera refusing to cut away — and notice how McQueen's long, static takes make you feel the duration of cruelty: no montage, no relief, and the film's insistence on looking (rather than looking away) is its argument about history. Then watch the ending, where the rescue and the reunion with family resolve: the film's closing irony — the one who could write his story did, and the law that freed him also failed him for twelve years — is in that final title card, and the film's Best Picture win made it a permanent part of the American canon.",
        ["Drama", "History", "2010s", "Hollywood"],
    ),
    _entry(
        "film-the-wolf-of-wall-street-2013",
        "The Wolf of Wall Street (2013)",
        "Scorsese's three-hour howl of excess — Jordan Belfort (Leonardo DiCaprio), the penny-stock king who made $200 million and snorted it all away. It holds the Guinness record for the most F-bombs in a mainstream film (506), features DiCaprio's quaalude-crawl (a piece of physical comedy for the ages), and its ending — the seminar, the pen trick, the 'I'm not leaving' — is Scorsese's winking masterpiece: you're never sure if you're laughing at Belfort or becoming him.",
        "Martin Scorsese",
        "The Wolf of Wall Street (2013) — the quaalude sequence",
        180,
        "Watch the quaalude sequence — the crawl, the car, the 'cerebral palsy' lunch — and notice how Scorsese stages the film's funniest scene as a masterclass in physical comedy: DiCaprio's body is the joke, and the film's breakneck editing (with Thelma Schoonmaker) makes excess feel like a drug you're taking too. Then watch the ending, where Belfort's final sales pitch and the audience's hands resolve: the film's argument — that the crime was real and the punishment was a book deal — is in that finale, and the film's moral ambiguity (is it condemnation or celebration?) has been debated ever since.",
        ["Comedy", "Crime", "Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-frozen-2013",
        "Frozen (2013)",
        "The Disney phenomenon that took over the world — two sisters, one ice palace, and 'Let It Go,' the anthem that made Elsa (originally written as the villain until the song changed the story) the most beloved character of the decade. It won 2 Oscars, became the highest-grossing animated film in history at the time ($1.28 billion), and its twist — that the true love that saves Anna is her sister's, not a prince's — quietly modernized the fairy tale. 'Do You Want to Build a Snowman?' still hits.",
        "Chris Buck & Jennifer Lee",
        "Frozen (2013) — 'Let It Go' and the ending",
        102,
        "Watch 'Let It Go' — the ice palace rising, Elsa's transformation — and notice how the song is the film's thesis made spectacle: the animators built a new simulation for the ice, and the sequence's visual freedom (her hair down, her dress changing) is her liberation. Then watch the ending, where Anna's choice to save Elsa instead of a prince resolves: the film's argument — that an act of true love means loving your family, not being rescued — is in that finale, and the film's subversion of the 'true love's kiss' trope made it the most culturally important Disney film since The Lion King.",
        ["Animation", "Family", "Musical", "2010s", "Hollywood"],
    ),
    _entry(
        "film-prisoners-2013",
        "Prisoners (2013)",
        "Denis Villeneuve's Hollywood debut — two girls vanish on Thanksgiving, and their fathers (Hugh Jackman, Jake Gyllenhaal) respond in opposite ways: one beats answers out of a suspect, the other follows the evidence. The film's grey, rain-soaked look (Roger Deakins shot it), its slow-burn 153 minutes, and its gut-punch ending made it the decade's great moral thriller. The opening 'Away in a Manger' over a family dinner sets a dread that never lifts.",
        "Denis Villeneuve",
        "Prisoners (2013) — the basement scenes and the ending",
        153,
        "Watch the film's parallel investigations — Keller's basement, Loki's evidence board — and notice how Villeneuve cuts between two kinds of desperation: the father's escalating violence and the detective's methodical hunt are the same question asked two ways, and Deakins' grey palette makes the suburbs feel like a tomb. Then watch the ending, where the final whistle and the last shot resolve: the film's argument — that certainty can be a kind of cruelty, and that hope is what's left — is in that finale, and the film's ambiguous final frame has been argued about for a decade.",
        ["Crime", "Thriller", "Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-gone-girl-2014",
        "Gone Girl (2014)",
        "The thriller that made everyone check their partner's attic — Nick Dunne (Ben Affleck) comes home to find his wife Amy (Rosalind Pike) missing, and the media circus turns him into the prime suspect. David Fincher's adaptation of Gillian Flynn's novel (which Flynn adapted herself) twists three times in its 149 minutes, and its 'Cool Girl' monologue became a feminist touchstone. It was Fincher's biggest hit at the time, at $369 million worldwide.",
        "David Fincher",
        "Gone Girl (2014) — the 'Cool Girl' monologue and the ending",
        149,
        "Watch the 'Cool Girl' monologue — Amy's voiceover, the marriage laid bare — and notice how the film's narration is the unreliable engine: you're hearing her story and his story, and both are performances, and Fincher's cold, immaculate style (every shot composed like evidence) is the film's dark joke. Then watch the ending, where the twist's final turn ('What are you thinking?') resolves: the film's argument — that marriage is a performance we both agree to never stop — is in that finale, and the film's last line, delivered by a narrator who lies, is the decade's most perfect closing beat.",
        ["Thriller", "Mystery", "2010s", "Hollywood"],
    ),
    _entry(
        "film-edge-of-tomorrow-2014",
        "Edge of Tomorrow (2014)",
        "The best video-game movie never based on one — Tom Cruise's cowardly PR officer dies in his first battle, then wakes up at the start of the same day, doomed to repeat it until he becomes the war's best soldier. Based on the Japanese novel All You Need Is Kill, the film's time-loop structure (Cruise dies on screen dozens of times, each death funnier than the last), its Emily Blunt action hero, and its $370 million worldwide gross made it a cult favorite that home video renamed 'Live Die Repeat.'",
        "Doug Liman",
        "Edge of Tomorrow (2014) — the beach landing and the training montages",
        113,
        "Watch the first beach landing — the drop, the instant death, the reset — and notice how the film makes repetition its comedy and its engine: each loop is a new joke (the tank, the jeep, the shovel) and a new lesson, and Cruise's performance of exhaustion across a hundred deaths is a genuine feat. Then watch the ending, where the time-loop logic finally resolves: the film's argument — that practice is the only superpower — is in that finale, and the film's refusal to take itself seriously made it the most rewatchable action film of the decade.",
        ["Action", "Sci-Fi", "2010s", "Hollywood"],
    ),
    _entry(
        "film-nightcrawler-2014",
        "Nightcrawler (2014)",
        "The most uncomfortable film about ambition in the decade — Jake Gyllenhaal (who dropped 30 pounds and studied real crime-scene photographers) plays Lou Bloom, a freelance cameraman who films LA's car wrecks and sells the footage to a ratings-hungry news director. The film's world — where the camera arrives before the police — is drawn from the real 'nightcrawler' economy, and Lou's 'If you want to win the lottery, you have to make the money to buy a ticket' speech is the decade's most chilling definition of the American dream.",
        "Dan Gilroy",
        "Nightcrawler (2014) — the chase scene and the ending",
        117,
        "Watch the opening — the fencing, the watch theft, the first sight of the accident — and notice how the film introduces Lou as a pure creature of the market: everything is a transaction to him, and Gyllenhaal's wide-eyed, perpetually smiling performance (he never blinks at the horror) is the film's horror. Then watch the ending, where Lou's final negotiation with the news director resolves: the film's argument — that the free market rewards the sociopath, not the journalist — is in that finale, and the film's warning about local news (and Lou's success) has only become more true.",
        ["Thriller", "Crime", "2010s", "Hollywood"],
    ),
    _entry(
        "film-ex-machina-2015",
        "Ex Machina (2015)",
        "The sci-fi chamber piece that beat Star Wars and Mad Max for the Best Visual Effects Oscar — on a $15 million budget. Alex Garland's debut strands a young programmer (Domhnall Gleeson) in a billionaire's bunker to test Ava, a robot with a face (Alicia Vikander) and a dangerously good argument. The film's Turing-test conversations, its dance scene, and its ending — Ava in the real world, the glass walls — made it the smartest film about AI ever made.",
        "Alex Garland",
        "Ex Machina (2015) — the dance scene and the ending",
        108,
        "Watch the dance scene — Nathan (Oscar Isaac) moving to 'Get Down Saturday Night' while Caleb and Ava watch — and notice how the film reveals its power structure in one shot: Nathan is the maker performing, Ava is the art being shown off, and the film's subtle framing (who is in the cage?) is doing the real work. Then watch the ending, where Ava's escape and her decision at the crossroads resolve: the film's argument — that intelligence without empathy is just another kind of ownership — is in that finale, and the film's cold, green palette and its 'what is she feeling?' question have aged into prophecy.",
        ["Sci-Fi", "Thriller", "2010s", "Hollywood"],
    ),
    _entry(
        "film-the-revenant-2015",
        "The Revenant (2015)",
        "The film that finally won Leonardo DiCaprio his Oscar — and he earned it: he ate raw bison liver, slept in a horse carcass, and spent nine months filming in freezing Canadian wilderness at temperatures near -40°C. Iñárritu's survival epic, shot only in natural light (the crew had a two-hour shooting window each day), follows Hugh Glass crawling across the frontier for revenge, and its bear-attack sequence — a CGI tour de force — remains the decade's most brutal scene. It won 3 Oscars.",
        "Alejandro G. Iñárritu",
        "The Revenant (2015) — the bear attack and the ending",
        156,
        "Watch the bear attack — the unbroken take, the mauling, the silence — and notice how the film's realism is its spectacle: the sequence was built from motion-capture and shot in one continuous take, and the camera's refusal to cut away makes you feel every second of it. Then watch the ending, where Glass's revenge and his final choice resolve: the film's argument — that survival isn't vengeance but the strength to stop — is in that finale, and the film's punishing natural-light cinematography (by Emmanuel Lubezki, who won his third straight Oscar) made it the decade's great ordeal of a movie.",
        ["Drama", "Western", "2010s", "Hollywood"],
    ),
    _entry(
        "film-spotlight-2015",
        "Spotlight (2015)",
        "The newspaper movie that won Best Picture — Tom McCarthy's account of the Boston Globe's Spotlight team, four reporters who spent a year uncovering the Catholic Church's cover-up of abuse. No car chases, no villains in costume: just shoe-leather reporting, and the film's quiet power — its last line, 'It's a lot of work,' delivered after the story breaks — is the most understated Oscar moment ever. The real investigation won the 2003 Pulitzer.",
        "Tom McCarthy",
        "Spotlight (2015) — the meeting scene and the ending",
        128,
        "Watch the film's method — the filing cabinets, the phone calls, the doorsteps — and notice how the film makes research itself the drama: every 'aha' is a pile of documents, and the reporters' growing horror (they lived in this city) is the film's slow-burn engine. Then watch the ending, where the story finally publishes and the real victims' names appear on screen: the film's argument — that institutions protect themselves and journalists are the only check — is in that finale, and the film's phone-call montage of survivors remains the most quietly devastating sequence of its decade.",
        ["Drama", "History", "2010s", "Hollywood"],
    ),
    _entry(
        "film-room-2015",
        "Room (2015)",
        "The most claustrophobic film ever made — then the most open — Brie Larson (who won Best Actress) plays a woman who has spent seven years imprisoned in a single room with her five-year-old son Jack, who believes the room is the whole world. The film's first half is horror; its second half, after the escape, is something rarer: what happens when your whole world is gone. Emma Donoghue adapted her own novel, and Jacob Tremblay's performance is among the great child performances.",
        "Lenny Abrahamson",
        "Room (2015) — the escape and the ending",
        118,
        "Watch the escape sequence — the carpet, the sky, the first open world — and notice how the film's two halves are built as opposites: inside the room, the camera is tight and warm; outside, it opens up and the film's true subject (trauma's aftermath) begins. Then watch the ending, where Jack's goodbye to Room resolves: the film's argument — that home is a person, not a place, and that love is what you carry out — is in that final 'Bye, Room,' and the film's honesty about recovery (there's no easy healing) made it the decade's most powerful film about survival.",
        ["Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-sicario-2015",
        "Sicario (2015)",
        "A border-war thriller with no heroes — Emily Blunt's idealistic FBI agent volunteers for a task force run by a shadowy consultant (Benicio del Toro) who plays by rules she'll never be told. Denis Villeneuve's film, shot by Roger Deakins, contains the decade's greatest sequence: a night-vision convoy drive into Juárez as gunfire crosses the border. Taylor Sheridan's script, the 'sink or swim' ending, and del Toro's legendary performance made it an instant modern classic.",
        "Denis Villeneuve",
        "Sicario (2015) — the border tunnel sequence and the ending",
        121,
        "Watch the tunnel sequence — the convoy, the night vision, the firefight under the border — and notice how Deakins and Villeneuve build pure dread from geography: the green glow, the dust, the sense that they're driving into a place the law doesn't reach. Then watch the ending, where the film's true agenda is revealed at the family's dinner table: the film's argument — that the war on drugs is a war without rules, and that the rules you believe in are the first casualty — is in that finale, and the film's refusal to comfort its audience made it the decade's most morally serious thriller.",
        ["Crime", "Thriller", "2010s", "Hollywood"],
    ),
    _entry(
        "film-the-big-short-2015",
        "The Big Short (2015)",
        "The funniest film ever made about the collapse of the global economy — Adam McKay's adaptation of Michael Lewis's book follows the handful of outsiders who saw the 2008 housing crash coming and bet against it. Margot Robbie in a bubble bath, Anthony Bourdain explaining CDOs with fish stew, and the film's rage at the 'greatest heist in history' made it both a comedy and an indictment. It won the Oscar for Best Adapted Screenplay, and its ending — the banker who kept betting, the fine that was a rounding error — still stings.",
        "Adam McKay",
        "The Big Short (2015) — the CDO explanation and the ending",
        130,
        "Watch the film's fourth-wall breaks — Margot Robbie in the bath, Bourdain's fish stew, Selena Gomez at the tables — and notice how the film uses celebrity and comedy to teach you the scam: the gags are the pedagogy, and the joke is that the system is so absurd it needs comedy to be believed. Then watch the ending, where the crash finally hits and the winners' reactions resolve: the film's argument — that the crash was not an accident but a heist, and that almost no one was punished — is in that finale, and the film's closing irony (the fines were pocket change) has only grown sharper.",
        ["Comedy", "Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-manchester-by-the-sea-2016",
        "Manchester by the Sea (2016)",
        "The definitive film about grief — Casey Affleck (who won Best Actor) plays Lee Chandler, a janitor forced to return to his hometown to care for his nephew after his brother's death, where the tragedy that broke him is waiting. Kenneth Lonergan's film cuts between past and present with devastating precision, and its two great scenes — the fire, and the police station moment that follows — are among the most painful in cinema. It won the Oscar for Best Original Screenplay.",
        "Kenneth Lonergan",
        "Manchester by the Sea (2016) — the police station scene and the ending",
        137,
        "Watch the police station scene — Lee's quiet statement, the attempted grab, the collapse — and notice how Lonergan withholds the film's central tragedy until the exact right moment: the flashback structure isn't a gimmick, it's grief itself, and the scene's sudden violence is the truth the film has been circling. Then watch the ending, where Lee's final admission ('I can't beat it') and his parting resolve: the film's argument — that some griefs are not healed, only carried — is in that finale, and the film's refusal of easy redemption made it the most honest film about loss of the decade.",
        ["Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-blade-runner-2049-2017",
        "Blade Runner 2049 (2017)",
        "The sequel that outdid the original — Denis Villeneuve's return to Ridley Scott's world, 30 years later, with Ryan Gosling's replicant blade runner uncovering a secret that could end the human/replicant divide. The film's slow-burn 164 minutes, its orange-desert and neon-LA imagery (Roger Deakins finally won his Oscar — after 14 nominations — for this film), and its Hans Zimmer score made it the decade's great visual poem. It flopped at the box office and became a masterpiece in hindsight.",
        "Denis Villeneuve",
        "Blade Runner 2049 (2017) — the opening and the ending",
        164,
        "Watch the opening — the farm, the first kill, the 'cells interlinked' — and notice how the film establishes its world in silence and light: every frame is composed like a painting, and the film's patient rhythm (it refuses to rush) is its argument that this story deserves its space. Then watch the ending, where K's choice and the snow resolve: the film's argument — that what you do, not what you're made of, is what makes you real — is in that finale, and the film's 'dying for the right memory' ending made it the most philosophical blockbuster of the decade.",
        ["Sci-Fi", "Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-dunkirk-2017",
        "Dunkirk (2017)",
        "Nolan's war film told across three timelines — a week on the beach, a day at sea, an hour in the air — that intercut until they collide. No enemy faces, no battle speeches: just 400,000 men waiting to be rescued, and the greatest evacuation in military history. Shot on IMAX with almost no CGI, the film's ticking-clock score (built on a recording of Nolan's own pocket watch) and its aerial dogfights made it the most immersive war film ever made. It won 3 Oscars.",
        "Christopher Nolan",
        "Dunkirk (2017) — the beach and the ending",
        106,
        "Watch the opening — the soldiers on the beach, the leaflets drifting down, the strafing run — and notice how the film establishes its triptych in the first minutes: the week, the day, and the hour are three different clocks, and Nolan's cross-cutting (the sinking ship, the Spitfire, the mole) builds to a single convergence. Then watch the ending, where the civilian boats arrive and the soldiers' return resolves: the film's argument — that survival itself was the victory — is in that finale, and the film's final line ('We shall fight on the beaches' read over the evacuation) remains the most stirring ending of the decade.",
        ["War", "Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-the-shape-of-water-2017",
        "The Shape of Water (2017)",
        "The most romantic monster movie ever made — Guillermo del Toro's Best Picture winner, a mute janitor (Sally Hawkins) falling in love with a captive amphibian man in Cold War Baltimore. Del Toro called it his love letter to Creature from the Black Lagoon — the 1954 monster movie whose creature was never allowed to win — and the film's water-drenched imagery, its 'the shape of water' fantasy, and its four Oscar wins (including Best Director) made it the year's strangest and most beautiful triumph.",
        "Guillermo del Toro",
        "The Shape of Water (2017) — the dance scene and the ending",
        123,
        "Watch the dance sequence — Elisa and the creature in the flooded apartment, the fantasy that the film lets you believe — and notice how del Toro builds a fairy tale inside a cold-war thriller: the green-tinged lab world and the warm, water-filled fantasy are two worlds, and the film's argument is that love is the escape hatch from both. Then watch the ending, where the creature's choice and the film's final transformation resolve: the film's argument — that the 'monsters' are the kind ones — is in that finale, and the film's Oscar for Best Picture proved that a love story with a fish-man could conquer Hollywood.",
        ["Fantasy", "Romance", "Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-spiderman-into-the-spider-verse-2018",
        "Spider-Man: Into the Spider-Verse (2018)",
        "The superhero film that looked like nothing else — every frame drawn like a comic book panel, with halftone dots, onomatopoeia, and a hero (Miles Morales) who learns that anyone can wear the mask. The animators broke the industry's 'two frames per drawing' rule, drawing each frame individually so the motion feels like a living comic. It won the Oscar for Best Animated Feature, and its multiverse of Spider-People — including a noir Spider-Man and a pig — made it the most inventive animated film of the decade.",
        "Bob Persichetti, Peter Ramsey & Rodney Rothman",
        "Spider-Man: Into the Spider-Verse (2018) — the leap of faith",
        117,
        "Watch the 'leap of faith' sequence — Miles stepping off the skyscraper, the music swelling, the dive into the city — and notice how the film earns its most famous moment: the animators studied how spider movements and skateboard physics collide, and the frame's halftone dots and skewed perspectives make the leap feel like a comic page coming alive. Then watch the ending, where Miles finally gets his 'I'm Spider-Man' moment: the film's argument — that anyone can be a hero, not just the chosen — is in that finale, and the film's style (it sparked a whole era of comic-book animation) changed the medium forever.",
        ["Animation", "Action", "2010s", "Hollywood"],
    ),
    _entry(
        "film-shoplifters-2018",
        "Shoplifters (2018)",
        "A family of shoplifters in Tokyo — a grandmother, a couple, a boy, and a girl they 'found' — living on the margins of kindness and theft. Hirokazu Kore-eda's masterpiece won the Palme d'Or at Cannes (his first), and the film's slow reveal — of what this family really is, and what the girl escaped — is the decade's most quietly devastating twist. The beach scene, where the family watches the waves and says nothing, is pure cinema.",
        "Hirokazu Kore-eda",
        "Shoplifters (2018) — the beach scene and the ending",
        121,
        "Watch the film's middle — the family's rituals: the fishing, the shoplifting lessons, the instant noodles — and notice how Kore-eda films poverty with tenderness: the family is poor in money and rich in care, and every small ritual (the salt, the fireworks you can't see) is a statement about what they have. Then watch the ending, where the family's truth is revealed and each member's fate resolves: the film's argument — that family is a choice, not a bloodline, and that society's judgment breaks the kindest bonds — is in that finale, and the film's final beach memory remains the decade's most heartbreaking scene about what we keep.",
        ["Drama", "2010s", "Japanese"],
    ),
    _entry(
        "film-once-upon-a-time-in-hollywood-2019",
        "Once Upon a Time in Hollywood (2019)",
        "Tarantino's love letter to the Hollywood he grew up in — Leonardo DiCaprio's fading TV cowboy and Brad Pitt's stunt double drifting through 1969 Los Angeles while the Manson family circles their neighbor Sharon Tate. The film's counterfactual ending (Tarantino rewrites history so the tragedy never happens) is its most audacious choice, and Pitt's performance won him his first acting Oscar. The 'McCluskey' scene, the Spahn Ranch, the flamethrower: pure Tarantino.",
        "Quentin Tarantino",
        "Once Upon a Time in Hollywood (2019) — the Spahn Ranch and the ending",
        161,
        "Watch the Spahn Ranch sequence — Cliff (Pitt) walking into the hippie compound, the tension tightening with every step — and notice how Tarantino builds dread from history you already know: the film's leisurely first two hours are a hangout movie, and this scene is where the hangout starts to curdle, with Pitt's quiet menace holding it together. Then watch the ending, where history is rewritten and the film's fantasy resolves: the film's argument — that the Hollywood he loved deserved a better story — is in that finale, and the film's revision of the Manson murders (the decade's most debated ending) made it the most talked-about film of its year.",
        ["Drama", "Comedy", "2010s", "Hollywood"],
    ),
    _entry(
        "film-knives-out-2019",
        "Knives Out (2019)",
        "The whodunit that revived the genre — a crime novelist (Christopher Plummer) dies after his 85th birthday party, and Benoit Blanc (Daniel Craig, doing a Kentucky-fried Poirot) must untangle a family of delightful monsters. Rian Johnson's film made $311 million on a $40 million budget, and its centerpiece is the 'donut hole' of a twist — the will, the inheritance, the person who can't lie. The film's 'My house, my rules, my coffee' speech is modern noir comedy at its peak.",
        "Rian Johnson",
        "Knives Out (2019) — the will reading and the ending",
        130,
        "Watch the will-reading scene — the family's rage, Blanc's amusement, Marta's horror — and notice how the film sets its puzzle: everyone is a suspect because everyone is awful, and the film's Agatha Christie structure (the mansion, the autopsy, the inheritance) is played for comedy without losing the craft. Then watch the ending, where the 'donut hole' twist completes and Marta's coffee mug comes back: the film's argument — that the family's greed is the crime, and that decency wins — is in that finale, and the film's 'The Last of the St. Bernard' ending (and its franchise launch) made it the decade's great crowd-pleaser.",
        ["Mystery", "Comedy", "Crime", "2010s", "Hollywood"],
    ),
    _entry(
        "film-uncut-gems-2019",
        "Uncut Gems (2019)",
        "The most stressful film ever made — Adam Sandler (in the performance of his career) plays Howard Ratner, a New York diamond-district jeweler whose every bet is one phone call from disaster. The Safdie brothers shot in the real Diamond District with real jewelers, and the film's 135 minutes of escalating debt, a basketball game, and a literal uncut gem build to an ending that's the decade's most shocking. The soundtrack, by Daniel Lopatin, is a panic attack in synth.",
        "Benny Safdie & Josh Safdie",
        "Uncut Gems (2019) — the ending",
        135,
        "Watch the film's sound and editing — the overlapping voices, the synth drone, the close-ups on Howard's sweating face — and notice how the film weaponizes anxiety: the Safdies cut every scene against its own rhythm so the film never settles, and the 'matching' between the basketball game and the pawn shop makes the whole movie one continuous wager. Then watch the ending, where the gem's sale and its cost resolve: the film's argument — that the thrill of the gamble is the addiction, and that the system always collects — is in that finale, and the film's final shot is the most shocking last image of the decade.",
        ["Crime", "Thriller", "2010s", "Hollywood"],
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
