#!/usr/bin/env python3
"""Batch: ADD 30 handcrafted films.json entries — the 1980s.

Sixth addition batch (v1.0 content pass toward 400 films): the blockbuster
decade and its shadow side — The Empire Strikes Back, Airplane!, The
Elephant Man, Blow Out, The Evil Dead, Das Boot, Fanny and Alexander,
Tootsie, The King of Comedy, Return of the Jedi, Scarface, The Right Stuff,
Videodrome, Amadeus, Ghostbusters, The Terminator, This Is Spinal Tap,
A Nightmare on Elm Street, Once Upon a Time in America, Back to the Future,
The Breakfast Club, Ran, Shoah, Aliens, Stand by Me, Platoon, Ferris
Bueller, and more. Handcrafted teaser + real fact + quality-bar instruction.
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
        "film-the-empire-strikes-back-1980",
        "The Empire Strikes Back (1980)",
        "The sequel that outgrew its original — the darkest, most loved film in the Star Wars saga, with the most famous twist in cinema history: 'No, I am your father.' (The line was never 'Luke, I am your father' — that's the misquote everyone remembers.) Irvin Kershner's film took the fairy tale into adult territory, and the Hoth battle, the asteroid chase, and the carbonite freeze remain the saga's peak.",
        "Irvin Kershner",
        "The Empire Strikes Back (1980) — the twist and the ending",
        124,
        "Watch the duel on Cloud City — the lightsaber fight, the severed hand, the 'No, I am your father' — and notice how the film's twist is built from the whole movie's structure: Luke's impatience, Yoda's warnings, and the cave vision all pay off in that moment. Then watch the ending, where the heroes are scattered and the last shot is a silent stare into space: the film's argument — that hope survives even defeat — is in that final image, and the film's cliffhanger ending was so bold that it convinced studios the sequel could be an art form.",
        ["Sci-Fi", "1980s", "Hollywood"],
    ),
    _entry(
        "film-airplane-1980",
        "Airplane! (1980)",
        "The joke-density champion — a joke every few seconds, most of them visual, delivered deadpan by a cast of dramatic actors (Leslie Nielsen's deadpan 'I am serious, and don't call me Shirley' became his career). Zucker, Abrahams and Zucker's spoof of disaster movies was made for $3.5 million and grossed $83 million, and its rapid-fire style invented the modern parody. It's the film comedy rewatchability was invented for.",
        "Jim Abrahams, David Zucker & Jerry Zucker",
        "Airplane! (1980) — the first twenty minutes",
        88,
        "Watch the first twenty minutes — the airport, the flashback, the 'hospital' run — and notice how the film packs its gags: the jokes come in layers (dialogue, background, props, and the same lines repeated straight-faced), and the deadpan delivery is the secret. Then watch the 'Don't call me Shirley' exchange and the inflatable autopilot: the film's argument — that comedy is timing plus sincerity — is in every frame, and the film's influence on parody (it's the benchmark every spoof since has been measured against) is total.",
        ["Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-the-elephant-man-1980",
        "The Elephant Man (1980)",
        "David Lynch's black-and-white masterpiece about Joseph Merrick, the severely deformed Victorian exhibited as a freak — and the film that proved Lynch could make a studio film without losing his strangeness. John Hurt's transformation (with makeup by Christopher Tucker) earned him an Oscar nomination, and the film's 'I am not an animal! I am a human being!' is one of cinema's great cries. It was nominated for 8 Oscars.",
        "David Lynch",
        "The Elephant Man (1980) — the hospital and the ending",
        124,
        "Watch the first half hour — the fairground, the mob, the 'freak' reveal — and notice how Lynch films Merrick's world in expressionist shadows: the film's black-and-white (shot by Freddie Francis) turns Victorian London into a nightmare cathedral, and the horror is in the crowd, not the man. Then watch the ending, where Merrick sleeps upright and the film's final dissolve — the star, the mother, the peace — lands: the film's argument, that dignity is the only true beauty, is in that last image, and the film's tenderness after Eraserhead's dread announced Lynch as the decade's great double talent.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-blow-out-1981",
        "Blow Out (1981)",
        "Brian De Palma's greatest film — a movie sound-effects man (John Travolta) who accidentally records a car crash that was actually an assassination. The film's obsession with recording, its fireworks finale, and its tragic ending — the scream that becomes a scream effect — make it the decade's most personal political thriller. It's a 'Blow-Up' meets 'The Conversation' conspiracy that ends in despair, and its final image is unforgettable.",
        "Brian De Palma",
        "Blow Out (1981) — the recording and the ending",
        108,
        "Watch the film's central obsession — Jack recording the night air, the crash, the tire-blowout that wasn't — and notice how De Palma builds the mystery from sound: the film is about what a recording can and cannot prove, and the editing turns the audio into the evidence. Then watch the ending, where the film's hope collapses into the final edit: the film's argument — that the truth gets packaged into entertainment — is in that last image, and the film's finale (the scream repurposed as a scream effect) is the most cynical ending of the decade.",
        ["Thriller", "1980s", "Hollywood"],
    ),
    _entry(
        "film-the-evil-dead-1981",
        "The Evil Dead (1981)",
        "The cabin-in-the-woods horror that launched Sam Raimi and Bruce Campbell — made for $350,000 by a gang of Detroit friends, with the camera itself as a villain (Raimi's famous 'crash zoom' POV shots). The film's gore was so extreme it earned the 'video nasty' label in the UK, and its sequel-as-remake (Evil Dead II) became a classic. 'Groovy.'",
        "Sam Raimi",
        "The Evil Dead (1981) — the cabin descent and the ending",
        85,
        "Watch the first hour — the cabin, the tape recording, the first possession — and notice how Raimi's low budget became the style: the shaking, charging camera (a 'shaky-cam' he invented with a plank of wood) makes the forest itself the monster, and the practical effects are gloriously handmade. Then watch the ending, where the film's hero is the last one standing: the film's argument — that horror is best when it's joyful — is in Campbell's performance, and the film's influence (on everything from the Coens' early work to the entire modern horror revival) is enormous for a $350,000 picture.",
        ["Horror", "1980s", "Hollywood"],
    ),
    _entry(
        "film-das-boot-1981",
        "Das Boot (1981)",
        "The definitive submarine film — Wolfgang Petersen's claustrophobic epic about a German U-boat crew in WWII, which refuses to make its sailors heroes or monsters: they're just men in a steel tube waiting to die. Filmed in a full-scale mock-up — a U-boat interior that could tilt and flood — the film's sound design (the pings, the depth charges, the creaking hull) is the greatest in its genre. The 209-minute director's cut is the one to watch.",
        "Wolfgang Petersen",
        "Das Boot (1981) — the depth-charge sequence",
        149,
        "Watch the depth-charge sequence — the crew sweating, the gauges, the pings — and notice how Petersen films the film's central terror: the submarine is a coffin that might be opening, and the film's sound design (recorded with real hydrophones) puts you inside the hull. Then watch the ending, where the boat is sunk by a single plane in port: the film's argument — that war wastes everyone equally — is in that final shot, and the film's rare German perspective on WWII made it the most internationally acclaimed war film of the decade.",
        ["War", "1980s", "German"],
    ),
    _entry(
        "film-fanny-and-alexander-1982",
        "Fanny and Alexander (1982)",
        "Ingmar Bergman's grand farewell — a five-hour family saga (in its TV cut) about two children, their actor family, and their monstrous stepfather, told with more warmth than anything else in Bergman's career. It won 4 Oscars including Best Foreign Language Film, and its Christmas scene — the family feast in the red-draped house — is the most beautiful sequence Bergman ever filmed. He called it his 'summing-up.'",
        "Ingmar Bergman",
        "Fanny and Alexander (1982) — the Christmas scene",
        188,
        "Watch the Christmas sequence — the family, the feast, the grandmother's house — and notice how Bergman films joy without irony: the warmth is genuine, which is what makes the stepfather's arrival so chilling. Then watch the film's later acts, where the children's world turns gothic: the film's argument — that childhood is a theater we never fully leave — is in every scene, and the film's blend of realism, ghost story, and family saga made it the definitive 'director's final statement' of the decade.",
        ["Drama", "1980s", "Swedish"],
    ),
    _entry(
        "film-tootsie-1982",
        "Tootsie (1982)",
        "The gender comedy that won the decade — Dustin Hoffman's out-of-work actor who becomes 'Dorothy Michaels' to land a soap opera role, then discovers that being a woman is a masterclass in how the world treats them. Hoffman spent hours in full makeup learning how men look at women, and the film's 10 Oscar nominations (including Hoffman's) made it the most respected comedy of its era. The 'I was a better man with you as a woman' scene is its heart.",
        "Sydney Pollack",
        "Tootsie (1982) — the soap opera scenes and the ending",
        116,
        "Watch the film's first act — Michael's audition failure, the transformation, the first day on set — and notice how Hoffman's performance is built from real experience: he had himself treated as 'Dorothy' in public, and the film's comedy is rooted in the humiliation he observed. Then watch the ending, where Michael reveals himself on live TV: the film's argument — that being a woman is the hardest role there is, and that Dorothy was the better man — is in that reveal, and the film's influence (it inspired a generation of gender comedies, and Murray's ad-libbed 'better man' line is one of cinema's great improvised moments).",
        ["Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-the-king-of-comedy-1982",
        "The King of Comedy (1982)",
        "The most uncomfortable comedy ever made — Robert De Niro's Rupert Pupkin, a delusional aspiring comic who kidnaps a talk-show host to get on television. Martin Scorsese's film flopped on release and was re-evaluated as prophecy: it predicted reality TV, stan culture, and the American hunger for fame at any cost. The ending, where Pupkin gets his 15 minutes, is the most ironic in cinema.",
        "Martin Scorsese",
        "The King of Comedy (1982) — the kidnap plan and the ending",
        109,
        "Watch the film's central comedy — Pupkin rehearsing in his basement with cardboard cutouts, the 'you're not famous' rejections — and notice how De Niro plays the delusion with total sincerity: the film's terror is that Pupkin believes, and the audience starts to, too. Then watch the ending, where Pupkin's stand-up set airs to the nation: the film's argument — that fame is a lottery the desperate are willing to die for — is in that final sequence, and the film's prophecy (every reality show is a Rupert Pupkin) has only sharpened with time.",
        ["Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-return-of-the-jedi-1983",
        "Return of the Jedi (1983)",
        "The trilogy closer that swapped the saga's darkness for its joy — the rescue of Han, the Ewoks, the second Death Star, and the redemption that the whole trilogy was building toward: 'I am a Jedi, like my father before me.' The film's throne-room duel between Luke, Vader, and the Emperor is the saga's moral core, and the film's famous 'celebration' ending (in its original form) was restored in later editions.",
        "Richard Marquand",
        "Return of the Jedi (1983) — the throne room and the ending",
        131,
        "Watch the throne-room sequence — the Emperor's temptation, the lightsaber, the moment Vader chooses his son — and notice how the film pays off the trilogy's theme: Luke refuses to strike, and that refusal is what saves everything. Then watch the ending, where the galaxy celebrates and the spirits of the redeemed look on: the film's argument — that the cycle of violence ends when someone refuses to fight — is in that final image, and the film's tonal shift (from Empire's despair to Jedi's hope) made it the trilogy's most debated and most loved ending.",
        ["Sci-Fi", "1980s", "Hollywood"],
    ),
    _entry(
        "film-scarface-1983",
        "Scarface (1983)",
        "The most excessive film ever made by a major studio — Al Pacino's Tony Montana, a Cuban refugee who becomes Miami's kingpin, with a mountain of cocaine, a chainsaw, and the most quoted line in gangster cinema: 'Say hello to my little friend.' Oliver Stone wrote it, Brian De Palma directed it, and the film's moral — that greed is a bullet with your name on it — is delivered with the decade's greatest excess. The remake of the 1932 original became the definitive gangster epic for a new generation.",
        "Brian De Palma",
        "Scarface (1983) — the ending",
        170,
        "Watch the final assault — the mansion, the cocaine, the 'Say hello to my little friend' — and notice how De Palma stages the film's moral as spectacle: Tony destroys everyone including himself, and the film's violence is its judgment. Then watch the opening, the 'World Is Yours' globe and the refugee processing, which plants the film's theme — the American dream as a pyramid of bodies — from the first frame: the film's argument, that the immigrant dream can curdle into the immigrant nightmare, made it the most influential gangster film of its decade, quoted by rappers and re-released to generations.",
        ["Crime", "1980s", "Hollywood"],
    ),
    _entry(
        "film-the-right-stuff-1983",
        "The Right Stuff (1983)",
        "The greatest American epic about heroes who aren't sure they're heroes — Philip Kaufman's adaptation of Tom Wolfe's book about the Mercury Seven astronauts and the test pilots (led by Sam Shepard's Chuck Yeager) who broke the sound barrier. The film's blend of soaring spectacle and deadpan comedy ('No bucks, no Buck Rogers'), its 4 Oscars, and its line 'The right stuff' made it the definitive film about American courage.",
        "Philip Kaufman",
        "The Right Stuff (1983) — the sound-barrier flights and the ending",
        193,
        "Watch the X-1 flight sequences — Yeager breaking the sound barrier, the shimmer, the silence — and notice how Kaufman films flight as both physics and mysticism: the test pilots are cowboys in a world of engineers, and the film's hero worship is earned by its humor. Then watch the ending, where Yeager's solo flight after the astronauts' parade lands the film's thesis: the film's argument — that the real right stuff is the willingness to risk it alone — is in that final flight, and the film's mix of awe and irony made it the decade's great American epic.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-videodrome-1983",
        "Videodrome (1983)",
        "The most prophetic horror film of the century — David Cronenberg's cable-TV executive (James Woods) who discovers a pirate signal that infects its viewers with a tumor that grows hallucinations. 'Long live the new flesh.' Made in 1983, it predicted reality TV, body modification, and the way screens colonize our nervous systems. The film's practical effects — the TV that breathes, the gun that grows into a hand — remain unsurpassed.",
        "David Cronenberg",
        "Videodrome (1983) — the TV and the ending",
        87,
        "Watch the film's first half — the signal, the hallucinations, the 'Videodrome' tape — and notice how Cronenberg stages the film's thesis visually: the media is a body, the body is a screen, and the line between watching and being watched dissolves. Then watch the ending, where Max commits the act the signal demands: the film's argument — that we become what we consume, and that television was always a weapon — is in that final image, and the film's influence (on everything from cyberpunk to the modern horror revival) grows every year.",
        ["Horror", "Sci-Fi", "1980s", "Hollywood"],
    ),
    _entry(
        "film-terms-of-endearment-1983",
        "Terms of Endearment (1983)",
        "The film that made you laugh and cry in the same scene — Shirley MacLaine's Aurora and Debra Winger's Emma, a mother-daughter war of love across decades, with Jack Nicholson's ex-astronaut neighbor ('Give my daughter the shot!'). It won 5 Oscars including Best Picture, and its hospital finale — the most famous 'running to the hospital' scene in cinema — is the decade's most devastating.",
        "James L. Brooks",
        "Terms of Endearment (1983) — the hospital scene",
        132,
        "Watch the film's tone-shifting engine — Aurora's meddling, Emma's rebellion, the comedy of a lifetime — and notice how Brooks (a TV comedy director making his debut) balances the laughs and the tears: the film's grief only works because the warmth was real. Then watch the ending, where Aurora fights the nurses for her daughter: the film's argument — that a mother's love is the most unreasonable force on Earth — is in that scene, and Nicholson's one-scene Oscar-winning turn (he improvised much of it) is the film's secret weapon.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-amadeus-1984",
        "Amadeus (1984)",
        "The film that made classical music a movie star — F. Murray Abraham's Salieri, who confesses to poisoning Mozart out of envy, and Tom Hulce's Mozart, a giggling genius who writes the music of God. Miloš Forman shot on real Prague locations with real period instruments, and the film won 8 Oscars including Best Picture. The 'too many notes' scene and the Requiem's completion are the film's twin peaks.",
        "Miloš Forman",
        "Amadeus (1984) — the 'too many notes' scene and the Requiem",
        160,
        "Watch the 'too many notes' scene — the Emperor's court, the transcription, Salieri's agony — and notice how the film dramatizes genius: the music is the plot, and Hulce's Mozart conducts it into existence while Abraham's Salieri watches his own mediocrity in real time. Then watch the ending, where Salieri dictates the Requiem as Mozart dictates from his deathbed: the film's argument — that envy is the only sin God punishes — is in that final scene, and the film's insistence that Mozart's music is divine made it the most influential music film ever made.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-ghostbusters-1984",
        "Ghostbusters (1984)",
        "The comedy that became a universe — Bill Murray, Dan Aykroyd, Harold Ramis, and Ernie Hudson as the scientists who go into business busting ghosts, with the Stay Puft Marshmallow Man and the most famous theme song in comedy ('Who you gonna call?'). It was the highest-grossing comedy of its decade, and its mix of genuine effects, horror-comedy, and Murray's deadpan ('He slimed me.') made it endlessly rewatchable.",
        "Ivan Reitman",
        "Ghostbusters (1984) — the library opening and the ending",
        105,
        "Watch the opening — the library ghost, the 'We're ready to believe you,' the proton packs — and notice how the film builds its world with straight faces: the comedy is in the sincerity, and the special effects (the Library Ghost's floating books) were state of the art. Then watch the ending, where the marshmallow man stomps Manhattan and the Ghostbusters face the giant: the film's argument — that science plus friendship beats any apocalypse — is in that finale, and the film's four-character chemistry (all four actors improvised constantly) is the reason it's still quoted daily.",
        ["Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-the-terminator-1984",
        "The Terminator (1984)",
        "The $6.4 million film that made James Cameron and Arnold Schwarzenegger — a killer robot sent back in time to erase the future's resistance leader. The film's chase structure, its stop-motion endoskeleton, and its 'I'll be back' (originally written as 'I'll come back,' changed on set) invented the modern action film. The sequel would cost 15 times as much; this one is lean, mean, and perfect.",
        "James Cameron",
        "The Terminator (1984) — the nightclub chase and the ending",
        107,
        "Watch the nightclub sequence — the mirrors, the shotgun, the first real look at the endoskeleton — and notice how Cameron builds the film's budget into style: the chase is relentless, the effects are practical, and Schwarzenegger's Terminator is a machine played with terrifying precision. Then watch the ending, where the film's time-loop logic closes: the film's argument — that the future is not fixed — is in the final shot, and the film's influence (every 'unstoppable killer' film, every time-travel thriller, every Arnold movie) traces back to this lean original.",
        ["Sci-Fi", "Action", "1980s", "Hollywood"],
    ),
    _entry(
        "film-this-is-spinal-tap-1984",
        "This Is Spinal Tap (1984)",
        "The mockumentary that invented a genre — Rob Reiner's fake rock band, Spinal Tap, with amps that 'go to eleven,' a Stonehenge set that's too small, and a string of drummers who keep dying. The film is so real that fans still think it's a documentary, and its improvisation (the band members wrote their own songs) made it the template for every fake-anything film since — including The Office.",
        "Rob Reiner",
        "This Is Spinal Tap (1984) — the 'go to eleven' scene",
        82,
        "Watch the 'go to eleven' scene — Nigel explaining his amp's volume knob, the interview's escalating absurdity — and notice how the film's comedy is 100% sincerity: the actors never once break character, and the deadpan is the whole joke. Then watch the Stonehenge debacle and the 'Shark Sandwich' review: the film's argument — that rock stardom is a beautiful fraud — is in every scene, and the film's influence (it coined the phrase 'mockumentary' for a generation and is quoted by actual bands) made it the funniest film ever made about music.",
        ["Comedy", "1980s", "Hollywood"],
    ),
    _entry(
        "film-a-nightmare-on-elm-street-1984",
        "A Nightmare on Elm Street (1984)",
        "The horror film that made dreams the enemy — Wes Craven's Freddy Krueger, who kills teenagers in their sleep, where they can't fight back. Robert Englund's burned, wisecracking killer and the film's inventive dream-deaths (the body-bag scene, the 'this is God' moment) made it the defining horror franchise of the 1980s. The film cost $1.8 million and grossed $26 million, and Freddy's glove became the genre's most famous prop.",
        "Wes Craven",
        "A Nightmare on Elm Street (1984) — the bathtub scene and the ending",
        91,
        "Watch the film's first dream sequence — the boiler room, the glove scraping metal, the first kill — and notice how Craven builds the horror from the dream logic: the sets bend, the rules shift, and the film's central question — how do you fight what you can't wake from? — is its engine. Then watch the ending, where the film's final image suggests the nightmare was never over: the film's argument — that childhood fears never fully leave — is in that last shot, and the film's blend of terror and black comedy made Freddy the first horror icon who was fun to root for.",
        ["Horror", "1980s", "Hollywood"],
    ),
    _entry(
        "film-once-upon-a-time-in-america-1984",
        "Once Upon a Time in America (1984)",
        "Sergio Leone's last film and his masterpiece — a four-hour (in its restored cut) epic of Jewish gangsters in New York, from childhood to old age, told in flashbacks that refuse to be chronological. Ennio Morricone's score (the 'Deborah's Theme') is among the greatest ever written, and Robert De Niro's Noodles is the film's haunted center. The studio's recut version was a disaster; the restored cut is one of the greatest films ever made.",
        "Sergio Leone",
        "Once Upon a Time in America (1984) — the ending",
        229,
        "Watch the film's structure — the 1933 massacre, the opium flashbacks, the 1968 return — and notice how Leone's editing makes memory the plot: the film moves through time the way Noodles moves through his own head, and the past is never past. Then watch the ending, where the film's final scene recontextualizes everything: the film's argument — that a life is a story told to itself, and that friendship and betrayal are the same coin — is in that last image, and the film's 229-minute patience is rewarded by the decade's greatest ending.",
        ["Crime", "1980s", "Hollywood"],
    ),
    _entry(
        "film-back-to-the-future-1985",
        "Back to the Future (1985)",
        "The perfect entertainment machine — Marty McFly accidentally goes back to 1955 and must make sure his parents fall in love or he'll cease to exist. Michael J. Fox replaced Eric Stoltz six weeks into filming (the studio realized the role needed comedy), the DeLorean needed '1.21 gigawatts' (the script originally said 'jigawatts'), and the film's clock-tower finale is the most satisfying last 20 minutes in blockbuster history. It grossed $381 million.",
        "Robert Zemeckis",
        "Back to the Future (1985) — the ending",
        116,
        "Watch the film's first act — the DeLorean, the '1.21 gigawatts,' the first time jump — and notice how the film's script (by Zemeckis and Bob Gale, rejected by every studio for years) plants every payoff: the clock tower, the skateboard, the 'Johnny B. Goode' — all set up before the first jump. Then watch the ending, where Marty races the lightning: the film's argument — that the future is made of choices, not fate — is in that final scene, and the film's airtight construction (every detail pays off) made it the benchmark for how to build a crowd-pleaser.",
        ["Sci-Fi", "1980s", "Hollywood"],
    ),
    _entry(
        "film-the-breakfast-club-1985",
        "The Breakfast Club (1985)",
        "The film that defined a generation of teenagers — five archetypes (the brain, the athlete, the basket case, the princess, the criminal) in Saturday detention, forced to actually talk to each other. John Hughes' film turned the Brat Pack into icons, and its ending — 'Dear Mr. Vernon' — with Simple Minds' 'Don't You (Forget About Me)' swelling, is the most famous closing scene of the decade. 'Does Barry Manilow know you raid his wardrobe?'",
        "John Hughes",
        "The Breakfast Club (1985) — the letter and the ending",
        97,
        "Watch the film's middle — the confessions, the 'screaming' scene, the 'you see us as you want to see us' speech — and notice how Hughes builds the film from talk: the detention room is a pressure cooker, and each character's mask comes off one scene at a time. Then watch the ending, where the letter is read over the montage: the film's argument — that teenagers are more than their labels, and that one day of honesty can change everything — is in that final scene, and the film's anthem ('Don't You Forget About Me') has soundtracked every high-school ending since.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-ran-1985",
        "Ran (1985)",
        "Kurosawa's King Lear — an aging warlord divides his kingdom among his sons, and the world burns. It took the 75-year-old director ten years to fund (he painted the storyboards himself, and they're exhibited as art), and it was Japan's most expensive film at the time. The battle sequences — filmed with thousands of extras in real armor, shot from a distance so the death reads as chaos — are the most overwhelming images in cinema. It won the Oscar for Best Costume Design.",
        "Akira Kurosawa",
        "Ran (1985) — the first battle and the ending",
        162,
        "Watch the first battle — the burning castle, the thousands of horsemen, the color-coded armies — and notice how Kurosawa films war as painting: the long shots refuse close-ups, and the carnage becomes abstract, which is the point — the warlord watches his world burn from a distance. Then watch the ending, where the blind Tsurumaru stands at the cliff's edge and the film cuts to the god who watches: the film's argument — that humanity is a madness the universe observes — is in that final image, and the film's combination of Shakespeare, Noh theater, and pure cinema made it the greatest late work of the greatest director.",
        ["Drama", "1980s", "Japanese"],
    ),
    _entry(
        "film-shoah-1985",
        "Shoah (1985)",
        "The greatest documentary ever made, by near-consensus — Claude Lanzmann's nine-and-a-half-hour oral history of the Holocaust, assembled from interviews with survivors, witnesses, and perpetrators, filmed over 11 years on the actual sites. There is no archival footage, no music, no narrator: just faces, places, and the unbearable details. Roger Ebert called it 'the film about the Holocaust that must be seen.'",
        "Claude Lanzmann",
        "Shoah (1985) — the Treblinka testimony",
        120,
        "Watch the testimonies — the survivor describing the arrival ramp, the former SS man describing the gas chamber — and notice how Lanzmann's method (long takes, patient questions, no archival images) forces you to build the horror in your own mind: the film trusts the witness and the viewer completely. Then watch the sequences filmed at the present-day sites, where the grass has grown over the mass graves: the film's argument — that memory is the only monument — is in those fields, and the film's refusal to explain or judge is its moral power.",
        ["Documentary", "1980s", "French"],
    ),
    _entry(
        "film-the-color-purple-1985",
        "The Color Purple (1985)",
        "The film that proved Spielberg could do more than blockbusters — his adaptation of Alice Walker's Pulitzer-winning novel about Celie, a Black woman in the Jim Crow South who writes letters to God. It introduced Whoopi Goldberg and Oprah Winfrey to cinema, earned 11 Oscar nominations (including Spielberg's first directing nom), and its 'Dear God' letters and the 'Shug and Celie' relationship broke ground for its time. The ending's reunion is one of cinema's great catharses.",
        "Steven Spielberg",
        "The Color Purple (1985) — the ending",
        154,
        "Watch the film's letters — Celie's voiceover, the abuse, the 'Dear God' — and notice how Spielberg turns Walker's epistolary novel into images: the film's beauty (the purple flowers, the singing) is the resistance, and Goldberg's performance (her film debut) carries decades in her eyes. Then watch the ending, where the sisters reunite and Celie finally says 'I'm poor, I'm Black, I may even be ugly — but dear God, I'm here': the film's argument — that dignity survives everything — is in that scene, and the film's 11 nominations (winning none) remains one of the Oscars' great injustices.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-aliens-1986",
        "Aliens (1986)",
        "The sequel that changed the rules — James Cameron took Ridley Scott's haunted-house horror and turned it into a war movie, with Sigourney Weaver's Ripley returning to the colony as a marine's last hope. The film's 'Game over, man!', its 'Get away from her, you bitch!', and its power-loader showdown with the Queen made it the benchmark for action sequels. It earned Weaver the first Oscar nomination for an action performance.",
        "James Cameron",
        "Aliens (1986) — the marines' first contact and the ending",
        137,
        "Watch the marines' descent — the sealed colony, the motion trackers, the 'they're coming outta the goddamn walls' — and notice how Cameron builds the film's two hours of tension from the first act's calm: the marines' confidence is the setup, and the ambush is the payoff. Then watch the ending, where Ripley faces the Queen in the power loader: the film's argument — that motherhood (Ripley and Newt) is the film's true subject — is in that final battle, and the film's blend of horror, war movie, and family drama made it the greatest sequel ever made.",
        ["Sci-Fi", "Action", "1980s", "Hollywood"],
    ),
    _entry(
        "film-top-gun-1986",
        "Top Gun (1986)",
        "The film that made Tom Cruise a superstar and the Navy's recruitment numbers soar — Maverick, Goose, the F-14s, and the most famous beach volleyball scene in cinema. Tony Scott shot real aircraft with real pilots, and the film's 'You've lost that lovin' feelin'' bar scene and its 'I feel the need, the need for speed' became pop-culture shorthand. It grossed $356 million and won the Oscar for Best Original Song.",
        "Tony Scott",
        "Top Gun (1986) — the opening carrier scene and the ending",
        110,
        "Watch the opening — the carrier deck, the launches, Kenny Loggins' 'Danger Zone' — and notice how Scott shoots the jets like a music video: the sun flares, the cockpit POVs, and the engines' roar make flight the film's real subject. Then watch the ending, where Maverick's final dogfight honors Goose's memory: the film's argument — that a pilot's edge is heart, not hardware — is in that finale, and the film's influence (it turned the Navy's TOPGUN program into a national institution) is the largest of any action film of its decade.",
        ["Action", "1980s", "Hollywood"],
    ),
    _entry(
        "film-stand-by-me-1986",
        "Stand by Me (1986)",
        "The best Stephen King adaptation ever made — four boys walk the railroad tracks to find a body, and find themselves instead. Rob Reiner's film of King's novella 'The Body' made River Phoenix a star, and its leech scene, its 'Lard-Ass Hogan' story, and its ending — the adult narrator writing 'I never had any friends later on like the ones I had when I was twelve' — are the decade's most tender moments.",
        "Rob Reiner",
        "Stand by Me (1986) — the train scene and the ending",
        89,
        "Watch the walk — the four boys, the tracks, the argument about Goofy — and notice how Reiner films the journey as both adventure and elegy: the boys' world (the junk yard, the junkyard dog, the leeches) is vivid, and the danger is real enough to matter. Then watch the ending, where the adult Gordie's voiceover delivers the film's last lines: the film's argument — that childhood friendships are the ones you measure everything else against — is in that final scene, and the film's four young leads (including a pre-fame Kiefer Sutherland as Ace) are the decade's best young ensemble.",
        ["Drama", "1980s", "Hollywood"],
    ),
    _entry(
        "film-platoon-1986",
        "Platoon (1986)",
        "The Vietnam film that finally told it straight — Oliver Stone's semi-autobiographical account of his own infantry tour, where the enemy is as much within as without. The film's 'we've been kicking ass for so long, I'm asking what's it all about?' and its ending — Charlie Sheen's narrator carried away on the chopper as Adagio for Strings swells — made it the definitive grunt's-eye war film. It won 4 Oscars including Best Picture.",
        "Oliver Stone",
        "Platoon (1986) — the village scene and the ending",
        120,
        "Watch the village sequence — the search, the abuse, the 'you call this a war?' — and notice how Stone films the moral collapse of his platoon: the film's two sergeants (Willem Dafoe's Sgt. Elias, Tom Berenger's Sgt. Barnes) are the film's conscience split in two, and the mud and fear are documentary-real. Then watch the ending, where the film's final shot carries the dead: the film's argument — that the war's true casualties were the soldiers themselves — is in that image, and the film's unglamorous realism (Stone's own letters home became the narration) changed how America saw its veterans.",
        ["War", "1980s", "Hollywood"],
    ),
    _entry(
        "film-ferris-buellers-day-off-1986",
        "Ferris Bueller's Day Off (1986)",
        "The ultimate skip-school fantasy — Matthew Broderick's Ferris, who fakes sick, steals a Ferrari, and leads all of Chicago in a parade. John Hughes' love letter to his hometown (the parade scene was shot at the real Von Steuben Day parade) and the film's fourth-wall-breaking asides made it the decade's most joyful comedy. 'Life moves pretty fast. If you don't stop and look around once in a while, you could miss it.'",
        "John Hughes",
        "Ferris Bueller's Day Off (1986) — the parade scene and the ending",
        103,
        "Watch the parade sequence — the floats, the 'Twist and Shout,' Ferris commandeering the float — and notice how Hughes stages the film's thesis as public spectacle: the whole city celebrates the truant, and the lip-synced joy is the film's heart. Then watch the ending, where Ferris's 'Life moves pretty fast' speech and the final freeze-frame land: the film's argument — that youth is a license to look around — is in that last image, and the film's cameos (his sister's 'I weep for the future' is delivered by Charlie Sheen) make it endlessly rewatchable.",
        ["Comedy", "1980s", "Hollywood"],
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
