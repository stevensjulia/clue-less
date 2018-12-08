
class Display:

    @staticmethod
    def display_board(current_board):
        study = ""
        hall = ""
        lounge = ""
        library = " "
        billiard = " "
        dining = " "
        conservatory = " "
        ballroom = " "
        kitchen = " "
        one = ""
        two = ""
        three = ""
        four = ""
        five = ""
        six = ""
        seven = ""
        eight = ""
        nine = ""
        ten = ""
        eleven = ""
        twelve = ""
        study_w = "Revolver"
        hall_w = ""
        lounge_w = " "
        library_w = " "
        billiard_w = " "
        dining_w = " "
        conservatory_w = " "
        ballroom_w = " "
        kitchen_w = " "

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
                    kitchen_w=kitchen_w,
                    )

        print(board)
