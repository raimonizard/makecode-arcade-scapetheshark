controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.scale += -0.1
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    sprites.destroyAllSpritesOfKind(SpriteKind.Projectile, effects.ashes, 200)
    mySprite2 = sprites.createProjectileFromSprite(assets.image`Fish1`, mySprite, mySprite.vx, mySprite.vy)
    animation.runImageAnimation(
    mySprite2,
    assets.animation`MovingFish`,
    200,
    true
    )
    music.play(music.createSoundEffect(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
    mySprite2.lifespan = 1200
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.InBackground)
    pause(1000)
})
info.onLifeZero(function () {
    music.stopAllSounds()
    game.gameOver(false)
    music.play(music.stringPlayable("C5 A B G A F G E ", 300), music.PlaybackMode.InBackground)
    game.setGameOverEffect(false, effects.melt)
    mySprite.startEffect(effects.disintegrate, 500)
    mySprite.destroy()
    game.setGameOverMessage(false, "The shark got you!")
})
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    mySprite.scale += 0.1
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    SharkLifes += -1
    info.changeScoreBy(100)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
    pause(750)
    music.play(music.createSoundEffect(WaveShape.Sine, 200, 600, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    myEnemy = sprites.create(assets.image`Shark1`, SpriteKind.Enemy)
    myEnemy.setPosition(randint(0, 160), randint(0, 120))
    animation.runImageAnimation(
    myEnemy,
    assets.animation`FishMoving`,
    300,
    true
    )
    myEnemy.follow(mySprite, randint(1, 10))
})
let mySprite2: Sprite = null
let myEnemy: Sprite = null
let mySprite: Sprite = null
scene.cameraFollowSprite(mySprite)
music.play(music.stringPlayable("C5 C C5 D B D A E ", 200), music.PlaybackMode.LoopingInBackground)
info.setLife(3)
music.setVolume(100)
scene.setBackgroundImage(assets.image`Earth`)
myEnemy = sprites.create(assets.image`Shark`, SpriteKind.Enemy)
animation.runImageAnimation(
myEnemy,
assets.animation`FishMoving`,
300,
true
)
let SharkLifes = 7
myEnemy.setPosition(160, 120)
myEnemy.setBounceOnWall(true)
mySprite = sprites.create(assets.image`Shiba`, SpriteKind.Player)
mySprite.setScale(0.5, ScaleAnchor.Middle)
controller.moveSprite(mySprite, 30, 30)
mySprite.setBounceOnWall(true)
mySprite.sayText("Go!")
game.splash("Scape the sharks", "Move with the arrows")
game.splash("Use A to shoot fish", "Use B to shrink")
myEnemy.follow(mySprite, randint(1, 10))
forever(function () {
    if (SharkLifes <= 0) {
        music.stopAllSounds()
        game.gameOver(true)
        game.setGameOverEffect(true, effects.confetti)
        game.setGameOverMessage(true, "YOU WIN!")
    }
})
