#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — 2020s (modern rebalance).

Eleventh addition batch (modern rebalance — brings films.json to 460 total):
Promising Young Woman, Sound of Metal, Nomadland, The Father, Judas and the
Black Messiah, CODA, West Side Story, The Worst Person in the World, Licorice
Pizza, The Batman, Top Gun: Maverick, RRR, Triangle of Sadness, The Whale,
Decision to Leave, The Menu, All Quiet on the Western Front, Marcel the Shell
with Shoes On, John Wick: Chapter 4, Spider-Man: Across the Spider-Verse, The
Boy and the Heron, Godzilla Minus One, May December, Air, Dune: Part Two,
Challengers, Anora, The Brutalist, Conclave, The Substance. Handcrafted
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
        "film-promising-young-woman-2020",
        "Promising Young Woman (2020)",
        "A revenge thriller wrapped in bubblegum pink — Carey Mulligan's Cassie, a med-school dropout, pretends to be drunk in bars to expose the men who take advantage of women. Emerald Fennell's debut won the Oscar for Best Original Screenplay, and the film's candy-colored visuals hide a plot that keeps re-inventing itself — the ending is a gut-punch that re-frames the whole movie. The 'It's not a joke' scene is the decade's most uncomfortable confrontation.",
        "Emerald Fennell",
        "Promising Young Woman (2020) — the ending",
        113,
        "Watch the film's first act — the bar routine, the 'nice guy' monologue, the reveal of Cassie's ledger — and notice how Fennell uses genre as camouflage: the film looks like a glossy comedy and keeps turning into a thriller, and every 'nice guy' Cassie meets is the same guy in a different shirt. Then watch the ending, where the plan's final turn is revealed: the film's argument — that the justice system lets predators walk, and that Cassie's revenge is the system's failure made personal — is in that finale, and the film's final scene re-colors everything you just watched.",
        ["Thriller", "Drama", "2020s", "Hollywood"],
    ),
    _entry(
        "film-sound-of-metal-2020",
        "Sound of Metal (2020)",
        "The film that lets you hear deafness — Riz Ahmed's drummer Ruben loses his hearing mid-tour, and the film's sound design does the impossible: it makes you experience his loss from the inside. Ahmed learned American Sign Language and drumming for the role, and the film won 2 Oscars, including Best Sound — the first time a film's sound was honored for what it takes away, not what it adds. The film's final scene — the silence he chooses — is its masterpiece.",
        "Darius Marder",
        "Sound of Metal (2020) — the hearing-loss sequence and the ending",
        120,
        "Watch the first act — the tour, the ringing, the sudden muffling — and notice how the sound design makes the film's subject physical: the audio literally degrades as Ruben's hearing does, and the silence at the edges of every scene is the film's point of view. Then watch the ending, where Ruben sits in the quiet he once feared: the film's argument — that accepting what you've lost is not giving up, it's a kind of freedom — is in that final scene, and the film's use of real ASL and a real deaf community (many cast members are deaf) made it the most authentic film about disability of its era.",
        ["Drama", "Music", "2020s", "Hollywood"],
    ),
    _entry(
        "film-nomadland-2020",
        "Nomadland (2020)",
        "The Best Picture winner that cast real van-dwellers as themselves — Frances McDormand's Fern, a woman who loses everything in the 2008 crash and takes to the road in a van, joining America's invisible community of nomads. Chloé Zhao became only the second woman — and the first woman of color — to win Best Director, and the film's unscripted scenes with real nomads (including the legendary Swankie) give it a documentary's truth with a poem's shape. The final shot is one of cinema's great goodbyes.",
        "Chloé Zhao",
        "Nomadland (2020) — the ending",
        107,
        "Watch the film's middle — the Amazon warehouse, the beet harvest, the desert gatherings — and notice how Zhao films labor with respect: the nomads' work is shown in full, unglamorized, and the film's wide desert shots (by Joshua James Richards) make each person tiny against the land they've chosen. Then watch the ending, where Fern's final choice at Swankie's cliff resolves: the film's argument — that home is a way of being, not a place — is in that finale, and the film's quiet, un-rushed goodbye made it the most contemplative Best Picture winner in decades.",
        ["Drama", "2020s", "Hollywood"],
    ),
    _entry(
        "film-the-father-2020",
        "The Father (2020)",
        "The dementia movie that puts you inside the confusion — Anthony Hopkins (who, at 83, became the oldest Best Actor winner ever) plays a man whose apartment keeps changing around him: different faces, different rooms, different truths. Florian Zeller adapted his own play, and the film's genius is structural: you experience the disorientation as it happens, so the film's final scene — the moment the character realizes what he's losing — lands like a physical blow.",
        "Florian Zeller",
        "The Father (2020) — the ending",
        97,
        "Watch the film's first ten minutes — the daughter's visit, the apartment that shifts — and notice how the film establishes its rules: there is no reliable narrator, and the editing (same scene, different cast) makes you feel the confusion rather than observe it. Then watch the ending, where the film's real setting is finally revealed and Hopkins' breakdown ('I feel as if I'm losing all my leaves') resolves: the film's argument — that memory is the self, and that losing it is a kind of death we inflict on the people who love us — is in that finale, and the film's use of the same apartment as both comfort and trap is the decade's most elegant metaphor.",
        ["Drama", "2020s", "Hollywood"],
    ),
    _entry(
        "film-judas-and-the-black-messiah-2021",
        "Judas and the Black Messiah (2021)",
        "The true story of the FBI's war on the Black Panthers — Daniel Kaluuya (who won Best Supporting Actor) plays Fred Hampton, the charismatic 21-year-old chairman of the Illinois chapter, and Lakeith Stanfield the informant the FBI planted beside him. Shaka King's film is a thriller that becomes a tragedy you already know the ending to, and its central tragedy — the man who brought the rival gangs together, taken down from the inside — is American history at its most bitter.",
        "Shaka King",
        "Judas and the Black Messiah (2021) — the breakfast program and the ending",
        126,
        "Watch Hampton's organizing scenes — the coalition meeting, the 'I am a revolutionary' speech, the breakfast program feeding children — and notice how the film shows why the FBI feared him: the breakfast program (feeding thousands of kids) was real, and the film's argument is that the man was killed for building power, not for violence. Then watch the ending, where the informant's testimony and the raid resolve: the film's argument — that the state destroys its own, and that the informant's betrayal was the system's tool — is in that finale, and the film's archival ending footage of the real Hampton makes the tragedy land twice.",
        ["Drama", "Crime", "History", "2020s", "Hollywood"],
    ),
    _entry(
        "film-coda-2021",
        "CODA (2021)",
        "The first film from a streaming service to win Best Picture — a hearing teenage girl, Ruby, is the only hearing member of a deaf family, torn between their fishing business and her singing dream. Troy Kotsur became the first deaf man to win an acting Oscar (for Best Supporting Actor), and the film's signature scene — Ruby singing while her family watches, unable to hear, reading the room's reactions — is the decade's most moving image of love. The 'both' scene at the audition is perfection.",
        "Sian Heder",
        "CODA (2021) — the audition scene and the ending",
        111,
        "Watch the audition scene — Ruby singing 'Both Sides Now' while her family watches in silence — and notice how the film makes deafness a point of view: the sound cuts out, the camera watches the family watching, and the scene becomes about what love looks like when it can't hear you. Then watch the ending, where Ruby's choice between family and future resolves: the film's argument — that the deaf family and the hearing daughter are each other's first language — is in that finale, and the film's Oscar sweep proved that a small, warm, crowd-pleasing movie could still conquer Hollywood.",
        ["Drama", "Music", "2020s", "Hollywood"],
    ),
    _entry(
        "film-west-side-story-2021",
        "West Side Story (2021)",
        "Spielberg's first musical — and he'd been waiting 50 years to make it. His remake of the 1957 classic (Romeo and Juliet in 1950s New York, Jets vs. Sharks) is the rare redo that justifies itself: the dancing is bigger, the racism is sharper, and Ariana DeBose (who won Best Supporting Actress — the first openly queer woman of color to win an acting Oscar) makes Anita's 'A Boy Like That / I Have a Love' the film's soul. Rita Moreno, from the original, returns in a new role.",
        "Steven Spielberg",
        "West Side Story (2021) — the 'America' number and the ending",
        156,
        "Watch the 'America' number — the streets, the choreography, the argument set to music — and notice how Spielberg and choreographer Justin Peck make the dance carry the politics: the number is a debate about Puerto Rico and the American dream, and the camera moves through it like it was born there. Then watch the ending, where the tragedy's final turn lands: the film's argument — that the kids inherit the adults' hate and pay for it — is in that finale, and the film's casting of real Latinx actors and its use of Spanish dialogue made it the definitive version.",
        ["Musical", "Romance", "Drama", "2020s", "Hollywood"],
    ),
    _entry(
        "film-the-worst-person-in-the-world-2021",
        "The Worst Person in the World (2021)",
        "A romantic comedy about the fear of committing to a romantic comedy — Renate Reinsve (who won Best Actress at Cannes) plays Julie, drifting through her late twenties between two men, two careers, and a thousand what-ifs. Joachim Trier's film is structured in chapters with a narrator, and its centerpiece — a sequence where the whole world freezes so Julie can run to the man she wants — is the most romantic scene of the decade. Nominated for 2 Oscars, including Best International Feature.",
        "Joachim Trier",
        "The Worst Person in the World (2021) — the frozen-city scene and the ending",
        128,
        "Watch the frozen-city scene — the world stopping, Julie running through the paused streets to Aksel — and notice how Trier earns the fantasy: the film's earlier realism makes the magic feel like a wish the character is allowed, and the scene's quiet ending (she gets there, and then what?) is the film's honesty. Then watch the ending, where the chapters resolve and Julie's choice is finally made: the film's argument — that being 'the worst person in the world' is just being human, and that not knowing is the condition — is in that finale, and the film's structure (with its narrator's goodbye) made it the decade's most intelligent romantic comedy.",
        ["Romance", "Comedy", "Drama", "2020s", "Norwegian"],
    ),
    _entry(
        "film-licorice-pizza-2021",
        "Licorice Pizza (2021)",
        "Paul Thomas Anderson's sunlit hangout movie — 1970s San Fernando Valley, where 15-year-old Gary (Cooper Hoffman, son of the late Philip Seymour Hoffman) runs a waterbed business and chases 25-year-old Alana (Alana Haim, in her debut). The film is less a plot than a place: the pinball arcade, the restaurant, the truck rolling backwards down the hill. Its best scene — a truck running out of gas, rolling backward through traffic — is pure comic filmmaking, and the film's title comes from a record store chain.",
        "Paul Thomas Anderson",
        "Licorice Pizza (2021) — the truck scene and the ending",
        133,
        "Watch the truck scene — the tank empty, the truck rolling backward down the hill, Gary steering from outside — and notice how PTA stages the decade's funniest set piece with almost no dialogue: the comedy is pure physics and timing, and the scene's escalation (the truck, the bus, the hill) is a masterclass in comic rhythm. Then watch the ending, where Gary and Alana's running resolve: the film's argument — that youth is a place you visit with the wrong person and leave with the right one — is in that finale, and the film's grainy 70s look (shot on film with period lenses) made it the decade's warmest time machine.",
        ["Comedy", "Drama", "Romance", "2020s", "Hollywood"],
    ),
    _entry(
        "film-the-batman-2022",
        "The Batman (2022)",
        "The detective version — Matt Reeves' 176-minute noir drops the origin story and gives Batman (Robert Pattinson) a real mystery: a serial killer (Paul Dano's Riddler) who's targeting Gotham's corrupt elite and leaving riddles for the Bat. The film's rain-soaked Gotham, its Nirvana-scored opening, and its centerpiece — the Penguin (Colin Farrell, unrecognizable) car chase — made it the moodiest and most visually striking Batman yet. Its final act reveals the city's biggest conspiracy: the flood, and what it washes away.",
        "Matt Reeves",
        "The Batman (2022) — the car chase and the ending",
        176,
        "Watch the Penguin chase — the tunnels, the flames, the Batmobile's reveal — and notice how Reeves shoots action as weather: the rain is the constant, the chase is lit by fire and headlights, and the film's Gotham feels like a city that's been drowning for years. Then watch the ending, where the flood and the city's choice resolve: the film's argument — that Gotham's corruption is systemic, and that Batman's real war is against the rot, not the criminals — is in that finale, and the film's 'I'm vengeance' thesis (turned, by the end, into hope) made it the most thoughtful superhero film of its era.",
        ["Action", "Crime", "Mystery", "2020s", "Hollywood"],
    ),
    _entry(
        "film-top-gun-maverick-2022",
        "Top Gun: Maverick (2022)",
        "The sequel that beat the original in every way — Tom Cruise refused to make it unless the actors actually flew the F/A-18s, so the cast trained for three years and shot real aerial footage in real jets, with cameras mounted in the cockpits. The result — $1.49 billion, Cruise's biggest hit ever, and the film that dragged audiences back to theaters after COVID — is the most visceral action film of the decade. The final mission, and the 'talk to me, Goose' callback, will have you in tears.",
        "Joseph Kosinski",
        "Top Gun: Maverick (2022) — the final mission",
        130,
        "Watch the aerial sequences — the canyon run, the dogfight, the close calls — and notice how the film's real flying makes it unbeatable: no greenscreen, actual G-forces (the actors vomited on set), and the sound design (the engines, the alarms) puts you in the cockpit. Then watch the final mission, where the impossible targeting run resolves: the film's argument — that the old ways (the mission, the man) still matter, and that some debts are paid by flying — is in that finale, and the film's callback to Goose's death made it the rare blockbuster that earns both its spectacle and its tears.",
        ["Action", "Drama", "2020s", "Hollywood"],
    ),
    _entry(
        "film-rrr-2022",
        "RRR (2022)",
        "The Indian epic that conquered the world — S.S. Rajamouli's three-hour historical fantasy about two real revolutionaries (fictionalized into best friends) taking on the British Raj with impossible, glorious violence. The film's set pieces — the 'Naatu Naatu' dance-off (which won the Oscar for Best Original Song, the first Indian film to ever win an Academy Award), the tiger fight, the flaming-wheel rescue — are the most joyful action filmmaking of the decade. It became India's third highest-grossing film ever.",
        "S.S. Rajamouli",
        "RRR (2022) — the 'Naatu Naatu' sequence and the ending",
        187,
        "Watch the 'Naatu Naatu' sequence — the dance-off at the governor's party, the two heroes out-dancing a hall of colonizers — and notice how the film's politics live in its spectacle: the dance is a rebellion, and the choreography (which took 6 months to prepare) is the film's argument that joy is itself an act of defiance. Then watch the ending, where the two friends' war against the Raj resolves: the film's argument — that freedom is earned through friendship, sacrifice, and absolutely impossible stunts — is in that finale, and the film's mix of history, myth, and maximalism made it the decade's most thrilling night at the movies.",
        ["Action", "History", "2020s", "Indian"],
    ),
    _entry(
        "film-triangle-of-sadness-2022",
        "Triangle of Sadness (2022)",
        "The cruise-ship satire that won the Palme d'Or — a supermodel couple (Harris Dickinson, Charlbi Dean) win a luxury yacht trip with the 1%, until the yacht sinks and the survivors wash up on an island where the hierarchy inverts: the only person who can fish is a toilet-cleaning crew member. Ruben Östlund's second Palme d'Or winner (after The Square) contains the decade's most talked-about scene — the seasick dinner — and its ending, with the island's final choice, is a thesis about power that keeps cutting deeper.",
        "Ruben Östlund",
        "Triangle of Sadness (2022) — the dinner scene and the ending",
        147,
        "Watch the dinner scene — the storm, the seasickness, the social order dissolving into chaos — and notice how Östlund stages the film's funniest and most grotesque sequence as a class allegory: the rich are helpless, the crew is practical, and the film's comedy is always also an argument. Then watch the ending, where Abigail's power play and the final choice resolve: the film's argument — that power is just whoever can provide, and that the 'civilized' were never in charge — is in that finale, and the film's ambiguous last scene (the rock, the silence) made it the decade's most argued-about ending.",
        ["Comedy", "Drama", "2020s", "Swedish"],
    ),
    _entry(
        "film-the-whale-2022",
        "The Whale (2022)",
        "The comeback of the decade — Brendan Fraser (who won Best Actor, after years away from Hollywood) plays Charlie, a 600-pound online writing teacher trying to reconnect with his estranged daughter in the five days he has left. Darren Aronofsky shot the film in a single apartment in a 4:3 frame (the shape of a human body), and Fraser wore prosthetics weighing up to 300 pounds. The film's final scene — 'Do you have any idea how proud I am of you?' — is devastating.",
        "Darren Aronofsky",
        "The Whale (2022) — the ending",
        117,
        "Watch the film's visual language — the 4:3 frame, the apartment's confines, the camera rarely leaving Charlie's space — and notice how the aspect ratio and the setting make you feel Charlie's imprisonment: the film's tight frame is his body, and every character who enters brings the world he can't reach. Then watch the ending, where Charlie's final effort and his daughter's arrival resolve: the film's argument — that the body is not the self, and that being seen is the one thing we all need — is in that finale, and Fraser's performance (and his Oscar speech) made the film the decade's great acting showcase.",
        ["Drama", "2020s", "Hollywood"],
    ),
    _entry(
        "film-decision-to-leave-2022",
        "Decision to Leave (2022)",
        "Park Chan-wook's detective story that's secretly a love story — a sleepless Busan detective (Park Hae-il) investigating a man's fall from a mountain becomes obsessed with the dead man's wife (Tang Wei), and the film becomes a puzzle about who is investigating whom. It won Park the Best Director prize at Cannes, and the film's second half — the seaside town, the phone calls, the final walk — is the decade's most elegant study of obsession. The ending is a twist that rewards a rewatch immediately.",
        "Park Chan-wook",
        "Decision to Leave (2022) — the ending",
        138,
        "Watch the film's editing — the match cuts between the detective's surveillance and the wife's daily life, the phone that connects them across time — and notice how Park films attraction as a form of detection: every shot of her is a clue he's collecting, and the film's visual wit (the phone screen as a mirror, the fog as a mood) makes the obsession tactile. Then watch the ending, where the seaside town's final scene resolves: the film's argument — that love and suspicion are the same attention, and that some decisions are final — is in that finale, and the film's last shot re-frames everything you've seen, making it the decade's most rewatchable mystery.",
        ["Mystery", "Romance", "Crime", "2020s", "Korean"],
    ),
    _entry(
        "film-the-menu-2022",
        "The Menu (2022)",
        "A horror-comedy about the people who decide what we eat — Ralph Fiennes' Chef Slowik runs a 12-seat restaurant on a private island, and his tasting menu for a table of foodie elites has one course the guests weren't expecting: them. Anya Taylor-Joy's Margot is the only guest who refuses to perform, and the film's thesis lands in the final course — the cheeseburger, and what it says about who food is really for. The 's'mores' reveal is the decade's most delicious dark joke.",
        "Mark Mylod",
        "The Menu (2022) — the final course and the ending",
        106,
        "Watch the film's escalating courses — the bread course with its perfect backstory, the 'memory' dish, the guests' complicity — and notice how the film's satire is structural: every course is a judgment on the guest who receives it, and the film's horror comes from the guests' inability to stop performing even as they're being killed. Then watch the ending, where Margot's request ('Can I have a cheeseburger?') resolves: the film's argument — that the fine-dining world serves status, not food, and that the one authentic thing on the island is a burger — is in that finale, and the film's final smile is the decade's most satisfying punchline.",
        ["Horror", "Comedy", "Thriller", "2020s", "Hollywood"],
    ),
    _entry(
        "film-all-quiet-on-the-western-front-2022",
        "All Quiet on the Western Front (2022)",
        "The German answer to war films — Netflix's adaptation of Erich Maria Remarque's 1929 novel follows a teenage soldier (Felix Kammerer) from eager enlistment to the trenches of WWI, told entirely from the German side, which makes its horror feel freshly earned. It won 4 Oscars, including Best International Feature, and its centerpiece — the final French counterattack, the mud, the hand-to-hand — is the most brutal war sequence of the decade. The stolen boots motif is the film's thesis made object.",
        "Edward Berger",
        "All Quiet on the Western Front (2022) — the final battle and the ending",
        148,
        "Watch the film's central image — the stolen boots, passed from dead soldier to dead soldier — and notice how Berger builds the film's argument from a single object: the war grinds through people, and the boots outlast them all, and the film's muddy, grey palette (shot with almost no music) makes the horror procedural. Then watch the ending, where the final offensive and the young soldier's last moments resolve: the film's argument — that the old men's war is paid for in boys, and that the peace is only a pause — is in that finale, and the film's closing irony (the armistice signed minutes after the deaths) is the decade's most devastating final note.",
        ["War", "Drama", "2020s", "German"],
    ),
    _entry(
        "film-marcel-the-shell-with-shoes-on-2022",
        "Marcel the Shell with Shoes On (2022)",
        "The most tender film of the decade, and it's about a one-inch-tall shell with one googly eye and tiny shoes — Marcel (voiced by Jenny Slate, in a feature spun off from the viral shorts she created with director Dean Fleischer Camp) lives in an Airbnb and narrates his tiny life: the tennis ball, the lint, the search for his family. The film's secret is that it's really about grief and connection, and its stop-motion Marcel interacting with the real world (a nana who gardens, a documentary crew) made it an Oscar nominee for Best Animated Feature. The final scene will wreck you.",
        "Dean Fleischer Camp",
        "Marcel the Shell with Shoes On (2022) — the ending",
        90,
        "Watch the film's blend of scales — Marcel tiny against real kitchens, the camera peering at him like he's a national treasure — and notice how the film's documentary framing is the joke and the heart: everyone who meets Marcel falls for him instantly, and the film's quiet humor (the '60 Minutes' satire, the group chat) makes room for its real subject. Then watch the ending, where Marcel's search for his family resolves: the film's argument — that the smallest lives contain the whole of love, and that community is built one tiny kindness at a time — is in that finale, and the film's final goodbye made it the decade's most moving animated film.",
        ["Animation", "Comedy", "Family", "2020s", "Hollywood"],
    ),
    _entry(
        "film-john-wick-chapter-4-2023",
        "John Wick: Chapter 4 (2023)",
        "The action film that raised the bar to unreachable heights — 169 minutes of the most precise, balletic, jaw-dropping fight choreography ever filmed, ending the saga with a 222-step stairway fight, an overhead long take, and a duel at sunrise. Keanu Reeves trained for months in jiu-jitsu, judo, and tactical shooting, and the film's 22-minute Paris sequence alone would be most action movies' climax. It became the franchise's biggest hit, at $440 million — and its ending gave the series the goodbye it deserved.",
        "Chad Stahelski",
        "John Wick: Chapter 4 (2023) — the Arc de Triomphe sequence and the ending",
        169,
        "Watch the Arc de Triomphe sequence — the roundabout, the traffic, the fight weaving between cars — and notice how the film stages action like a musical: the choreography is set to the city's rhythm, the camera moves with the fighters, and every weapon (the nunchucks, the knives, the car) is an instrument. Then watch the ending, where the duel at sunrise and John's final choice resolve: the film's argument — that even the legend can choose peace, and that the debt is finally paid — is in that finale, and the film's reverence for its own genre (with a mid-credits tease) made it the definitive action film of its era.",
        ["Action", "Crime", "2020s", "Hollywood"],
    ),
    _entry(
        "film-spiderman-across-the-spider-verse-2023",
        "Spider-Man: Across the Spider-Verse (2023)",
        "The sequel that outdid the masterpiece — Miles Morales returns, and the film's multiverse of Spider-People (hundreds of them, each in their own animation style) is the most audacious visual experiment in mainstream animation history. The film's first half is a buddy movie, its second half a tragedy about fate, and its cliffhanger ending made audiences scream in theaters. It won the Oscar for Best Animated Feature, and its 'leap of faith' follow-up — Miles swinging through the wrong universe — is animation's greatest action sequence.",
        "Joaquim Dos Santos, Kemp Powers & Justin K. Thompson",
        "Spider-Man: Across the Spider-Verse (2023) — the chase sequence and the ending",
        140,
        "Watch the chase through the Spider-Society — hundreds of Spider-People, each in their own style, Miles dodging through them — and notice how the film makes its visual language its plot: the different universes are different animation schools colliding, and the chase's changing styles (Indian Spider-Man's watercolor, the Spider-Punk's collages) are the film's argument that no single story is the only one. Then watch the ending, where the cliffhanger and Miles' choice resolve: the film's argument — that the canon is not fate, and that the hero writes their own story — is in that finale, and the film's audacity (a $100M+ blockbuster ending on a cliffhanger) made it the decade's boldest studio film.",
        ["Animation", "Action", "2020s", "Hollywood"],
    ),
    _entry(
        "film-the-boy-and-the-heron-2023",
        "The Boy and the Heron (2023)",
        "Hayao Miyazaki's final film — he came out of retirement at 82 to make it — and Studio Ghibli released it in Japan with zero trailers or marketing, trusting the master's name alone. The result won the Oscar for Best Animated Feature: a boy grieving his mother in WWII Japan follows a talking heron into a dream-world, and the film's hand-drawn wonder (60 animators, no CGI shortcuts) is a farewell to a whole way of making movies. The ending is a goodbye you feel in your chest.",
        "Hayao Miyazaki",
        "The Boy and the Heron (2023) — the tower and the ending",
        124,
        "Watch the film's world-building — the heron's lies, the tower's door, the parakeets — and notice how Miyazaki's dream-logic is really emotional logic: every surreal image (the warawara, the pelican, the granduncle's blocks) is a feeling made visible, and the hand-drawn animation (each frame painted by hand) gives the fantasy a warmth no CGI can match. Then watch the ending, where the boy's choice about the world he's offered resolves: the film's argument — that we must live with our imperfections rather than build perfect ones — is in that finale, and the film's status as Miyazaki's farewell (he has 'retired' before, but this time it feels real) made it the decade's most precious animated film.",
        ["Animation", "Fantasy", "2020s", "Japanese"],
    ),
    _entry(
        "film-godzilla-minus-one-2023",
        "Godzilla Minus One (2023)",
        "The Godzilla film that finally won an Oscar — nearly 70 years after the original, this Japanese entry took Best Visual Effects with a team of just 35 artists and a budget around $15 million (a fraction of what Hollywood spends on one scene). Set in 1945 Japan, it reframes the monster as the trauma of war made flesh, and its human story — a kamikaze pilot who chose to live — is the best Godzilla has ever had. The 'minus one' title means Japan at zero, then losing more.",
        "Takashi Yamazaki",
        "Godzilla Minus One (2023) — the Ginza sequence and the ending",
        125,
        "Watch the Ginza sequence — the city, the monster's first full reveal, the impossible roar — and notice how the film earns its horror from context: Japan is rubble, the war has just ended, and Godzilla arrives as the country's debts made physical, with the film's VFX (a 35-person team) doing more with less than any Hollywood blockbuster. Then watch the ending, where the plan against Godzilla and the human cost resolve: the film's argument — that the survivor's guilt is the real monster, and that living is the act of courage — is in that finale, and the film's Oscar win (the first for the 70-year franchise) made it the most beloved Godzilla of all time.",
        ["Action", "Sci-Fi", "2020s", "Japanese"],
    ),
    _entry(
        "film-may-december-2023",
        "May December (2023)",
        "The most unsettling film about performance ever made — Natalie Portman's actress arrives to study Julianne Moore's Gracie, a woman who became a tabloid legend by beginning a relationship with a 13-year-old boy she later married. Todd Haynes' film (loosely inspired by the Mary Kay Letourneau case) is a comedy that curdles into horror, and its centerpiece — the 'garbage' scene, where Charles Melton's Joe finally confronts what was done to him — is the decade's most quietly devastating moment. The score, a piano theme that keeps swerving, is genius.",
        "Todd Haynes",
        "May December (2023) — the 'garbage' scene and the ending",
        117,
        "Watch the 'garbage' scene — Joe (Charles Melton) confronting Gracie in the kitchen, the decades of grooming finally named — and notice how Haynes lets the moment breathe in long, uncomfortable takes: the film's comedy (the actress's method, the melodrama) has been hiding this wound, and the scene's restraint is its power. Then watch the ending, where Elizabeth's final performance and the film's last shot resolve: the film's argument — that predators rewrite the story to make themselves the victims, and that performance is how they do it — is in that finale, and the film's 'is this a joke?' tone made it the decade's most discussed depiction of abuse.",
        ["Drama", "2020s", "Hollywood"],
    ),
    _entry(
        "film-air-2023",
        "Air (2023)",
        "The movie about a sneaker that shouldn't work — and does — Ben Affleck's film tells how Nike, an also-ran in basketball shoes, signed a rookie named Michael Jordan in 1984, and the film never shows Jordan's face (a deliberate choice: the legend is too big for the screen). Matt Damon's Sonny Vaccaro staking his career on one phone call, Viola Davis' mother's quiet power, and the film's final montage make it the decade's most purely satisfying business drama. The last shot — the shoes — is a love letter.",
        "Ben Affleck",
        "Air (2023) — the pitch scene and the ending",
        112,
        "Watch the film's center — Sonny's pitch, the 'your mother knows what you're worth' scene, the phone call to the Jordan family — and notice how the film builds tension without a single basketball scene: the drama is in the negotiation, and Viola Davis' Deloris Jordan (the film's secret weapon) delivers the decade's best monologue about what her son is worth. Then watch the ending, where the deal's final terms and the first Air Jordan resolve: the film's argument — that belief in someone is the real product, and that Jordan changed the game by being valued correctly — is in that finale, and the film's decision to keep Michael unseen makes his legend feel bigger than any actor could play.",
        ["Drama", "2020s", "Hollywood"],
    ),
    _entry(
        "film-dune-part-two-2024",
        "Dune: Part Two (2024)",
        "The sci-fi epic that made the desert sing — Denis Villeneuve's second half of Frank Herbert's novel has Paul Atreides (Timothée Chalamet) becoming a Fremen leader, a messiah he doesn't want to be, and the film's centerpiece — the sandworm ride, shot on real dunes with real heat — is the decade's greatest action sequence. It grossed over $700 million, won 2 Oscars (Sound and Visual Effects), and its 'the holy war' ending — Paul's march to the south — is sci-fi's most chilling prophecy about faith and power.",
        "Denis Villeneuve",
        "Dune: Part Two (2024) — the sandworm ride and the ending",
        166,
        "Watch the sandworm ride sequence — the first ride, the sand, the scale — and notice how Villeneuve films it practically: the dunes are real (shot in Jordan and Abu Dhabi), the riders are real, and the film's IMAX frames make you feel the desert's immensity, with Hans Zimmer's thumping score doing the rest. Then watch the ending, where Paul's choice to lead the war south and the film's final image resolve: the film's argument — that messiahs are made by the people who need them, and that Paul's tragedy is that he knows it — is in that finale, and the film's warning about charismatic power (delivered in a sci-fi epic) made it the decade's most serious blockbuster.",
        ["Sci-Fi", "Adventure", "2020s", "Hollywood"],
    ),
    _entry(
        "film-challengers-2024",
        "Challengers (2024)",
        "The horniest tennis movie ever made — and there's almost no actual tennis — Luca Guadagnino's triangle: Tashi (Zendaya), a tennis prodigy turned coach; her husband Art, a champion she built; and Patrick, his best friend and her ex, who meet in one final match. The film's structure cuts between the match and the decade of their entanglement, and its final point — scored to Trent Reznor and Atticus Ross's pulsing score (which won the Golden Globe) — is the most electric ending of the decade. 'I'm taking care of it' will live rent-free in your head.",
        "Luca Guadagnino",
        "Challengers (2024) — the final match and the ending",
        131,
        "Watch the final match — the tiebreak, the flashbacks intercutting with the points, the film's tennis-as-love-language — and notice how Guadagnino makes the match the film's climax and its metaphor: every shot is a memory, every point a power play, and the camera (including a famous shot from the ball's perspective) makes you feel the game like the players do. Then watch the ending, where the match's final point and the three characters' futures resolve: the film's argument — that love and competition are the same game, and that the point is to keep playing — is in that finale, and the film's decision to end on the frozen moment made it the decade's most discussed final shot.",
        ["Drama", "Romance", "2020s", "Hollywood"],
    ),
    _entry(
        "film-anora-2024",
        "Anora (2024)",
        "The Palme d'Or winner that became an Oscar phenomenon — Sean Baker's film follows Ani (Mikey Madison, who won Best Actress), a Brooklyn sex worker who marries the son of a Russian oligarch, and the wedding's collapse into a single chaotic Brooklyn night. The film's middle hour — a violent, hilarious, exhausting search through the city — is the decade's great screwball descent, and its ending — the car, the tears, the 'thank you' — is the most devastating final scene in recent memory. Baker won 4 Oscars himself (Producer, Director, Editor, and Original Screenplay).",
        "Sean Baker",
        "Anora (2024) — the Brighton Beach sequence and the ending",
        139,
        "Watch the Brighton Beach sequence — the search, the goons, the comedy curdling into exhaustion — and notice how Baker (shooting on 35mm with handheld naturalism) builds the film's middle like a silent-comedy nightmare: the jokes get darker as the night goes on, and Ani's fury (she fights back in every scene) is the film's engine. Then watch the ending, where the car ride and the film's final exchange resolve: the film's argument — that the Cinderella story is a job, and that the transaction was never about love — is in that finale, and the film's last shot (the closest thing to a hug Baker has ever filmed) made it the decade's most heartbreaking final image.",
        ["Drama", "Comedy", "Romance", "2020s", "Hollywood"],
    ),
    _entry(
        "film-the-brutalist-2024",
        "The Brutalist (2024)",
        "A 215-minute American epic with an intermission — Adrien Brody (who won his second Best Actor Oscar, 22 years after The Pianist) plays László Tóth, a Hungarian Jewish architect who survives the Holocaust and rebuilds his life in America, only to be consumed by the patron (Guy Pearce) who funds his masterpiece. Brady Corbet shot the film in 34 days on VistaVision, and its second half — the tower, the betrayal, the epilogue that reframes everything — is the decade's most ambitious filmmaking. The 'it's not a spoiler' ending is a masterstroke.",
        "Brady Corbet",
        "The Brutalist (2024) — the epilogue and the ending",
        215,
        "Watch the film's construction sequences — the concrete, the measurements, the tower rising — and notice how the film uses architecture as psychology: László's buildings are his soul poured into stone, and the film's long, patient takes (shot on VistaVision for an old-Hollywood grandeur) make the craft the story. Then watch the ending, where the epilogue's reveal re-frames the entire film: the film's argument — that American patronage is a new kind of colonialism, and that the immigrant's genius is the patron's trophy — is in that finale, and the film's 215-minute runtime, intermission and all, made it the decade's great statement about what it costs to build.",
        ["Drama", "History", "2020s", "Hollywood"],
    ),
    _entry(
        "film-conclave-2024",
        "Conclave (2024)",
        "The Vatican thriller that won Best Adapted Screenplay — Ralph Fiennes' Cardinal Lawrence must run the papal conclave after the Pope's sudden death, and the film's sealed-doors election becomes a mystery: secret factions, buried scandals, and a final twist that re-frames the whole institution. Edward Berger (who directed All Quiet on the Western Front) stages the cardinals' red-robed processions like a thriller, and the film's ending — the new pope's identity, and Lawrence's last choice — is the decade's best final reveal. The 'confetti' imagery is genius.",
        "Edward Berger",
        "Conclave (2024) — the twist and the ending",
        120,
        "Watch the film's process — the conclave's rituals, the voting, the corridors of red-robed cardinals — and notice how Berger films the Church's machinery as a thriller's set design: the white smoke, the locked doors, the whispers are the genre's vocabulary, and the film's 'confetti' motif (the ballots, the ashes) keeps reminding you what's at stake. Then watch the ending, where the final revelation and Lawrence's choice resolve: the film's argument — that institutions must evolve or die, and that faith can survive the institution — is in that finale, and the film's twist (which rewards the attentive viewer) made it the most talked-about ending of the awards season.",
        ["Drama", "Mystery", "Thriller", "2020s", "Hollywood"],
    ),
    _entry(
        "film-the-substance-2024",
        "The Substance (2024)",
        "The body-horror phenomenon — Demi Moore (who won the Golden Globe for Best Actress, the first major award of her career) plays an aging TV star who injects a black-market serum that creates a younger, 'better' version of herself — with rules: one week each, no exceptions. Coralie Fargeat's film won Best Screenplay at Cannes, became Mubi's biggest hit ever ($77 million), and its escalation — the second act's final sequence is the most audacious body-horror set piece of the century — turned the Hollywood ageism critique into a gore masterpiece. The ending is unforgettable.",
        "Coralie Fargeat",
        "The Substance (2024) — the transformation and the ending",
        141,
        "Watch the film's central mechanism — the injection, the splitting, the 'one week each' rule — and notice how Fargeat makes the metaphor literal with total commitment: the body horror is the Hollywood ageism, and the film's surgical, candy-colored style (the corridors, the lab, the neon) turns the beauty industry into a nightmare factory. Then watch the ending, where the final confrontation and the film's last image resolve: the film's argument — that the industry consumes women and produces monsters, and that the monster is the product — is in that finale, and the film's refusal to blink (it goes further than any mainstream film in decades) made it the decade's most talked-about horror film.",
        ["Horror", "Sci-Fi", "2020s", "Hollywood"],
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
