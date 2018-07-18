# this is the test document for doing the refractor challenge. 
# this challenge with indentation took me 2 hours or more to figure out

def main():   
    show_help()
    
    shopping_list = []
    
    while True:
    # ask for new items
        new_item = input("> ")
    
        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SHOW':
            show_list(shopping_list)
            continue
        add_to_list(shopping_list, new_item)

        show_list(shopping_list)