player_sprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . 3 3 3 . . . . . . . 
            . . . . . 3 . . . 3 . . . . . . 
            . . . . . 3 . . . 3 . . . . . . 
            . . . . . . 3 3 3 . . . . . . . 
            . . . . . . 3 3 3 . . . . . . . 
            . . . . . 3 3 3 3 3 . . . . . . 
            . . . . 3 . 3 3 3 . 3 . . . . . 
            . . . 3 . . 3 3 3 . . 3 . . . . 
            . . . . . . 3 3 3 . . . . . . . 
            . . . . . . 3 3 3 . . . . . . . 
            . . . . . . 3 3 3 . . . . . . . 
            . . . . . 3 . . . 3 . . . . . . 
            . . . . 3 . . . . . 3 . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(player_sprite)