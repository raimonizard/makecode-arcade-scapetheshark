let mySprite: Sprite = null
scene.setBackgroundImage(assets.image`Earth`)
scene.cameraFollowSprite(mySprite)
let myEnemy = sprites.create(assets.image`Shark`, SpriteKind.Enemy)
animation.runImageAnimation(
myEnemy,
assets.animation`SharkMoving`,
500,
true
)
myEnemy.setPosition(160, 120)
myEnemy.setBounceOnWall(true)
mySprite = sprites.create(assets.image`Shiba`, SpriteKind.Player)
mySprite.setScale(0.5, ScaleAnchor.Middle)
mySprite.sayText(":)")
mySprite.setBounceOnWall(true)
controller.moveSprite(mySprite, 20, 20)
myEnemy.follow(mySprite, 10)
game.splash("Scape the shark!")
