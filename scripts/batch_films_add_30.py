#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries (v1.0 content pass).

The 130-topic pool was heavy on canon and light on crowd-pleasers, modern
blockbusters, and off-beat gems. This batch appends 30 NEW topics spanning
1927 → 2022 — classics (Metropolis, Some Like It Hot), seventies/eighties
pillars (Alien, The Shining, Raiders, E.T.), nineties icons (Shawshank,
Heat, Fight Club), and modern + niche picks (The Lives of Others, La Haine,
Amores Perros, The Handmaiden, Aftersun, Banshees) — each with a
handcrafted teaser that makes you WANT to watch, a real, verifiable fact,
and an instruction that passes the §2.1 quality bar (actionable, specific,
time-bounded, curiously framed). Cap 450 (SCHEMA.md). Appends only — never
rewrites existing entries. Existing IDs are rejected (no silent overwrite).
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
        "film-metropolis-1927",
        "Metropolis (1927)",
        "The first sci-fi blockbuster — 37,000 extras, a budget that bankrupted its studio, and a robot double named Maria who nearly burns a city. Fritz Lang built an entire metropolis in miniature, and its image of the working class as machine parts still haunts every dystopia made since.",
        "Fritz Lang",
        "Metropolis (1927) — the machine scene and the robot Maria",
        60,
        "Watch the machine scene — Freder, the 'Moloch' furnace, the hands at the dials — where Lang's whole thesis is in one image: the workers as replaceable machine parts. Then watch Maria's transformation, the robot built in the famous ring-of-light laboratory, and notice how the film flips its own warning: the false savior built to betray the workers is finally consumed by the truth it tried to bury.",
        ["Sci-Fi", "Classic", "German"],
    ),
    _entry(
        "film-modern-times-1936",
        "Modern Times (1936)",
        "Chaplin's last ride as the Tramp — and the only time the character ever 'speaks' on screen, in a gibberish song Chaplin wrote himself. The feeding machine, the roller-skating near the department-store ledge, and a final walk into the sunrise that was meant to be the Tramp's farewell.",
        "Charles Chaplin",
        "Modern Times (1936) — the feeding machine and the ending",
        87,
        "Watch the feeding-machine sequence — the 'automatic waiter' that feeds the Tramp while he works — and notice how Chaplin predicted the assembly line's absurdity decades before it was a cliché: the machine's breakdown is the film's whole argument. Then watch the ending, the Tramp and the Gamin walking away singing: Chaplin wrote it as a farewell to the character, and the gibberish song he sings is his only sung performance.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-double-indemnity-1944",
        "Double Indemnity (1944)",
        "The film that defined film noir — a housewife, her husband's 'accident,' and the insurance man who writes the murder into a policy. Wilder and Raymond Chandler rewrote the script chain-smoking in an office, and the real 1927 murder that inspired James M. Cain's novella used the same trick: a policy with double indemnity.",
        "Billy Wilder",
        "Double Indemnity (1944) — the first meeting and the garage murder",
        107,
        "Watch the first meeting — Walter and Phyllis, the anklet, the stairway — and notice how Wilder stages attraction as a business negotiation: every line is a policy clause. Then watch the garage murder, where the film's famous logic — that a murder on a train is statistically invisible — plays out, and the ending, where the film's last words land on a clock: Wilder's most perfectly wound noir device.",
        ["Noir", "Classic", "Hollywood"],
    ),
    _entry(
        "film-sunset-boulevard-1950",
        "Sunset Boulevard (1950)",
        "A silent-film star, a pool, and a dead man narrating his own murder — the Hollywood kiss-off told from the grave. Gloria Swanson, a genuine silent queen, played Norma Desmond with her real history in the frame, and 'I'm ready for my close-up' remains cinema's most famous curtain line.",
        "Billy Wilder",
        "Sunset Boulevard (1950) — the opening and Norma's close-up",
        110,
        "Watch the opening — the body in the pool, the voiceover from the dead — and notice how Wilder breaks the first rule of narration on purpose: the corpse talks, and the mystery becomes 'how,' not 'who.' Then watch the New Year's party, where Norma performs a silent-film pantomime for the guests who've come to use her house, and the ending, where the close-up she's always wanted finally comes — on the wrong side of a lens.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-12-angry-men-1957",
        "12 Angry Men (1957)",
        "One room, one hot afternoon, twelve strangers, a boy's life — and a directorial debut shot in 19 days. Sidney Lumet started the camera high and let it sink as the room closed in, and the whole film hangs on a single word: 'guilty.' The only juror ever named is Davis.",
        "Sidney Lumet",
        "12 Angry Men (1957) — the first vote and the knife",
        96,
        "Watch the first vote — eleven hands go up — and notice how Lumet makes the room itself a character: the camera starts above the action and slowly drops until the walls crowd the frame. Then watch the knife scene, where Juror 8 produces the switchblade from his pocket: the film's argument about reasonable doubt is staged as a single object, and the film's famous ending — the final reveal of the verdict — turns on a word nobody in the room said.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-some-like-it-hot-1959",
        "Some Like It Hot (1959)",
        "Marilyn Monroe, two musicians in drag, a Florida hotel, and the most-quoted last line in cinema history — 'Well, nobody's perfect.' Monroe's slow 'Where am I?' takes pushed the shoot weeks over schedule, and Wilder later said the film was worth every take. The world got one of its greatest comedies anyway.",
        "Billy Wilder",
        "Some Like It Hot (1959) — the train compartment and the last line",
        121,
        "Watch the train-compartment scene — Josephine and Daphne meeting Sugar — and notice how Wilder plays the disguise for suspense, not just farce: every close call is a thriller beat in heels. Then watch the ending, where Joe E. Brown's 'Nobody's perfect' — voted the greatest film line of all time — lands: Wilder earns it with an Osgood-Daphne courtship that's genuinely tender, which is why the joke still lands.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-graduate-1967",
        "The Graduate (1967)",
        "The film that taught the 1960s how to feel alienated — a 21-year-old played by a 30-year-old Dustin Hoffman, an older woman, a scuba suit, and Simon & Garfunkel soundtracking a generation's drift. Mike Nichols' directorial debut, and its ending — two people on a bus, smiles fading — is the most honest 'happy ending' ever shot.",
        "Mike Nichols",
        "The Graduate (1967) — the opening and the bus ending",
        106,
        "Watch the opening — Benjamin at the airport, the fish tank, the pool — and notice how Nichols films paralysis: the camera floats behind glass, and the parents' party plays like a horror scene in daylight. Then watch the final scene on the bus, where the smiles turn to doubt: Nichols refused to cut it happy, and the film's whole argument about 'plastics' and the future is in those two faces as they stop smiling.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-one-flew-over-the-cuckoos-nest-1975",
        "One Flew Over the Cuckoo's Nest (1975)",
        "Only the second film ever to sweep the five major Oscars — and it was shot in a real asylum with real patients as extras. Jack Nicholson's McMurphy versus Nurse Ratched was never meant to be a fair fight; that's the point. The ending's sacrifice moved the crew to tears on set.",
        "Miloš Forman",
        "One Flew Over the Cuckoo's Nest (1975) — the group session and the ending",
        133,
        "Watch McMurphy's first group session — the laughter, the cigarette, the vote — and notice how Forman stages the ward as a bureaucracy, not a hospital: Ratched wins by procedure, never by force. Then watch the fishing trip, where the 'patients' are free for one afternoon, and the ending, where the story's true hero is the giant Chief: the film's argument about institutional power lands in the window he smashes.",
        ["Drama", "1970s", "Hollywood"],
    ),
    _entry(
        "film-alien-1979",
        "Alien (1979)",
        "'In space no one can hear you scream' — and in the chestburster scene the crew genuinely didn't know what was coming: Ridley Scott filmed their real shock. H.R. Giger's biomechanical nightmare, a ship named after Odysseus' vessel, and the genre's greatest final girl in Ripley, who only becomes the hero once the men are gone.",
        "Ridley Scott",
        "Alien (1979) — the first hour and the chestburster scene",
        117,
        "Watch the first hour's slow dread — the derelict ship, the egg, Kane's facehugger — and notice how Scott withholds the monster: the horror is architecture, corridors, and the ship's breathing. Then watch the chestburster dinner scene, where the cast's genuine panic is on film: the only time a cast's real, unrehearsed shock ever made a movie's scariest moment, and the reason nobody drinks water during it.",
        ["Sci-Fi", "Horror", "1970s", "Hollywood"],
    ),
    _entry(
        "film-the-shining-1980",
        "The Shining (1980)",
        "Kubrick's 'all work and no play' — Shelley Duvall's breakdown was real, Danny Lloyd didn't know he was in a horror film until he was an adult, and the hedge maze was Kubrick's invention because he found the novel's hedge animals 'unfilmable.' Stephen King still doesn't like it. That's how you know it's a masterpiece.",
        "Stanley Kubrick",
        "The Shining (1980) — the typewriter scene and the ending",
        144,
        "Watch the 'all work and no play' scene — the typewriter pages, Duvall's genuine terror, the dozens of takes Kubrick demanded — and notice how the film's horror is repetition: the same words, the same corridors, the same twins. Then watch the ending, the maze and the photograph: Kubrick's coldest joke — that the hotel has always owned Jack — lands in a single freeze-frame that still breaks the internet.",
        ["Horror", "1980s", "Hollywood"],
    ),
    _entry(
        "film-raiders-of-the-lost-ark-1981",
        "Raiders of the Lost Ark (1981)",
        "Harrison Ford had dysentery the day they shot the Cairo swordfight — so instead of the planned duel he just shot the swordsman, and the most iconic moment in adventure cinema was born from food poisoning. Spielberg and Lucas wanted Bond with a whip; they got the film that invented the modern blockbuster.",
        "Steven Spielberg",
        "Raiders of the Lost Ark (1981) — the opening and the truck chase",
        115,
        "Watch the opening — the jungle, the boulder, the golden idol — and notice how Spielberg does more with a silhouette, a rope, and a panicked face in eight minutes than most films do in two hours: geography, stakes, and character in one tutorial. Then watch the truck chase, shot with 70 stuntmen and weeks of rehearsal: the whip, the convoy, and the pure kinetic joy of a man holding on.",
        ["Action", "Adventure", "1980s", "Hollywood"],
    ),
    _entry(
        "film-et-the-extra-terrestrial-1982",
        "E.T. the Extra-Terrestrial (1982)",
        "E.T. was Spielberg's imaginary friend — the alien he invented as a lonely kid after his parents' divorce. The bikes-against-the-moon image became its poster, Reese's Pieces invented product placement, and 'I'll be right here' made grown adults weep in theaters worldwide. It outgrossed Star Wars.",
        "Steven Spielberg",
        "E.T. the Extra-Terrestrial (1982) — the first meeting and the finale",
        115,
        "Watch the first meeting — Elliott in the shed, E.T.'s hand, the whispered 'phone home' — and notice how Spielberg films the alien's body language: every gesture is a child's, because E.T. is the child Spielberg was. Then watch the finale, the bicycles against the moon and the goodbyes: the film's whole argument about grief, imagination, and saying goodbye — Spielberg's own — is in that last shot.",
        ["Sci-Fi", "Family", "1980s", "Hollywood"],
    ),
    _entry(
        "film-come-and-see-1985",
        "Come and See (1985)",
        "Roger Ebert called it the most powerful anti-war film ever made — and it feels less like watching than surviving. Its teenage lead, Aleksei Kravchenko, had never acted; the film was nearly banned; and its title comes from the Book of Revelation. It is a horror film about the Nazi occupation of Belarus, and it never looks away.",
        "Elem Klimov",
        "Come and See (1985) — the first hour and the barn",
        60,
        "Watch the first hour — Florya digging in the sand, the rifle, the drift into the partisans — and notice how Klimov films war as a fairy tale gone wrong: the color and the boy both drain as the film goes on. Then watch the barn scene, the film's unbearable center, where the village's fate is shown in full: the ending's epilogue — the real Khatyn massacre that inspired it — is the film's final refusal to let you forget.",
        ["War", "Drama", "1980s", "Soviet"],
    ),
    _entry(
        "film-die-hard-1988",
        "Die Hard (1988)",
        "The film that turned 'Die Hard on a…' into its own genre, adapted from a novel called Nothing Lasts Forever. Bruce Willis was a TV star cast against type, the Nakatomi Plaza is the real Fox Plaza, and the TV-safe version of the catchphrase is 'yippee-ki-yay, melon farmer.' Barefoot hero, glass ceiling, one perfect action movie.",
        "John McTiernan",
        "Die Hard (1988) — the takeover and the vault scene",
        132,
        "Watch the first act — the Christmas party, the takeover, the fire hose — and notice how McTiernan builds the skyscraper as a chessboard: every floor, vent, and elevator is a move. Then watch the vault scene, where John fakes a surrender by dropping a watch and a body — the film's cleverest beat — and the ending, where Hans is the only one who ever truly outsmarts him, and the film lets John shoot a terrorist with a taped-on gun for pure holiday cheer.",
        ["Action", "1980s", "Hollywood"],
    ),
    _entry(
        "film-silence-of-the-lambs-1991",
        "The Silence of the Lambs (1991)",
        "The third film ever to sweep the five major Oscars — and Anthony Hopkins is on screen for just 16 minutes, the shortest Best Actor performance ever to win. The 'Goodbye Horses' dance, the 'fava beans' whisper, and a Clarice Starling who talks her way into your nightmares. Jodie Foster read the novel on a flight and couldn't put it down.",
        "Jonathan Demme",
        "The Silence of the Lambs (1991) — the first meeting and the basement finale",
        118,
        "Watch the first meeting — Clarice in the cell, the 'I've eaten some men' speech — and notice how Demme films Lecter's eyes: the camera holds on his face while he holds on hers, so you become the one being examined. Then watch the night-vision basement finale, where Clarice's real recorded heartbeat is the soundtrack: the film's scariest sequence is also its most empathetic, because the film is about her, not him.",
        ["Thriller", "Horror", "1990s", "Hollywood"],
    ),
    _entry(
        "film-shawshank-redemption-1994",
        "The Shawshank Redemption (1994)",
        "The highest-rated film on IMDb for over a decade — and it flopped at the box office, grossing less than its budget before VHS and word of mouth made it immortal. It was shot in a real decommissioned prison, the Ohio State Reformatory, and 'Brooks was here' still makes people ugly-cry. The movie is literally about hope, and it's somehow earned.",
        "Frank Darabont",
        "The Shawshank Redemption (1994) — the rooftop scene and the ending",
        142,
        "Watch the opening — Andy in court, the prison gates, the first night — and notice how Darabont films the intake as a kind of baptism: the hosed-down, powdered men becoming 'inmates.' Then watch the rooftop beer scene, where Andy gets the crew cold beers and the guards 'forget' to notice: the film's argument — that hope is a discipline, not a feeling — is staged as a single impossible gesture, and the ending's rain is the release.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-heat-1995",
        "Heat (1995)",
        "The diner scene where De Niro and Pacino finally share a screen — the first time in their careers, despite both being in The Godfather Part II. Michael Mann recorded the bank robbery's gunfire live on a real street, and its audio is still the gold standard for movie shootouts. It's a 170-minute heist film about the one thing cops and robbers have in common: loneliness.",
        "Michael Mann",
        "Heat (1995) — the diner scene and the bank robbery",
        45,
        "Watch the diner scene — 'I don't know how to do anything else' — and notice how Mann stages the two great actors' first meeting as a negotiation between equals who recognize each other's cage: the whole film's theme is in the handshake. Then watch the bank robbery, where the real, live-recorded gunfire is the film's signature: Mann captured the shootout's silence-and-roar rhythm on the street, and every heist film since quotes it.",
        ["Crime", "Action", "1990s", "Hollywood"],
    ),
    _entry(
        "film-la-haine-1995",
        "La Haine (1995)",
        "Shot in three weeks in black and white on the streets of a Paris banlieue, after a real police beating killed a young man. Its opening joke — a man falls from a building and says 'so far, so good' — is the whole film: 24 hours in a place where everything is about to break. Vincent Cassel's breakout, and the most influential French film of the decade.",
        "Mathieu Kassovitz",
        "La Haine (1995) — the opening and the subway confrontation",
        98,
        "Watch the opening — the falling-man joke, the credits over a burning car — and notice how Kassovitz sets the film's clock: 'so far, so good' is the refrain, and everything before the ending is the fall. Then watch the subway confrontation, where the three friends' different ways of being powerless collide: the film's argument — that the state's violence creates the riot — lands in the final freeze-frame, which Kassovitz has said was the only ending he could make.",
        ["Drama", "1990s", "French"],
    ),
    _entry(
        "film-fight-club-1999",
        "Fight Club (1999)",
        "David Fincher hid Tyler Durden in single frames of the film — flashes you'd miss at 24fps — as a subliminal dare. The twist, the 'first rule,' and Project Mayhem became generational shorthand so powerful the film outlived its author's intent: the first rule is quoted as a lifestyle, not a warning. Chuck Palahniuk wrote the novel after being beaten up at work.",
        "David Fincher",
        "Fight Club (1999) — the opening and the single-frame cuts",
        139,
        "Watch the opening — the brain, the gun, the circling — and notice how Fincher's editing is the plot: the film runs on subliminal flashes and match cuts that plant the twist before you can name it. Then watch the single-frame cuts of Tyler spliced into the narrator's world — Fincher's confession that the world was always his — and the ending, where the story's rules finally collapse into the view from the 90th floor.",
        ["Thriller", "1990s", "Hollywood"],
    ),
    _entry(
        "film-memento-2000",
        "Memento (2000)",
        "The thriller told backwards — each scene ends where the next begins, so the audience loses its memory along with the hero. Nolan's brother Jonathan wrote the original story 'Memento Mori'; the DVD included a hidden chronological cut; and the whole film turns on a single tattoo: 'Remember Sammy Jankis.' It made Nolan's career.",
        "Christopher Nolan",
        "Memento (2000) — the first ten minutes and the Sammy Jankis scene",
        113,
        "Watch the first ten minutes, played in reverse — the Polaroid unsnapping, the bullet casing — and notice how Nolan makes you feel the disability: you know only what Leonard knows, one scene at a time. Then watch the Sammy Jankis scene, where the film's whole architecture — memory, guilt, self-deception — is revealed: the twist isn't who did it, it's who Leonard is, and the ending's confession is the film's thesis stated aloud.",
        ["Thriller", "2000s", "Hollywood"],
    ),
    _entry(
        "film-amores-perros-2000",
        "Amores Perros (2000)",
        "Mexico City, a car crash, and three stories about love and dogs — the film that launched director Alejandro González Iñárritu, writer Guillermo Arriaga, and Gael García Bernal in one shot. The title literally translates as 'Love's a Bitch,' the linking crash was inspired by a real Mexico City accident, and the opening dogfight made some audiences walk out.",
        "Alejandro González Iñárritu",
        "Amores Perros (2000) — the first story and the crash",
        60,
        "Watch the opening — the first story's dogfight, the ring, the money — and notice how Iñárritu's handheld camera makes you feel the fight's economics before a word is spoken: the dogs are the poor's lottery. Then watch the crash, the film's pivot, and the third story — El Chivo, the hitman, and the dogs he saves: the film's argument that love and violence share the same leash lands in its final, wordless image.",
        ["Drama", "2000s", "Mexican"],
    ),
    _entry(
        "film-the-lives-of-others-2006",
        "The Lives of Others (2006)",
        "East Germany, 1984: a Stasi officer bugs a playwright's apartment — and ends up protecting the lives he was sent to destroy. It won the Oscar for Best Foreign Language Film, and its ending's act of grace is based on a real Stasi file the director found after writing his version: the real HGW XX/7 did the same thing. The film is about the last free man in a surveillance state: the listener.",
        "Florian Henckel von Donnersmarck",
        "The Lives of Others (2006) — the first act and the ending",
        137,
        "Watch the first act — the bugging equipment, the apartment's first evening, the profile of Dreyman — and notice how the film makes surveillance the main character: the shots are framed through lenses and speakers, and Wiesler's face is the only place the state's machinery becomes human. Then watch the ending, where Dreyman discovers the file and the mystery of who saved him: the film's argument — that art can change the person who polices it — is delivered in a single, silent act of grace.",
        ["Thriller", "Drama", "2000s", "German"],
    ),
    _entry(
        "film-interstellar-2014",
        "Interstellar (2014)",
        "The black hole Gargantua was computed from real physics equations by Nobel laureate Kip Thorne — and the simulation was so accurate it produced an actual scientific paper. On the 'Mountains' planet, time dilation is literal: an hour there is seven years at home. Nolan shot in real locations and real IMAX, and one of the most reckless, beautiful docking sequences ever filmed.",
        "Christopher Nolan",
        "Interstellar (2014) — the docking sequence and the tesseract",
        45,
        "Watch the 'No Time for Caution' docking sequence — the spinning Endurance, the manual override, Hans Zimmer's organ — and notice how Nolan earns it: the film's physics (time dilation, gravity, the black hole's lensing) has been teaching you why this moment works. Then watch the tesseract, where Cooper falls through the bookshelf of time: the film's argument — that love is a force with its own physics — is staged as a father's reach through the fifth dimension.",
        ["Sci-Fi", "2010s", "Hollywood"],
    ),
    _entry(
        "film-la-la-land-2016",
        "La La Land (2016)",
        "The opening number was shot on a real closed Los Angeles freeway — a hundred-plus dancers, one continuous take, in a film made in just 42 days. It won six Oscars and tied the record for the most nominations ever (14, alongside All About Eve and Titanic), and its final 'what if' montage is the most devastating happy ending in modern musicals. Ryan Gosling's piano playing is actually him.",
        "Damien Chazelle",
        "La La Land (2016) — the freeway opening and the epilogue",
        128,
        "Watch the opening — 'Another Day of Sun,' the gridlocked freeway, the car doors — and notice how Chazelle films it in one long, moving take: the camera pulls through the traffic as the dancers take over, and the film declares itself a musical in three minutes. Then watch the epilogue, the 'what if' that never happened, playing out inside Sebastian's club: the film's argument — that love and ambition are a trade — is delivered in the final shot of Mia's face.",
        ["Musical", "Romance", "2010s", "Hollywood"],
    ),
    _entry(
        "film-the-handmaiden-2016",
        "The Handmaiden (2016)",
        "Sarah Waters' Victorian novel Fingersmith, transplanted to 1930s Japanese-occupied Korea and given two and a half plot twists — Park Chan-wook's most gorgeous film and his most devious. The con, the heiress, the house, and the rope: a love story that keeps turning its own machinery inside out, with some of the most beautiful cinematography of the decade.",
        "Park Chan-wook",
        "The Handmaiden (2016) — the first two acts",
        60,
        "Watch the first act — Sook-hee arriving at the manor, the library, the uncle's ceremonies — and notice how Park withholds the story's true shape: the film is three acts, and each rewrites the last. Then watch the second act's turn, where the handmaiden's con meets the heiress's own: the film's argument — that the system of men will be outmaneuvered by the women it underestimates — is delivered in a rooftop escape, a rope, and a kiss, and the ending's ship sails off on a perfect final image.",
        ["Romance", "Thriller", "2010s", "Korean"],
    ),
    _entry(
        "film-coco-2017",
        "Coco (2017)",
        "The 'Remember Me' twist is the film's heart: a lullaby disguised as a pop song, and the truth about who really wrote it. Pixar built the Land of the Dead from real Mexican artisans' work and spent years researching Día de los Muertos — the marigold bridge was their hardest technical challenge. It's the rare film that makes you cry twice: once for family, once for memory.",
        "Lee Unkrich",
        "Coco (2017) — the opening and the Remember Me scene",
        105,
        "Watch the opening — the papel picado, the ofrenda, the ban on music — and notice how the film plants its themes as objects: the torn family photo, the guitar, the name 'Mamá Coco.' Then watch the 'Remember Me' scene in the tower, where the song's true meaning is revealed: the film's argument — that memory is a form of love, and that forgetting is the only real death — is delivered in a lullaby, and the ending's 'I'm home' makes the whole audience the family.",
        ["Animation", "Family", "2010s", "Hollywood"],
    ),
    _entry(
        "film-lady-bird-2017",
        "Lady Bird (2017)",
        "Greta Gerwig's solo directorial debut, shot in her actual hometown of Sacramento, about a girl who insists on calling herself Lady Bird and the mother who can't stop loving her loudly. It held a 100% Rotten Tomatoes score off its first 196 reviews — a record at the time — and its ending voicemail is one of the most quietly devastating final scenes ever filmed.",
        "Greta Gerwig",
        "Lady Bird (2017) — the opening and the voicemail ending",
        94,
        "Watch the opening — 'Lady Bird' in the car, the name argument, the jump from the moving vehicle — and notice how Gerwig establishes the film's subject in two minutes: the war between a girl and her mother is a love story. Then watch the ending — the voicemail, the tears, the name: the film's argument — that growing up is learning to hear the person who raised you — lands in a single message, and the final shot of Christine walking into the city is the most honest coming-of-age image of the decade.",
        ["Drama", "Comedy", "2010s", "Hollywood"],
    ),
    _entry(
        "film-minari-2020",
        "Minari (2020)",
        "Semi-autobiographical: Lee Isaac Chung's own family moved to rural Arkansas in the 1980s to chase a farm dream, and the grandmother who arrives from Korea is based on his real one. Youn Yuh-jung's Oscar made her the first Korean actor ever to win an acting award — she thanked her sons for making her work. The title means watercress: the weed that grows anywhere, like a family.",
        "Lee Isaac Chung",
        "Minari (2020) — the first act and the ending",
        115,
        "Watch the first act — the move, the mobile home, the 'mountain water' well-digging — and notice how Chung films the farm as both promise and trap: the land is beautiful and poisonous, and the family's hope is in the planting. Then watch the grandmother's arrival — the hanbok, the wrestling show, the card games — and the ending's fire: the film's argument — that a family's worth isn't in what it grows but in how it tends itself — is delivered in the creek, the seeds, and the water they finally carry uphill.",
        ["Drama", "Family", "2020s", "Hollywood"],
    ),
    _entry(
        "film-aftersun-2022",
        "Aftersun (2022)",
        "Charlotte Wells' debut was built from her own home videos of a holiday with a father she lost too young. Paul Mescal's sunny, sad performance and the film's final 'Under Pressure' karaoke scene made it the most talked-about ending of its year. Watch it once as a holiday film. Watch it twice as a grief film. Both are correct.",
        "Charlotte Wells",
        "Aftersun (2022) — the first hour and the Under Pressure scene",
        102,
        "Watch the first hour as a memory — the pool, the sunburn cream, the camcorder — and notice how Wells shoots the holiday in textures: the MiniDV grain, the oversaturated sun, the moments the father disappears from the frame. Then watch the ending, the 'Under Pressure' dance and the strobe-lit nightclub: the film's argument — that a child can only understand a parent's darkness in retrospect — is delivered in that montage, and the final shot of Sophie looking back at the man who was her father is the most devastating image of the decade.",
        ["Drama", "2020s", "Hollywood"],
    ),
    _entry(
        "film-banshees-of-inisherin-2022",
        "The Banshees of Inisherin (2022)",
        "A friendship ends for no reason, on a fictional island off Ireland, in 1923 — and Colin Farrell and Brendan Gleeson (reunited from In Bruges) play it like a breakup. Martin McDonagh wrote it during lockdown, about the quiet civil wars inside friendships and countries. The donkey, the fingers, and the ending's one-word promise are pitch-black genius.",
        "Martin McDonagh",
        "The Banshees of Inisherin (2022) — the breakup and the ending",
        114,
        "Watch the first act — the pub, the 'we're done' announcement, the shattered routine — and notice how McDonagh stages the breakup like a country going to war: the island's civil war is on the mainland, and Colm and Pádraic's is on the shore. Then watch the ending — the house, the fire, the final exchange — where the film refuses to resolve: McDonagh's argument — that some separations are as pointless and total as war — is delivered in a one-word promise, and the last shot leaves the island exactly where it started.",
        ["Comedy", "Drama", "2020s", "Irish"],
    ),
]


def main() -> int:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    by_id = {t["id"]: t for t in data}
    by_name = {t["name"].lower(): t for t in data}

    missing_fields = []
    for t in NEW_TOPICS:
        if t["id"] in by_id:
            print(f"ERROR: id already exists: {t['id']}")
            return 1
        if t["name"].lower() in by_name:
            print(f"ERROR: name already exists: {t['name']}")
            return 1
        if len(t["teaser"]) > 450:
            missing_fields.append(f"teaser too long ({len(t['teaser'])}): {t['id']}")
        if len(t["exploreAction"]["instruction"]) > 450:
            missing_fields.append(
                f"instruction too long ({len(t['exploreAction']['instruction'])}): {t['id']}"
            )
        if len(t["name"]) > 80:
            missing_fields.append(f"name too long ({len(t['name'])}): {t['id']}")
    if missing_fields:
        for m in missing_fields:
            print(f"ERROR: {m}")
        return 1

    data.extend(NEW_TOPICS)
    PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"added {len(NEW_TOPICS)} entries → {len(data)} total")
    return 0


if __name__ == "__main__":
    sys.exit(main())
