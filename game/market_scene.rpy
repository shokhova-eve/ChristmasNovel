label market_scene:
    
    scene bg market

    "The Christmas Market is alive with twinkling lights, the scent of spices, and cheerful chatter filling the air."
    r "Wow, this place is magical! Where do we start?"

    # Group settles in with drinks
    "The group gathers around a small wooden table, steaming cups in their hands."
    "Rima, Ania, and Nissa hold vibrant red mugs of fruchtpunsch, while Juls, Jane, and the MC sip from darker glühwein cups."
    "Luna sits at Rima’s feet, her tail wagging, wearing a shimmering collar that softly glows."

    menu:
        "Ask about Luna's collar":
            jump luna_collar

        "Visit the cruelty-free tea and chocolate stand with Rima":
            jump tea_chocolates

        "Check out the traditional candle stand with Jane":
            jump candles

        "Explore the Christmas tree decor stand with Ania":
            jump decor

        "Follow Juls and the reindeer":
            jump reindeer_mishap

label luna_collar:
    a "Luna’s collar looks... magical. What’s the story behind it?"
    r "Oh, it’s an enchanted anti-anxiety collar. Crowds make her nervous, so I thought this might help."
    j "Anti-anxiety, you say?"
    "Juls grins mischievously and takes the collar from Luna, holding it up to the MC."
    j "Here, try it on. You’ve been jittery about that mysterious girl you want to impress!"
    r "Hey, give it back to Luna!"
    a "Juls, stop teasing."
    "Rima retrieves the collar and gently puts it back on Luna, who gives a soft bark of approval."
    return

label tea_chocolates:
    r "You’ll love this stand. They have cruelty-free organic chocolates and teas."
    scene bg_tea_chocolates with dissolve
    r "These truffles are made with ethically sourced cocoa. Try one!"
    u "This is amazing. The tea smells incredible too."
    "Luna sniffs the air curiously but remains calm, her glowing collar keeping her at ease."
    return

label candles:
    e "Let me show you the traditional candle stand. It’s a must-see!"
    scene bg_candles with dissolve
    e "These are hand-poured and scented with authentic holiday fragrances."
    u "This one’s perfect. It even has tiny snowflake details."
    return

label decor:
    a "Over here! The Christmas tree decor stand has the cutest ornaments."
    scene bg_tree_decor with dissolve
    a "Look at this glass snowflake. Isn’t it beautiful?"
    u "It’s perfect. She’d love it."
    return

label reindeer_mishap:
    scene bg_reindeer_stable with dissolve
    "Luna suddenly bolts toward a woman carrying a small velvet bag, accidentally bumping into her."
    "The bag falls to the ground, spilling a fine, shimmering powder."
    j "Ooh, what’s this?"
    "Juls picks up the bag before the woman can retrieve it."
    woman "Hey, careful with that! It’s fairy dust for the reindeers!"
    j "Fairy dust? For flying reindeers? This is going to be fun!"
    "Before anyone can stop her, Juls sprinkles the powder onto one of the reindeer."
    "The reindeer snorts, then suddenly leaps into the air, soaring over the market!"
    scene bg_market_chaos with shake
    "Juls lets out a wild laugh as the crowd erupts in chaos."
    j "Best. Idea. Ever!"
    u "Juls, what have you done?!"
    "Stalls topple as the reindeer flies erratically, drawing gasps and cheers from the crowd."
    r "We need to get out of here, now!"
    scene bg_christmas_market_exit with fade
    "The group regathers outside the market, panting."
    a "Let’s not do that again."
    r "Luna, you okay?"
    "Luna wags her tail, seemingly unfazed, thanks to her magical collar."
    j "Totally worth it."
    return
