#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — 1920s–1940s (golden age + noir).

Second addition batch (v1.0 content pass toward 400 films): silent-era
expressionism, screwball, wartime Hollywood, and the birth of film noir —
The Cabinet of Dr. Caligari, Nosferatu, Potemkin, Keaton/Chaplin, M,
Frankenstein, King Kong, Capra, Hitchcock's first masterpieces, the
1940s-noir core (Laura, Detour, Out of the Past). Handcrafted teaser
(makes you WANT to watch) + real fact + quality-bar instruction.
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
        "film-cabinet-of-dr-caligari-1920",
        "The Cabinet of Dr. Caligari (1920)",
        "The film that invented the horror movie's look — painted shadows, crooked doors, and a set where nothing is straight, because a madman is telling the story. It was nearly lost after its studio went bankrupt, and its twist ending — the first in cinema — still lands a century later.",
        "Robert Wiene",
        "The Cabinet of Dr. Caligari (1920) — the first half hour",
        60,
        "Watch the opening — the fair, the sleepwalker Cesare, the first 'wake up' — and notice how the tilted sets and painted shadows make the world itself unreliable: nothing is straight because the story is a confession. Then watch the ending, the frame story's twist, and notice how the reveal rewrites every image you trusted: the film's madness is in the architecture.",
        ["Horror", "Classic", "German"],
    ),
    _entry(
        "film-nosferatu-1922",
        "Nosferatu (1922)",
        "The first vampire movie — an unauthorized Dracula so scary its studio was sued into bankruptcy and ordered to destroy every print. A few survived. Max Schreck's rat-faced Count Orlok, with ears that could hear your heartbeat, remains the scariest vampire ever put on film.",
        "F.W. Murnau",
        "Nosferatu (1922) — the castle arrival and the ending",
        90,
        "Watch Hutter's arrival at Orlok's castle — the coachman who is also the count, the signature of the contract — and notice how Murnau films evil as stillness: Orlok barely moves, which is why he terrifies. Then watch the ending, where the vampire's weakness becomes the film's final image: the sunrise, the maiden, and the dissolve that made 'nosferatu' a synonym for nightmare.",
        ["Horror", "Classic", "German"],
    ),
    _entry(
        "film-battleship-potemkin-1925",
        "Battleship Potemkin (1925)",
        "The film that taught directors how to edit — its Odessa Steps sequence, a massacre cut into accelerating chaos, is the most studied minute in cinema history. Eisenstein shot it on a real battleship with a real crew, and the film was banned in several countries for being too good at inciting revolution.",
        "Sergei Eisenstein",
        "Battleship Potemkin (1925) — the Odessa Steps sequence",
        45,
        "Watch the Odessa Steps sequence — the nurse, the baby carriage, the pram bouncing down the stairs — and notice how Eisenstein builds panic from editing alone: the same staircase shot from new angles, each cut making the descent longer and the danger closer. The sequence is the textbook for every chase, siege, and riot scene made since.",
        ["Drama", "Classic", "Soviet"],
    ),
    _entry(
        "film-the-gold-rush-1925",
        "The Gold Rush (1925)",
        "Chaplin called this his masterpiece — the film where the Tramp eats his own shoe for dinner and turns bread rolls into dancing feet. He built a whole mountain town in a studio because a real blizzard wrecked his location shoot, and the cabin-teetering-over-the-cliff scene is pure genius.",
        "Charles Chaplin",
        "The Gold Rush (1925) — the shoe dinner and the cabin scene",
        95,
        "Watch the shoe-eating scene — the Tramp boils his boot and slurps the laces like spaghetti — and notice how Chaplin makes poverty hilarious and heartbreaking in the same shot: the dinner table manners are the joke, the hunger is the truth. Then watch the cabin teetering on the cliff edge, where the whole cast balancing keeps it level: pure slapstick physics from the greatest comedian who ever lived.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-general-1926",
        "The General (1926)",
        "Buster Keaton's Civil War chase film — he did every stunt himself, including dropping a real locomotive through a real bridge. It was a flop that ruined his independence, then decades later was crowned one of the greatest films ever made. Keaton never smiled on camera; audiences have been smiling for him since.",
        "Buster Keaton",
        "The General (1926) — the bridge collapse and the chase",
        75,
        "Watch the pursuit — Johnny's engine chasing the stolen General, the Union soldiers dropping rails behind them — and notice how Keaton builds comedy from machinery: every lever, coal shovel, and misplaced rail is a gag, and the geography is the joke. Then watch the bridge collapse, a real locomotive falling into a real river, and the pursuit's reversal: the film's genius is that the hero wins by being exactly as clever as the equipment he's given.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-sunrise-1927",
        "Sunrise: A Song of Two Humans (1927)",
        "The first film with synchronized music and sound effects, and the first to win the Academy Award for Unique and Artistic Picture — the 'film of films,' critics called it. F.W. Murnau, lured from Germany with an unheard-of contract, filmed a husband's temptation and redemption with images so beautiful the story barely needs to be told.",
        "F.W. Murnau",
        "Sunrise (1927) — the city sequence and the ending",
        90,
        "Watch the 'temptress' sequence — the city woman, the marsh, the planned drowning — and notice how Murnau shoots desire and guilt as weather: the fog, the reeds, the moonlight do the acting. Then watch the trolley ride into the city, where the film's visual effects (superimpositions, a moving camera) turn a streetcar into a dream: the film's argument — that love can be almost destroyed and still saved — is in the final image of the sunrise.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-city-lights-1931",
        "City Lights (1931)",
        "The last great silent film, made three years after sound arrived — Chaplin refused to hear the Tramp speak, and the gamble made it one of his biggest hits. The blind flower girl who mistakes the Tramp for a millionaire, and the final scene — the greatest ending in silent cinema, by Chaplin's own admission.",
        "Charles Chaplin",
        "City Lights (1931) — the opening and the final scene",
        87,
        "Watch the opening — the statue unveiling, the Tramp asleep in its lap, the derisive trumpet — and notice how Chaplin builds the film from small humiliations: the comedy is the Tramp's dignity under attack. Then watch the ending, where the flower girl's sight returns and her hand recognizes his: Chaplin said the look in his eyes was the best thing he ever did, and the close-up of the Tramp's face — hope and terror in one expression — is the most moving shot in his career.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-m-1931",
        "M (1931)",
        "Fritz Lang's first sound film — a child murderer in Berlin, a city that hunts him, and a whistle that announces his arrival: the tune is 'In the Hall of the Mountain King,' and Peter Lorre whistled it himself on set. The film's final scene — a kangaroo court of criminals trying a monster — is the most uncomfortable moral trial in cinema.",
        "Fritz Lang",
        "M (1931) — the balloon scene and the trial",
        110,
        "Watch the opening — the children's song, the balloon, the mother's call at the empty staircase — and notice how Lang makes the horror mostly off-screen: you hear the murderer before you see him, and the whistle is the signature. Then watch the trial, where the criminals judge the child-killer: the film's argument — that a society that hunts with pitchforks becomes the monster it fears — is delivered in Peter Lorre's confession, the greatest monologue of early sound cinema.",
        ["Thriller", "Classic", "German"],
    ),
    _entry(
        "film-frankenstein-1931",
        "Frankenstein (1931)",
        "The monster who defined monsters — Boris Karloff's flat head, neck bolts, and slow, tragic walk were all director James Whale's inventions, and the film's lightning-laboratory 'It's alive!' is the most imitated line in horror. Whale made the creature sympathetic enough that the mob at the end feels like the real monster.",
        "James Whale",
        "Frankenstein (1931) — the creation scene and the ending",
        70,
        "Watch the creation scene — the lightning, the operating table, the hand reaching up — and notice how Whale's staging (the high ceilings, the shadows, the laboratory gears) makes science feel like a cathedral of dread. Then watch the scene by the lake, where the creature meets the little girl and the flowers float: the film's tragedy is in that moment — the monster who only wants a friend — and the ending's mob carries the real guilt.",
        ["Horror", "Classic", "Hollywood"],
    ),
    _entry(
        "film-king-kong-1933",
        "King Kong (1933)",
        "The original monster movie — an 18-inch stop-motion ape that became a 50-foot legend. Willis O'Brien's animation was so ahead of its time that audiences genuinely believed the Kong footage was real, and the Empire State Building finale has been copied by every kaiju, ape, and alien since. The film was banned in some countries for its 'excessive' horror.",
        "Merian C. Cooper & Ernest B. Schoedsack",
        "King Kong (1933) — the first island encounter and the ending",
        100,
        "Watch Kong's first reveal — the jungle, the natives, the giant hand through the gate — and notice how the film teases the monster: you hear him, feel the tremors, see his shadow for a full reel before he appears. Then watch the Empire State Building finale, where the stop-motion Kong swats at biplanes: the film's argument — that beauty kills the beast — is in the last line, and the animation still holds up because it was built on weight, not speed.",
        ["Adventure", "Classic", "Hollywood"],
    ),
    _entry(
        "film-it-happened-one-night-1934",
        "It Happened One Night (1934)",
        "The first film ever to sweep the five major Oscars — and it started as a 'lesser' Columbia picture nobody wanted. Claudette Colbert's hitchhiking leg flash and Clark Gable's 'walls of Jericho' blanket made the film a phenomenon: sales of men's undershirts collapsed because Gable went without one.",
        "Frank Capra",
        "It Happened One Night (1934) — the hitchhiking scene and the ending",
        105,
        "Watch the hitchhiking scene — the leg, the car that stops, the 'how did you do that?' — and notice how Capra builds the film's chemistry from bickering: the war between the heiress and the reporter IS the romance. Then watch the 'Walls of Jericho' sequence, the blanket strung between two beds, and the ending's trumpet call: the film's argument — that love is a truce between two stubborn people — made it the template for every romantic comedy since.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-39-steps-1935",
        "The 39 Steps (1935)",
        "Hitchcock's first great chase film — a man on the run with a murder charge, handcuffed to a woman he doesn't trust, and a secret that's never what it seems. It made Hitchcock's name internationally, and its 'wrong man' formula would power his entire career. The film's ending, in a music hall, is the prototype for every Hitchcock reveal.",
        "Alfred Hitchcock",
        "The 39 Steps (1935) — the handcuff escape and the finale",
        85,
        "Watch the escape from the train — the handcuffed couple, the bedroom door, the 'I'm married' cover story — and notice how Hitchcock turns a constraint into comedy: the cuffs make every scene a negotiation. Then watch the finale at the Palladium, where the man in the audience is the one the hero's been chasing: the film's twist — that the spy was hiding in plain sight as a performer — is the template for a century of reveals.",
        ["Thriller", "Classic", "Hollywood"],
    ),
    _entry(
        "film-top-hat-1935",
        "Top Hat (1935)",
        "The film that made Fred Astaire and Ginger Rogers the standard for movie dancing — and the one that gave us 'Cheek to Cheek,' which Astaire later called the best song he ever danced to. The feather dress nearly ruined the take (the feathers flew up his nose), and Rogers — who 'did everything he did, backwards and in high heels' — was dancing on $5,000 worth of it.",
        "Mark Sandrich",
        "Top Hat (1935) — the Cheek to Cheek number",
        100,
        "Watch 'Cheek to Cheek' — the white feathers, the slow circling, the camera barely moving — and notice what makes Astaire and Rogers unbeatable: the dance tells the whole love story, and the steps are the dialogue. Then watch 'Top Hat, White Tie and Tails,' where Astaire's tap solo uses his cane like a weapon: the film's elegance is its argument — that style is substance, and that a man in a top hat can win any war with his feet.",
        ["Musical", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-wizard-of-oz-1939",
        "The Wizard of Oz (1939)",
        "The film that turned sepia into color on a farm in Kansas — the most famous transition in cinema. Judy Garland was 16 and paid $500 a week; 'Over the Rainbow' was nearly cut for slowing the film; and the Wicked Witch's exit was real fire: Margaret Hamilton was badly burned during filming. The ruby slippers sold at auction for $666,000.",
        "Victor Fleming",
        "The Wizard of Oz (1939) — the tornado and the yellow brick road",
        100,
        "Watch the transition — the sepia farm, the tornado, the door opening into color — and notice how the film makes the fantasy physical: Munchkinland was built in full scale, and the camera movement sells the wonder. Then watch 'Over the Rainbow,' sung before the journey: the song's melancholy is the film's secret engine — Dorothy is already homesick before she leaves — and the ending's 'there's no place like home' only works because of that sadness.",
        ["Fantasy", "Musical", "Classic", "Hollywood"],
    ),
    _entry(
        "film-gone-with-the-wind-1939",
        "Gone with the Wind (1939)",
        "The longest Hollywood film of its era and the biggest box-office hit in history (adjusted for inflation, it still is). It made Hattie McDaniel the first Black actor to win an Oscar — she was barred from the Atlanta premiere. The burning of Atlanta was real: they set fire to the standing sets of other films, including King Kong's gates.",
        "Victor Fleming",
        "Gone with the Wind (1939) — the burning of Atlanta and the ending",
        120,
        "Watch the burning of Atlanta sequence — the wounded in the streets, the hospital, the wagon through the flames — and notice how the film spends its famous budget: real fires, real sets, and the skyline collapse. Then watch the ending, Scarlett's 'I'll think about it tomorrow': the film's argument — that survival is a kind of stubbornness — is in that line, and the last shot of her silhouette against the sky is the most quoted image of the Hollywood studio system.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-mr-smith-goes-to-washington-1939",
        "Mr. Smith Goes to Washington (1939)",
        "James Stewart's idealistic freshman senator against a corrupt machine — the film was banned in several countries and booed by Washington insiders at its premiere, which tells you how accurate it felt. The filibuster scene, Stewart hoarse and rambling until he collapses, is the greatest political speech in American cinema.",
        "Frank Capra",
        "Mr. Smith Goes to Washington (1939) — the filibuster scene",
        129,
        "Watch the filibuster — Jefferson Smith standing for hours, reading the Declaration, being called every liar in the book — and notice how Capra films exhaustion: the sweat, the voice going, the clock. The scene is built from Stewart's real stamina — he nearly passed out — and the film's argument, that one honest man can outlast a machine, is delivered standing up. The ending, with the revelation and the collapse, is Capra's faith made literal.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-stagecoach-1939",
        "Stagecoach (1939)",
        "The western that made John Wayne a star and turned Monument Valley into cinema's most famous backdrop. John Ford cast Wayne — who'd been toiling in B-movies — as the Ringo Kid, and the stagecoach's journey through Apache territory redefined the genre overnight. Orson Welles said he watched it forty times before making Citizen Kane.",
        "John Ford",
        "Stagecoach (1939) — the first view of Monument Valley and the chase",
        96,
        "Watch the opening tracking shot — the Monument Valley desert, the stagecoach, Wayne's first close-up with his rifle — and notice how Ford introduces the Ringo Kid: the camera moves toward him, a star being born in one dolly shot. Then watch the chase, where Ford cross-cuts the galloping Apaches with the passengers inside: the film's argument — that a society of strangers can become a family in danger — is staged in that coach, and the ending's shootout is the payoff.",
        ["Western", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-rules-of-the-game-1939",
        "The Rules of the Game (1939)",
        "Jean Renoir's comedy of manners about a weekend house party where everyone lies about love — it was a scandal, banned, cut, and nearly lost forever, then restored to become one of the most influential films ever made. The rabbit-hunt sequence is the film's thesis: the aristocrats hunt animals with the same casual violence they use on each other.",
        "Jean Renoir",
        "The Rules of the Game (1939) — the party and the rabbit hunt",
        105,
        "Watch the party sequence — the dancing, the chases through the chateau, the guests colliding — and notice how Renoir's deep-focus camera holds everything in frame: the chaos is the comedy, and the overlapping couples are the rules of the game. Then watch the rabbit hunt, where the guns are fired at animals with champagne-stained hands: the film's argument — that this society is already dead, it just hasn't noticed — is in that sequence, and the ending's shooting is the game's final rule.",
        ["Comedy", "Classic", "French"],
    ),
    _entry(
        "film-ninotchka-1939",
        "Ninotchka (1939)",
        "The film sold as 'Garbo laughs!' — the great tragic star's first comedy, a Soviet envoy in Paris who falls for champagne, a hat, and a man. Ernst Lubitsch directed, and the film's lightness was a pointed rebuke to the Nazi-Soviet pact that had just been signed. The 'Lubitsch touch' is on every frame.",
        "Ernst Lubitsch",
        "Ninotchka (1939) — the hat scene and the ending",
        110,
        "Watch the hat scene — Ninotchka's first evening in Paris, the hat, the 'why do you have to make fun of women?' — and notice how Lubitsch does comedy with a raised eyebrow: the political commissar's surrender is staged as a hat, and the revolution falls for a bonnet. Then watch the ending, where the lovers are reunited in a Constantinople café: the film's argument — that joy is the revolution — is delivered in Garbo's smile, the one the whole film was built to earn.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-maltese-falcon-1941",
        "The Maltese Falcon (1941)",
        "John Huston's directorial debut and the film that defined film noir — a detective, a fat man, a liar, and a statue everyone's dying for. It was the third adaptation of Dashiell Hammett's novel in ten years, and it got it right. The falcon, it turns out, is a fake — and 'the stuff that dreams are made of' is borrowed from The Tempest.",
        "John Huston",
        "The Maltese Falcon (1941) — the reveal and the ending",
        100,
        "Watch the ending — the falcon weighed, the lead revealed, the killers turned over — and notice how Huston stages the film's great deflation: everyone has killed for a fake, and Sam Spade's shrug is the whole genre. Then watch the final scene, where Spade sends Brigid away and the camera holds on the falcon: the film's argument — that the quest matters more than the prize — is in that last shot, and 'the stuff that dreams are made of' is the noir worldview in one line.",
        ["Noir", "Classic", "Hollywood"],
    ),
    _entry(
        "film-sullivans-travels-1941",
        "Sullivan's Travels (1941)",
        "Preston Sturges' comedy about a director who wants to make a serious film about suffering — until he experiences real suffering and learns that laughter is the best gift you can give the poor. It's the only Hollywood film that defends slapstick as a moral act, and the chain-gang movie-theater scene is its proof.",
        "Preston Sturges",
        "Sullivan's Travels (1941) — the chain gang and the ending",
        90,
        "Watch the film's second half — Sullivan's amnesia, the chain gang, the bread line — and notice how Sturges flips his own comedy: the jokes stop when the suffering starts, and the tone change is the point. Then watch the chain-gang movie night, where the prisoners howl with laughter at a cartoon: the film's argument — that comedy is not escape but medicine — is delivered in that darkened room, and the ending's choice to make people laugh is Sturges' manifesto.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-to-be-or-not-to-be-1942",
        "To Be or Not to Be (1942)",
        "The boldest comedy ever made during wartime — a Polish theater troupe outwits the Gestapo, and the Nazis are played for fools while their victims laugh at the edge of death. Made while the Holocaust was underway, it was called tasteless and then praised as the bravest film of its year. Jack Benny's 'So they call me Concentration Camp Ehrhardt?' is the film in one line.",
        "Ernst Lubitsch",
        "To Be or Not to Be (1942) — the Hamlet soliloquy and the ending",
        99,
        "Watch the opening — the Hamlet soliloquy interrupted by an audience member, the 'my name is Joseph Tura' — and notice how Lubitsch builds the film on theater tricks: the troupe's acting skills are both the comedy and the plot. Then watch the finale, where the actors impersonate the Gestapo and the real Gestapo arrives: the film's argument — that performance is a weapon against tyranny — is delivered as a farce, and the ending's curtain call makes the audience part of the troupe.",
        ["Comedy", "Classic", "Hollywood"],
    ),
    _entry(
        "film-shadow-of-a-doubt-1943",
        "Shadow of a Doubt (1943)",
        "Hitchcock's own favorite of his films — a small-town girl who adores her uncle, until she realizes he's the 'Merry Widow Murderer.' The 'Merry Widow' waltz is the film's secret language: every time the villain whistles it, a woman is about to die. The ending's train-whistle motif is the film's darkest joke.",
        "Alfred Hitchcock",
        "Shadow of a Doubt (1943) — the ring scene and the ending",
        108,
        "Watch the 'Merry Widow' waltz scenes — Uncle Charlie humming the tune, the ring engraved inside the band — and notice how Hitchcock makes music the menace: the waltz is the villain's signature, and every whistle is a death sentence. Then watch the ending, where the town celebrates the man who died as a hero: the film's argument — that evil can wear a beloved face and be buried with honors — is the most subversive ending in classic Hollywood.",
        ["Thriller", "Classic", "Hollywood"],
    ),
    _entry(
        "film-laura-1944",
        "Laura (1944)",
        "The noir told by a man in love with a corpse — a detective investigating a murder falls for the dead woman's portrait, and then she walks in alive. Otto Preminger's elegant thriller made Clifton Webb a star, and the painting of Laura became so iconic it was auctioned for real. The film's twist is hidden in plain sight in the very first scene.",
        "Otto Preminger",
        "Laura (1944) — the portrait scene and the reveal",
        88,
        "Watch the opening — the voiceover, the portrait, the 'she was beautiful' — and notice how Preminger films obsession: the camera keeps returning to the painting, and the dead woman becomes more present than the living. Then watch the reveal — Laura walking into her own funeral investigation — and the film's central question: is the killer the one who couldn't let her go? The ending, with the detective's confession, is the film's final stroke of elegance.",
        ["Noir", "Classic", "Hollywood"],
    ),
    _entry(
        "film-meet-me-in-st-louis-1944",
        "Meet Me in St. Louis (1944)",
        "The film that gave us 'Have Yourself a Merry Little Christmas' — Judy Garland singing to her little sister about a Christmas that might not come, in a song that was rewritten because it was too sad. Vincente Minnelli's Technicolor valentine to turn-of-the-century St. Louis features the most charming Halloween scene in cinema.",
        "Vincente Minnelli",
        "Meet Me in St. Louis (1944) — the Christmas song and the ending",
        113,
        "Watch the Christmas Eve scene — Esther singing 'Have Yourself a Merry Little Christmas' to Tootie, the tears, the promise — and notice how Minnelli films the song as a small family tragedy: the lyrics were originally 'it may be your last,' and Judy's performance carries the melancholy under the cheer. Then watch the ending, the family deciding not to move after all: the film's argument — that home is the people, not the place — is in that reversal, and the final shot of the family together is the war-era audience's dream.",
        ["Musical", "Classic", "Hollywood"],
    ),
    _entry(
        "film-detour-1945",
        "Detour (1945)",
        "The cheapest great film ever made — shot in six days for about $30,000, with two stars and a lot of hitchhiking. A pianist, a dead man whose identity he steals, and a woman who knows the truth. The film's voiceover — 'Fate, or some mysterious force, can put the finger on you' — is the most fatalistic speech in noir.",
        "Edgar G. Ulmer",
        "Detour (1945) — the voiceover and the ending",
        68,
        "Watch the opening — the hitchhiking, the rain, the 'fate can put the finger on you' voiceover — and notice how Ulmer builds an entire world from two faces and a car: the budget forced him to film despair, and despair never looked cheaper or more real. Then watch the ending, where the film's hero is trapped by his own lie: the film's argument — that we are all on a detour from the lives we meant to live — is delivered in the final shot, and it's the purest expression of noir pessimism ever put on film.",
        ["Noir", "Classic", "Hollywood"],
    ),
    _entry(
        "film-notorious-1946",
        "Notorious (1946)",
        "The film where Hitchcock made the longest kiss in cinema history — by breaking it into 3-second takes and splicing them together, because the censors had a 3-second rule. Ingrid Bergman's spy must marry the Nazi, and Cary Grant has to watch. The film's descent into the wine cellar is the most elegant suspense sequence Hitchcock ever staged.",
        "Alfred Hitchcock",
        "Notorious (1946) — the wine cellar scene",
        101,
        "Watch the wine cellar sequence — Alicia and Devlin searching for the 'coffee,' the party upstairs, the cork slipping — and notice how Hitchcock builds suspense from the most ordinary objects: the champagne, the key, the bottle of sand. The scene is a masterclass in 'what if the audience knows more than the characters,' and the film's romance is built on the most adult premise in 1940s cinema: a woman who must betray her husband for the man she loves.",
        ["Thriller", "Classic", "Hollywood"],
    ),
    _entry(
        "film-its-a-wonderful-life-1946",
        "It's a Wonderful Life (1946)",
        "The Christmas film that flopped so hard it bankrupted its studio — then became a TV perennial and one of the most beloved films ever made. Jimmy Stewart based his performance on his real war trauma, and the film's 'you've been given a great gift: a chance to see what the world would be like without you' is the most hopeful premise in cinema.",
        "Frank Capra",
        "It's a Wonderful Life (1946) — the bridge scene and the ending",
        130,
        "Watch the 'without you' sequence — George's guardian angel showing him Bedford Falls as Pottersville — and notice how Capra films the town's darkness: the same streets, the same people, all hollowed out. Then watch the ending, where the town pours its savings into the basket and the bell rings: the film's argument — that a man's life is measured in the lives he touched — is delivered with the most unashamed sentimentality ever put on film, and it works because Stewart's despair was real.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-the-best-years-of-our-lives-1946",
        "The Best Years of Our Lives (1946)",
        "Three veterans come home from the war to a country that's moved on — filmed with a real double-amputee (Harold Russell, who won TWO Oscars) and on real locations, not sets. It was the biggest box-office hit of the decade, and its 'welcome home' scene, where the flyer stares at the junked planes in a boneyard, is one of the most honest images in American film.",
        "William Wyler",
        "The Best Years of Our Lives (1946) — the aircraft boneyard scene",
        170,
        "Watch the aircraft boneyard — Fred the bombardier walking through the rows of surplus planes, the wind, the silence — and notice how Wyler films the war's cost without a single explosion: the machinery of death sits rusting, and the veteran's face says everything. Then watch the ending, where the three men's fates resolve — the amputee's wedding, the pilot's job: the film's argument, that coming home is its own battlefield, made it the film veterans trusted most.",
        ["Drama", "Classic", "Hollywood"],
    ),
    _entry(
        "film-out-of-the-past-1947",
        "Out of the Past (1947)",
        "The definitive film noir — Robert Mitchum as a man whose past walks back into a small town with legs and a gun. The film's dialogue is quoted in every noir class: 'You're like a leaf that the wind blows from one gutter to another.' The ending, a bullet and a telephone, is the genre's perfect punctuation.",
        "Jacques Tourneur",
        "Out of the Past (1947) — the Mexico flashback and the ending",
        97,
        "Watch the flashback — the Mexico City meeting, the phone booth, the first double-cross — and notice how Tourneur films memory as doom: the past isn't a place you left, it's a trap you're already in. Then watch the ending, where Jeff's past and present collide in a mountain cabin: the film's argument — that a man can't outrun his choices — is delivered with the genre's most perfect final image, and Mitchum's shrug is the whole noir worldview.",
        ["Noir", "Classic", "Hollywood"],
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
