def on_a_pressed():
    global mySprite2
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile, effects.ashes, 200)
    mySprite2 = sprites.create_projectile_from_sprite(assets.image("""
            Fish1
        """),
        mySprite,
        mySprite.vx,
        mySprite.vy)
    animation.run_image_animation(mySprite2,
        assets.animation("""
            MovingFish
        """),
        200,
        True)
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            200,
            1,
            255,
            0,
            100,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)
    mySprite2.lifespan = 1200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
    music.play(music.melody_playable(music.power_down),
        music.PlaybackMode.IN_BACKGROUND)
    pause(1000)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_life_zero():
    music.stop_all_sounds()
    game.game_over(False)
    music.play(music.string_playable("C5 A B G A F G E ", 300),
        music.PlaybackMode.IN_BACKGROUND)
    game.set_game_over_effect(False, effects.melt)
    mySprite.start_effect(effects.disintegrate, 500)
    mySprite.destroy()
    game.set_game_over_message(False, "The shark got you!")
info.on_life_zero(on_life_zero)

def on_on_overlap2(sprite2, otherSprite2):
    global SharkLifes, myEnemy
    SharkLifes += -1
    info.change_score_by(100)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
    pause(750)
    music.play(music.create_sound_effect(WaveShape.SINE,
            200,
            600,
            255,
            0,
            150,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    myEnemy = sprites.create(assets.image("""
        Shark1
    """), SpriteKind.enemy)
    myEnemy.set_position(randint(0, 160), randint(0, 120))
    animation.run_image_animation(myEnemy, assets.animation("""
        FishMoving
    """), 300, True)
    myEnemy.follow(mySprite, randint(1, 10))
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

mySprite2: Sprite = None
myEnemy: Sprite = None
mySprite: Sprite = None
scene.camera_follow_sprite(mySprite)
music.play(music.string_playable("E B C5 A B G A F ", 200),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
info.set_life(3)
music.set_volume(100)
scene.set_background_image(assets.image("""
    Earth
"""))
myEnemy = sprites.create(assets.image("""
    Shark
"""), SpriteKind.enemy)
animation.run_image_animation(myEnemy, assets.animation("""
    FishMoving
"""), 300, True)
SharkLifes = 7
myEnemy.set_position(160, 120)
myEnemy.set_bounce_on_wall(True)
mySprite = sprites.create(assets.image("""
    Shiba
"""), SpriteKind.player)
mySprite.set_scale(0.5, ScaleAnchor.MIDDLE)
controller.move_sprite(mySprite, 30, 30)
mySprite.set_bounce_on_wall(True)
mySprite.say_text("Go!")
game.splash("Scape the shark!")
game.splash("Use A to shoot fish!")
myEnemy.follow(mySprite, randint(1, 10))

def on_forever():
    if SharkLifes <= 0:
        music.stop_all_sounds()
        game.game_over(True)
        game.set_game_over_effect(True, effects.confetti)
        game.set_game_over_message(True, "YOU WIN!")
forever(on_forever)
