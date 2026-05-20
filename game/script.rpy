## ============================================================
##  natsu no owari  //  夏の終わり  ("End of Summer")
##  script.rpy  —  main scene
##
##  TWO CHARACTERS:
##    mc    — the protagonist  (player-named, referred to as "Ren" by default)
##    hana  — Hana, mc's girlfriend who initiates the breakup
##
##  STRUCTURE:
##    label start          → name input
##    label festival_day   → arrival, light mood
##    label festival_dusk  → unease begins
##    label riverside      → the breakup
##    label aftermath_stay → choice: stay and talk
##    label aftermath_go   → choice: let her go
##    label ending_stay    → bittersweet closure
##    label ending_go      → quiet, open ending
## ============================================================


# ────────────────────────────────────────────────────────────
#  START  —  player name input
# ────────────────────────────────────────────────────────────

label start:

    $ player_name = renpy.input(
        "What is your name?",
        default="Ren",
        length=16
    ).strip() or "Ren"

    jump festival_day


# ────────────────────────────────────────────────────────────
#  ACT 1  —  THE FESTIVAL  (afternoon → dusk)
# ────────────────────────────────────────────────────────────

label festival_day:

    scene bg festival_day with dissolve
    play music audio.bgm_festival fadeout 0.5 fadein 1.5

    show hana happy at center with dissolve

    narrator "The 47th Nagatsuki Summer Festival. The air smells of yakitori smoke and spilled ramune."

    narrator "Paper lanterns line every stall. Children dart between yukata-clad couples."

    narrator "And Hana is beside me — her hair pinned up with a pale blue kanzashi I gave her last summer."

    mc "I keep losing you in the crowd."

    hana happy "That's because you walk too slow!"

    hana smile "Come on — the goldfish scooping stall closes at seven."

    mc "You've been saying that every year since we were fifteen."

    hana smile "And I've won exactly zero goldfish. Tonight is different."

    mc "That's also what you say every year."

    hana happy "...Shut up and walk faster."

    narrator "She laughs — that bright, unguarded laugh I fell in love with."

    narrator "But somewhere behind her eyes, something is different."

    narrator "I notice it the way you notice a crack in familiar porcelain."

    narrator "Small. Certain."


    ## ── scene transition: dusk ──

    scene bg festival_dusk with dissolve
    play sound audio.sfx_fireworks

    show hana neutral at center with dissolve

    narrator "The sun bleeds out over the river. Lanterns bloom to life one by one."

    narrator "We find a bench near the water's edge, away from the noise."

    mc "You're quiet."

    hana neutral "Am I?"

    mc "You've been quiet since the takoyaki stand. Did something happen?"

    show hana uneasy at center with dissolve

    hana uneasy "No. I just... wanted to watch the lanterns for a bit."

    narrator "She presses her fingers together in her lap."

    narrator "She only does that when she's trying to say something she hasn't found the words for yet."

    mc "Hana."

    hana uneasy "..."

    mc "Talk to me."

    narrator "A long silence. The festival continues behind us, indifferent."

    show hana looking_away at center with dissolve

    hana looking_away "Let's walk. Somewhere quieter."

    narrator "She stands before I can answer."

    narrator "And I already know."


# ────────────────────────────────────────────────────────────
#  ACT 2  —  THE RIVERSIDE  (the breakup)
# ────────────────────────────────────────────────────────────

label riverside:

    scene bg riverside with fade_black
    stop music fadeout 2.0
    play sound audio.sfx_wind

    show hana sad at left with dissolve

    narrator "We reach the stone steps by the river."

    narrator "The festival is still audible — faint taiko drums, a child's laughter —"
    narrator "but here, by the water, it feels far away."

    narrator "Hana stands with her back half-turned, watching the dark current."

    play music audio.bgm_quiet fadein 2.0

    mc "How long have you been holding this?"

    show hana sad at left

    hana sad "..."

    hana sad "Since spring, maybe. I kept telling myself it was just a feeling. That it would pass."

    mc "And did it?"

    show hana looking_away at left with dissolve

    hana looking_away "No."

    narrator "The word lands quietly. That's almost worse than if she'd shouted it."

    mc "Is there someone else?"

    show hana surprised at left with dissolve

    hana surprised "No. God, no. Please don't think that."

    show hana sad at left with dissolve

    hana sad "It's not that. It's... it's us. The shape of us."

    hana sad "We fit perfectly, [player_name]. We always have. And I think that's been the problem."

    mc "Fitting together is a problem?"

    hana sad "When you stop growing because you're so comfortable fitting... yes."

    narrator "I want to argue. I have fifteen counter-arguments ready."

    narrator "But she's crying now. Just slightly. The kind she tries to hide."

    narrator "And I realize every one of those arguments is just fear with better vocabulary."

    stop sound fadeout 1.5
    play music audio.bgm_heartbreak fadein 2.0

    show hana cry at left with dissolve

    hana cry "I love you. I want you to know that isn't the question."

    hana cry "The question is — who are we going to be in ten years if we never ask anything hard of ourselves?"

    hana cry "I've been asking it for months. And the answer scares me."

    mc "So what do you want me to say right now?"

    show hana looking_away at left with dissolve

    hana looking_away "I don't want you to say anything. I just..."

    hana looking_away "I wanted to tell you here. At the festival. Where everything started."

    narrator "Three summers ago. A goldfish scooping stall. She won on her first try and acted surprised."

    narrator "She had been practicing for a week."

    narrator "I never told her I knew."

    play sound audio.sfx_fireworks

    narrator "Fireworks open above the river."

    narrator "Gold, then crimson, then white."

    narrator "Hana watches them with tears still drying on her face."

    narrator "She's never looked more like herself."

    ## ── PLAYER CHOICE ──

    menu:

        "Stay. I'm not ready to let go yet.":
            jump aftermath_stay

        "Let her go. She deserves that much.":
            jump aftermath_go


# ────────────────────────────────────────────────────────────
#  BRANCH A  —  STAY AND TALK
# ────────────────────────────────────────────────────────────

label aftermath_stay:

    show hana sad at left

    mc "I'm not going to pretend I'm okay."

    mc "And I'm not going to walk away from this bench tonight acting like it didn't happen."

    show hana surprised at left with dissolve

    hana surprised "[player_name]..."

    mc "You said you love me. I believe you."

    mc "I love you too. Which means I'm allowed to be wrecked right now."

    show hana cry at left with dissolve

    hana cry "Yes. You are."

    narrator "We stay there on the steps until the fireworks end."

    narrator "Not talking very much. Just existing side by side, the way we always have."

    narrator "The festival crowd begins to thin."

    narrator "At some point, she rests her head on my shoulder."

    narrator "I don't move."

    show hana sad at left with dissolve

    hana sad "I think I'm going to go study abroad. In Kyoto. Next semester."

    hana sad "I've been putting off telling you that too."

    mc "Of course you have."

    mc "...Kyoto. That's not the end of the world."

    hana sad "No. It's not."

    narrator "Neither of us says what we're both thinking."

    narrator "That distance has a way of making 'not the end of the world' feel exactly like that."

    jump ending_stay


# ────────────────────────────────────────────────────────────
#  BRANCH B  —  LET HER GO
# ────────────────────────────────────────────────────────────

label aftermath_go:

    show hana looking_away at left

    mc "Okay."

    show hana surprised at left with dissolve

    hana surprised "...Okay?"

    mc "I mean it. Okay."

    mc "Not 'I'm fine with this.' Not 'this doesn't hurt.'"

    mc "Just... okay. I hear you. And I think you're right, even though I hate that you are."

    show hana cry at left with dissolve

    hana cry "Please don't be kind right now. It makes this harder."

    mc "Then be angry at me. That would help us both."

    hana cry "I can't. I've tried."

    narrator "She covers her mouth. Steadies herself."

    show hana sad at left with dissolve

    hana sad "Will you walk back to the festival with me? Just... for a little while longer."

    hana sad "I don't want to remember this place as only this."

    mc "Yeah. I can do that."

    narrator "We walk back toward the lights."

    narrator "Not holding hands. Not side by side exactly."

    narrator "Just close enough that our arms almost touch."

    jump ending_go


# ────────────────────────────────────────────────────────────
#  ENDINGS
# ────────────────────────────────────────────────────────────

label ending_stay:

    scene bg festival_night with dissolve
    stop music fadeout 2.0

    show hana neutral at right with dissolve

    narrator "We leave when the last stall closes."

    narrator "She squeezes my hand once before she gets in the taxi."

    narrator "Not a promise. Not a goodbye."

    narrator "Just — I see you."

    hide hana with dissolve

    narrator "I stand on the street long after the car is gone."

    narrator "The lanterns are being taken down."

    narrator "One of the paper ones breaks free from its string and lifts into the dark."

    narrator "I watch it until I can't."

    stop music

    narrator "   ─   ─   ─"

    narrator "   夏の終わり。"
    narrator "   The end of summer."
    narrator "   But summer ends every year."

    return


label ending_go:

    scene bg festival_night with dissolve
    stop music fadeout 2.0

    show hana smile at center with dissolve

    narrator "We play one more round of the goldfish scooping stall."

    narrator "She loses. I lose. We both laugh at that."

    narrator "Real laughter — the kind that doesn't know it's supposed to be sad."

    narrator "Around ten, she says she should go."

    show hana neutral at center with dissolve

    hana neutral "Thank you."

    hana neutral "For tonight. For everything."

    mc "Go study in Kyoto."

    mc "Make yourself into whoever you're supposed to be."

    show hana sad at center with dissolve

    hana sad "You too, [player_name]."

    hide hana with dissolve

    narrator "She disappears into the crowd."

    narrator "I stay until the last firework fades."

    narrator "The sky goes dark."

    narrator "The city hums."

    narrator "And I think — maybe this is also a kind of love."

    narrator "The kind that lets go."

    stop music

    narrator "   ─   ─   ─"

    narrator "   夏の終わり。"
    narrator "   The end of summer."
    narrator "   Some things are only beautiful because they end."

    return
