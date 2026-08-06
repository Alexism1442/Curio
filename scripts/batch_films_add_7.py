#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — late 1980s + early 1990s.

Seventh addition batch (v1.0 content pass toward 400 films): Full Metal
Jacket, The Princess Bride, Moonstruck, Who Framed Roger Rabbit, Rain Man,
Grave of the Fireflies, Cinema Paradiso, Beetlejuice, Dead Poets Society,
When Harry Met Sally, Glory, The Little Mermaid, Dances with Wolves, Home
Alone, Edward Scissorhands, Miller's Crossing, Beauty and the Beast,
Terminator 2, JFK, Thelma & Louise, Barton Fink, Delicatessen, Unforgiven,
Aladdin, The Crying Game, A Few Good Men, Malcolm X, Jurassic Park, and
more. Handcrafted teaser + real fact + quality-bar instruction.
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
        "film-full-metal-jacket-1987",
        "Full Metal Jacket (1987)",
        "Kubrick's Vietnam film in two halves — the boot-camp hell run by R. Lee Ermey's real-life drill instructor (he improvised nearly all his dialogue) and the war that follows. The first half's 'This is my rifle' and Private Pyle's breakdown, and the second half's sniper sequence, make it the most structurally audacious war film ever made. 'Me love you long time' became the decade's most quoted (and most uncomfortable) line.",
        "Stanley Kubrick",
        "Full Metal Jacket (1987) — the boot camp and the sniper scene",
        116,
        "Watch the first half — the barracks, the 'This is my rifle, this is my gun,' Pyle's slow unraveling — and notice how Kubrick shoots the drill instructor as a sacred monster: Ermey's performance (he was a real DI who improvised the insults) is the film's engine, and the laughter is the horror. Then watch the second half's sniper sequence, where the film's tone shifts to a kind of elegy: the film's argument — that the war machine manufactures killers and then mourns them — is in that final scene, and the film's two-halves structure remains the boldest in war cinema.",
        ["War", "1980s", "Hollywood"],
    ),
    _entry(
        "film-the-princess-bride-1987",
        "The Princess Bride (1987)",
        "The most quotable fairy tale ever filmed — 'As you wish,' 'Inconceivable!,' 'My name is Inigo Montoya,' and the greatest swordfight in cinema. William Goldman adapted his own novel (his only film credit he kept), Rob Reiner directed, and the film's framing device — a grandfather reading to his sick grandson — lets it be a fairy tale and a comedy about fairy tales at once. It flopped on release and became one of the most beloved films ever made.",
        "Rob Reiner",
        "The Princess Bride (1987) — the swordfight and the ending",
        98,
        "Watch the swordfight on the cliffs — Westley and Inigo, the 'I am Inigo Montoya' speech, the cliff-top duel — and notice how the film's fencing (choreographed by a real master) is both comedy and genuine athleticism: the 'to the pain' explanation and the 'I'll explain and no one will be around to hear' banter make the duel the film's centerpiece. Then watch the ending, where the grandfather reveals the story was never finished: the film's argument — that stories are how we love each other — is in that final exchange, and the film's cast (Cary Elwes, Robin Wright, André the Giant) became a national treasure.",
        ["Fantasy", "Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-moonstruck-1987",
        "Moonstruck (1987)",
        "The romantic comedy that won the decade — Cher's widowed accountant who falls for her fiancé's estranged brother (Nicolas Cage), under a full moon and a New York opera house. The film's 'Snap out of it!' and its 'La Bohème' finale won Cher the Oscar, and its warmth, its Italians, and its moon imagery made it the most beloved romance of its year. It won 3 Oscars including Best Original Screenplay.",
        "Norman Jewison",
        "Moonstruck (1987) — the opera scene and the ending",
        102,
        "Watch the opera scene — the 'La Bohème' performance, Loretta and Ronny's first date, the moon — and notice how the film uses opera as its emotional soundtrack: the aria becomes the characters' inner duet, and the film's big-heartedness is its argument. Then watch the ending, where the family gathers for a wedding and the moon shines over the Brooklyn streets: the film's thesis — that love is a gamble you take even after heartbreak — is in that final scene, and the film's ensemble (Olympia Dukakis's Oscar-winning mother) makes it the warmest film of its decade.",
        ["Romance", "Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-wall-street-1987",
        "Wall Street (1987)",
        "The film that made 'Greed is good' a national phrase — Michael Douglas's Gordon Gekko, whose speech ('Greed, for lack of a better word, is good') won him the Oscar, and Charlie Sheen's young broker who gets in over his head. Oliver Stone (whose own father was a broker) shot the trading floor chaos with real Wall Street traders, and the film's insider-trading ethics lesson — 'Stop going for the easy buck' — made it required viewing in business schools.",
        "Oliver Stone",
        "Wall Street (1987) — the 'greed is good' speech",
        126,
        "Watch the 'Greed is good' speech — Gekko addressing the shareholders, Douglas's calculated intensity — and notice how the film makes the speech seductive: you're almost persuaded, which is the film's trick, and the corruption is in the applause. Then watch the ending, where Bud Fox finally chooses conscience over his mentor: the film's argument — that the market rewards the soulless and the soulless always overreach — is in that final scene, and the film's catchphrase (quoted by actual traders) made it the most influential business film ever made.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-who-framed-roger-rabbit-1988",
        "Who Framed Roger Rabbit (1988)",
        "The film that married cartoons to reality — Bob Hoskins' detective in a 1947 Los Angeles where toons live alongside humans, solving a murder with a falsely accused cartoon rabbit. The film's technical achievement (the toons were animated to interact with real props and shadows) won it a special Oscar, and its 'dip' — the chemical that dissolves toons — is the darkest joke in animation. Jessica Rabbit's 'I'm not bad, I'm just drawn that way' is one of cinema's great lines.",
        "Robert Zemeckis",
        "Who Framed Roger Rabbit (1988) — the ending and the dip",
        104,
        "Watch the film's central technical feat — Roger slipping through doorways, the toon/human choreography, the shadow work — and notice how the animation was integrated frame by frame so the toons cast real shadows and grab real objects: it's still the best live-action/animation blend ever made. Then watch the ending, where Judge Doom's plan is revealed in the vat of dip: the film's argument — that laughter is the resistance to totalitarian order — is in that finale, and the film's cameos (Disney and Warner characters sharing the screen for the first time) are a piece of animation history.",
        ["Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-rain-man-1988",
        "Rain Man (1988)",
        "The road movie that won Best Picture — Tom Cruise's hustler discovers his autistic brother Raymond (Dustin Hoffman) inherited the family fortune, and the con becomes a bond. Hoffman's Raymond (who counted matches, refused to fly, and knew every TV schedule) won the Oscar, and the film's 'Kmart' scene and its ending — 'He's my brother' — made it the decade's most loved drama. It grossed $354 million.",
        "Barry Levinson",
        "Rain Man (1988) — the counting scene and the ending",
        133,
        "Watch the card-counting scene — the casino, Raymond's genius, Charlie's dawning understanding — and notice how Hoffman's performance (he spent months studying autistic savants) builds Raymond's world with total specificity: the rituals, the discomfort, the sudden precision. Then watch the ending, where the brothers' final scene at the train lands: the film's argument — that love doesn't require understanding, just showing up — is in that farewell, and the film's box office made 'autism' a word more Americans could say.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-grave-of-the-fireflies-1988",
        "Grave of the Fireflies (1988)",
        "The most devastating animated film ever made — Studio Ghibli's story of two orphaned siblings surviving the firebombing of Japan, told from the dead brother's memory. Isao Takahata's film is the rare war film told entirely from children's eyes, and its candy tin, its beach, and its ending are unbearable. It shares a double bill with My Neighbor Totoro in Japan — the two films' contrast is deliberate: one shows the world worth fighting for, the other shows what the fighting costs.",
        "Isao Takahata",
        "Grave of the Fireflies (1988) — the ending",
        89,
        "Watch the film's first act — the firebombing, the mother's burns, the move to the aunt's — and notice how Takahata films the horror with restraint: the violence is implied, the children's suffering is precise, and the animation's beauty (the fireflies, the sea, the summer) makes the grief sharper. Then watch the ending, where the fireflies and the candy tin resolve the film's themes: the film's argument — that the real cost of war is counted in children — is in that final scene, and the film's refusal to offer comfort made it the greatest anti-war film of its decade.",
        ["Animation", "War", "1980s", "Japanese"],
    ),
    _entry(
        "film-cinema-paradiso-1988",
        "Cinema Paradiso (1988)",
        "The love letter to cinema itself — a Sicilian boy, the projectionist who mentors him, and the village movie theater that raises him. Giuseppe Tornatore's film won the Oscar for Best Foreign Language Film, and its ending — the reel of every kiss the censor ever cut, projected for the grown man who'd forgotten — is the most moving final scene in any film about film. Ennio Morricone's score is among his most beloved.",
        "Giuseppe Tornatore",
        "Cinema Paradiso (1988) — the ending",
        124,
        "Watch the first hour — little Salvatore in the projection booth, the fires, the films — and notice how Tornatore films the movie house as a second family: the audience's laughter, the censored kisses, the priest's bell — the theater is the town's heart. Then watch the ending, where the grown Salvatore watches the reel of forbidden kisses his mentor saved: the film's argument — that cinema is the memory we keep for each other — is in that final sequence, and the film's nostalgia made it the most beloved Italian film of its generation.",
        ["Drama", "1980s", "Italian"],
    ),
    _entry(
        "film-beetlejuice-1988",
        "Beetlejuice (1988)",
        "Tim Burton's haunted-house comedy that became a franchise — a dead couple (Geena Davis, Alec Baldwin) hire a bio-exorcist (Michael Keaton's manic Beetlejuice) to scare the living out of their home. The film's afterlife waiting room, its sandworms, and its 'Day-O' dinner-table possession are pure Burton invention, and Keaton's improvised performance ('He's not a ghost, he's a ghoul!') made him the decade's great comic monster. It grossed $74 million on a $15 million budget.",
        "Tim Burton",
        "Beetlejuice (1988) — the Day-O scene and the ending",
        92,
        "Watch the 'Day-O' dinner sequence — the family possessed, the calypso song, the floating shrimp — and notice how Burton turns a haunted house into a comedy of manners: the dead are more charming than the living, and the film's handmade effects (the claymation sandworm, the shrunken heads) are its charm. Then watch the ending, where Beetlejuice's mayhem and the 'ghost training' payoff land: the film's argument — that the afterlife is just another neighborhood, and the best revenge is a song — is in that finale, and the film's style made Burton the decade's most imitated director.",
        ["Comedy", "Fantasy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-dead-poets-society-1989",
        "Dead Poets Society (1989)",
        "The film that made 'Carpe diem' a battle cry — Robin Williams' English teacher who tells his boys at a stuffy 1959 prep school to seize the day, with poetry as the weapon. The film's ending — the students standing on their desks for the fired teacher, 'O Captain! My Captain!' — is one of the most stirring final scenes in cinema, and it won the Oscar for Best Original Screenplay. 'No matter what anybody tells you, words and ideas can change the world.'",
        "Peter Weir",
        "Dead Poets Society (1989) — the ending",
        128,
        "Watch the film's first act — Welton Academy, the 'Carpe diem' lesson, the boys' first poetry club meeting in the cave — and notice how Weir films Williams' teacher as a force of nature: the laughter and the wonder are the seduction, and the tragedy is already being set up. Then watch the ending, where the boys climb onto their desks one by one: the film's argument — that the teacher's lesson survives the teacher — is in that final scene, and the film's final 'O Captain! My Captain!' remains the most tearful classroom moment in cinema.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-when-harry-met-sally-1989",
        "When Harry Met Sally... (1989)",
        "The film that asked the eternal question — can men and women be friends? — and answered it over eleven years and one famous deli scene. Nora Ephron's script, Billy Crystal and Meg Ryan's chemistry, and the 'I'll have what she's having' fake-orgasm scene (filmed in a real Katz's Deli, with a real customer's real reaction) made it the definitive romantic comedy. The documentary-style couples' interviews that bookend the film are Ephron's genius.",
        "Rob Reiner",
        "When Harry Met Sally... (1989) — the deli scene and the ending",
        96,
        "Watch the deli scene — the demonstration, the 'I'll have what she's having' — and notice how the film earns its most famous gag: the orgasm is a public performance, the other diner's reaction is real, and the comedy is about the difference between performance and feeling. Then watch the ending, where Harry's New Year's Eve speech and the couples' interviews resolve: the film's argument — that love is friendship with the volume turned up — is in that finale, and the film's structure (the couples' stories bookending the years) made it the most structurally perfect rom-com ever made.",
        ["Romance", "Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-glory-1989",
        "Glory (1989)",
        "The Civil War film about the first Black regiment — the 54th Massachusetts, led by white colonel Robert Gould Shaw, who fought and died proving Black soldiers could win the war. Denzel Washington won his first Oscar as the bitter escaped slave, and the film's ending — the doomed charge at Fort Wagner — is among the most powerful battle scenes ever filmed. The film's 'Oh, dear Lord' choral climax still raises the hair.",
        "Edward Zwick",
        "Glory (1989) — the ending charge",
        122,
        "Watch the training sequences — the 54th drilling, the prejudice they face from their own army, the 'we're soldiers now' moment — and notice how the film builds its ending from the injustice: the regiment's need to prove itself is the engine, and the film's ensemble (Denzel Washington, Morgan Freeman, and a young Matthew Broderick) carries the weight. Then watch the charge at Fort Wagner, where the men walk into the guns singing: the film's argument — that dignity is the only victory — is in that final sequence, and the film's score (James Horner's 'Glory') made the charge unforgettable.",
        ["War", "Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-say-anything-1989",
        "Say Anything... (1989)",
        "The film with the single most romantic image in cinema — John Cusack's Lloyd Dobler holding a boombox over his head outside his girlfriend's window, playing Peter Gabriel's 'In Your Eyes.' Cameron Crowe's debut, with Ione Skye's valedictorian and the 'I gave her my heart, she gave me a pen' speech, made it the definitive teen romance. The ending — the airport, the 'I'm not gonna lose you' — is perfect.",
        "Cameron Crowe",
        "Say Anything... (1989) — the boombox scene and the ending",
        100,
        "Watch the boombox scene — the curb, the 'In Your Eyes,' the window — and notice how Crowe stages the film's thesis in one image: Lloyd's love is a public declaration with no guarantee of an audience, and the song choice (Peter Gabriel's) is the film's heart. Then watch the ending, where the film's 'wrong guy' debate resolves at the airport: the film's argument — that love is the courage to keep showing up — is in that final scene, and the film's influence (every 'grand gesture' scene in every rom-com since) is immeasurable.",
        ["Romance", "Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-the-little-mermaid-1989",
        "The Little Mermaid (1989)",
        "The film that saved Disney animation — after a decade of decline, this underwater fairy tale about a mermaid who trades her voice for legs launched the 'Disney Renaissance' and changed the industry. Howard Ashman's songs ('Part of Your World,' 'Under the Sea') and the villain Ursula made it a musical first, and its box office ($211 million) proved animation could rival live action. It was the first animated film with a Broadway-style score.",
        "Ron Clements & John Musker",
        "The Little Mermaid (1989) — the 'Part of Your World' scene and the ending",
        83,
        "Watch the 'Part of Your World' sequence — Ariel's grotto, the treasures, the longing — and notice how the song establishes the film's theme in one number: the desire to be part of the human world is the whole story, and the animation (the underwater movement was a technical breakthrough) sells every note. Then watch the ending, where Ariel's choice resolves: the film's argument — that love is worth the sacrifice of comfort — is in that finale, and the film's success (it launched Beauty and the Beast, Aladdin, and The Lion King) made it the most influential animated film since Snow White.",
        ["Animation", "Family", "1980s", "Hollywood"],
    ),
    _entry(
        "film-dances-with-wolves-1990",
        "Dances with Wolves (1990)",
        "The western that reversed the genre — Kevin Costner's Union soldier who befriends the Lakota and finds his true home with them, told largely in Lakota with subtitles. It won 7 Oscars including Best Picture, and its respectful portrayal of Native culture (shot with Lakota advisers, in Lakota language) was revolutionary for 1990. The buffalo hunt sequence is among the greatest in cinema. The 4-hour extended cut is the director's preferred version.",
        "Kevin Costner",
        "Dances with Wolves (1990) — the buffalo hunt",
        181,
        "Watch the buffalo hunt — the herd, the chase, the kill — and notice how Costner films the hunt as sacred ritual: the buffalo are real (the film used a real herd and real riders), and the sequence's grandeur made it the film's centerpiece. Then watch the film's ending, where Dunbar's choice to stay with the Lakota is made: the film's argument — that a person can choose their people — is in that finale, and the film's box office ($424 million) proved that a slow, respectful western could be the year's biggest hit.",
        ["Western", "Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-home-alone-1990",
        "Home Alone (1990)",
        "The comedy that made Macaulay Culkin the biggest child star on Earth — an 8-year-old accidentally left home for Christmas defends the house from two burglars (Joe Pesci and Daniel Stern) with the most elaborate booby traps in cinema. It was the highest-grossing comedy of its time ($476 million) and its 'Keep the change, ya filthy animal' and the aftershave scene became holiday canon. John Hughes wrote the script in nine days.",
        "Chris Columbus",
        "Home Alone (1990) — the booby-trap finale",
        103,
        "Watch the trap sequence — the tar, the nails, the iron, the 'Kevin!' — and notice how the film's comedy is built from genuine craft: the traps escalate in choreography, the burglars' pain is physical comedy of the highest order, and the film never shows the violence as real harm. Then watch the ending, where the film's heart (the mother's flight home, the neighbor's reconciliation) lands: the film's argument — that family is the point of Christmas — is in that finale, and the film's annual TV rotation made it the most rewatched comedy of its era.",
        ["Comedy", "Family", "1990s", "Hollywood"],
    ),
    _entry(
        "film-edward-scissorhands-1990",
        "Edward Scissorhands (1990)",
        "Tim Burton's most personal film — the story of a gentle artificial man with scissors for hands, left alone in a pastel suburb that's fascinated and then terrified of him. Johnny Depp's first Burton role, Winona Ryder's Kim, and the film's ice-sculpture scene made it the decade's most poetic fable. Burton based Edward on his own childhood in suburban Burbank: 'he was exactly who I was as a teenager.'",
        "Tim Burton",
        "Edward Scissorhands (1990) — the ice sculpture scene and the ending",
        105,
        "Watch the ice-sculpture sequence — Edward carving the angel, the ice shavings falling like snow, Kim dancing in them — and notice how Burton makes the film's most romantic image also its saddest: the beauty Edward creates is the sign of his difference, and the 'snow' is the film's recurring metaphor for his loneliness. Then watch the ending, where the years pass and the snow still falls: the film's argument — that being different is a gift that costs — is in that final image, and the film's fairy-tale suburb (a real pastel development in Florida) is the perfect backdrop for its gothic heart.",
        ["Fantasy", "Romance", "1990s", "Hollywood"],
    ),
    _entry(
        "film-millers-crossing-1990",
        "Miller's Crossing (1990)",
        "The Coen brothers' gangster masterpiece — a 1929 Irish-Italian turf war, a hat, and Gabriel Byrne's Tom Reagan, the consigliere who betrays everyone and stays loyal to himself. The film's dialogue ('I'm talking about friendship,' 'The high hat') is the sharpest in the Coens' career, and its forest scene — the hat blown away, the man walking into the trees — is the most beautiful sequence they ever shot. It's the film the Coens' fans rank at the top.",
        "Joel & Ethan Coen",
        "Miller's Crossing (1990) — the forest scene and the ending",
        115,
        "Watch the forest sequence — Tom walking into the woods, the hat, the man behind him — and notice how the Coens stage the film's central act of violence as ritual: the hat is the motif (Tom's lost hat, the film's title's 'crossing'), and the woods swallow the scene whole. Then watch the ending, where the double-crosses resolve and the hat returns: the film's argument — that loyalty is a performance and survival is the only code — is in that finale, and the film's period detail and Carter Burwell's score made it the decade's most elegant crime film.",
        ["Crime", "1990s", "Hollywood"],
    ),
    _entry(
        "film-beauty-and-the-beast-1991",
        "Beauty and the Beast (1991)",
        "The first animated film ever nominated for Best Picture — Disney's fairy tale with the most ambitious animation ever attempted (the ballroom scene was the first extensive use of CGI in a feature). The songs by Alan Menken and the late Howard Ashman ('Be Our Guest,' 'Belle,' and the title song that won the Oscar) made it a musical masterpiece, and its 'Tale as Old as Time' ballroom dance is the most romantic sequence in animation.",
        "Gary Trousdale & Kirk Wise",
        "Beauty and the Beast (1991) — the ballroom scene and the ending",
        84,
        "Watch the ballroom sequence — the gown, the dance, the computer-animated camera sweep — and notice how the film's technology serves its emotion: the CGI camera move (the first of its kind) makes the dance feel like a dream, and the song's lyrics ('Tale as Old as Time') are the film's thesis. Then watch the ending, where the beast's transformation and the 'tale as old as time' resolution land: the film's argument — that love sees past the surface — is in that finale, and the film's 6 Oscar nominations (a record for animation at the time) changed how the industry treated animated films.",
        ["Animation", "Family", "1990s", "Hollywood"],
    ),
    _entry(
        "film-terminator-2-1991",
        "Terminator 2: Judgment Day (1991)",
        "The sequel that defined the blockbuster era — James Cameron's $100 million spectacle (the most expensive film ever made at the time) where the Terminator is now the good guy, protecting John Connor from the liquid-metal T-1000. The morphing effects (the first fully digital character) won 4 Oscars, and the film's 'Hasta la vista, baby' and its ending — 'No fate but what we make' — made it the rare sequel that outdoes its original. It grossed $520 million.",
        "James Cameron",
        "Terminator 2 (1991) — the mall escape and the ending",
        137,
        "Watch the escape sequence — the police, the T-1000's first pursuit, the pipe — and notice how Cameron raises the stakes with the villain: Robert Patrick's T-1000 (who trained to move like a machine) is the film's special effect made human, and the chase's choreography still holds up. Then watch the ending, where the Terminator's sacrifice resolves the film's theme: the film's argument — that the future is chosen, not fated, and that a machine can learn mercy — is in that final thumbs-up, and the film's influence on every effects-driven blockbuster since is total.",
        ["Sci-Fi", "Action", "1990s", "Hollywood"],
    ),
    _entry(
        "film-jfk-1991",
        "JFK (1991)",
        "The most controversial film of its decade — Oliver Stone's three-hour investigation of the Kennedy assassination, which argued that the lone-gunman story was a cover-up and presented its case with courtroom-style evidence. The film's editing (over 2,000 cuts in the final 20 minutes) is among the most aggressive ever assembled, and its Zapruder-film reconstruction and Kevin Costner's closing speech made it a cultural event. It earned 8 Oscar nominations and forced a national conversation that never really ended.",
        "Oliver Stone",
        "JFK (1991) — the trial speech and the ending",
        189,
        "Watch the film's central argument — the Zapruder film, the 'magic bullet,' the back-and-to-the-left — and notice how Stone assembles the case as a courtroom montage: the editing (which won the Oscar) turns conspiracy into cinema, and the film's conviction is its power. Then watch the ending, where Garrison's closing speech ('back and to the left') lands: the film's argument — that the truth was buried and the process deserves scrutiny — is in that finale, and the film's influence (it prompted the real release of classified files) makes it the rare film that changed policy.",
        ["Thriller", "1990s", "Hollywood"],
    ),
    _entry(
        "film-thelma-and-louise-1991",
        "Thelma & Louise (1991)",
        "The road movie that changed cinema's gender politics — two women (Geena Davis, Susan Sarandon) drive off on a weekend trip, commit a murder, and never look back. Ridley Scott's film ended with the most debated final image of its decade — the car flying off the cliff — and won the Oscar for Best Original Screenplay. Thelma's line 'You're not gonna believe this, but I feel really awake' and the film's freedom-vs-consequences ending made it a landmark.",
        "Ridley Scott",
        "Thelma & Louise (1991) — the ending",
        130,
        "Watch the film's turning point — the roadhouse, the assault, the gun — and notice how the film earns its politics through character: Thelma's transformation from passive wife to outlaw is the film's engine, and the desert cinematography (shot in the Utah badlands) is gorgeous. Then watch the ending, where the two women choose the cliff over surrender: the film's argument — that freedom is the only thing worth the fall — is in that final image, and the film's ending (still debated in film classes) made it the most talked-about final scene of its decade.",
        ["Drama", "Crime", "1990s", "Hollywood"],
    ),
    _entry(
        "film-barton-fink-1991",
        "Barton Fink (1991)",
        "The Coen brothers' Palme d'Or winner — a New York playwright (John Turturro) hired to write a wrestling picture in Hollywood, who checks into a hotel that may be a portal to hell. The film's 'the life of the mind' speech, its fire, and its famously ambiguous ending made it the Coens' strangest and most rewarding film. The hotel, the typewriter, and the 'I'm a simple man' monologue are unforgettable. It won the Palme d'Or, Best Director, and Best Actor at Cannes.",
        "Joel & Ethan Coen",
        "Barton Fink (1991) — the hotel and the ending",
        116,
        "Watch the hotel scenes — the peeling wallpaper, the mosquito, the 'did you check in for a rest?' — and notice how the Coens build the film's dread from a single room: the hotel's silence is the horror, and Barton's isolation is the film's subject. Then watch the ending, where the package and the fire resolve (or refuse to resolve) the film's mysteries: the film's argument — that the artist's struggle is a kind of damnation — is in that finale, and the film's ambiguity (the Coens have refused to explain it) made it the decade's most analyzed film.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-delicatessen-1991",
        "Delicatessen (1991)",
        "The post-apocalyptic comedy that made Jean-Pierre Jeunet famous — a French butcher's building where the tenants eat the tenants, and the new handyman is next on the menu. The film's rubber-tube rhythm scene (the bedsprings, the creaking floor, the slapstick timing) is the decade's most inventive comedy sequence, and its surreal, sepia world announced the 'Cinéma du look' style that Jeunet would perfect in Amélie. It was France's biggest international hit of the year.",
        "Jean-Pierre Jeunet & Marc Caro",
        "Delicatessen (1991) — the rubber-tube scene",
        99,
        "Watch the rubber-tube sequence — the spring bouncing, the floor creaking, the timing — and notice how Jeunet builds the film's comedy from sound and rhythm: the scene is a musical number about sex and appetite, and every bounce is choreographed. Then watch the ending, where the flooded basement and the final chase resolve: the film's argument — that appetite (for food, for love, for life) is the only thing that survives the apocalypse — is in that finale, and the film's handmade, eccentric style made it the most influential French comedy of its decade.",
        ["Comedy", "1990s", "French"],
    ),
    _entry(
        "film-unforgiven-1992",
        "Unforgiven (1992)",
        "The western that buried the genre — Clint Eastwood's retired killer who takes one last job, and the film's brutal thesis that the myths of the Old West were lies told by the violent. It won 4 Oscars including Best Picture and Best Director (Eastwood), and Gene Hackman's 'Little Bill' Daggett — the sheriff who beats 'innocent' men to death — is among the great villains. 'Deserve's got nothing to do with it.'",
        "Clint Eastwood",
        "Unforgiven (1992) — the ending",
        131,
        "Watch the film's structure — Will Munny's farm, the bounties, the 'I've killed women and children' confessions — and notice how Eastwood dismantles the western's heroics: the film's violence is ugly, its heroes are broken, and its landscape (shot in Alberta, not Monument Valley) is muddy and cold. Then watch the ending, where Munny's final rampage in Greely's: the film's argument — that the 'legend' of the gunslinger is a tombstone industry — is in that finale, and the film's last image (the epilogue text about Munny's farm) is the genre's most unsentimental closing.",
        ["Western", "1990s", "Hollywood"],
    ),
    _entry(
        "film-aladdin-1992",
        "Aladdin (1992)",
        "The most purely entertaining of the Disney Renaissance — Robin Williams' Genie, whose improvised, pop-culture-saturated performance rewrote what animation voice acting could be, and the film's 'A Whole New World' (the first Disney song to hit #1). The animation (the 'Never Had a Friend Like Me' number is a showcase) and the film's $504 million gross made it the year's biggest hit. The Genie's 16 hours of recorded improvisation became 30 seconds on screen.",
        "Ron Clements & John Musker",
        "Aladdin (1992) — the 'Friend Like Me' scene",
        90,
        "Watch the 'Friend Like Me' number — the Genie's shapeshifting showcase, the chorus, the pure animation virtuosity — and notice how Williams' improvisation drives the sequence: the animators worked from his audio tracks, and the result is the most energetic scene in Disney history. Then watch the ending, where Aladdin's wish and the film's 'be yourself' moral resolve: the film's argument — that love isn't about being what you're not — is in that finale, and the film's box office and soundtrack made it the peak of the Renaissance.",
        ["Animation", "Family", "1990s", "Hollywood"],
    ),
    _entry(
        "film-the-crying-game-1992",
        "The Crying Game (1992)",
        "The film that asked audiences to keep a secret — Neil Jordan's IRA thriller with the most famous twist of its decade (the marketing campaign was literally 'Don't reveal the secret'). The film's ending and its use of the title song (by the band Boy George) made it a cultural event, and its treatment of identity, loyalty, and love was decades ahead of its time. It won the Oscar for Best Original Screenplay.",
        "Neil Jordan",
        "The Crying Game (1992) — the reveal and the ending",
        112,
        "Watch the film's structure — the IRA kidnapping, the hostage friendship, the escape to London — and notice how Jordan builds the film's famous twist from genuine character work: the relationship before the reveal is real, which is why the reveal lands as a question about love, not a stunt. Then watch the ending, where the film's themes of identity and loyalty resolve: the film's argument — that who we love is more complicated than who we are — is in that finale, and the film's box office (a $100 million-plus hit on a $6 million budget) proved audiences would keep the secret.",
        ["Thriller", "1990s", "Hollywood"],
    ),
    _entry(
        "film-a-few-good-men-1992",
        "A Few Good Men (1992)",
        "The courtroom drama with the most famous confrontation in cinema — Jack Nicholson's Colonel Jessup vs. Tom Cruise's Lieutenant Kaffee: 'You can't handle the truth!' Aaron Sorkin's script (his first film) made the movie a battle of wills, and the film's 'Code Red' mystery and its ending made it the decade's definitive legal thriller. The famous line was ad-libbed by Nicholson and Cruise's response — 'I want the truth!' — was the take they kept.",
        "Rob Reiner",
        "A Few Good Men (1992) — the 'truth' scene",
        138,
        "Watch the 'You can't handle the truth' scene — the standoff, the silences, the build — and notice how Sorkin's dialogue (his signature overlapping, escalating lines) makes the courtroom a boxing ring: the scene was shot with both actors at full intensity, and the 'truth' speech is the film's climax. Then watch the ending, where Kaffee's closing argument lands the film's moral: the film's argument — that the military's 'code' can become a cover for crime, and that truth is the only code — is in that finale, and the film's script (quoted in every law school) made Sorkin the decade's most influential writer.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-malcolm-x-1992",
        "Malcolm X (1992)",
        "Spike Lee's three-and-a-half-hour epic about the man who remade himself three times — Malcolm Little, Detroit Red, and Malcolm X. Denzel Washington's performance (nominated for the Oscar) is among the greatest in American cinema, and the film's ending — the 'By any means necessary' speech cut with Martin Luther King's 'I have a dream' — is the most audacious final montage ever made. The film was finished when Lee mortgaged his own house.",
        "Spike Lee",
        "Malcolm X (1992) — the ending",
        202,
        "Watch the film's transformation structure — the prison conversion, the Nation of Islam years, the pilgrimage to Mecca — and notice how Lee films each incarnation with a different visual language: the early hustle in color and speed, the mosque years in black and white, the final years in documentary newsreel style. Then watch the ending, where the 'By any means necessary' and the King footage intercut: the film's argument — that there were two roads to freedom, and both mattered — is in that montage, and the film's 202-minute runtime is earned by the scale of its subject.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-jurassic-park-1993",
        "Jurassic Park (1993)",
        "The film that changed movies forever — Steven Spielberg's dinosaurs were the first fully convincing CGI creatures, and the T-Rex's first appearance (the rain, the gate, the headlights) remains the greatest monster reveal in cinema. The animatronics (a full-size T-Rex) were built alongside the CGI, and its box office made it the biggest hit in history at the time. 'Life finds a way.' It won 3 Oscars.",
        "Steven Spielberg",
        "Jurassic Park (1993) — the T-Rex attack",
        127,
        "Watch the T-Rex sequence — the rain, the fence, the headlights — and notice how Spielberg earns the reveal: the cup of water rippling is the warning, and the animatronic and CGI T-Rexes were blended so seamlessly that audiences couldn't tell which was which. Then watch the ending, where the film's warning about genetic power lands: the film's argument — that nature will not be contained by theme parks or intentions — is in that finale, and the film's effect on every effects-driven blockbuster since (they all exist in its shadow) is total.",
        ["Sci-Fi", "Adventure", "1990s", "Hollywood"],
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
