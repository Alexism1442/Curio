#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — 2000s + 2010s (final batch).

Ninth addition batch (v1.0 content pass — brings films.json to 400 total):
Crouching Tiger Hidden Dragon, Gladiator, Requiem for a Dream, Almost
Famous, The Fellowship of the Ring, Moulin Rouge!, Y Tu Mamá También, The
Royal Tenenbaums, The Pianist, Catch Me If You Can, Finding Nemo, Kill Bill
Vol. 1, The Return of the King, Shaun of the Dead, The Incredibles, Before
Sunset, Batman Begins, The Departed, The Prestige, Casino Royale, Little
Miss Sunshine, Ratatouille, Zodiac, Slumdog Millionaire, The Wrestler,
District 9, The Grand Budapest Hotel, Birdman, Inside Out, Hereditary.
Handcrafted teaser + real fact + quality-bar instruction. Appends only;
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
        "film-crouching-tiger-hidden-dragon-2000",
        "Crouching Tiger, Hidden Dragon (2000)",
        "The film that introduced the world to wuxia — Ang Lee's martial-arts romance with the most beautiful fight scenes ever filmed (the bamboo-forest duel is the genre's Mona Lisa). It was the first foreign-language film to gross over $100 million in the US, won 4 Oscars (including Best Foreign Language Film), and its flying, wire-worked fights — choreographed by Yuen Woo-ping — made gravity itself a special effect.",
        "Ang Lee",
        "Crouching Tiger, Hidden Dragon (2000) — the bamboo forest fight",
        120,
        "Watch the bamboo-forest duel — Li Mu Bai and Yu Shu Lien's student, the bending trees, the weightless choreography — and notice how the wire work is used for poetry, not spectacle: the fighters move through the air like thoughts, and the fight is a conversation. Then watch the ending, where the film's themes of honor and love resolve at Wudang Mountain: the film's argument — that the heart is a wilderness no discipline can tame — is in that finale, and the film's box office proved subtitled cinema could be a blockbuster.",
        ["Action", "2000s", "Hollywood"],
    ),
    _entry(
        "film-gladiator-2000",
        "Gladiator (2000)",
        "The film that revived the sword-and-sandal epic — Russell Crowe's Maximus, betrayed by the emperor's son and sold into slavery, who rises through the arena to face his enemy. It won 5 Oscars including Best Picture, and its opening battle (the Germanic forest, filmed with 2,000 extras and CGI crowds) and the 'Are you not entertained?' moment made it the decade's first great blockbuster. Crowe's Oscar for Best Actor made him the era's defining movie star.",
        "Ridley Scott",
        "Gladiator (2000) — the opening battle and the ending",
        155,
        "Watch the opening battle — the Germanic forest, the fire arrows, the charge — and notice how the film combines practical effects (real horsemen, real fire) with CGI crowds to create a battle that feels physical: the film's realism is its spectacle, and Maximus's 'Are you not entertained?' is the film's thesis about the arena's relationship to the audience. Then watch the ending, where Maximus's final fight and his return to his family resolve: the film's argument — that honor is the only thing the arena can't take — is in that finale, and the film's famous wheat-field imagery bookends its moral.",
        ["Action", "Drama", "2000s", "Hollywood"],
    ),
    _entry(
        "film-requiem-for-a-dream-2000",
        "Requiem for a Dream (2000)",
        "The most brutal film about addiction ever made — Darren Aronofsky's four intercut stories (a Brooklyn mother, her son, his girlfriend, and his friend) told with the film's signature 'hip-hop montage' (the rapid-cut obsession shots) and Clint Mansell's 'Lux Aeterna' score (since used in everything from The Lord of the Rings trailers to every sports hype video). Ellen Burstyn's performance earned an Oscar nomination, and the film's ending — the refrigerator, the 'ass to ass,' the final montage — is the decade's most devastating.",
        "Darren Aronofsky",
        "Requiem for a Dream (2000) — the ending",
        102,
        "Watch the film's parallel structure — the four stories, the seasons, the escalation — and notice how Aronofsky's style (the split-screen, the rapid montages, the 'hip-hop' obsession shots) makes addiction feel like a machine: each story is a different addiction, and the editing is the high. Then watch the ending, where the four fates converge in the final montage: the film's argument — that the dream is the drug — is in that finale, and the film's refusal to offer hope (it's the rare film that warns, not comforts) made it the decade's most argued-over masterpiece.",
        ["Drama", "2000s", "Hollywood"],
    ),
    _entry(
        "film-almost-famous-2000",
        "Almost Famous (2000)",
        "Cameron Crowe's autobiographical love letter to rock 'n' roll — a 15-year-old journalist (based on Crowe himself, who wrote for Rolling Stone at that age) touring with a fictional band. The film's 'Tiny Dancer' bus scene — the whole bus singing along, dissolving the band's feud — is the decade's most beloved musical moment, and the film won the Oscar for Best Original Screenplay. 'I'm a golden god!' and 'The T-shirt' are legendary.",
        "Cameron Crowe",
        "Almost Famous (2000) — the Tiny Dancer scene and the ending",
        122,
        "Watch the 'Tiny Dancer' scene — the bus, the feud, the song, everyone singing — and notice how Crowe builds the film's heart from a single Elton John song: the moment is about music's power to heal, and the film's 'band-aids and groupies' world is drawn from Crowe's real teenage experiences. Then watch the ending, where William's final interview and the 'I'm a golden god' moment resolve: the film's argument — that the people you meet when you're young are the ones who matter forever — is in that finale, and the film's soundtrack (the greatest of its decade) makes it endlessly rewatchable.",
        ["Drama", "Music", "2000s", "Hollywood"],
    ),
    _entry(
        "film-lotr-fellowship-2001",
        "The Lord of the Rings: The Fellowship of the Ring (2001)",
        "The film that proved fantasy could be cinema's biggest genre — Peter Jackson's adaptation of Tolkien, filmed in New Zealand over 15 months with all three movies at once. The film's 'You shall not pass!' (the Balrog, Gandalf's fall) is the decade's defining fantasy moment, and the film's blend of practical effects (the scale doubles, the armor, the Shire) and CGI set the standard. It won 4 Oscars and grossed $897 million, launching the most successful trilogy in history.",
        "Peter Jackson",
        "The Lord of the Rings: The Fellowship of the Ring (2001) — the Mines of Moria sequence",
        178,
        "Watch the Mines of Moria sequence — the tomb, the drum-beats, the Balrog, Gandalf's 'You shall not pass!' — and notice how the film's tension is built from sound: the drums, the whispers, the silence before the fire — and how the Balrog's reveal blends a real flame rig with CGI. Then watch the ending, where the Fellowship breaks: the film's argument — that the quest will cost everyone everything, including each other — is in that finale, and the film's 178-minute runtime (an epic for an epic) made it the defining fantasy film of its era.",
        ["Fantasy", "Adventure", "2000s", "Hollywood"],
    ),
    _entry(
        "film-moulin-rouge-2001",
        "Moulin Rouge! (2001)",
        "The jukebox musical that reinvented the genre — Baz Luhrmann's fin-de-siècle Parisian cabaret where the songs are pop hits ('Lady Marmalade,' 'Roxanne') performed as opera, with Nicole Kidman's Satine and Ewan McGregor's Christian. The film's 'Elephant Love Medley' and its 'Come What May' (the only original song) made it a phenomenon, and its 8 Oscar nominations (winning 2) and $179 million gross made it the year's most stylized hit. The ending, with 'The Show Must Go On,' is devastating.",
        "Baz Luhrmann",
        "Moulin Rouge! (2001) — the Elephant Love Medley",
        127,
        "Watch the 'Elephant Love Medley' — the rooftop, the dueling pop lyrics, the declaration — and notice how Luhrmann's method (taking familiar songs and staging them as opera) makes the film's emotions universal: the medley is a love story told through everyone else's words, and the effect is strangely more romantic. Then watch the ending, where Satine's sacrifice and the 'Come What May' resolution land: the film's argument — that love is the only thing worth dying for, and the show must go on — is in that finale, and the film's visual excess (the can-can, the glitter, the neon) is the decade's most distinctive style.",
        ["Musical", "Romance", "2000s", "Hollywood"],
    ),
    _entry(
        "film-y-tu-mama-tambien-2001",
        "Y Tu Mamá También (2001)",
        "The Mexican road movie that launched Alfonso Cuarón — two teenage boys and an older woman (Maribel Verdú) drive to a mythical beach, and the film's sexuality, politics, and class warfare unfold in the gaps. The film's famous twist — the two boys' secret — and its ending (the woman's confession, the beach, the letter) made it the decade's most quietly radical film. The narration (an omniscient voiceover that tells you the futures of everyone the characters pass) is Cuarón's signature device.",
        "Alfonso Cuarón",
        "Y Tu Mamá También (2001) — the ending",
        106,
        "Watch the film's middle — the driving, the arguing, the 'if you could choose your last meal' game — and notice how Cuarón (with cinematographer Emmanuel Lubezki) films the road as a documentary of Mexico: the film's beauty and its politics share the frame, and the characters' obliviousness is the point. Then watch the ending, where the beach's reality and the letter resolve: the film's argument — that youth ends when you learn what you've been hiding from — is in that finale, and the film's mix of sex, comedy, and grief made it the decade's most talked-about foreign-language film.",
        ["Drama", "2000s", "Mexican"],
    ),
    _entry(
        "film-the-royal-tenenbaums-2001",
        "The Royal Tenenbaums (2001)",
        "Wes Anderson's breakthrough — a family of prodigies who've all failed as adults, reuniting when the father (Gene Hackman) fakes a fatal illness. The film's 'Needle in the Hay' scene (Richie's suicide attempt, set to Elliott Smith), its Margot-on-the-bus scene ('They're gonna look at you and think...'), and its 'the Royal Tenenbaums' chapter-book structure made Anderson the decade's most distinctive voice. It earned an Oscar nomination for its screenplay.",
        "Wes Anderson",
        "The Royal Tenenbaums (2001) — the ending",
        110,
        "Watch the film's structure — the chapters, the 'Crosby, Stills & Nash' moments, the perfectly arranged frames — and notice how Anderson's style (the symmetry, the costumes, the deadpan) is the film's comedy and its sadness at once: the family is a collection of beautiful failures, and the film treats them with total affection. Then watch the ending, where the family's reconciliation (and the slow-motion walk) resolves: the film's argument — that family is the only institution that forgives everything — is in that finale, and the film's influence (every 'quirky ensemble' film since) is immeasurable.",
        ["Comedy", "Drama", "2000s", "Hollywood"],
    ),
    _entry(
        "film-the-pianist-2002",
        "The Pianist (2002)",
        "Roman Polanski's Holocaust film — the true story of Władysław Szpilman, a Polish pianist who survived the Warsaw Ghetto through hiding, luck, and music. It won 3 Oscars including Best Director (Polanski, who survived the Kraków ghetto as a child), and Adrien Brody — who sold his car, gave up his apartment, and lost 30 pounds for the role — became the youngest Best Actor winner ever at 29. The film's final scene — the German officer, the piano, the Chopin — is one of cinema's great finales.",
        "Roman Polanski",
        "The Pianist (2002) — the ending",
        150,
        "Watch the film's central survival sequence — Szpilman alone in the ruined ghetto, the silence, the hunger — and notice how Polanski films the horror as emptiness: no score, no drama, just one man and the winter. Then watch the ending, where the German officer discovers Szpilman and asks him to play: the film's argument — that music is the one thing the war couldn't kill — is in that scene, and the film's restraint (Polanski shows the horror without exploitation) made it the decade's most personal Holocaust film.",
        ["Drama", "War", "2000s", "Hollywood"],
    ),
    _entry(
        "film-catch-me-if-you-can-2002",
        "Catch Me If You Can (2002)",
        "The true story of Frank Abagnale Jr., who passed $2.5 million in bad checks as a fake airline pilot, doctor, and lawyer before age 21 — and the FBI agent (Tom Hanks) who finally caught him. Leonardo DiCaprio's charm, the John Williams score, and the film's 'game of cat and mouse' structure made it one of Spielberg's most purely enjoyable films. The film's ending — the real Abagnale's fate (he now works for the FBI) — is the best part of the true story.",
        "Steven Spielberg",
        "Catch Me If You Can (2002) — the opening and the ending",
        141,
        "Watch the opening credits — the jazz, the silhouettes, the animated con — and notice how the film announces its style in the first two minutes: the era's Rat Pack cool, the game, and the charm are the movie's engine, and DiCaprio's Frank is one of the most likable con men ever filmed. Then watch the ending, where Frank's final run and the real story's twist (he escaped, then returned, then joined the FBI) resolve: the film's argument — that the con artist and the cop are the same kind of lonely — is in that finale, and the film's true-story depth made it the decade's most rewatchable comedy.",
        ["Comedy", "Crime", "2000s", "Hollywood"],
    ),
    _entry(
        "film-finding-nemo-2003",
        "Finding Nemo (2003)",
        "Pixar's ocean epic — a clownfish father (Albert Brooks) crosses the Pacific to rescue his son, with a forgetful blue tang (Ellen DeGeneres's Dory) as his guide. The film's rendering of water — the most difficult animation challenge of its era — won the Oscar for Best Animated Feature, and its 'P. Sherman, 42 Wallaby Way, Sydney' became a global catchphrase. It grossed $940 million, making it the best-selling DVD of all time.",
        "Andrew Stanton",
        "Finding Nemo (2003) — the ending",
        100,
        "Watch the film's first act — the coral reef, the 'right whale' lecture, the boat — and notice how Pixar's water simulation (a technical milestone: the light, the current, the physics) makes the ocean the film's real star: the animation was so convincing it won the Oscar. Then watch the ending, where Marlin finally lets Nemo go ('You're free. I'm free.'): the film's argument — that love means letting go — is in that finale, and the film's balance of comedy (Dory's 'Just keep swimming'), peril, and heart made it the most beloved Pixar film of its era.",
        ["Animation", "Family", "2000s", "Hollywood"],
    ),
    _entry(
        "film-kill-bill-vol-1-2003",
        "Kill Bill: Vol. 1 (2003)",
        "Tarantino's martial-arts revenge epic — Uma Thurman's Bride, the Yellow Jumpsuit, the Hattori Hanzo sword, and the House of Blue Leaves massacre. The film's anime sequence (the backstory of O-Ren Ishii) and its 'Crazy 88' fight — shot in black and white to pass censorship — are among the decade's great set pieces. The film is a love letter to every genre Tarantino grew up on, and the 'Bride vs. O-Ren' snow-garden duel is its masterpiece.",
        "Quentin Tarantino",
        "Kill Bill: Vol. 1 (2003) — the House of Blue Leaves sequence",
        111,
        "Watch the House of Blue Leaves sequence — the Bride versus the Crazy 88, the 'snow' of severed limbs, the shift to black and white — and notice how Tarantino choreographs the film's centerpiece as a rock-opera of violence: the wuxia wire work, the samurai precision, and the soundtrack (the 'Ironside' theme, the 'Battle Without Honor or Humanity') make the massacre a musical. Then watch the ending, where the Bride's mission is revealed to be just beginning: the film's structure — a revenge epic split in two — is its boldest choice, and the film's style made it the most influential action film of its decade.",
        ["Action", "Crime", "2000s", "Hollywood"],
    ),
    _entry(
        "film-lotr-return-of-the-king-2003",
        "The Return of the King (2003)",
        "The finale that swept all 11 Oscars it was nominated for — tying Ben-Hur and Titanic for the most wins ever — and the first fantasy film to win Best Picture. The film's multiple endings ('My friends, you bow to no one,' the eagles, the ship to the West) became a cultural in-joke, but its climax — the Ring's destruction at Mount Doom, Gollum's fall — is the decade's greatest payoff. It grossed $1.1 billion, the first fantasy film to cross a billion.",
        "Peter Jackson",
        "The Return of the King (2003) — the ending",
        201,
        "Watch the film's final act — the Ride of the Rohirrim, the battle before the Black Gate, the Ring's destruction — and notice how the film earns its eleven endings: each farewell (the hobbits, the 'you bow to no one,' the ship) closes a different thread, and the film's 201-minute runtime is built to make you feel the loss of leaving Middle-earth. Then watch the final scene, where Frodo sails West and Sam's line ('I'm back') lands: the film's argument — that the smallest people carry the greatest burdens — is in that finale, and the film's Oscar sweep remains the fantasy genre's greatest triumph.",
        ["Fantasy", "Adventure", "2000s", "Hollywood"],
    ),
    _entry(
        "film-shaun-of-the-dead-2004",
        "Shaun of the Dead (2004)",
        "The 'romantic comedy with zombies' that launched Edgar Wright and the Cornetto Trilogy — Simon Pegg's slacker Shaun walks to the corner shop through the apocalypse, and the film's running gags (the 'gag' foreshadowing, the record-throwing scene set to 'Don't Stop Me Now') are the decade's most inventive comedy. The film's structure — every detail planted in the first act pays off in the third — made it the most rewatchable comedy of its decade. Its famous final scene, with the zombie on the leash, is perfect.",
        "Edgar Wright",
        "Shaun of the Dead (2004) — the record-throwing scene and the ending",
        99,
        "Watch the record-throwing scene — the pub, the 'Don't Stop Me Now' needle drop, the synchronized tracklisting — and notice how Wright's editing (the whip pans, the match cuts, the planted gags) makes the film a comedy machine: the joke is the craft, and the foreshadowing (the 'gag' at the start returns as the weapon at the end) rewards rewatching. Then watch the ending, where the film's 'rom-com' structure completes: the film's argument — that even the apocalypse can't stop a bloke from getting his life together — is in that finale, and the film's balance of horror and heart made it the decade's defining British comedy.",
        ["Comedy", "Horror", "2000s", "Hollywood"],
    ),
    _entry(
        "film-the-incredibles-2004",
        "The Incredibles (2004)",
        "The superhero film that worked as a family drama — Brad Bird's story of a retired caped crusader (Craig T. Nelson) and his superpowered family, forced back into action. The film's 'No capes!' warning, its midlife-crisis satire, and its baby (Jack-Jack's scene is the decade's funniest animation) made it the best-reviewed film of its year. It won 2 Oscars (including Best Animated Feature) and grossed $633 million, and its sequel, 14 years later, was equally beloved.",
        "Brad Bird",
        "The Incredibles (2004) — the ending and the 'no capes' scene",
        115,
        "Watch the 'No capes!' scene — Edna Mode's rant, the montage of superhero deaths — and notice how the film's comedy is its philosophy: the film argues that costumes (and the heroics they imply) kill people, and that real heroism is family. Then watch the ending, where the family's combined powers defeat the villain: the film's argument — that a family is a team where each member's flaw is another's strength — is in that finale, and the film's mix of action, satire, and genuine feeling made it the most adult 'kids' film of its decade.",
        ["Animation", "Family", "2000s", "Hollywood"],
    ),
    _entry(
        "film-before-sunset-2004",
        "Before Sunset (2004)",
        "The sequel that outdid its original — Richard Linklater reunited Ethan Hawke and Julie Delpy nine years after Before Sunrise, for one real-time evening in Paris. The film's 'missed flight' structure, its walk through the city, and its ending — Celine's song, the 'I know' — are the most romantic in cinema. The film's 'you're going to miss your plane' ending (deliberately unresolved) made audiences scream, and the trilogy's third film, Before Midnight, would answer it nine years later.",
        "Richard Linklater",
        "Before Sunset (2004) — the ending",
        80,
        "Watch the film's real-time structure — the walk, the bookshop, the car — and notice how the film's 80 minutes unfold in something close to real time: the conversation is the plot, and the chemistry (Hawke and Delpy co-wrote much of the dialogue) is the film's engine. Then watch the ending, where Celine's song ('the waltz') and the final 'I know' resolve: the film's argument — that the question 'what if' is the most romantic thing two people can share — is in that finale, and the film's refusal to answer it (before Midnight did) made it the most argued-about ending of its decade.",
        ["Romance", "Drama", "2000s", "Hollywood"],
    ),
    _entry(
        "film-batman-begins-2005",
        "Batman Begins (2005)",
        "The reboot that reinvented the superhero film — Christopher Nolan's origin story grounded Batman in fear, realism, and a city that needs him. Christian Bale's Bruce Wayne, the League of Shadows, the Tumbler, and the film's 'why do we fall?' mantra made it the template for the modern comic-book movie. It grossed $374 million and launched the Dark Knight trilogy, the most critically acclaimed superhero series ever made.",
        "Christopher Nolan",
        "Batman Begins (2005) — the training sequence and the ending",
        140,
        "Watch the training sequence — Bruce in the ice, the League of Shadows, the 'mindset' lesson — and notice how Nolan grounds the superhero fantasy in discipline: the film's Batman is built from training, fear, and technology, not magic, and the 'fear is a weapon' theme is the film's engine. Then watch the ending, where the film's final line ('I'm Batman') and the Joker card tease resolve: the film's argument — that a hero is made by refusing to give up — is in that finale, and the film's realism (no camp, no gadgets-for-gadgets) changed what audiences expected from comic-book films.",
        ["Action", "2000s", "Hollywood"],
    ),
    _entry(
        "film-the-departed-2006",
        "The Departed (2006)",
        "The film that finally won Scorsese his Oscar — his Boston crime thriller where the mob has a mole in the police and the police have a mole in the mob. The film's 'rat' imagery, its three-hander (Leonardo DiCaprio, Matt Damon, Jack Nicholson's Costello), and its notorious ending — the elevator, the betrayal, the rat — made it the decade's great crime film. It won 4 Oscars including Best Picture and Best Director, and its final shot is among the most discussed in cinema.",
        "Martin Scorsese",
        "The Depressed (2006) — the ending",
        151,
        "Watch the film's structure — the two moles, the 'rat' voiceover, the parallel lives — and notice how Scorsese (remaking the Hong Kong classic Infernal Affairs) builds the tension from the audience knowing both secrets: every scene is a near-miss, and the film's Boston accent work is a genre in itself. Then watch the ending, where the film's signature twist (the elevator, the head-shot) and the final 'rat' image resolve: the film's argument — that the system breeds everyone, and the rat always survives — is in that finale, and the film's Oscar sweep (Scorsese's first) made it the capstone of his career.",
        ["Crime", "Thriller", "2000s", "Hollywood"],
    ),
    _entry(
        "film-the-prestige-2006",
        "The Prestige (2006)",
        "The magician movie that's actually about obsession — Christopher Nolan's duel between two turn-of-the-century illusionists (Hugh Jackman, Christian Bale) who escalate from rivalry to mutual destruction. The film's structure — 'the pledge, the turn, the prestige' — is the plot, and its twist (the Tesla machine, the clones, the tanks) is the most carefully built reveal in Nolan's career. Michael Caine's 'Are you watching closely?' is the film's thesis.",
        "Christopher Nolan",
        "The Prestige (2006) — the reveal and the ending",
        130,
        "Watch the film's structure — the three-act magic trick, the diaries, the 'are you watching closely?' — and notice how Nolan (adapting Christopher Priest's novel) tells the story as a magic trick itself: the film's first half is the pledge, its middle the turn, and the reveal is the prestige. Then watch the ending, where the truth about the two magicians and the tanks is revealed: the film's argument — that obsession is a sacrifice of everything, including the self — is in that finale, and the film's twist (which rewards a second viewing) made it the most rewatchable film of its year.",
        ["Mystery", "Thriller", "2000s", "Hollywood"],
    ),
    _entry(
        "film-casino-royale-2006",
        "Casino Royale (2006)",
        "The Bond film that reinvented Bond — Daniel Craig's brutal, human 007 in a reboot that threw out the gadgets and the jokes and kept the menace. The film's parkour opening chase, its 'I'm the money' poker game, and its ending — the betrayal, the 'The bitch is dead' — are the darkest in the franchise's history. The film's 'Vesper' romance (Eva Green) is the only love story Bond has ever been allowed to lose, and the film's box office ($616 million) made Craig the definitive modern Bond.",
        "Martin Campbell",
        "Casino Royale (2006) — the parkour chase and the ending",
        144,
        "Watch the opening chase — the construction site, the parkour, the embassy — and notice how the film announces its reboot in the first ten minutes: the black-and-white prologue (Bond's first two kills) and the physical, bruising action (no gadgets) make Bond feel real for the first time. Then watch the ending, where Bond's first love is taken and the film's famous final line lands: the film's argument — that the spy's life costs everything, and the cold is a choice — is in that finale, and the film's moral seriousness made it the franchise's greatest film.",
        ["Action", "Thriller", "2000s", "Hollywood"],
    ),
    _entry(
        "film-little-miss-sunshine-2006",
        "Little Miss Sunshine (2006)",
        "The indie road-trip comedy that became a phenomenon — a dysfunctional family's VW bus trip to a child beauty pageant, with a deadpan dad, a suicidal Proust scholar (Steve Carell), a coke-addicted grandpa (Alan Arkin, who won the Oscar), and a silent teenage boy. The film's 'Super Freak' dance finale and its 'chicken' diner scene made it the most beloved comedy of its year. It won 2 Oscars (including Best Original Screenplay) and grossed $101 million on an $8 million budget.",
        "Jonathan Dayton & Valerie Faris",
        "Little Miss Sunshine (2006) — the ending",
        101,
        "Watch the film's first hour — the family, the VW bus (the clutch repair is a running gag), the breakdowns — and notice how the film builds its comedy from the family's dysfunction: every character's failure is the setup, and the film's tone (sad and funny at once) is its signature. Then watch the ending, where Olive's 'Super Freak' routine and the family's jail cell dance resolve: the film's argument — that family is the place where failure is allowed — is in that finale, and the film's $8-million-budget success made it the indie phenomenon of its year.",
        ["Comedy", "Drama", "2000s", "Hollywood"],
    ),
    _entry(
        "film-ratatouille-2007",
        "Ratatouille (2007)",
        "The greatest film ever made about food — Brad Bird's story of Remy, a rat who wants to be a chef in Paris, and the 'anyone can cook' philosophy. The film's critical scene — the food critic Anton Ego's childhood bite of ratatouille, which unlocks his memory — is the decade's most moving single image, and the film won the Oscar for Best Animated Feature. The film's famous quote — 'The world is often unkind to new talent, new creations' — is the film's thesis.",
        "Brad Bird",
        "Ratatouille (2007) — the Ego scene and the ending",
        111,
        "Watch the film's final act — the dish, the critic, the flashback — and notice how the film builds to its most famous moment: Ego's bite of ratatouille transports him to his childhood, and the film's argument — that food is memory, and that greatness is a matter of taste, not class — is delivered in that one bite. Then watch the ending, where the restaurant's fate and the 'anyone can cook' moral resolve: the film's message — that genius comes from anywhere, even a sewer — is in that finale, and the film's animation (the most realistic food ever rendered) made it the definitive culinary film.",
        ["Animation", "Family", "2000s", "Hollywood"],
    ),
    _entry(
        "film-zodiac-2007",
        "Zodiac (2007)",
        "The greatest true-crime film ever made — David Fincher's meticulous account of the Zodiac killer, whose cipher-taunting of San Francisco went unsolved. The film's 157 minutes follow the detectives and journalists (Jake Gyllenhaal's cartoonist, Mark Ruffalo's inspector, Robert Downey Jr.'s reporter) through a decade of obsession, and its basement scene — the 'movie theater' confrontation — is among the decade's most terrifying. The film's digital cinematography (Fincher shot on digital cameras, a first) is its signature.",
        "David Fincher",
        "Zodiac (2007) — the basement scene",
        157,
        "Watch the basement scene — the projectionist's house, the 'I'd recognize him anywhere' meeting — and notice how Fincher builds the decade's most terrifying sequence from total stillness: no music, no cuts, just two men and a staircase, and the film's refusal to show the killer's face is the point. Then watch the ending, where the case's unsolved mystery and the 'one man knows' coda resolve: the film's argument — that obsession is its own form of madness, and that some doors stay open — is in that finale, and the film's patient, factual structure (based on Robert Graysmith's book) made it the definitive document of the case.",
        ["Crime", "Thriller", "2000s", "Hollywood"],
    ),
    _entry(
        "film-slumdog-millionaire-2008",
        "Slumdog Millionaire (2008)",
        "The underdog story that swept the Oscars (8 wins including Best Picture) — an 18-year-old Mumbai 'slumdog' who knows the answers on Who Wants to Be a Millionaire because his brutal life taught him each one. Danny Boyle's film (with the 'Jai Ho' finale) was the year's phenomenon, and its 'who wants to be a millionaire?' structure turned the game show into a memoir. The child actors (recruited from real Mumbai slums) are the film's heart, and the film's ending dance number is the decade's most joyful final scene.",
        "Danny Boyle",
        "Slumdog Millionaire (2008) — the ending",
        120,
        "Watch the film's structure — the game show, the flashbacks, the 'It is written' — and notice how Boyle intercuts Jamal's answers with the moments that taught them: each question is a chapter of his life, and the film's editing (by Chris Dickens, who won the Oscar) makes the structure feel inevitable. Then watch the ending, where the reunion and the 'Jai Ho' dance number resolve: the film's argument — that the poor know more than the rich, because life doesn't come with instructions — is in that finale, and the film's box office and Oscar sweep made it the feel-good phenomenon of its year.",
        ["Drama", "Romance", "2000s", "Hollywood"],
    ),
    _entry(
        "film-the-wrestler-2008",
        "The Wrestler (2008)",
        "The comeback story that out-came-back its actor — Mickey Rourke's Randy 'The Ram' Robinson, a washed-up 1980s wrestler who can't stop climbing into the ring. Darren Aronofsky's film is the decade's most honest portrait of a body and a soul wearing out, and its ending — the Ram's final match, the 'I'm an old broken-down piece of meat' speech — is the decade's most devastating. Rourke's performance (nominated for the Oscar) remains the great cinematic comeback.",
        "Darren Aronofsky",
        "The Wrestler (2008) — the ending",
        109,
        "Watch the film's first act — the deli counter, the trailer, the steroids — and notice how Aronofsky films the Ram's life in long takes and close-ups: the film's handheld camera (shot on video) makes the body the subject, and every bruise is a line of dialogue. Then watch the ending, where the Ram's decision to take the final match and the 'I'm here' speech resolve: the film's argument — that the only place a broken man is whole is the arena — is in that finale, and the film's ending (deliberately ambiguous, cut before the landing) is the decade's most debated final scene.",
        ["Drama", "2000s", "Hollywood"],
    ),
    _entry(
        "film-district-9-2009",
        "District 9 (2009)",
        "The alien-invasion film told from the aliens' side — Neill Blomkamp's debut, a mockumentary about an alien refugee camp in Johannesburg, made for $30 million with a first-time lead (Sharlto Copley, a friend of Blomkamp's who'd never acted). The film's apartheid allegory, its 'prawns,' and its ending — the metal flower, the promise — made it the most original sci-fi film of its decade. It earned 4 Oscar nominations including Best Picture.",
        "Neill Blomkamp",
        "District 9 (2009) — the ending",
        112,
        "Watch the film's first act — the documentary interviews, the eviction, the 'prawns' — and notice how the mockumentary form (with real South African news footage and interviews) makes the sci-fi premise feel like current events: the film's apartheid allegory is the point, and the aliens' treatment is the horror. Then watch the ending, where Wikus's transformation and the metal flower resolve: the film's argument — that the persecuted become monsters only to survive, and that redemption is a promise kept — is in that finale, and the film's $210 million gross on a $30 million budget made it the decade's most profitable original film.",
        ["Sci-Fi", "2000s", "Hollywood"],
    ),
    _entry(
        "film-the-grand-budapest-hotel-2014",
        "The Grand Budapest Hotel (2014)",
        "Wes Anderson's masterpiece — a concierge (Ralph Fiennes, in the performance of his career) and his lobby boy across a fictional European nation, told in nested flashbacks. The film's pastel palette, its changing aspect ratios (each era gets a different frame shape), and its 'courtesan au chocolat' pastry are Anderson's style at its purest. It won 4 Oscars and was nominated for Best Picture, and its comedy — the prison escape, the 'little known fact' — is the decade's most refined.",
        "Wes Anderson",
        "The Grand Budapest Hotel (2014) — the opening and the ending",
        99,
        "Watch the film's structure — the author, the hotel, the 'lobby boy' Zero, the layers of narration — and notice how Anderson's style (the symmetry, the pastels, the aspect-ratio shifts for each era) is the film's comedy and its melancholy: the film is about a world that's about to vanish, and the beauty is the elegy. Then watch the ending, where the film's final reveal (the 'memento' and the girl with the book) resolves: the film's argument — that the past is a hotel we're all checking out of — is in that finale, and the film's 4 Oscars (its production design, score, costume, and makeup) made it the most awarded comedy of its decade.",
        ["Comedy", "Drama", "2010s", "Hollywood"],
    ),
    _entry(
        "film-birdman-2014",
        "Birdman (2014)",
        "The film that looks like one continuous shot — Alejandro González Iñárritu's Broadway comedy about a washed-up superhero actor (Michael Keaton, playing his own history) trying to mount a serious play. The film's 'one take' illusion (it was shot in long takes, edited to appear continuous) won it 4 Oscars including Best Picture, and its drum score, its backstage chaos, and its ending — the flight, the window — made it the decade's most audacious film. The film's 2014 release — before the superhero-satire boom — made its timing perfect.",
        "Alejandro G. Iñárritu",
        "Birdman (2014) — the ending",
        119,
        "Watch the film's technical feat — the continuous takes, the backstage corridors, the camera weaving between scenes — and notice how the 'one shot' illusion (shot by Emmanuel Lubezki with digital stitching) makes the chaos feel like a fever: the film's anxiety is in the camera. Then watch the ending, where Riggan's final scene and the ambiguous flight resolve: the film's argument — that art is a battle against your own identity — is in that finale, and the film's 4 Oscars (including Best Picture) made it the year's most honored and most debated film.",
        ["Drama", "Comedy", "2010s", "Hollywood"],
    ),
    _entry(
        "film-inside-out-2015",
        "Inside Out (2015)",
        "Pixar's most profound film — the story of an 11-year-old girl told from inside her head, where the emotions (Joy, Sadness, Anger, Fear, Disgust) run headquarters. The film's thesis — that sadness is essential, not an enemy — is delivered in the film's most devastating scene (Bing Bong's farewell, 'Take her to the moon for me') and won it the Oscar for Best Animated Feature. The film's 'core memories' and its 'train of thought' are the decade's most inventive animation.",
        "Pete Docter",
        "Inside Out (2015) — the Bing Bong scene and the ending",
        95,
        "Watch the Bing Bong scene — the imaginary friend, the rocket, the 'take her to the moon for me' — and notice how the film's most famous moment is built from pure emotional mathematics: the character's sacrifice is the film's thesis made literal, and the scene's place in the 'core memory' structure makes it land like a grenade. Then watch the ending, where Joy finally understands Sadness's role: the film's argument — that a full life needs all its emotions, and that sadness is what connects us — is in that finale, and the film's psychology (it consulted real scientists) made it the most intellectually ambitious family film ever made.",
        ["Animation", "Family", "2010s", "Hollywood"],
    ),
    _entry(
        "film-hereditary-2018",
        "Hereditary (2018)",
        "The horror film that made grief itself the monster — Ari Aster's debut about a family unraveling after the death of its matriarch, with Toni Collette's performance (the most acclaimed in modern horror) at its center. The film's most infamous moment — the telephone pole, the car, the 'we didn't hear anything' — happens in the first act and redefines the film as a study of how families survive (or don't) the unthinkable. The film's miniature-diorama imagery and its final reveal made it the decade's most discussed horror film.",
        "Ari Aster",
        "Hereditary (2018) — the aftermath scene and the ending",
        127,
        "Watch the aftermath sequence — the morning after, the denial, the 'we didn't hear anything' — and notice how Aster films the film's central horror as a family dinner: the grief is unbearable and unspoken, and the film's restraint (the worst thing happens early, quietly) is its power. Then watch the ending, where the film's supernatural logic and the dioramas resolve: the film's argument — that grief is a house you can't leave, and that the family is the horror — is in that finale, and the film's box office and acclaim made it the most important horror film of its decade.",
        ["Horror", "2010s", "Hollywood"],
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
