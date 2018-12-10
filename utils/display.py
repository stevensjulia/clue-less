
ROOM = 'Room'
BALLROOM = 'Ballroom'
BILLIARD_ROOM = 'Billiard Room'
CONSERVATORY = 'Conservatory'
DINING_ROOM = 'Dining Room'
HALL = 'Hall'
KITCHEN = 'Kitchen'
LIBRARY = 'Library'
LOUNGE = 'Lounge'
STUDY = 'Study'

STUDY_LIBRARY = 'three'
STUDY_HALL = 'one'
HALL_BILLIARD = 'four'
HALL_LOUNGE = 'two'
LOUNGE_DINING = 'five'
LIBRARY_CONSERVATORY = 'eight'
LIBRARY_BILLIARD = 'six'
BILLIARD_BALLROOM = 'nine'
BILLIARD_DINING = 'seven'
DINING_KITCHEN = 'ten'
CONSERVATORY_BALLROOM = 'eleven'
BALLROOM_KITCHEN = 'twelve'

class Display:

    @staticmethod
    def display_board(current_board):
        # display room state
        study = current_board.get_character_in_space(STUDY)
        hall = current_board.get_character_in_space(HALL)
        lounge = current_board.get_character_in_space(LOUNGE)
        library = current_board.get_character_in_space(LIBRARY)
        billiard = current_board.get_character_in_space(BILLIARD_ROOM)
        dining = current_board.get_character_in_space(DINING_ROOM)
        conservatory = current_board.get_character_in_space(CONSERVATORY)
        ballroom = current_board.get_character_in_space(BALLROOM)
        kitchen = current_board.get_character_in_space(KITCHEN)

        # display hallway state
        one = current_board.get_character_in_space(STUDY_HALL)
        two = current_board.get_character_in_space(HALL_LOUNGE)
        three = current_board.get_character_in_space(STUDY_LIBRARY)
        four = current_board.get_character_in_space(HALL_BILLIARD)
        five = current_board.get_character_in_space(LOUNGE_DINING)
        six = current_board.get_character_in_space(LIBRARY_BILLIARD)
        seven = current_board.get_character_in_space(BILLIARD_DINING)
        eight = current_board.get_character_in_space(LIBRARY_CONSERVATORY)
        nine = current_board.get_character_in_space(BILLIARD_BALLROOM)
        ten = current_board.get_character_in_space(DINING_KITCHEN)
        eleven = current_board.get_character_in_space(CONSERVATORY_BALLROOM)
        twelve = current_board.get_character_in_space(BALLROOM_KITCHEN)

        # display weapons
        study_w = current_board.get_weapon_in_space(STUDY)
        hall_w = current_board.get_weapon_in_space(HALL)
        lounge_w = current_board.get_weapon_in_space(LOUNGE)
        library_w = current_board.get_weapon_in_space(LIBRARY)
        billiard_w = current_board.get_weapon_in_space(BILLIARD_ROOM)
        dining_w = current_board.get_weapon_in_space(DINING_ROOM)
        conservatory_w = current_board.get_weapon_in_space(CONSERVATORY)
        ballroom_w = current_board.get_weapon_in_space(BALLROOM)
        kitchen_w = current_board.get_weapon_in_space(KITCHEN)
        print(kitchen_w)

        board = "\n" \
                "--------------------------------------------------------------------------------\n" \
                "|     Study    |               |      Hall     |               |     Lounge    |\n" \
                "|              |               |               |               |               |\n" \
                "|{study:^14}|{one:^15}|{hall:^15}|{two:^15}|{lounge:^15}|\n" \
                "|{study_w:^14}|               |{hall_w:^15}|               |{lounge_w:^15}|\n" \
                "|______________|_______________|_______________|_______________|_______________|\n" \
                "|              |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\n" \
                "|              |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\n" \
                "|{three:^14}|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|{four:^15}|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|{five:^15}|\n" \
                "|              |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\n" \
                "|______________|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|_______________|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|_______________|\n" \
                "|   Library    |               | Billiard Room |               |  Dining Room  |\n" \
                "|              |               |               |               |               |\n" \
                "|{library:^14}|{six:^15}|{billiard:^15}|{seven:^15}|{dining:^15}|\n" \
                "|{library_w:^14}|               |{billiard_w:^15}|               |{dining_w:^15}|\n" \
                "|______________|_______________|_______________|_______________|_______________|\n" \
                "|              |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\n" \
                "|              |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\n" \
                "|{eight:^14}|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|{nine:^15}|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|{ten:^15}|\n" \
                "|              |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|               |\n" \
                "|______________|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|_______________|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|_______________|\n" \
                "| Conservatory |               |   Ballroom    |               |    Kitchen    |\n" \
                "|              |               |               |               |               |\n" \
                "|{conservatory:^14}|{eleven:^15}|{ballroom:^15}|{twelve:^15}|{kitchen:^15}|\n" \
                "|{conservatory_w:^14}|               |{ballroom_w:^15}|               |{kitchen_w:^15}|\n" \
                "|______________|_______________|_______________|_______________|_______________|\n".format(
                    study=study,
                    hall=hall,
                    lounge=lounge,
                    library=library,
                    billiard=billiard,
                    dining=dining,
                    conservatory=conservatory,
                    ballroom=ballroom,
                    kitchen=kitchen,
                    one=one,
                    two=two,
                    three=three,
                    four=four,
                    five=five,
                    six=six,
                    seven=seven,
                    eight=eight,
                    nine=nine,
                    ten=ten,
                    eleven=eleven,
                    twelve=twelve,
                    study_w=study_w,
                    hall_w=hall_w,
                    lounge_w=lounge_w,
                    library_w=library_w,
                    billiard_w=billiard_w,
                    dining_w=dining_w,
                    conservatory_w=conservatory_w,
                    ballroom_w=ballroom_w,
                    #kitchen_w=kitchen_w,
                    kitchen = "kitchen_w"
                    )

        return board
