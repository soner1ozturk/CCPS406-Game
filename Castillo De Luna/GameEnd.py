def end_of_game():
    print('''
    

            ╔═══╦═══╦═╗─╔╦═══╦═══╦═══╦════╦╗─╔╦╗──╔═══╦════╦══╦═══╦═╗─╔╦═══╗
            ║╔═╗║╔═╗║║╚╗║║╔═╗║╔═╗║╔═╗║╔╗╔╗║║─║║║──║╔═╗║╔╗╔╗╠╣╠╣╔═╗║║╚╗║║╔═╗║
            ║║─╚╣║─║║╔╗╚╝║║─╚╣╚═╝║║─║╠╝║║╚╣║─║║║──║║─║╠╝║║╚╝║║║║─║║╔╗╚╝║╚══╗
            ║║─╔╣║─║║║╚╗║║║╔═╣╔╗╔╣╚═╝║─║║─║║─║║║─╔╣╚═╝║─║║──║║║║─║║║╚╗║╠══╗║
            ║╚═╝║╚═╝║║─║║║╚╩═║║║╚╣╔═╗║─║║─║╚═╝║╚═╝║╔═╗║─║║─╔╣╠╣╚═╝║║─║║║╚═╝║
            ╚═══╩═══╩╝─╚═╩═══╩╝╚═╩╝─╚╝─╚╝─╚═══╩═══╩╝─╚╝─╚╝─╚══╩═══╩╝─╚═╩═══╝
    
    
    
                              (,);    /\                        
                         ((  ^_   ||            ...         
                          ' /  \  ||           (()))        
                            L {=) ||           {' ())       
                             ) -  ||            )_ (()      
                           (_   \====       @  (   (_)      
                           | (___/{ }        \7 \ _) |      
                            \____\/)          {)=== /\      
                            |    |             \ |    |     
                            |_/\_|               |    |     
                             |  |                |    |     
                              ) )\               |    |     
                            _/| |/               |    |     
                           ( ,\ |_               '~~~~'     
                            \_(___)              _/Y 
    
    
    
    
    
    ''')
    
def end_of_game_conditions(badguy):
    if (badguy.get_health()<=0):
        print("Brave warrior! You have defeated the evil Orion! Now, there is nothing stopping you from find the princess. Remember the key!")
