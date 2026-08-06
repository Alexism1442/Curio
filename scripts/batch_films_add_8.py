#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — the 1990s (peak decade).

Eighth addition batch (v1.0 content pass toward 400 films): Philadelphia,
Groundhog Day, Three Colours: Blue, Forrest Gump, Léon: The Professional,
The Lion King, Three Colours: Red, Ed Wood, Toy Story, Se7en, Braveheart,
Twelve Monkeys, Casino, Trainspotting, Scream, The English Patient, Jerry
Maguire, Good Will Hunting, L.A. Confidential, The Fifth Element, Boogie
Nights, Run Lola Run, Saving Private Ryan, The Truman Show, The Thin Red
Line, The Sixth Sense, The Green Mile, Being John Malkovich, American
Beauty, Eyes Wide Shut. Handcrafted teaser + real fact + quality-bar
instruction. Appends only; rejects duplicate ids/names; caps 450.
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
        "film-philadelphia-1993",
        "Philadelphia (1993)",
        "The first Hollywood studio film about AIDS — Tom Hanks' lawyer fired for having the disease, who sues his firm with Denzel Washington's homophobic attorney defending the other side. Hanks won his first Oscar, and the film's ending — the lawyer dying at his own party — is among the decade's most moving. The opera aria scene ('La Mamma Morta') is the film's heart: 'I'm not going to be ashamed.'",
        "Jonathan Demme",
        "Philadelphia (1993) — the opera scene and the ending",
        125,
        "Watch the opera sequence — Andrew listening to Maria Callas, describing the aria's meaning to his lawyer — and notice how the film uses the music to say what the characters can't: the aria is about a mother's love and a world that rejects her, and the tears are the film's argument. Then watch the ending, where the verdict and the deathbed scene resolve: the film's message — that dignity is not conditional — is in that finale, and the film's courage (it was the first mainstream film to put its hero's gay identity at the center) made it a landmark.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-groundhog-day-1993",
        "Groundhog Day (1993)",
        "The funniest philosophical film ever made — a cynical weatherman (Bill Murray) trapped in the same day until he learns to live it properly. Harold Ramis' comedy was initially dismissed and is now studied as a Buddhist parable: the film is literally about samsara, the cycle of rebirth, and the path through it. The 'snowman' montage and the ending — the clock striking 6:00 and the day finally moving — are perfect.",
        "Harold Ramis",
        "Groundhog Day (1993) — the montage and the ending",
        101,
        "Watch the film's middle — the despair montage (the alarm clock, the suicides, the 'I'm not going to live by their rules anymore'), then the growth montage (the piano lessons, the ice sculptures, the saving of lives) — and notice how Murray's performance carries the character's arc through repetition: the same morning, played a dozen ways. Then watch the ending, where the day finally changes: the film's argument — that the meaning of life is to become the person who deserves the life you're given — is in that final scene, and the film's influence (every time-loop story since owes it) is total.",
        ["Comedy", "1990s", "Hollywood"],
    ),
    _entry(
        "film-three-colours-blue-1993",
        "Three Colours: Blue (1993)",
        "The first panel of Krzysztof Kieślowski's trilogy based on the French flag — blue for liberty, and the story of a woman (Juliette Binoche) who loses her husband and daughter in a car crash and tries to erase herself from the world. The film's blue — the swimming pool, the light through the window, the sugar cube — is its visual language, and the film's final image (a montage of faces resolving into the glass) is the most discussed in its director's career. It won the Golden Lion.",
        "Krzysztof Kieślowski",
        "Three Colours: Blue (1993) — the opening and the ending",
        98,
        "Watch the opening — the crash, the sudden silence, the blue light — and notice how Kieślowski films grief as a sensory experience: the music stops, the colors wash out, and Julie's retreat from the world (the apartment sale, the 'I don't want any belongings') is the film's subject. Then watch the ending, where the film's mosaic of faces (everyone touched by the dead composer's music) resolves: the film's argument — that liberty is not freedom from connection but freedom to choose it — is in that final image, and the film's music (the concerto that completes itself) is among cinema's greatest.",
        ["Drama", "1990s", "French"],
    ),
    _entry(
        "film-forrest-gump-1994",
        "Forrest Gump (1994)",
        "The film that made the decade weep — Tom Hanks' simple man who runs through three decades of American history, meeting presidents, starting trends, and loving Jenny. The film's digital insertion of Forrest into real newsreels (with real presidents) was a landmark effect, and its 'Life is like a box of chocolates' and its feather bookends made it the decade's most beloved film. It won 6 Oscars including Best Picture and grossed $678 million.",
        "Robert Zemeckis",
        "Forrest Gump (1994) — the running and the ending",
        142,
        "Watch the historical inserts — Forrest shaking hands with presidents, teaching Elvis to dance, the 'I had to see what Vietnam was like' — and notice how the effects (Forrest composited into real news footage) make the film's fantasy feel like memory. Then watch the ending, where the feather returns and Forrest talks to Jenny's grave: the film's argument — that a good heart is the only compass you need — is in that finale, and the film's politics (loved and debated from both sides) made it the most-discussed film of its year.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-leon-the-professional-1994",
        "Léon: The Professional (1994)",
        "The hitman movie with a heart — Jean Reno's Léon, a lonely killer who takes in Mathilda, a 12-year-old (Natalie Portman's debut) whose family was murdered. Luc Besson's film is violent and tender at once, and Gary Oldman's corrupt DEA agent Stansfield — 'Everyone! … I love that word' — is one of the great screen villains. The plant, the milk, and the ending are among the most quoted in action cinema.",
        "Luc Besson",
        "Léon: The Professional (1994) — the ending",
        110,
        "Watch the training sequences — Léon teaching Mathilda the trade, the milk, the plant — and notice how Besson builds the film's odd-couple bond through ritual: the plant is Léon's only friend before Mathilda, and the film's tenderness is never sentimental. Then watch the ending, where Léon's final act (the 'This is from Mathilda' grenade trick) resolves: the film's argument — that love transforms even the coldest professional — is in that finale, and the film's mix of action and emotion made it the most influential European action film of its decade.",
        ["Action", "Crime", "1990s", "Hollywood"],
    ),
    _entry(
        "film-the-lion-king-1994",
        "The Lion King (1994)",
        "The highest-grossing animated film of its era and the most beloved of the Disney Renaissance — Hamlet with lions, Elton John's songs, and the most famous death scene in animation (Mufasa's stampede). The film's 'Circle of Life' opening, its 'Hakuna Matata,' and its 'Can You Feel the Love Tonight' (which won the Oscar) made it a cultural constant, and its 1994 gross ($763 million) was a record for an animated film. It ran on Broadway for 25 years.",
        "Roger Allers & Rob Minkoff",
        "The Lion King (1994) — the stampede and the ending",
        88,
        "Watch the stampede sequence — the wildebeests, Mufasa's fall, Simba's 'Dad, wake up' — and notice how the film earns its grief: the animation (a stampede of millions of wildebeests) was a technical milestone, and the scene's silence after the roar is the film's emotional core. Then watch the ending, where Simba's return and the 'Circle of Life' resolution land: the film's argument — that we are all part of something that outlives us — is in that finale, and the film's blend of Shakespeare, Disney, and African imagery made it the Renaissance's defining work.",
        ["Animation", "Family", "1990s", "Hollywood"],
    ),
    _entry(
        "film-three-colours-red-1994",
        "Three Colours: Red (1994)",
        "The final panel of Kieślowski's trilogy — red for fraternity — and the director's last film: a model (Irène Jacob) who hits a retired judge's dog and discovers the old man has been listening to his neighbors' phone calls. The film's theme — that we are all connected, whether we know it or not — is made literal in the film's final image, a ferry rescue that ties the entire trilogy together. It earned three Oscar nominations, and its ending is the most satisfying conclusion in modern cinema.",
        "Krzysztof Kieślowski",
        "Three Colours: Red (1994) — the ending",
        99,
        "Watch the film's parallel structure — Valentine's story and the judge's story, the two halves that keep almost touching — and notice how Kieślowski films destiny as coincidence: the crossing paths (the dog, the car, the theater) are the film's argument in miniature. Then watch the ending, where the ferry survivors (who include characters from all three films) are revealed: the film's message — that fraternity is the invisible web that holds us — is in that final montage, and the film's last shot (the window) is the most elegant period at the end of a career in cinema.",
        ["Drama", "1990s", "French"],
    ),
    _entry(
        "film-ed-wood-1994",
        "Ed Wood (1994)",
        "The most affectionate film ever made about failure — Tim Burton's black-and-white tribute to the 'worst director of all time,' Ed Wood, who made Plan 9 from Outer Space with total sincerity. Johnny Depp's Wood and Martin Landau's Bela Lugosi (which won Landau the Oscar) are the film's heart, and the film's argument — that passion matters more than talent — makes it the rare comedy that's genuinely moving. The graveyard scenes with Lugosi are among Burton's best.",
        "Tim Burton",
        "Ed Wood (1994) — the Lugosi scenes and the ending",
        127,
        "Watch the Lugosi scenes — the aging Dracula star, his despair, his friendship with the only man who still believes in him — and notice how Landau's performance (he studied Lugosi's films and mannerisms obsessively) makes the film's comedy heartbreaking. Then watch the ending, where the premiere of Plan 9 plays out: the film's argument — that art is the attempt, not the result — is in that finale, and the film's black-and-white photography (shot to match the 1950s B-movie look) makes it the most loving 'bad movie' ever made.",
        ["Comedy", "Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-toy-story-1995",
        "Toy Story (1995)",
        "The first feature film made entirely on computers — Pixar's story of a cowboy doll (Tom Hanks) jealous of the new spaceman (Tim Allen) changed animation forever. John Lasseter's film proved CGI could carry emotion, and its box office ($373 million) launched the most successful animation studio in history. The film's themes — jealousy, friendship, and the fear of being replaced — are so universal that its sequel, Toy Story 3, made grown adults sob in theaters.",
        "John Lasseter",
        "Toy Story (1995) — the ending",
        81,
        "Watch the film's opening act — Andy's room, the toys' secret life, Woody's jealousy — and notice how the film's technology serves the story: the toys' limited movement (the first CGI had to work within plastic logic) became character, and the animation's warmth was a breakthrough. Then watch the ending, where the toys unite to save Buzz: the film's argument — that being replaced is survivable when you have friends — is in that finale, and the film's influence (every animated film since exists in its shadow) made it the most important debut in animation history.",
        ["Animation", "Family", "1990s", "Hollywood"],
    ),
    _entry(
        "film-se7en-1995",
        "Se7en (1995)",
        "The serial-killer film that defined the 1990s — David Fincher's rain-soaked thriller about two detectives hunting a killer who murders according to the seven deadly sins. The film's opening credits (with the famous 'slit fingers' sequence) announced Fincher's style, and its ending — 'What's in the box?' — is the most shocking final scene of the decade. Morgan Freeman's Somerset and Brad Pitt's Mills are the definitive detective pair.",
        "David Fincher",
        "Se7en (1995) — the ending",
        127,
        "Watch the opening credits — the fingers, the razor, the 'Gluttony' case — and notice how Fincher's style (the desaturated color, the handheld tension, the dirty details) makes the city itself a character: the film's world is an apocalypse that hasn't happened yet. Then watch the ending, where the box and the 'anger' sin resolve: the film's argument — that the world is a place where the innocent are punished and the clever are damned — is in that finale, and the film's refusal to blink (the studio wanted a happier ending; Fincher and the writers won) made it the decade's defining thriller.",
        ["Thriller", "Crime", "1990s", "Hollywood"],
    ),
    _entry(
        "film-braveheart-1995",
        "Braveheart (1995)",
        "The epic that won 5 Oscars including Best Picture — Mel Gibson's William Wallace, the Scottish warrior who led a rebellion against England. The film's 'Freedom!' cry, its Battle of Stirling Bridge (filmed with 3,000 extras and no CGI armies), and its ending — the execution and the 'They may take our lives, but they'll never take our freedom!' — made it the decade's most stirring historical epic, even as historians noted the liberties it took with the actual history.",
        "Mel Gibson",
        "Braveheart (1995) — the ending",
        178,
        "Watch the Battle of Stirling sequence — the guerrilla tactics, the charge, the 'hold, hold' — and notice how the film's battle scenes were shot practically: real extras, real mud, real horses, which is why the violence feels physical rather than digital. Then watch the ending, where Wallace's execution and his final word resolve: the film's argument — that freedom is a value worth dying for, and that a martyr's cry outlives the executioner — is in that finale, and the film's emotional power (it made audiences chant 'Freedom' in theaters) made it a phenomenon.",
        ["War", "Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-twelve-monkeys-1995",
        "Twelve Monkeys (1995)",
        "The time-travel nightmare that out-wrenched its inspiration — Terry Gilliam's expansion of the 1962 short film La Jetée, with Bruce Willis as a man sent back from a plague-ravaged future to find the source. Brad Pitt's manic mental patient (which earned him his first Oscar nomination) and the film's ending — the airport, the bullet, the 'I'm in insurance' — are unforgettable. The film's production design (Gilliam's cluttered, decaying world) is the most distinctive of the decade.",
        "Terry Gilliam",
        "Twelve Monkeys (1995) — the ending",
        129,
        "Watch the film's structure — the past, the future, the asylum, the dreams that may be memories — and notice how Gilliam keeps the timeline deliberately unreliable: the film never tells you what's real, and the repetition (the airport, the woman, the gun) is the point. Then watch the ending, where the loop's true shape is revealed: the film's argument — that the future is already written, and the present is just its memory — is in that finale, and the film's influence (every 'twist' time-travel film since) is enormous.",
        ["Sci-Fi", "1990s", "Hollywood"],
    ),
    _entry(
        "film-casino-1995",
        "Casino (1995)",
        "Scorsese's Las Vegas epic — De Niro's casino boss, Sharon Stone's hustler wife (who earned an Oscar nomination), and Joe Pesci's psychopath, in a three-hour chronicle of how the mob ran Vegas and lost it. The film's opening — the car bombing, the 'voiceover from the grave' structure — and its ending — the desert, the coin toss — make it the decade's great crime tragedy. 'In the end, we get it all.'",
        "Martin Scorsese",
        "Casino (1995) — the opening and the ending",
        178,
        "Watch the opening — the car bomb, the explosion, the coin floating in the air — and notice how Scorsese announces the film's structure in one shot: the whole movie is a flashback from a man who's already dead, and the 'voiceover' (real casino history, adapted) gives it documentary weight. Then watch the ending, where the casino is imploded and the coin lands: the film's argument — that greed is a machine that eats its owners — is in that finale, and the film's 178-minute sprawl (the most expensive Scorsese film ever at the time) is justified by its operatic sweep.",
        ["Crime", "1990s", "Hollywood"],
    ),
    _entry(
        "film-trainspotting-1996",
        "Trainspotting (1996)",
        "The film that made addiction feel alive — Danny Boyle's Edinburgh junkies, Renton's 'Choose Life' monologue, and the most inventive filmmaking of the decade. The 'worst toilet in Scotland' dive, the baby on the ceiling, and the Iggy Pop soundtrack ('Lust for Life') made it a phenomenon. Ewan McGregor's breakout, and the film's balance of comedy, horror, and genuine sadness ('It's shite being Scottish') made it the defining British film of its era.",
        "Danny Boyle",
        "Trainspotting (1996) — the opening and the ending",
        94,
        "Watch the opening — the 'Choose Life' monologue, the running through the streets, the 'Lust for Life' — and notice how Boyle's filmmaking (the speed, the wit, the color) makes the film's subject bearable: the style is the strategy, and the film's famous 'worst toilet' dive turns disgust into surreal comedy. Then watch the ending, where Renton's final 'Choose Life' and the money resolve: the film's argument — that escape from addiction is also a kind of betrayal, and that self-interest is the only reliable friend — is in that finale, and the film's box office made it the most successful Scottish film ever.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-scream-1996",
        "Scream (1996)",
        "The horror film that winked and still terrified — Wes Craven's slasher where the characters know the rules of horror movies and try to use them to survive. The opening scene (Drew Barrymore, the phone call, 'What's your favorite scary movie?') is the most famous horror opening of the decade, and the film's 'rules' scene — 'There are certain rules that one must abide by in order to successfully survive a horror movie' — made it the genre's smartest entry. It grossed $173 million and revived horror.",
        "Wes Craven",
        "Scream (1996) — the opening and the rules scene",
        111,
        "Watch the opening — the phone call, the popcorn, the 'what's your favorite scary movie?' — and notice how Craven stages the film's meta-gambit: Drew Barrymore (a star, in the opening) breaks every rule of the genre, and her death in the first ten minutes tells you no one is safe. Then watch the rules scene, where Randy explains the genre's logic: the film's argument — that horror is a conversation with its own audience — is in that scene, and the film's blend of satire and genuine scares (it's still scary) made it the most influential horror film of its decade.",
        ["Horror", "1990s", "Hollywood"],
    ),
    _entry(
        "film-the-english-patient-1996",
        "The English Patient (1996)",
        "The epic romance that swept the Oscars (9 wins including Best Picture) — a burned man in an Italian villa tells his nurse the story of the love affair that destroyed him in the North African desert. Ralph Fiennes and Kristin Scott Thomas's affair, the cave paintings, and the ending — 'I'm in love with ghosts' — made it the decade's most beautiful tragedy. The film's desert cinematography and its patient structure are the opposite of modern storytelling, and it won anyway.",
        "Anthony Minghella",
        "The English Patient (1996) — the ending",
        162,
        "Watch the film's structure — the villa, the flashbacks, the affair unfolding in the desert — and notice how Minghella (who also wrote the script) cross-cuts the two timelines so the love story and the war story resolve together: the sand, the maps, the 'I want all this to be in your arms' are the film's imagery. Then watch the ending, where the patient's final request and the morphine resolve: the film's argument — that love is a wound that outlives its causes — is in that finale, and the film's 9 Oscars made it the year's definitive statement.",
        ["Romance", "War", "1990s", "Hollywood"],
    ),
    _entry(
        "film-jerry-maguire-1996",
        "Jerry Maguire (1996)",
        "The sports agent rom-com that gave the decade its most quoted lines — 'Show me the money!,' 'You complete me,' and 'You had me at hello.' Cameron Crowe's film made Cuba Gooding Jr. an Oscar winner (the 'show me the money' scene was his showcase), and Tom Cruise's best-loved performance — the slick agent who grows a conscience and a heart — carries the film. The ending, with the apology note and the 'I'm looking for my family,' is pure Crowe.",
        "Cameron Crowe",
        "Jerry Maguire (1996) — the 'show me the money' scene and the ending",
        139,
        "Watch the 'Show me the money' scene — the phone call, the escalating desperation, Cuba Gooding Jr.'s improvisation — and notice how the scene became a cultural phrase overnight: the comedy is in the commitment, and the film's blend of satire (the mission statement) and sincerity is its balance. Then watch the ending, where Jerry's apology ('I love you. You complete me.') and the final choice resolve: the film's argument — that the 'human head' is a real thing worth keeping — is in that finale, and the film's box office ($274 million) made it the year's romantic hit.",
        ["Romance", "Comedy", "1990s", "Hollywood"],
    ),
    _entry(
        "film-good-will-hunting-1997",
        "Good Will Hunting (1997)",
        "The film that made Matt Damon and Ben Affleck Oscar winners — a janitor at MIT who's secretly a math genius, and the therapist (Robin Williams, in his Oscar-winning role) who sees the boy behind the brain. The film's 'It's not your fault' scene — Williams' most famous moment — and its ending ('I gotta see about a girl') made it the decade's most loved drama. The screenplay, written by Damon and Affleck in their twenties, is the film's legend.",
        "Gus Van Sant",
        "Good Will Hunting (1997) — the 'it's not your fault' scene and the ending",
        126,
        "Watch the 'It's not your fault' scene — the office, the repetition, the tears — and notice how the film's best moment is built from stillness: Williams' therapist drops the intellectual game and simply says it, over and over, until Will breaks. Then watch the ending, where the 'I gotta see about a girl' note and the drive west resolve: the film's argument — that the point of genius is to live, not to perform — is in that finale, and the film's screenplay (written by two friends who sold it for $500,000 while insisting they star) is the decade's great Hollywood fable.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-la-confidential-1997",
        "L.A. Confidential (1997)",
        "The neo-noir that brought the genre back — Curtis Hanson's adaptation of James Ellroy's novel about three L.A. cops (Russell Crowe, Guy Pearce, Kevin Spacey) whose paths cross in a corrupt 1950s department. The film's 'Rollo Tomasi' scene, its 'badge' theme, and its ending — the shootout and the quiet resolution — are the noir formula perfected. Kim Basinger won the Oscar, and the film's ensemble is among the decade's best.",
        "Curtis Hanson",
        "L.A. Confidential (1997) — the ending",
        138,
        "Watch the film's structure — the three cops, their three codes, the 'Nite Owl' massacre that binds them — and notice how Hanson and his writer (Brian Helgeland) compress Ellroy's novel into a perfect machine: every character's flaw is the plot's lever. Then watch the ending, where the cover-up collapses and the three men's fates resolve: the film's argument — that justice in a corrupt system is a private act — is in that finale, and the film's production design (the perfect 1950s Los Angeles) makes it the most beautiful crime film of its decade.",
        ["Crime", "Noir", "1990s", "Hollywood"],
    ),
    _entry(
        "film-the-fifth-element-1997",
        "The Fifth Element (1997)",
        "The most joyful sci-fi film ever made — Luc Besson's comic-book future where Bruce Willis' cabbie must save the world with a perfect being (Milla Jovovich) and the help of a diva, a priest, and Chris Tucker's Ruby Rhod. The film's opera sequence — the blue alien diva singing a mix of rock and classical — is one of cinema's great set pieces, and its visual style (Jean Paul Gaultier's costumes, the flying cars) defined 90s futurism. 'Multipass!'",
        "Luc Besson",
        "The Fifth Element (1997) — the opera sequence",
        126,
        "Watch the opera sequence — the diva's aria, the shape-shifting rock singer, the chase woven through the performance — and notice how Besson stages the film's wildest idea (an alien opera as a plot device) with total commitment: the scene is funny, gorgeous, and thrilling at once, and the diva's song was written to blend opera and techno. Then watch the ending, where the 'fifth element' reveal lands: the film's argument — that love is the element that holds the universe together — is in that finale, and the film's French-budget sci-fi ambition made it the most distinctive blockbuster of its year.",
        ["Sci-Fi", "Action", "1990s", "Hollywood"],
    ),
    _entry(
        "film-boogie-nights-1997",
        "Boogie Nights (1997)",
        "Paul Thomas Anderson's astonishing debut about the 1970s adult-film industry's rise and fall — Mark Wahlberg's Dirk Diggler, Julianne Moore's Amber Waves, and the film's famous one-take opening tracking shot through the nightclub. The film's 'firecracker' scene (the pool, the drug deal, Alfred Molina's fantastic performance) and its ending — the 'Jessie's Girl' moment — are among the decade's great set pieces. The film is a tragedy wearing a party's clothes.",
        "Paul Thomas Anderson",
        "Boogie Nights (1997) — the firecracker scene",
        155,
        "Watch the firecracker scene — the pool party, the firecrackers, Molina's escalating madness — and notice how Anderson builds the film's tonal pivot in one sequence: the laughter curdles into terror, and the film's 'family' (the porn 'family') begins to break. Then watch the ending, where Dirk's 'Jessie's Girl' moment in the club resolves his arc: the film's argument — that the dream of fame is a firecracker that burns everyone it touches — is in that finale, and the film's 155 minutes announced Anderson as the decade's most exciting new director.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-run-lola-run-1998",
        "Run Lola Run (1998)",
        "The kinetic German thriller that plays like a video game — Lola has 20 minutes to find 100,000 marks to save her boyfriend, and the film plays the same scenario three times with three different outcomes. Tom Tykwer's film (with its techno score and its animated interludes) was the decade's most influential European film, and its 'butterfly effect' structure — small choices, wildly different endings — made it the ancestor of every branching-story film since.",
        "Tom Tykwer",
        "Run Lola Run (1998) — the three runs",
        81,
        "Watch the first run — the phone call, the clock, the sprint — and notice how Tykwer builds the film's engine from rhythm: the techno score, the red hair, the stopwatch structure, and the 'what if' montages (the quick flashes of each character's possible future) make the film a meditation on chance disguised as a chase. Then watch the ending, where the third run's different choices resolve: the film's argument — that luck is a choice we keep making — is in that finale, and the film's influence (on everything from video games to Sliding Doors) is total.",
        ["Thriller", "1990s", "German"],
    ),
    _entry(
        "film-saving-private-ryan-1998",
        "Saving Private Ryan (1998)",
        "The war film that reset the genre — Steven Spielberg's D-Day opening, 25 minutes of handheld chaos on Omaha Beach, is the most harrowing battle sequence ever filmed and the reason every war film since looks different. The film's 'Earn this' ending and its bookend structure (the cemetery, the flag) made it the decade's most honored film (5 Oscars including Best Director). Its realism (shot with desaturated film, no heroics) changed how wars are portrayed.",
        "Steven Spielberg",
        "Saving Private Ryan (1998) — the D-Day opening",
        169,
        "Watch the D-Day sequence — the landing craft, the water, the chaos — and notice how Spielberg films war without heroism: the handheld camera, the muffled sound, the dying men calling for their mothers, and the sheer sensory overload make it unbearable and unmissable. Then watch the ending, where the aged Ryan asks 'Tell me I've led a good life': the film's argument — that the dead's sacrifice must be earned by the living — is in that finale, and the film's influence on every war film, game, and documentary since is immeasurable.",
        ["War", "1990s", "Hollywood"],
    ),
    _entry(
        "film-the-truman-show-1998",
        "The Truman Show (1998)",
        "The prophecy disguised as a comedy — Jim Carrey's Truman, who discovers his entire life is a TV show and his 'hometown' is a soundstage. Peter Weir's film predicted reality TV, surveillance culture, and the simulation question a decade before social media, and its ending — Truman's boat hitting the studio wall, the door, the 'Good morning, and in case I don't see ya' — is the most perfect final scene of its decade. 'In case I don't see ya: good afternoon, good evening, and good night.'",
        "Peter Weir",
        "The Truman Show (1998) — the ending",
        103,
        "Watch the film's middle — the 'bad weather' the director throws at him, the escalating glitches, the realization — and notice how Weir builds the film's world as a machine: the production design (the perfect town, the hidden cameras) is the joke, and Carrey's dramatic turn (his first) is the film's engine. Then watch the ending, where Truman hits the wall and opens the door: the film's argument — that even a perfect cage is still a cage, and the unknown is worth the risk — is in that finale, and the film's prophecy (we all live in the show now) made it the most prescient film of its era.",
        ["Drama", "Sci-Fi", "1990s", "Hollywood"],
    ),
    _entry(
        "film-the-thin-red-line-1998",
        "The Thin Red Line (1998)",
        "The war film as meditation — Terrence Malick's Guadalcanal epic, told through voiceovers that turn the soldiers' inner lives into the subject. The film's 7 Oscar nominations, its 'the island' imagery, and its ending — the survivors' questions about the nature of war — made it the most philosophical war film ever made. Its casting is a legend: the film had a 'who's who' of actors (including many whose scenes were cut), and Malick's 20-year absence before it made its arrival an event.",
        "Terrence Malick",
        "The Thin Red Line (1998) — the first hour",
        170,
        "Watch the first hour — the landing, the jungle, the voiceovers — and notice how Malick films war as nature: the grass, the trees, the 'light' the soldiers keep mentioning are the film's real subject, and the battles are intercut with the island's beauty, which is the point. Then watch the ending, where the survivors' questions ('Who's doing this to us?') resolve: the film's argument — that war is a mystery, not a story — is in that finale, and the film's refusal to give the audience a conventional hero made it the decade's most argued-over film.",
        ["War", "1990s", "Hollywood"],
    ),
    _entry(
        "film-the-sixth-sense-1999",
        "The Sixth Sense (1999)",
        "The film with the twist everyone remembers — 'I see dead people.' M. Night Shyamalan's ghost story about a boy who sees the dead and the therapist (Bruce Willis) trying to help him became the decade's most profitable film ($672 million on a $40 million budget), and its ending — the reveal that rewrites the entire film — is the most famous twist of its era. The film earned 6 Oscar nominations, and its 'shyamalan twist' became a genre of its own.",
        "M. Night Shyamalan",
        "The Sixth Sense (1999) — the ending",
        107,
        "Watch the film a second time after knowing the ending — the anniversary dinner, the wedding video, the moments Cole's secret is hidden in plain sight — and notice how Shyamalan plants the twist in every scene: the film is built to be rewatched, and the 'I see dead people' reveal is the key that unlocks it. Then watch the ending, where the truth resolves: the film's argument — that the dead need to be heard, and that healing requires facing what you fear — is in that finale, and the film's box office made the twist ending the decade's dominant cinematic trend.",
        ["Thriller", "1990s", "Hollywood"],
    ),
    _entry(
        "film-the-green-mile-1999",
        "The Green Mile (1999)",
        "Frank Darabont's follow-up to Shawshank — a death-row guard (Tom Hanks) discovers his gentle giant of an inmate (Michael Clarke Duncan) has a healing gift. The film's 'the mouse' (Mr. Jingles), its 'I'm tired, boss' speech, and its 189-minute length made it the decade's great spiritual drama. It earned 4 Oscar nominations, and its mix of miracle and execution — the film's central question about who deserves to die — made audiences weep.",
        "Frank Darabont",
        "The Green Mile (1999) — the 'I'm tired, boss' scene",
        189,
        "Watch the 'I'm tired, boss' scene — John Coffey's confession, his weariness, his acceptance — and notice how the film earns its supernatural premise through performance: Duncan's gentle giant (nominated for the Oscar) is the film's heart, and the execution chamber's ritual is its horror. Then watch the ending, where the film's framing (the aged Paul recounting his gift and his curse) resolves: the film's argument — that mercy is the only real power — is in that finale, and the film's 189 minutes are the most patient mainstream drama of its year.",
        ["Drama", "Fantasy", "1990s", "Hollywood"],
    ),
    _entry(
        "film-being-john-malkovich-1999",
        "Being John Malkovich (1999)",
        "The strangest film ever nominated for major Oscars — a puppeteer (John Cusack) finds a portal on the 7½th floor of an office building that lets you be John Malkovich for 15 minutes. Charlie Kaufman's debut script, Spike Jonze's direction, and Malkovich's game performance (he enters the portal himself) made it the decade's most original film. The 'Malkovich Malkovich' scene is the most audacious in modern comedy. It earned 3 Oscar nominations.",
        "Spike Jonze",
        "Being John Malkovich (1999) — the portal and the ending",
        112,
        "Watch the portal discovery — the 7½th floor (the sets were built with tiny ceilings and low doors), the '15 minutes' rule — and notice how the film builds its fantasy with total commitment: the metaphysics are treated as real, which is what makes the comedy and the horror land. Then watch the ending, where the film's century-spanning final scene resolves: the film's argument — that identity is a vessel we're all desperate to escape — is in that finale, and the film's influence (on everything from Eternal Sunshine to every 'mind-bending comedy' since) is enormous.",
        ["Comedy", "Fantasy", "1990s", "Hollywood"],
    ),
    _entry(
        "film-american-beauty-1999",
        "American Beauty (1999)",
        "The film that swept the Oscars (5 wins including Best Picture) — Lester Burnham's midlife rebellion, the plastic bag in the wind, and the 'look closer' thesis. Sam Mendes' debut made Kevin Spacey and Annette Bening icons of suburban desperation, and the film's most famous scene — the plastic bag floating in the wind, filmed by Wes Bentley's Ricky with a camcorder — became the decade's defining image. The ending, with the blood on the white wall, is the most quoted final scene of the year.",
        "Sam Mendes",
        "American Beauty (1999) — the plastic bag scene and the ending",
        122,
        "Watch the plastic bag scene — Ricky's footage, his narration about 'the most beautiful thing I've ever filmed' — and notice how the film's most famous image is also its thesis: the beauty is in the ordinary, and Lester's whole arc is about learning to see it. Then watch the ending, where the film's final images (the red roses, the blood, the voiceover) resolve: the film's argument — that happiness is a decision made before it's too late — is in that finale, and the film's mix of satire and tenderness made it the defining film of the decade's end.",
        ["Drama", "1990s", "Hollywood"],
    ),
    _entry(
        "film-eyes-wide-shut-1999",
        "Eyes Wide Shut (1999)",
        "Kubrick's final film — Tom Cruise and Nicole Kidman's married couple, a confession, and a descent into a secret society's masked orgy. The film's 400 days of shooting (a Guinness record) and its deliberate, dreamlike pace made it the decade's most misunderstood masterpiece, dismissed on release and re-evaluated as a profound study of jealousy and marriage. The orgy's digital masking (figures inserted to avoid an NC-17) is its most infamous detail, and the ending's 'the most important thing in our lives' is Kubrick's final line of cinema.",
        "Stanley Kubrick",
        "Eyes Wide Shut (1999) — the orgy sequence and the ending",
        159,
        "Watch the orgy sequence — the masked ritual, the 'Fidelio' password, the hallucinatory atmosphere — and notice how Kubrick films the film's central scene as a dream of transgression: the ritual is staged with the precision of a nightmare, and the mystery (who was watching? who was saved?) is the point. Then watch the ending, where the couple's conversation in the toy store resolves: the film's argument — that marriage survives not by avoiding temptation but by choosing each other — is in that final exchange, and the film's last line is the most quietly profound ending in Kubrick's career.",
        ["Drama", "Mystery", "1990s", "Hollywood"],
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
