from PIL import Image
import os, sys
import random

num_generated_images = 25

hands_path = "./hands_no_bg_resized/"
faces_path = "./img_align_celeba/"
output_path = "./combined/"

#hands_path = "D:/UofT/Fall22/capstone/tests/other_hands/"
#faces_path = "D:/UofT/Fall22/capstone/tests/other_faces/"
#output_path = "D:/UofT/Fall22/capstone/tests/combined_other/"

hands_list = os.listdir( hands_path )
faces_list = os.listdir( faces_path )

def combine():

    count = 0
    
    for face in faces_list:
        
        # Get image of face
        face_im = Image.open(faces_path + face)
        fname = os.path.basename(face)
        
        # Get image of hand
        chosen_hand = random.choice(hands_list)
        hand_im = Image.open(hands_path + chosen_hand)
        angle = random.randrange(0,360,10)
        hand_im = hand_im.rotate(angle)

        # Place hand over face
        face_im.paste(hand_im, (20,50), mask=hand_im)

        # Save resulting image
        face_im.save(output_path + fname, 'PNG', quality=90)

        count += 1

        if (count > num_generated_images):
            break

combine()

"""
path = "D:/UofT/Fall22/capstone/hands_no_bg/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        im = Image.open(path+item)
        f = os.path.basename(item)
        imResize = im.resize((160,120), Image.LANCZOS)
        imResize.save("D:/UofT/Fall22/capstone/hands_no_bg_resized/" + f, 'PNG', quality=90)

resize()
"""