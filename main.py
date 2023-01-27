mySprite: Sprite = None
scene.set_background_image(assets.image("""
    Earth
"""))
scene.camera_follow_sprite(mySprite)
myEnemy = sprites.create(assets.image("""
    Shark
"""), SpriteKind.enemy)
animation.run_image_animation(myEnemy,
    assets.animation("""
        SharkMoving
    """),
    500,
    True)
myEnemy.set_position(160, 120)
myEnemy.set_bounce_on_wall(True)
mySprite = sprites.create(assets.image("""
    Shiba
"""), SpriteKind.player)
mySprite.set_scale(0.5, ScaleAnchor.MIDDLE)
mySprite.say_text(":)")
mySprite.set_bounce_on_wall(True)
controller.move_sprite(mySprite, 20, 20)
myEnemy.follow(mySprite, 10)
game.splash("Scape the shark!")