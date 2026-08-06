#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — the 1960s.

Fourth addition batch (v1.0 content pass toward 400 films): the decade that
broke Hollywood's rules — The Apartment, Spartacus, Peeping Tom, L'Avventura,
Last Year at Marienbad, The Manchurian Candidate, To Kill a Mockingbird,
The Birds, Goldfinger, Mary Poppins, Blow-Up, The Battle of Algiers, Bonnie
and Clyde, Planet of the Apes, Rosemary's Baby, Night of the Living Dead,
and more. Handcrafted teaser + real fact + quality-bar instruction.
Appends only; rejects duplicate ids/names; caps 450 (SCHEMA.md).
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
        "film-the-apartment-1960",
        "The Apartment (1960)",
        "The most cynical comedy ever to win Best Picture — a clerk who lends his apartment to executives for their affairs, until he falls for the elevator girl who's having an affair with his boss. Billy Wilder's film was so frank for 1960 that it needed the Production Code's special approval. The ending — 'Shut up and deal' — is the greatest last line in comedy.",
        "Billy Wilder",
        "The Apartment (1960) — the New Year's Eve scene and the ending",
        125,
        "Watch the New Year's Eve scene — the empty apartment, the cold, the broken mirror — and notice how Wilder films loneliness as architecture: C.C. Baxter's generosity has cost him everything, and the party next door is the sound of the life he's missing. Then watch the ending, where Fran walks in and the deck of cards appears: the film's argument — that love is a gamble and the only honest bet — is in that final line, and the film's balance of tragedy and farce is the finest in Wilder's career.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-spartacus-1960",
        "Spartacus (1960)",
        "The film that broke the Hollywood blacklist — Kirk Douglas insisted the blacklisted Dalton Trumbo get on-screen credit, and the studio era's censorship of names ended with this film. The 'I am Spartacus' scene, where the slaves stand one by one to protect their leader, is the most stirring image of solidarity in cinema, and the film's gladiator epic won 4 Oscars.",
        "Stanley Kubrick",
        "Spartacus (1960) — the 'I am Spartacus' scene",
        120,
        "Watch the 'I am Spartacus' scene — the Romans demanding the leader, the first slave standing, the wave of voices — and notice how the film turns a historical footnote into the cinema's greatest scene of mass defiance: each 'I am Spartacus' is a life offered. Then watch the ending, where the cross and the reunion rewrite history: the film's argument — that the rebellion's spirit outlives its defeat — is in that final image, and the film's scale (8,000 extras) is the last of the great studio epics.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-peeping-tom-1960",
        "Peeping Tom (1960)",
        "The film that destroyed a career and created a genre — Michael Powell's portrait of a photographer who films his victims as he kills them was so reviled on release that it ended one of Britain's greatest directors. The film's argument — that the audience is complicit, watching with the killer — was decades ahead of its time. Now it's recognized as a masterpiece of self-reflexive horror.",
        "Michael Powell",
        "Peeping Tom (1960) — the opening and the ending",
        101,
        "Watch the opening — the POV of the killer filming the first murder, the mirror revealing the camera — and notice how Powell implicates you from the first shot: you're holding the camera, and the film's subject is the pleasure of watching. Then watch the ending, where Mark's final victim is his own mirror: the film's argument — that the camera is a weapon and the audience its accomplice — is delivered in that last frame, and the film's recovery from 'career-ending disgrace' to 'masterpiece' is the great rehabilitation in film history.",
        ["Horror", "Classic", "Hollywood"],
    ),
    _entry(
        "film-lavventura-1960",
        "L'Avventura (1960)",
        "The film that changed cinema's rules — a woman vanishes on a volcanic island, and the search slowly becomes a different story: the man and her best friend falling in love, the missing woman never found. Audiences booed it at Cannes; it won the Jury Prize anyway. The final shot, the camera holding on a couple who've forgotten the woman they came to find, is modern cinema's declaration of independence.",
        "Michelangelo Antonioni",
        "L'Avventura (1960) — the island search and the ending",
        143,
        "Watch the island sequence — the search party, the sea, the silence — and notice how Antonioni films the mystery as atmosphere: the woman disappears and the film refuses to solve it, because the real subject is the emptiness the disappearance reveals. Then watch the ending, where the couple embrace on a hillside while the missing woman is remembered only in a line of dialogue: the film's argument — that modern love is a distraction from modern loneliness — is in that final shot, and the film's patience invented a new kind of movie.",
        ["Drama", "Classic", "Italian"],
    ),
    _entry(
        "film-the-virgin-spring-1960",
        "The Virgin Spring (1960)",
        "Ingmar Bergman's medieval ballad of rape and vengeance — a father discovers his daughter's killers and takes an Old Testament revenge, then doubts himself at the film's end. The final image, a spring rising from the ground where the girl died, is the most discussed miracle in Bergman's career, and the film directly inspired The Last House on the Left.",
        "Ingmar Bergman",
        "The Virgin Spring (1960) — the revenge and the spring",
        89,
        "Watch the revenge sequence — the father, the birch, the slow, deliberate violence — and notice how Bergman films vengeance as liturgy: every gesture is a ritual, and the film's medieval setting makes the horror timeless. Then watch the ending, where the father's confession and the spring's appearance collide: the film's argument — that God's silence and God's presence are the same mystery — is in that water, and the film's Oscar for Best Foreign Language Film made Bergman's name in America.",
        ["Drama", "Classic", "Swedish"],
    ),
    _entry(
        "film-the-hustler-1961",
        "The Hustler (1961)",
        "The pool-hall tragedy that made Paul Newman a star — a young shark who beats the great Minnesota Fats, then loses everything he's won because he can't lose well. Jackie Gleason's Fats, the hushed 'Minnesota Fats' introduction, and the film's final rematch are the definitive movie-pool scenes. The sequel, The Color of Money, reunited Newman with the role 25 years later.",
        "Robert Rossen",
        "The Hustler (1961) — the first match and the ending",
        134,
        "Watch the first match — Fast Eddie against Fats, the $200 game that runs through the night — and notice how Rossen films pool as a duel of souls: the chalk, the silence, the slow orbits are the drama, and Gleason's Fats is unbeatable because he never needs to win. Then watch the ending, where Eddie refuses to take the fix and walks away from the game: the film's argument — that winning isn't the point, pride is — is in that final refusal, and Piper Laurie's Sarah is the film's tragic conscience.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-last-year-at-marienbad-1961",
        "Last Year at Marienbad (1961)",
        "The most mysterious film ever made — a man insists he met a woman at Marienbad last year; she insists she doesn't remember. In a baroque hotel where time and identity dissolve, the film repeats its images like a haunted memory. Written by Alain Robbe-Grillet, it's the purest expression of the French New Wave's avant-garde — a film you don't follow, you surrender to.",
        "Alain Resnais",
        "Last Year at Marienbad (1961) — the first twenty minutes",
        45,
        "Watch the opening — the tracking shots through the hotel's endless corridors, the voiceover repeating 'Once more' — and notice how Resnais builds the film from repetition: the same doors, the same statues, the same phrases, until time itself becomes a place. Then watch the lovers' scenes, where the past is invented in the present: the film's argument — that memory is a performance, not a record — is the whole movie, and its influence on art, music videos, and every 'ambiguous masterpiece' since is immeasurable.",
        ["Drama", "Classic", "French"],
    ),
    _entry(
        "film-west-side-story-1961",
        "West Side Story (1961)",
        "The musical that won 10 Oscars including Best Picture — Shakespeare's Romeo and Juliet as a New York gang war, with Bernstein's score and Sondheim's lyrics. The opening aerial shot of Manhattan and the finger-snapping Jets were filmed on real New York streets, and the film's dances — the gym, the rooftop 'Maria' — are the greatest movie choreography of the studio era.",
        "Robert Wise & Jerome Robbins",
        "West Side Story (1961) — the opening and the gym dance",
        152,
        "Watch the opening — the aerial shot, the finger snaps, the Jets' territorial prowl — and notice how the film turns a city street into a ballet stage: Robbins' choreography makes violence into dance, and the film's color photography (Oscar-winning) is still gorgeous. Then watch the gym dance, where the two gangs meet in slow motion across a basketball court: the film's argument — that love is a truce in a war neither side started — is in that number, and the ending's tragedy lands harder because the dancing was so alive.",
        ["Musical", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-manchurian-candidate-1962",
        "The Manchurian Candidate (1962)",
        "The most paranoid film ever made by a major studio — a Korean War hero programmed to assassinate a presidential candidate, with his own mother (Angela Lansbury, three years older than her on-screen son) pulling the strings. The film was pulled from circulation after JFK's assassination and unseen for 25 years. Frank Sinatra's Raymond Shaw and the film's brainwashing sequence are the Cold War's greatest nightmares.",
        "John Frankenheimer",
        "The Manchurian Candidate (1962) — the brainwashing scene and the ending",
        126,
        "Watch the brainwashing sequence — the garden party on the train, the faces, the 'Raymond Shaw is the kindest, bravest, warmest, most wonderful human being' — and notice how Frankenheimer films the mind-control as a dream gone wrong: the ladies' club matrons are the hypnotists, and the comedy is the horror. Then watch the ending, where the programming meets its final order: the film's argument — that the machinery of power eats its own — is delivered in the film's last shot, and the film's 'forgotten for 25 years' history is its own conspiracy story.",
        ["Thriller", "Classic", "Hollywood"],
    ),
    _entry(
        "film-to-kill-a-mockingbird-1962",
        "To Kill a Mockingbird (1962)",
        "The most loved legal drama in cinema — Gregory Peck's Atticus Finch defending a Black man in the Depression-era South, from Harper Lee's Pulitzer-winning novel. Peck won the Oscar, Robert Duvall made his film debut as Boo Radley (never seen until the end), and the film's ending — Scout seeing the world from Boo's porch — is the most gentle moral lesson in American film.",
        "Robert Mulligan",
        "To Kill a Mockingbird (1962) — the courtroom and the ending",
        129,
        "Watch the courtroom scene — Atticus' closing argument, the 'she did something that in our society is unspeakable' — and notice how the film makes justice personal: the verdict is wrong and the film lets you feel the town's weight on the children watching. Then watch the ending, where Scout stands on Boo Radley's porch and sees her neighborhood through his eyes: the film's argument — that empathy is the whole moral system — is in that final shot, and Elmer Bernstein's score makes it the most tender courtroom film ever made.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-birds-1963",
        "The Birds (1963)",
        "Hitchcock's only supernatural horror — a California town attacked by birds, with no explanation and no ending. The film has almost no score: the 'music' is electronic birdsong, and the film's slow escalation — a single gull, then a swarm — is the most patient horror build in the director's career. Tippi Hedren's attic scene was shot with real birds, and she still carries the memory.",
        "Alfred Hitchcock",
        "The Birds (1963) — the playground attack and the ending",
        119,
        "Watch the playground attack — the crows gathering on the jungle gym, the children running — and notice how Hitchcock builds the film's dread from stillness: the birds don't attack so much as arrive, and the film's famous overhead shot of the town burning is the apocalypse in miniature. Then watch the ending, where the family drives away through a world of silent birds: the film's refusal to explain — no cause, no cure, no resolution — is its power, and the final image is the most ambiguous ending in Hitchcock's career.",
        ["Horror", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-great-escape-1963",
        "The Great Escape (1963)",
        "The prisoner-of-war epic that made 'The Great Escape' a phrase — 76 Allied POWs tunneling out of Stalag Luft III, based on a true story (and a real disaster: 50 of the real escapers were executed). Steve McQueen's motorcycle jump over the barbed wire was done by his stunt double on a specially built bike, and the film's 'cooler king' Hilts is the most iconic POW in cinema.",
        "John Sturges",
        "The Great Escape (1963) — the motorcycle jump and the ending",
        172,
        "Watch the escape sequence — the tunnel, the dirt distribution, the 'X' — and notice how Sturges films the prep as the drama: the movie's tension is in shovels and sawdust, not action, and the escape itself is almost an afterthought. Then watch the ending, where the recaptured officers are marched into the field — the film's refusal to end happily, and McQueen's last leap at the wire: the film's argument — that the escape was worth it even for those who died — is in that final field, and the motorcycle jump remains the most imitated stunt in cinema.",
        ["War", "Classic", "Hollywood"],
    ),
    _entry(
        "film-goldfinger-1964",
        "Goldfinger (1964)",
        "The Bond film that defined Bond — the Aston Martin DB5 with the ejector seat, the laser table, the gold-painted woman, and 'A martini. Shaken, not stirred.' Sean Connery at his peak, Honor Blackman's Pussy Galore, and Shirley Bassey's title song made it the template for every spy film since. It was the first Bond to gross over $100 million worldwide.",
        "Guy Hamilton",
        "Goldfinger (1964) — the laser scene and the pre-title sequence",
        110,
        "Watch the pre-title sequence — Bond in the rubber duck, the diver, the hotel — and notice how the film announces its formula: the cold open, the quip, the girl, and the title song that plays over the credits like a second movie. Then watch the laser scene, where Bond is strapped to a table as the beam approaches: the film's argument — that Bond wins with wit, not weapons — is in that scene, and the film's 'Operation Grand Slam' plan (robbing Fort Knox) remains the genre's most elegant villain plot.",
        ["Action", "Classic", "Hollywood"],
    ),
    _entry(
        "film-mary-poppins-1964",
        "Mary Poppins (1964)",
        "The film that won Julie Andrews her Oscar for her screen debut — a nanny who floats in with an umbrella and teaches a stiff Edwardian family to fly. The film's mix of live action and animation (the 'Jolly Holiday' sequence) was the most complex ever done, and 'Supercalifragilisticexpialidocious' entered the dictionary. Disney spent five years adapting P.L. Travers' books; the film's 13 nominations remain a record for a Disney film.",
        "Robert Stevenson",
        "Mary Poppins (1964) — the chimney sweep dance and the ending",
        139,
        "Watch the 'Jolly Holiday' sequence — Mary and Bert stepping into the animated park — and notice how the film blends the two worlds: the animation was painted to match live-action lighting, and the technology had never been done at this scale. Then watch 'Chim Chim Cher-ee' on the rooftops, where the dancing is pure joy: the film's argument — that wonder is a discipline, not a luxury — is in the ending, where the kite and the laughter show the father finally learning to play.",
        ["Musical", "Family", "Classic", "Hollywood"],
    ),
    _entry(
        "film-a-hard-days-night-1964",
        "A Hard Day's Night (1964)",
        "The film that invented the music video — the Beatles' first movie, a mock-documentary of 36 hours in their lives, directed by Richard Lester with a style (fast cuts, running gags, camera tricks) that MTV would steal wholesale two decades later. The opening chase down the street and the 'Can't Buy Me Love' field sequence are the most influential pop-film moments ever shot.",
        "Richard Lester",
        "A Hard Day's Night (1964) — the opening chase and the field sequence",
        87,
        "Watch the opening — the Fab Four running down the street, the police, the train — and notice how Lester shoots the film as a visual joke machine: the running gag, the fourth-wall looks, the sheer velocity. Then watch the 'Can't Buy Me Love' sequence, where the band escapes into a field and plays among the sheep: the film's argument — that the Beatles' anarchy was a kind of intelligence — is in that freedom, and the film's influence on pop culture is incalculable: it made 'a rock band movie' a genre.",
        ["Musical", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-sound-of-music-1965",
        "The Sound of Music (1965)",
        "The film that made people climb mountains — Julie Andrews' governess and the von Trapp children, and the most beloved musical of all time. Its helicopter shot over the Alps opening, the 'Do-Re-Mi' gazebo dance, and the film's 5 Oscars (including Best Picture) made it the highest-grossing film of the decade. The real von Trapps were musical but not, as the film has it, escaping under a blanket of songs — the reality is even more remarkable.",
        "Robert Wise",
        "The Sound of Music (1965) — the Do-Re-Mi sequence and the ending",
        174,
        "Watch the 'Do-Re-Mi' sequence — the gazebo, the steps, the children learning to sing — and notice how the film uses Salzburg itself as the set: the locations were real, and the songs were shot in single takes with the actual children's voices. Then watch the ending, where the family climbs the mountains to Switzerland: the film's argument — that love and music are the only escape routes — is in that final climb, and the film's box office (it out-grossed Gone with the Wind in its first run) made it the people's picture of the decade.",
        ["Musical", "Classic", "Hollywood"],
    ),
    _entry(
        "film-doctor-zhivago-1965",
        "Doctor Zhivago (1965)",
        "David Lean's romantic epic of the Russian Revolution — Omar Sharif's poet-doctor torn between two women and a country tearing itself apart. The film's 'Lara's Theme' balalaika became one of the most famous melodies in cinema, and the frozen 'ice palace' scenes were shot in Spain with tons of artificial snow. It won 5 Oscars and was the highest-grossing film of its year.",
        "David Lean",
        "Doctor Zhivago (1965) — the ice palace and the ending",
        120,
        "Watch the ice palace sequence — the dacha encased in frozen crystal, the lovers inside — and notice how Lean turns weather into emotion: the frost is the outside world's beauty and cruelty, and the film's wide shots make the characters tiny against history. Then watch the ending, where the film leaps forward to the 1940s and the reunion that comes too late: the film's argument — that the personal is the political, and love is the one thing the revolution can't plan — is in that final walk, and the film's score carries the whole epic's longing.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-shop-on-main-street-1965",
        "The Shop on Main Street (1965)",
        "The Czech masterpiece about the Holocaust that's also a dark comedy — a small-town nobody 'Aryanizes' a Jewish widow's button shop, and the two of them drift into an impossible friendship. The film won the Oscar for Best Foreign Language Film, and its ending — the old woman's gift and the hangman's noose — is one of the most quietly devastating final scenes in cinema.",
        "Ján Kadár & Elmar Klos",
        "The Shop on Main Street (1965) — the ending",
        128,
        "Watch the first hour — Tono's reluctant 'appointment,' the widow's trusting confusion, the buttons — and notice how the film makes the machinery of the Holocaust feel domestic: the horror is in who profits, not who shoots. Then watch the ending, where Tono's attempt to hide the truth collapses: the film's argument — that the worst crimes are committed by ordinary men who 'had no choice' — is in that final scene, and the film's blend of comedy and tragedy makes it the most human Holocaust film ever made.",
        ["Drama", "Classic", "Czech"],
    ),
    _entry(
        "film-blow-up-1966",
        "Blow-Up (1966)",
        "The film that brought the Swinging Sixties to the screen and the first with full-frontal nudity released in the US — a fashion photographer who blows up his photos of a park and discovers a murder hidden in the grain. Michelangelo Antonioni's mystery refuses to solve itself, and the film's ending — a group of mimes playing tennis with an invisible ball — is the most famous non-sequitur in cinema.",
        "Michelangelo Antonioni",
        "Blow-Up (1966) — the photo enlargements and the ending",
        111,
        "Watch the photo sequence — the park, the couple, the enlargements that reveal a body — and notice how Antonioni films perception as obsession: the blow-ups get grainier, the truth gets fainter, and the photographer is left holding images that prove nothing. Then watch the ending, the invisible tennis match: the film's argument — that reality is what we agree to see — is delivered by a mime's imaginary ball, and the film's influence on every 'reality is a construct' thriller since is incalculable.",
        ["Mystery", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-battle-of-algiers-1966",
        "The Battle of Algiers (1966)",
        "The film the Pentagon shows its officers — a documentary-style reconstruction of the Algerian independence struggle, shot on real locations with non-actors, that has been used by armies and revolutionaries alike as a training manual. Its central sequence, the 'three women planting bombs,' cuts between the bombers and their targets with a moral neutrality that still burns. The torture scenes are graphic and unblinking.",
        "Gillo Pontecorvo",
        "The Battle of Algiers (1966) — the bombing sequence",
        120,
        "Watch the bombing sequence — the three women, the baskets, the stadium and the cafés — and notice how Pontecorvo refuses to judge: the bombs are shown from the bombers' eyes and the victims' eyes, and the film's impartiality is its power. Then watch the ending, where the film's structure — a flashback from the last days of the revolution — reveals its method: the film's argument, that insurgency is a chess match of terror and counter-terror, made it required viewing at West Point, the Pentagon, and guerrilla camps alike.",
        ["War", "Classic", "Italian"],
    ),
    _entry(
        "film-whos-afraid-of-virginia-woolf-1966",
        "Who's Afraid of Virginia Woolf? (1966)",
        "The film that broke the Production Code — Elizabeth Taylor (her second Oscar) and Richard Burton as a couple who invite a younger pair over for a night of verbal warfare, in a film whose language and frankness made it the first to carry the new 'suggested for mature audiences' rating. Mike Nichols' directorial debut, and the film's 'Hump the Hostess' party is the most savage hour in American cinema.",
        "Mike Nichols",
        "Who's Afraid of Virginia Woolf? (1966) — the party and the ending",
        131,
        "Watch the party sequence — George and Martha's verbal duel, the guests' slow realization they're witnesses to a marriage's autopsy — and notice how Nichols films the four walls closing in: the film was shot on a set with a ceiling, and the claustrophobia is the point. Then watch the ending, where the invented son is 'killed' and the games finally stop: the film's argument — that we marry our fantasies and then must bury them — is in that quiet final scene, and Taylor and Burton's performances are the greatest married-combat in cinema.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-bonnie-and-clyde-1967",
        "Bonnie and Clyde (1967)",
        "The film that ended old Hollywood — its glamorous killers, its pop-music violence, and its slow-motion ambush finale scandalized critics and electrified audiences, launching the 'New Hollywood' era. Warren Beatty produced and starred, Faye Dunaway's beret became a fashion statement, and the film's score (the banjo 'Foggy Mountain Breakdown') turned a crime spree into a folk song.",
        "Arthur Penn",
        "Bonnie and Clyde (1967) — the ending ambush",
        111,
        "Watch the ending — the ambush, the birds scattering, the slow-motion ballet of bullets — and notice how Penn films the death as both ecstasy and horror: the slow motion made the violence feel like liberation and execution at once, and the final close-up of Bonnie's eyes is the New Hollywood's founding image. Then watch the earlier scenes, where the gang's comedy (the bank teller photo, the 'we rob banks' banter) makes the ending unbearable: the film's argument — that fame and violence are the same American dream — is in that last sequence.",
        ["Crime", "Classic", "Hollywood"],
    ),
    _entry(
        "film-cool-hand-luke-1967",
        "Cool Hand Luke (1967)",
        "Paul Newman's prisoner who refuses to break — the film with the most quoted line in American cinema: 'What we've got here is failure to communicate.' The egg-eating contest (50 eggs), the 'I can eat fifty eggs' bet, and the ending — Luke shot down in a church, his smile winning even in death — made it the counterculture's favorite film of 1967.",
        "Stuart Rosenberg",
        "Cool Hand Luke (1967) — the egg scene and the ending",
        126,
        "Watch the egg-eating scene — Luke vs. the bet, the crowd chanting, the slow collapse — and notice how the film builds the film's central myth: Luke's defiance is performance, and the chain gang's worship is the audience's. Then watch the ending, where Luke is cornered in the church and emerges smiling: the film's argument — that the system can kill the man but never the legend — is in that final image, and the film's Christ parallels (the night he 'died' and rose) made it the decade's most-loved allegory.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-in-the-heat-of-the-night-1967",
        "In the Heat of the Night (1967)",
        "The film that made the 'slap heard round the world' — Sidney Poitier's Black detective slapping a white plantation owner who slaps him first. It won 5 Oscars including Best Picture, and 'They call me Mr. Tibbs!' became one of cinema's most quoted lines. The Mississippi murder mystery made Poitier the biggest star in America, and the film's racism is shown with an honesty rare for 1967.",
        "Norman Jewison",
        "In the Heat of the Night (1967) — the slap scene and the ending",
        109,
        "Watch the slap scene — the plantation, the white man's hand, Virgil Tibbs' response — and notice how the film lets the moment land without music or commentary: the slap was filmed in one take and the audience's gasp was recorded live at previews. Then watch the ending, where Tibbs solves the case and boards the train: the film's argument — that the South can't be saved by its own myths — is in that departure, and the film's theme song, Ray Charles' 'In the Heat of the Night,' won the Oscar.",
        ["Crime", "Classic", "Hollywood"],
    ),
    _entry(
        "film-planet-of-the-apes-1968",
        "Planet of the Apes (1968)",
        "The twist ending that launched a franchise — Charlton Heston's astronaut discovers he's been on Earth all along, and the Statue of Liberty's arm in the sand delivers the most famous final image in sci-fi. Rod Serling (of The Twilight Zone) co-wrote, and John Chambers' ape makeup won a special Oscar. 'You maniacs! You blew it up!' is the decade's most quoted curse.",
        "Franklin J. Schaffner",
        "Planet of the Apes (1968) — the courtroom and the ending",
        112,
        "Watch the courtroom scene — Taylor on trial, the apes' society, the 'human zoo' — and notice how the film's makeup lets the actors act: the ape society is a complete political allegory (science vs. faith, the military, the press), and the satire is the film's engine. Then watch the ending, the forbidden zone and the statue: the film's argument — that humanity's destiny is written in its own weapons — is delivered in that final shot, and the film's 'damn you all to hell' remains the angriest last line in sci-fi.",
        ["Sci-Fi", "Classic", "Hollywood"],
    ),
    _entry(
        "film-rosemarys-baby-1968",
        "Rosemary's Baby (1968)",
        "The film that made paranoia a genre — a young wife whose neighbors are witches, whose husband made a deal, and whose baby is the Antichrist. Roman Polanski adapted Ira Levin's novel with a realism that never winks: the horror is in Mia Farrow's isolated, gaslit wife and the film's refusal to let her be believed. Ruth Gordon won the Oscar, and the film's ending — 'Hail Satan' — is the most unsettling smile in horror.",
        "Roman Polanski",
        "Rosemary's Baby (1968) — the neighbors and the ending",
        136,
        "Watch the first act — the Castevets' arrival, the 'old-fashioned' charm, the seduction — and notice how Polanski films the cult as domesticity: the evil is baked into a Manhattan apartment's neighborly chat, and Rosemary's gaslighting is the horror. Then watch the ending, where Rosemary looks into the bassinet: the film's argument — that motherhood can be a trap built by everyone around you — is in that final 'Hail Satan,' and the film's refusal to rescue its heroine made it the most disturbing mainstream film of its decade.",
        ["Horror", "Classic", "Hollywood"],
    ),
    _entry(
        "film-night-of-the-living-dead-1968",
        "Night of the Living Dead (1968)",
        "The film that invented the modern zombie — made for $114,000 by a Pittsburgh ad man (George Romero) and his friends, it became one of the most profitable and most imitated films in history. Its cannibal ghouls, its gore, and its ending — the Black hero shot by the white posse — scandalized and electrified audiences. The film fell into public domain, which is why it's been everywhere, forever.",
        "George A. Romero",
        "Night of the Living Dead (1968) — the ending",
        96,
        "Watch the first half hour — the cemetery, the ghoul, the farmhouse siege — and notice how Romero films the horror with documentary flatness: the news reports, the TV bulletins, the matter-of-fact gore make it feel like coverage of a real catastrophe. Then watch the ending, where Ben survives the night and is shot by the rescue party: the film's argument — that the real monsters are the ones with guns — is in that final image, and the film's radical ending (a Black man killed by 'the good guys') made it the most subversive horror film of the century.",
        ["Horror", "Classic", "Hollywood"],
    ),
    _entry(
        "film-butch-cassidy-and-the-sundance-kid-1969",
        "Butch Cassidy and the Sundance Kid (1969)",
        "The western as buddy comedy — Paul Newman and Robert Redford as the outlaws who can't stop being charming, even when the super-posse is closing in. William Goldman's script ('Who are those guys?'), the bicycle scene set to 'Raindrops Keep Fallin' on My Head,' and the freeze-frame ending made it one of the most influential films of the New Hollywood. It won 4 Oscars.",
        "George Roy Hill",
        "Butch Cassidy and the Sundance Kid (1969) — the ending freeze-frame",
        110,
        "Watch the bicycle scene — Butch and Etta on the bike, 'Raindrops Keep Fallin' on My Head,' the golden light — and notice how the film smuggles a love song into a western: the movie's tone is its revolution, and the humor is the armor. Then watch the ending, where the two men charge the entire Bolivian army and the film freezes mid-jump: the film's argument — that legends are made by refusing to stop being fun — is in that freeze-frame, and the film's buddy chemistry invented a genre.",
        ["Western", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-wild-bunch-1969",
        "The Wild Bunch (1969)",
        "The film that ended the western's innocence — Sam Peckinpah's outlaws in 1913 Mexico, and the most violent shootout in cinema history (the final massacre runs in slow-motion ballets). The film's violence was denounced and defended, its editing (a technique called 'the Peckinpah cut') changed action cinema, and its theme — that the old outlaws are obsolete in a modern world — made it the last great statement of the genre's tragic mode.",
        "Sam Peckinpah",
        "The Wild Bunch (1969) — the opening and the final massacre",
        145,
        "Watch the opening — the children watching the scorpions, the bank robbery, the ambush — and notice how Peckinpah cross-cuts the innocent children with the massacre: the film announces its subject — the cruelty of watching — in the first ten minutes. Then watch the final shootout, where the bunch walks into the compound to free their man: the film's argument — that honor is the only thing left when the world moves on — is in that slow-motion ballet, and the film's editing (often 8 cuts per second) rewired how violence is filmed.",
        ["Western", "Classic", "Hollywood"],
    ),
    _entry(
        "film-midnight-cowboy-1969",
        "Midnight Cowboy (1969)",
        "The only X-rated film ever to win Best Picture — a Texas dreamer (Jon Voight) who comes to New York to be a hustler and finds only a sickly con man (Dustin Hoffman) to share his misery. The film's 'I'm walkin' here!' — Hoffman's ad-lib at a real cab — is one of cinema's most quoted moments, and the ending's bus ride to Florida is a tragedy wearing a buddy-movie coat.",
        "John Schlesinger",
        "Midnight Cowboy (1969) — the 'I'm walkin' here' scene and the ending",
        113,
        "Watch the 'I'm walkin' here!' scene — Ratso and Joe crossing the street, the cab, the slap — and notice how the film's New York is a documentary of desperation: the locations are real, the poverty is unglamorous, and the friendship is the only warmth. Then watch the ending, where Joe sells his blood to buy Ratso's bus ticket south: the film's argument — that love is the only currency the city can't counterfeit — is in that final bus ride, and the film's X rating (for language and frankness) was a landmark that forced the ratings board to evolve.",
        ["Drama", "Classic", "Hollywood"],
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
