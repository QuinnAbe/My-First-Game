
import sys
import os
import getopt
import pygame
pygame.init()


idle_left = [pygame.image.load("Idle/Idle left/Idle left (1).png"), pygame.image.load("Idle/Idle left/Idle left(2).png"), pygame.image.load("Idle/Idle left/Idle left(3).png"),
             pygame.image.load("Idle/Idle left/Idle left(4).png"),
             pygame.image.load("Idle/Idle left/Idle left(5).png"), pygame.image.load("Idle/Idle left/Idle left(6).png"), pygame.image.load("Idle/Idle left/Idle left(7).png"),
             pygame.image.load("Idle/Idle left/Idle left(8).png"),
             pygame.image.load("Idle/Idle left/Idle left(9).png"), pygame.image.load("Idle/Idle left/Idle left(10).png"), pygame.image.load("Idle/Idle left/Idle left(11).png"),
             pygame.image.load("Idle/Idle left/Idle left(12).png"),
             pygame.image.load("Idle/Idle left/Idle left(13).png"), pygame.image.load("Idle/Idle left/Idle left(14).png"), pygame.image.load("Idle/Idle left/Idle left(15).png")]

idle_right = [pygame.image.load("Idle/Idle right/Idle (1).png"), pygame.image.load("Idle/Idle right/Idle (2).png"), pygame.image.load("Idle/Idle right/Idle (3).png"),
              pygame.image.load("Idle/Idle right/Idle (4).png"),
              pygame.image.load("Idle/Idle right/Idle (5).png"), pygame.image.load("Idle/Idle right/Idle (6).png"), pygame.image.load("Idle/Idle right/Idle (7).png"),
              pygame.image.load("Idle/Idle right/Idle (8).png"),
              pygame.image.load("Idle/Idle right/Idle (9).png"), pygame.image.load("Idle/Idle right/Idle (10).png"), pygame.image.load("Idle/Idle right/Idle (11).png"),
              pygame.image.load("Idle/Idle right/Idle (12).png"),
              pygame.image.load("Idle/Idle right/Idle (13).png"), pygame.image.load("Idle/Idle right/Idle (14).png"), pygame.image.load("Idle/Idle right/Idle (15).png"),]

walk_right = [pygame.image.load("Walk/Walk right/Walk (1).png"), pygame.image.load("Walk/Walk right/Walk (2).png"), pygame.image.load("Walk/Walk right/Walk (3).png"),
              pygame.image.load("Walk/Walk right/Walk (4).png"),
              pygame.image.load("Walk/Walk right/Walk (5).png"), pygame.image.load("Walk/Walk right/Walk (6).png"), pygame.image.load("Walk/Walk right/Walk (7).png"),
              pygame.image.load("Walk/Walk right/Walk (8).png"),
              pygame.image.load("Walk/Walk right/Walk (9).png"), pygame.image.load("Walk/Walk right/Walk (10).png"), pygame.image.load("Walk/Walk right/Walk (11).png"),
              pygame.image.load("Walk/Walk right/Walk (12).png"),
              pygame.image.load("Walk/Walk right/Walk (13).png"), pygame.image.load("Walk/Walk right/Walk (14).png"), pygame.image.load("Walk/Walk right/Walk (15).png")]

walk_left = [pygame.image.load("Walk/Walk left/Walk left(1).png"), pygame.image.load("Walk/Walk left/Walk left(2).png"), pygame.image.load("Walk/Walk left/Walk left(3).png"),
             pygame.image.load("Walk/Walk left/Walk left(4).png"),
             pygame.image.load("Walk/Walk left/Walk left(5).png"), pygame.image.load("Walk/Walk left/Walk left(6).png"), pygame.image.load("Walk/Walk left/Walk left(7).png"),
             pygame.image.load("Walk/Walk left/Walk left(8).png"),
             pygame.image.load("Walk/Walk left/Walk left(9).png"), pygame.image.load("Walk/Walk left/Walk left(10).png"), pygame.image.load("Walk/Walk left/Walk left(11).png"),
             pygame.image.load("Walk/Walk left/Walk left(12).png"),
             pygame.image.load("Walk/Walk left/Walk left(13).png"), pygame.image.load("Walk/Walk left/Walk left(14).png"), pygame.image.load("Walk/Walk left/Walk left(15).png")]

dead_ani = [pygame.image.load("Dead/Dead (1).png"), pygame.image.load("Dead/Dead (2).png"), pygame.image.load("Dead/Dead (3).png"), pygame.image.load("Dead/Dead (4).png"),
            pygame.image.load("Dead/Dead (5).png"), pygame.image.load("Dead/Dead (6).png"), pygame.image.load("Dead/Dead (7).png"), pygame.image.load("Dead/Dead (8).png"),
            pygame.image.load("Dead/Dead (9).png"), pygame.image.load("Dead/Dead (10).png"), pygame.image.load("Dead/Dead (11).png"), pygame.image.load("Dead/Dead (12).png"),
            pygame.image.load("Dead/Dead (13).png"), pygame.image.load("Dead/Dead (14).png"), pygame.image.load("Dead/Dead (15).png")]

jump_right = [pygame.image.load("Jump/Jump right/Jump (1) 1.00.42 PM.png"), pygame.image.load("Jump/Jump right/Jump (2) 1.00.42 PM.png"), pygame.image.load("Jump/Jump right/Jump (3) 1.00.42 PM.png"),
              pygame.image.load("Jump/Jump right/Jump (4) 1.00.42 PM.png"),
              pygame.image.load("Jump/Jump right/Jump (5) 1.00.42 PM.png"), pygame.image.load("Jump/Jump right/Jump (6) 1.00.42 PM.png"), pygame.image.load("Jump/Jump right/Jump (7) 1.00.42 PM.png"),
              pygame.image.load("Jump/Jump right/Jump (8) 1.00.42 PM.png"),
              pygame.image.load("Jump/Jump right/Jump (9) 1.00.42 PM.png"), pygame.image.load("Jump/Jump right/Jump (10) 1.00.42 PM.png"), pygame.image.load("Jump/Jump right/Jump (11) 1.00.42 PM.png"),
              pygame.image.load("Jump/Jump right/Jump (12) 1.00.42 PM.png"),
              pygame.image.load("Jump/Jump right/Jump (13) 1.00.42 PM.png"), pygame.image.load("Jump/Jump right/Jump (14) 1.00.42 PM.png"), pygame.image.load("Jump/Jump right/Jump (15) 1.00.42 PM.png"),]

jump_left = [pygame.image.load("Jump/Jump left/Jump left(1) 1.00.42 PM.png"), pygame.image.load("Jump/Jump left/Jump left(2) 1.00.42 PM.png"), pygame.image.load("Jump/Jump left/Jump left(3) 1.00.42 PM.png"),
             pygame.image.load("Jump/Jump left/Jump left(4) 1.00.42 PM.png"),
             pygame.image.load("Jump/Jump left/Jump left(5) 1.00.42 PM.png"), pygame.image.load("Jump/Jump left/Jump left(6) 1.00.42 PM.png"), pygame.image.load("Jump/Jump left/Jump left(7) 1.00.42 PM.png"),
             pygame.image.load("Jump/Jump left/Jump left(8) 1.00.42 PM.png"),
             pygame.image.load("Jump/Jump left/Jump left(9) 1.00.42 PM.png"), pygame.image.load("Jump/Jump left/Jump left(10) 1.00.42 PM.png"), pygame.image.load("Jump/Jump left/Jump left(11) 1.00.42 PM.png"),
             pygame.image.load("Jump/Jump left/Jump left(12) 1.00.42 PM.png"),
             pygame.image.load("Jump/Jump left/Jump left(13) 1.00.42 PM.png"), pygame.image.load("Jump/Jump left/Jump left(14) 1.00.42 PM.png"), pygame.image.load("Jump/Jump left/Jump left(15) 1.00.42 PM.png")]
 
run_right = [pygame.image.load("Run/Run right/Run (1).png"), pygame.image.load("Run/Run right/Run (2).png"), pygame.image.load("Run/Run right/Run (3).png"), pygame.image.load("Run/Run right/Run (4).png"),
             pygame.image.load("Run/Run right/Run (5).png"), pygame.image.load("Run/Run right/Run (6).png"), pygame.image.load("Run/Run right/Run (7).png"), pygame.image.load("Run/Run right/Run (8).png"),
             pygame.image.load("Run/Run right/Run (9).png"), pygame.image.load("Run/Run right/Run (10).png"), pygame.image.load("Run/Run right/Run (11).png"), pygame.image.load("Run/Run right/Run (12).png"),
             pygame.image.load("Run/Run right/Run (13).png"), pygame.image.load("Run/Run right/Run (14).png"), pygame.image.load("Run/Run right/Run (15).png")]

run_left = [pygame.image.load("Run/Run left/Run left(1).png"), pygame.image.load("Run/Run left/Run left(2).png"), pygame.image.load("Run/Run left/Run left(3).png"), pygame.image.load("Run/Run left/Run left(4).png"),
            pygame.image.load("Run/Run left/Run left(5).png"), pygame.image.load("Run/Run left/Run left(6).png"), pygame.image.load("Run/Run left/Run left(7).png"), pygame.image.load("Run/Run left/Run left(8).png"),
            pygame.image.load("Run/Run left/Run left(9).png"), pygame.image.load("Run/Run left/Run left(10).png"), pygame.image.load("Run/Run left/Run left(11).png"), pygame.image.load("Run/Run left/Run left(12).png"),
            pygame.image.load("Run/Run left/Run left(13).png"), pygame.image.load("Run/Run left/Run left(14).png"), pygame.image.load("Run/Run left/Run left(15).png")]


zombiewalk_right = [pygame.image.load("zombie/zombie walk right/Walk (1).png"), pygame.image.load("zombie/zombie walk right/Walk (2).png"),
                    pygame.image.load("zombie/zombie walk right/Walk (3).png"), pygame.image.load("zombie/zombie walk right/Walk (4).png"),
                    pygame.image.load("zombie/zombie walk right/Walk (5).png"), pygame.image.load("zombie/zombie walk right/Walk (6).png"),
                    pygame.image.load("zombie/zombie walk right/Walk (7).png"), pygame.image.load("zombie/zombie walk right/Walk (8).png"),
                    pygame.image.load("zombie/zombie walk right/Walk (9).png"), pygame.image.load("zombie/zombie walk right/Walk (10).png")]

zombiewalk_left = [pygame.image.load("zombie/zombie walk left/Walk left(1).png"), pygame.image.load("zombie/zombie walk left/Walk left(2).png"),
                   pygame.image.load("zombie/zombie walk left/Walk left(3).png"), pygame.image.load("zombie/zombie walk left/Walk left(4).png"),
                   pygame.image.load("zombie/zombie walk left/Walk left(5).png"), pygame.image.load("zombie/zombie walk left/Walk left(6).png"),
                   pygame.image.load("zombie/zombie walk left/Walk left(7).png"), pygame.image.load("zombie/zombie walk left/Walk left(8).png"),
                   pygame.image.load("zombie/zombie walk left/Walk left(9).png"), pygame.image.load("zombie/zombie walk left/Walk left(10).png")]
                
zombieattack_left = [pygame.image.load("zombie/zombie attack left/Attack left(1).png"), pygame.image.load("zombie/zombie attack left/Attack left(2).png"),
                     pygame.image.load("zombie/zombie attack left/Attack left(3).png"), pygame.image.load("zombie/zombie attack left/Attack left(4).png"),
                     pygame.image.load("zombie/zombie attack left/Attack left(5).png"), pygame.image.load("zombie/zombie attack left/Attack left(6).png"),
                     pygame.image.load("zombie/zombie attack left/Attack left(7).png"), pygame.image.load("zombie/zombie attack left/Attack left(8).png")]

zombieattack_right = [pygame.image.load("zombie/zombie attack right/Attack (1).png"), pygame.image.load("zombie/zombie attack right/Attack (2).png"),
                      pygame.image.load("zombie/zombie attack right/Attack (3).png"), pygame.image.load("zombie/zombie attack right/Attack (4).png"),
                      pygame.image.load("zombie/zombie attack right/Attack (5).png"), pygame.image.load("zombie/zombie attack right/Attack (6).png"),
                      pygame.image.load("zombie/zombie attack right/Attack (7).png"), pygame.image.load("zombie/zombie attack right/Attack (8).png")]


bg = pygame.image.load("woods.jpg")

spikes = pygame.image.load("Objects/spike.png")

stars = pygame.image.load("Objects/star.png")

logs = pygame.image.load("Objects/wood.png")

platform = pygame.image.load("Objects/platform.png")






 
