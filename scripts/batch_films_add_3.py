#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — 1940s–1950s (noir, neorealism, golden age).

Third addition batch (v1.0 content pass toward 400 films): The Treasure of
the Sierra Madre, The Red Shoes, All About Eve, On the Waterfront, The
Searchers, High Noon, Paths of Glory, Ben-Hur, North by Northwest, and more
— including one famously terrible film (Plan 9 from Outer Space). Handcrafted
teaser + real fact + quality-bar instruction. Appends only; rejects
duplicate ids/names; caps 450 (SCHEMA.md).
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
        "film-the-treasure-of-the-sierra-madre-1948",
        "The Treasure of the Sierra Madre (1948)",
        "The gold-fever movie with the most quoted misquote in cinema — 'Badges? We don't need no stinkin' badges!' (the real line is even better). John Huston directed his own father, Walter, to a Best Supporting Actor Oscar, and the film's lesson — that the gold doesn't corrupt the men, it just reveals them — made it the definitive movie about greed.",
        "John Huston",
        "The Treasure of the Sierra Madre (1948) — the gold discovery and the ending",
        126,
        "Watch the discovery — the gold dust, the shared fever, the first cracks of suspicion — and notice how Huston films greed as a slow infection: the three partners change one scene at a time, and the mountain does nothing but sit there. Then watch the ending, where the gold is blown back into the hills by the wind: the film's argument — that the treasure was never worth the men it cost — is delivered in the most ironic final image in the western genre.",
        ["Adventure", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-red-shoes-1948",
        "The Red Shoes (1948)",
        "The film that made ballet cinematic — its 15-minute ballet sequence, shot with the real Sadler's Wells company, is the most influential dance footage ever filmed. Powell & Pressburger's fairy tale about a dancer forced to choose between love and art ends with one of cinema's great tragedies, and the film's Technicolor red shoes outshine everything in the frame.",
        "Michael Powell & Emeric Pressburger",
        "The Red Shoes (1948) — the ballet sequence",
        133,
        "Watch the 'Red Shoes' ballet — the newspaper dance, the transformation, the color bleeding through — and notice how Powell edits dream and reality together: the camera becomes the dancer's point of view, and the stage dissolves into the world. Then watch the ending, where the fairy tale's price is paid: the film's argument — that art demands everything and gives nothing back — is in the final shot, and the red shoes keep dancing after their owner is gone.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-white-heat-1949",
        "White Heat (1949)",
        "James Cagney's comeback as a mother-fixated gangster who lives for one thing — 'Top of the world, Ma!' The film ends with the most famous gangster death in cinema: Cody Jarrett, cornered on a chemical plant, shooting the tanks and grinning as the world explodes around him. The 'traitor in the gang' setup became the template for a century of crime films.",
        "Raoul Walsh",
        "White Heat (1949) — the ending explosion",
        114,
        "Watch the ending — Cody on the plant, the tanks, the grin — and notice how Walsh stages the death as an act of ownership: Jarrett doesn't get caught, he chooses the explosion, and 'Top of the world, Ma!' turns the genre's most violent death into a declaration. Then watch the earlier prison scenes, where Cody's headaches and his mother's visits establish the character's engine: the film's argument — that the criminal is the product of his childhood — is in every scene with Ma Jarrett.",
        ["Crime", "Classic", "Hollywood"],
    ),
    _entry(
        "film-kind-hearts-and-coronets-1949",
        "Kind Hearts and Coronets (1949)",
        "The blackest comedy in the Ealing canon — a disinherited duke's heir murders his way through the eight relatives ahead of him, all played by one actor, Alec Guinness. The film's genius is its tone: the murderer narrates with the calm of a memoirist, and the ending's twist — a jail cell, a noose, and a dropped memoir — is the perfect punchline.",
        "Robert Hamer",
        "Kind Hearts and Coronets (1949) — the eight d'Ascoynes and the ending",
        106,
        "Watch Alec Guinness play all eight d'Ascoynes — the banker, the general, the clergyman, the photographer — and notice how each is a different performance, not a gag: the film's comedy is in the murders' deadpan presentation, not the character work. Then watch the ending, where Louis, finally a duke, drops his memoir through the cell bars: the film's argument — that English society is a system of polite murder — is delivered with the most elegant black comedy ending ever filmed.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-all-about-eve-1950",
        "All About Eve (1950)",
        "The film with the most Oscar nominations in history (14, tied with Titanic and La La Land) — Bette Davis's comeback as an aging stage star, and Anne Baxter as the ingenue who's not what she seems. 'Fasten your seatbelts, it's going to be a bumpy night' was ad-libbed by Davis, and Marilyn Monroe appears in one scene as a starlet who can't sit still.",
        "Joseph L. Mankiewicz",
        "All About Eve (1950) — the award speech opening and the ending",
        138,
        "Watch the opening — the award ceremony, the speech, the flashback that contradicts it — and notice how Mankiewicz structures the film as a confession: every narrator is lying, and the audience is the last to know. Then watch the ending, where the film's final shot reveals the next Eve waiting in the wings: the film's argument — that ambition is a ladder with someone always climbing behind you — is delivered in that mirror, and the 'Margo and Eve' face-off scenes are the greatest two-hander in studio-era cinema.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-in-a-lonely-place-1950",
        "In a Lonely Place (1950)",
        "The most romantic noir ever made, and the most honest about its own darkness — Humphrey Bogart as a screenwriter suspected of murder who falls for the woman who alibis him, then destroys the relationship with his own violence. The film's ending, where the love story dies because the hero can't stop being who he is, is the genre's truest tragedy.",
        "Nicholas Ray",
        "In a Lonely Place (1950) — the 'I was born when she kissed me' scene and the ending",
        94,
        "Watch the 'I was born when she kissed me' speech — Dixon telling Laurel how she changed him, the tenderness that can't hold — and notice how Ray films the film's central contradiction: the man confesses his love in the same breath as his capacity for violence. Then watch the ending, where the phone call confirms his innocence and the relationship is already over: the film's argument — that love can't survive the suspicion it was built on — is delivered in the final close-up, the most heartbreaking conclusion in noir.",
        ["Noir", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-asphalt-jungle-1950",
        "The Asphalt Jungle (1950)",
        "The film that invented the heist movie — a professor's 'perfect crime' that comes apart because people are people. John Huston shot the burglary in documentary detail, and the film's rule — that every heist fails because of one human flaw — became the genre's law. Marilyn Monroe appears in a small role that made audiences notice her.",
        "John Huston",
        "The Asphalt Jungle (1950) — the heist sequence",
        112,
        "Watch the heist sequence — the safecracker, the doctor, the lookouts — and notice how Huston builds the film as a documentary of a crime: the planning scenes are as tense as the robbery itself, and the clock is the villain. Then watch the ending, where the wounded Dix wanders toward the horses he loves: the film's argument — that every criminal is chasing something that isn't money — is in that final walk, and 'the asphalt jungle' became the name for the city itself.",
        ["Crime", "Classic", "Hollywood"],
    ),
    _entry(
        "film-strangers-on-a-train-1951",
        "Strangers on a Train (1951)",
        "The film where Hitchcock refined his whole method — a tennis star meets a psychopath who proposes the perfect 'criss-cross' murder: you kill mine, I'll kill yours. The film's cross-cutting (tennis match ↔ murder in progress) is the most imitated sequence in suspense cinema, and the merry-go-round finale literally spins out of control.",
        "Alfred Hitchcock",
        "Strangers on a Train (1951) — the tennis cross-cut and the finale",
        101,
        "Watch the tennis match sequence — Guy's head swiveling between the game and the murder across town — and notice how Hitchcock edits the two events into one heartbeat: every point scored is a step closer to disaster. Then watch the ending on the runaway carousel, where the film's violence becomes mechanical: the film's argument — that we are all Bruno waiting for someone to say yes — is in Robert Walker's performance, the most charming monster Hitchcock ever created.",
        ["Thriller", "Classic", "Hollywood"],
    ),
    _entry(
        "film-a-streetcar-named-desire-1951",
        "A Streetcar Named Desire (1951)",
        "The film that announced Marlon Brando — his 'STELLA!' and his torn T-shirt changed American acting forever. Vivien Leigh's Blanche, the fading Southern belle lying about her age and her past, won the Oscar, and the film's shadows and music (the 'blue piano') turned Tennessee Williams' play into the most atmospheric film of its decade.",
        "Elia Kazan",
        "A Streetcar Named Desire (1951) — the Stanley and Stella scenes",
        122,
        "Watch the 'STELLA!' scene — the stairway, the rain, the reunion — and notice how Brando's performance redefines movie acting: the naturalism is a shock even now, and the film's Method style changed Hollywood overnight. Then watch Blanche's final scenes, where her lies collapse one by one: the film's argument — that desire destroys the people who can't afford it — is delivered in the film's most famous line, 'Whoever you are, I have always depended on the kindness of strangers.'",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-african-queen-1951",
        "The African Queen (1951)",
        "Humphrey Bogart's only Oscar — for a film shot on real African rivers with real leeches, real mud, and real fevers. Katharine Hepburn's spinster and Bogart's gin-soaked boat captain fall in love while dodging a German gunboat in WWI. The film's unlikely romance became the template for every opposites-attract adventure since.",
        "John Huston",
        "The African Queen (1951) — the rapids sequence",
        105,
        "Watch the rapids sequence — the boat, the leeches, the 'I never dreamed that any mere physical experience could be so stimulating' — and notice how Huston films the two characters' romance as a battle with the river: the obstacles ARE the courtship. Then watch the ending, where the two prisoners-of-love face a German firing squad and manage to marry mid-sentence: the film's argument — that love is a partnership against the world — is delivered with the genre's most charming last-minute escape.",
        ["Adventure", "Classic", "Hollywood"],
    ),
    _entry(
        "film-high-noon-1952",
        "High Noon (1952)",
        "The western that runs in real time — 85 minutes on screen, 85 minutes in the story, with a clock ticking toward noon. Gary Cooper's marshal, abandoned by the town he protected, was widely read as an allegory for the blacklist era, and the film's refusal to make heroism easy was a direct challenge to the genre's myth of the lone cowboy.",
        "Fred Zinnemann",
        "High Noon (1952) — the waiting and the final shootout",
        85,
        "Watch the waiting — the marshal's walk through town, the people refusing to help, the clock — and notice how Zinnemann builds the film from silence: the ticking is the score, and every citizen's refusal is a small betrayal. Then watch the final shootout, where the marshal is saved by the one person who came back: the film's argument — that a town that won't defend itself deserves what it gets — is in that last shot of the marshal dropping his badge in the dust.",
        ["Western", "Classic", "Hollywood"],
    ),
    _entry(
        "film-umberto-d-1952",
        "Umberto D. (1952)",
        "The masterpiece of Italian neorealism — a retired civil servant with nothing left but his dog, his dignity, and one month's rent. Vittorio De Sica filmed a real pensioner, and the film's most famous scene — the maid's hands on the kitchen counter — is cinema's purest portrait of poverty. The ending, where the old man almost kills his dog rather than let it starve, is unbearable.",
        "Vittorio De Sica",
        "Umberto D. (1952) — the maid's hands and the ending",
        89,
        "Watch the kitchen sequence — the maid Maria, the coffee, the ants — and notice how De Sica films poverty without plot: the scene is just a morning in a cheap room, and the camera's patience makes it devastating. Then watch the ending, where Umberto walks with his dog toward the train tracks and turns back: the film's argument — that dignity is the last thing poverty can take — is in that final walk, and the film remains the highest achievement of the neorealist movement it ended.",
        ["Drama", "Classic", "Italian"],
    ),
    _entry(
        "film-the-quiet-man-1952",
        "The Quiet Man (1952)",
        "John Wayne and Maureen O'Hara in the most beautiful Irish film ever made — shot on location in Cong, County Galway, with the local village as cast. The film's centerpiece, a brawl that travels through town, across a pub, and into a stream, is the most famous fight in cinema. Wayne's boxer who refuses to fight is the film's sly argument about manhood.",
        "John Ford",
        "The Quiet Man (1952) — the fight through town",
        129,
        "Watch the fight — Sean and Will from the cottage through the town, the villagers following like a parade — and notice how Ford films the brawl as comedy: every bystander is a referee, and the violence is courtship. Then watch the ending, where Mary's dowry is settled and the film's real question — what does a man owe his pride? — is answered: the film's argument, that love is worth more than honor, is delivered with the genre's most Irish grin.",
        ["Romance", "Classic", "Hollywood"],
    ),
    _entry(
        "film-on-the-waterfront-1954",
        "On the Waterfront (1954)",
        "The film with the most quoted line in Oscar history — 'You don't understand! I coulda had class. I coulda been a contender.' Marlon Brando's dockworker against the mob, and the film won 8 Oscars including Best Picture. Elia Kazan made it as his defense of testifying against his Communist friends — the film is a confession disguised as a thriller.",
        "Elia Kazan",
        "On the Waterfront (1954) — the 'contender' scene and the ending",
        108,
        "Watch the 'contender' scene — Terry and Charley in the cab, the confession, the 'I coulda been somebody' — and notice how Brando makes the film's politics personal: the speech is about a brother, not a union, and the emotion is what survives the allegory. Then watch the ending, where Terry walks through the union goons to face the truth: the film's argument — that silence is complicity — is in that walk, and the dockworkers following him is the film's final statement on solidarity.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-dial-m-for-murder-1954",
        "Dial M for Murder (1954)",
        "Hitchcock's most airtight plot — a tennis player plans the perfect murder of his wife, and it goes wrong when the key ends up under the carpet. Grace Kelly's phone, the scissors, and the film's structure (the murder attempt happens at the 30-minute mark, and the rest is the unraveling) make it the purest puzzle box in the director's career.",
        "Alfred Hitchcock",
        "Dial M for Murder (1954) — the murder attempt and the key",
        105,
        "Watch the murder attempt — the phone call, the scarf, the scissors — and notice how Hitchcock films the film's centerpiece in a single take: the camera stays put, the geometry does the work, and the killing is both sudden and inevitable. Then watch the unraveling, where the inspector's cigarette and the key's journey undo the perfect crime: the film's argument — that chance is the only true murderer — is in that carpet, and the film's 3D staging makes every shot feel like a chessboard.",
        ["Thriller", "Classic", "Hollywood"],
    ),
    _entry(
        "film-sabrina-1954",
        "Sabrina (1954)",
        "The Cinderella story with the classiest triangle in Hollywood — a chauffeur's daughter (Audrey Hepburn) returns from Paris transformed, and the two Larrabee brothers fall for her: the businessman (Humphrey Bogart) and the playboy (William Holden). The film's 'champagne at the party' scene is the most elegant courting sequence in studio comedy.",
        "Billy Wilder",
        "Sabrina (1954) — the party scene and the ending",
        113,
        "Watch the party scene — Sabrina in white, the champagne, the 'she's a beatnik' confusion — and notice how Wilder stages the film's central reversal: the man who never noticed her sees her for the first time, and the camera tells you the moment it happens. Then watch the ending, where the wrong brother turns out to be the right one: the film's argument — that love is about who sees you, not who you've rehearsed for — is in the final scene, and the film's Paris fantasy is the most beautiful ever shot.",
        ["Romance", "Classic", "Hollywood"],
    ),
    _entry(
        "film-rebel-without-a-cause-1955",
        "Rebel Without a Cause (1955)",
        "The film that invented the teenager — James Dean's Jim Stark, the red jacket, the chickie run, and the planetarium. Dean died a month before it opened, and the film became his monument and the template for every youth film since. The 'chickie run' toward the cliff is the most famous car scene in cinema.",
        "Nicholas Ray",
        "Rebel Without a Cause (1955) — the chickie run and the planetarium",
        111,
        "Watch the chickie run — the two cars, the leather jackets, the cliff — and notice how Ray films the dare as a rite of passage: the boys are performing manhood for each other, and the camera knows they're children. Then watch the planetarium scene, where the stargazing lecture turns into a confession: the film's argument — that the adults have abandoned the young — is in that dome, and the ending's tragedy is the price the film pays for its honesty.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-ladykillers-1955",
        "The Ladykillers (1955)",
        "The last great Ealing comedy — five crooks rent a room from a sweet old lady and discover she's the only one who's not a fool. Alec Guinness' Professor, with his terrifying teeth, and the film's ending — the crooks eliminated by their own incompetence and the old lady's teapot — make it the darkest comedy of its era. The Coen brothers remade it; they couldn't touch it.",
        "Alexander Mackendrick",
        "The Ladykillers (1955) — the heist and the ending",
        91,
        "Watch the heist planning — the Professor's lectures, the cello case full of notes — and notice how Mackendrick plays the film's comedy at the edge of menace: Guinness' gentility is the joke, and the robbery is almost an afterthought. Then watch the ending, where the old lady's teapot dispatches the gang one by one: the film's argument — that innocence is the most powerful force in England — is in that teapot, and the final image of the statue's mouth sealing the truth is perfect.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-searchers-1956",
        "The Searchers (1956)",
        "The greatest western ever made — John Wayne's Ethan Edwards spends years hunting the Comanches who took his niece, and the film asks whether the hunter or the hunted is the real monster. John Ford's use of doorways as frames — the famous final shot, where Ethan walks away and the door closes on him — is the most analyzed image in American cinema.",
        "John Ford",
        "The Searchers (1956) — the ending doorway shot",
        119,
        "Watch the final shot — the family framed in the doorway, Ethan turning away, the door closing — and notice how Ford ends the film with exclusion: the hero who saved the girl is not welcome inside, and the film's racism is finally named. Then watch the opening, the same doorway framing the woman who will die: the film's argument — that obsession is a kind of wilderness — is in that symmetry, and the film's complexity made it the favorite of Scorsese, Spielberg, and Lucas.",
        ["Western", "Classic", "Hollywood"],
    ),
    _entry(
        "film-invasion-of-the-body-snatchers-1956",
        "Invasion of the Body Snatchers (1956)",
        "The Cold War paranoia film — a small town's residents are replaced by emotionless pod duplicates, and nobody can prove it. The film's ending was changed by the studio (a happy framing added), and the original — 'They're here already! You're next!' — was restored decades later. It's the definitive statement on conformity, made in the year of the Red Scare.",
        "Don Siegel",
        "Invasion of the Body Snatchers (1956) — the pod reveal",
        80,
        "Watch the pod reveal — the half-formed duplicate, the scream, the 'there's no emotion' — and notice how Siegel films the horror as a realization rather than an attack: the pods don't kill, they replace, and the town's calm is the terror. Then watch the ending, where the film's paranoia peaks at the freeway: the film's argument — that the biggest threat to individuality is the comfort of sameness — is in that final run, and the restored ending remains the scariest last shot of the decade.",
        ["Sci-Fi", "Classic", "Hollywood"],
    ),
    _entry(
        "film-wild-strawberries-1957",
        "Wild Strawberries (1957)",
        "The film that turned old age into art — an elderly professor driving to receive an honorary degree, haunted by dreams of his own death and the love he walked away from. Ingmar Bergman cast 77-year-old Victor Sjöström, the great silent director, and the film's dream of the coffin and the empty streets is the most famous in Bergman's career.",
        "Ingmar Bergman",
        "Wild Strawberries (1957) — the dream opening and the ending",
        91,
        "Watch the opening dream — the coffin, the clock without hands, the face — and notice how Bergman films mortality: the professor's own funeral is the film's first image, and the dream logic is flawless. Then watch the strawberry-picking flashback, where the summer of his youth unfolds: the film's argument — that we are haunted by the lives we didn't live — is in that meadow, and the ending, where the old man is finally reconciled with his family, is Bergman's gentlest conclusion.",
        ["Drama", "Classic", "Swedish"],
    ),
    _entry(
        "film-sweet-smell-of-success-1957",
        "Sweet Smell of Success (1957)",
        "The meanest film ever made in Hollywood — Burt Lancaster's columnist J.J. Hunsecker, who destroys people with a paragraph, and Tony Curtis' press agent who'll do anything to climb. The film's dialogue, written by Clifford Odets, is the sharpest ever put on screen: 'The cat's in the bag and the bag's in the river.'",
        "Alexander Mackendrick",
        "Sweet Smell of Success (1957) — the 'cat's in the bag' scene",
        96,
        "Watch the 'cat's in the bag and the bag's in the river' scene — Sidney's phone call, the deal, the despair — and notice how Mackendrick films the city's corruption as a night world: the jazz clubs, the neon, the cigarettes. Then watch J.J.'s scenes, where Lancaster's power is pure menace: the film's argument — that New York runs on favors and fear — is delivered in every line, and the film's ending, with Sidney destroyed and J.J. untouched, is the most cynical in Hollywood history.",
        ["Noir", "Classic", "Hollywood"],
    ),
    _entry(
        "film-paths-of-glory-1957",
        "Paths of Glory (1957)",
        "The first great anti-war film by a major director — three French soldiers executed for cowardice to cover a general's blunder. Kirk Douglas' colonel defends them, and the film's ending — a terrified German girl singing for a hall of dying men — is one of cinema's most devastating final scenes. The film was banned in France for 17 years.",
        "Stanley Kubrick",
        "Paths of Glory (1957) — the court-martial and the ending",
        88,
        "Watch the court-martial — the generals, the 'cowardice' verdict, the defense that can't be heard — and notice how Kubrick films the trial as theater: the verdict is written before it begins, and the officers' polish is the horror. Then watch the ending, where the German girl's song silences the execution detail's audience: the film's argument — that war is class murder — is delivered in that song, and the final close-up of the condemned man's tears is Kubrick's most human image.",
        ["War", "Classic", "Hollywood"],
    ),
    _entry(
        "film-plan-9-from-outer-space-1957",
        "Plan 9 from Outer Space (1957)",
        "The film crowned 'the worst ever made' — and beloved because of it. Ed Wood's aliens raise the dead to stop humanity from building a weapon that could destroy the universe (the bomb, naturally). Bela Lugosi died early in shooting, so his body double — a chiropractor who held a cape over his face — stands in for the rest. The flying saucers are paper plates on strings.",
        "Ed Wood",
        "Plan 9 from Outer Space (1957) — the opening and the graveyard",
        79,
        "Watch the opening — the narrator, the graves, the 'future events such as these will affect you in the future' — and notice how Wood's sincerity turns every mistake into charm: the wrong shadows, the swinging doors, the earnest horror. Then watch the saucer scenes, where the strings are visible and the plates wobble: the film's argument — that ambition doesn't need budget — is in every frame, and its fame as 'the worst movie ever' has made it the most rewatched cult film in history.",
        ["Sci-Fi", "Classic", "Hollywood"],
    ),
    _entry(
        "film-touch-of-evil-1958",
        "Touch of Evil (1958)",
        "The film with the greatest opening shot in cinema — a three-minute, 20-second crane shot following a car through a border town, with the bomb planted in the trunk. Orson Welles stars as the corrupt cop Quinlan, and the studio mangled his cut; the 1998 restoration followed his 58-page memo, and the film became the last great noir. Charlton Heston plays a Mexican — which was already a joke in 1958.",
        "Orson Welles",
        "Touch of Evil (1958) — the opening crane shot",
        111,
        "Watch the opening — the car, the border, the bomb, the three-minute unbroken crane shot — and notice how Welles announces the whole film in one movement: the camera glides over the town, the bomb ticks, and the explosion is the film's thesis. Then watch the ending, where Quinlan's frame-up unravels in a motel room: the film's argument — that the law is just another racket — is in the final recording, and the film's shadows (shot by Russell Metty) are the last great statement of noir style.",
        ["Noir", "Classic", "Hollywood"],
    ),
    _entry(
        "film-north-by-northwest-1959",
        "North by Northwest (1959)",
        "The film that invented the modern action movie — Cary Grant mistaken for a spy, chased across America by the most polite killers in cinema. The crop-duster attack and the Mount Rushmore finale are the most famous set pieces in Hitchcock's career, and the film's 'MacGuffin' — the microfilm nobody cares about — became the director's own favorite in-joke.",
        "Alfred Hitchcock",
        "North by Northwest (1959) — the crop-duster scene",
        136,
        "Watch the crop-duster scene — the empty road, the biplane, the cornfield — and notice how Hitchcock builds suspense from emptiness: the scene has no music, no dialogue, just the plane's engine and Grant's bewilderment, and it's the most studied action sequence ever staged. Then watch the Mount Rushmore finale, where the chase literally climbs the presidents' faces: the film's argument — that identity is a performance — is in the film's title itself, and the ending's last-second rescue is the wittiest in the director's career.",
        ["Thriller", "Classic", "Hollywood"],
    ),
    _entry(
        "film-anatomy-of-a-murder-1959",
        "Anatomy of a Murder (1959)",
        "The most honest courtroom drama ever made — James Stewart defending a man who killed his wife's rapist, with the word 'panties' in the opening scene, which shocked 1959. The film is based on a real Michigan case, Duke Ellington wrote and appears in the score, and the verdict is left genuinely ambiguous — a first for Hollywood.",
        "Otto Preminger",
        "Anatomy of a Murder (1959) — the courtroom scenes",
        160,
        "Watch the opening — the murder, the 'panties' line, the interrogation — and notice how Preminger films the law as theater: every witness is a performance, and the film's frankness about sex was a landmark in censorship history. Then watch the closing arguments, where Stewart's defense builds from small details: the film's argument — that justice is a contest of storytelling — is in that ambiguity, and the ending's unresolved verdict remains the film's boldest choice.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-rio-bravo-1959",
        "Rio Bravo (1959)",
        "The greatest hangout movie ever made — Howard Hawks' sheriff, a drunk, a kid, and a cripple hold a killer in a jail while the outlaw's gang surrounds the town. Hawks made it as a direct rebuke to High Noon: real men don't ask for help. The ending, where the drunk gets his gun and the cripple's dynamite wins the day, is pure Hawks.",
        "Howard Hawks",
        "Rio Bravo (1959) — the ending standoff",
        141,
        "Watch the film's rhythm — the jail, the poker game, the singing of 'My Rifle, My Pony and Me' — and notice how Hawks builds character through hanging out: the plot barely moves, and the friendship is the plot. Then watch the ending, where the four men work as one machine: the film's argument — that a team of flawed men beats an army of professionals — is in that standoff, and Dean Martin's Dude, redeemed by the fight, gives the film its heart.",
        ["Western", "Classic", "Hollywood"],
    ),
    _entry(
        "film-ben-hur-1959",
        "Ben-Hur (1959)",
        "The film that won a record 11 Oscars — a record that stood for 38 years — and the chariot race remains the most spectacular action sequence ever filmed: 40,000 extras, months of construction, and a real race with real injuries. The sea battle and the crucifixion cost more than most films of the era, and William Wyler's epic became the measuring stick for Hollywood ambition.",
        "William Wyler",
        "Ben-Hur (1959) — the chariot race",
        120,
        "Watch the chariot race — the nine chariots, the whip, the wreck — and notice how the sequence was shot for real: no CGI, actual stuntmen on actual horses, and the crash (Messala's chariot) was an accident they kept. The race runs nine minutes and the audience forgets to breathe. Then watch the film's quieter engine — the friendship of Ben-Hur and Messala destroyed by empire: the film's argument, that vengeance and mercy are the two roads, is delivered in the ending's miracle.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-hidden-fortress-1958",
        "The Hidden Fortress (1958)",
        "The film that inspired Star Wars — George Lucas has admitted the princess-escaped-from-the-fortress plot and the two bickering peasants came straight from Kurosawa. Toshiro Mifune's general and the film's sweeping widescreen battles made it Japan's biggest hit of the year, and the peasants' greed is the film's secret weapon.",
        "Akira Kurosawa",
        "The Hidden Fortress (1958) — the gold chase and the ending",
        139,
        "Watch the gold chase — the peasants hauling the treasure, the general's plan, the princess in disguise — and notice how Kurosawa films the escape as a comedy of greed: the two peasants' scheming IS the plot engine, and the princess's dignity is the counterweight. Then watch the ending, where the fortune is won and thrown away: the film's argument — that honor beats gold — is in the final image, and the film's widescreen framing (its first for Kurosawa) made it the template for the modern epic.",
        ["Adventure", "Classic", "Japanese"],
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
