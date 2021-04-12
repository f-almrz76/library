from colorama import Fore
import Book2
import magazine
import podcast
import audiobook

# this variable is for all of media type
SHELF = []
dash = "-" * 40
header = ["Media_type", "Name", "progress"]


def my_sort(lst):
    """
    This function sort a list of object  with special metric :progress
    """
    lst = sorted(lst, key=lambda x: x.progress, reverse=True)
    for item in lst:
        media_type = type(item).__name__
        print(Fore.WHITE + '{:<10s} {:>10s} {:>10f}'.format(media_type, item.title, item.progress))


NAME = input(Fore.BLUE + " Hi Please Enter your name : ")
print(Fore.RED + f"---------- Welcome {NAME}----------")
while True:
    print(Fore.LIGHTBLUE_EX + ' What do you want to do ? ')
    print(Fore.BLUE + "1. Add a Book / Magazine / Podcast / Aoudio Book")
    print(Fore.BLUE + "2. Show my book shelves")
    print(Fore.BLUE + '3. Add read pages or time listen')
    print(Fore.BLUE + '4. sort my book shelf')
    print(Fore.BLUE + '5. Exit')

    choice = input()

    if choice == '1':
        while True:
            print(Fore.LIGHTBLUE_EX + 'Which media type do you want to add ?')
            print(Fore.BLUE + "1.Book")
            print(Fore.BLUE + "2.Magazine")
            print(Fore.BLUE + "3.Podcast")
            print(Fore.BLUE + "4.Audio book")
            print(Fore.BLUE + "5.Previous")

            choice_1 = input()
            if choice_1 == '1':
                num = int(input(Fore.LIGHTBLUE_EX+ 'How many books do you want to add ?'))
                for i_1 in range(num):
                    SHELF.append(Book2.get_data())
                print(Fore.YELLOW + dash)
                continue
            elif choice_1 == '2':
                num = int(input('\033[34m' + 'How many magazines do you want to add ?'))
                for i_12 in range(num):
                    SHELF.append(magazine.get_data())
                print(Fore.YELLOW + dash)
                continue
            elif choice_1 == '3':
                num = int(input(Fore.LIGHTBLUE_EX + 'How many podcasts do you want to add ?'))
                for i_13 in range(num):
                    SHELF.append(podcast.get_data())
                print(Fore.YELLOW + dash)
                continue
            elif choice_1 == '4':
                num = int(input(Fore.LIGHTBLUE_EX + 'How many audio books do you want to add ?'))
                for i_14 in range(num):
                    SHELF.append(audiobook.get_data())
                print(Fore.YELLOW + dash)
                continue
            elif choice_1 == '5':
                print(Fore.YELLOW + dash)
                break
        continue
    elif choice == '2':
        print(Fore.WHITE + dash)
        print(Fore.WHITE + '{:<15s} {:>15s}'.format(header[0], header[1]))
        print(Fore.WHITE + dash)
        for item_2 in SHELF:
            media_type_2 = type(item_2).__name__
            print(Fore.WHITE + '{:<15s} {:>15s}'.format(media_type_2, item_2.title))
        print(Fore.YELLOW + dash)
        continue

    elif choice == '3':
        while True:
            print(Fore.LIGHTBLUE_EX + 'Which media_type did you read or listen?')
            print(Fore.BLUE + "1.Book")
            print(Fore.BLUE + "2.Magazine")
            print(Fore.BLUE + "3.Podcast")
            print(Fore.BLUE + "4.Audio book")
            print(Fore.BLUE + "5.Previous")

            choice_3 = input()
            if choice_3 == '1':
                book_3 = input(Fore.LIGHTBLUE_EX+" Which book do you want ?")
                try:
                    book_31 = next(item for item in SHELF if item.title == book_3)
                    read_page_3 = int(input(Fore.LIGHTBLUE_EX+" How many pages do you read ?"))
                    Book2.Book.read(book_3, read_page_3)
                    print(Fore.YELLOW + dash)
                except:
                    print(Fore.WHITE + " This book doesn't exist.")
                continue
            elif choice_3 == '2':
                magazine_3 = input(Fore.LIGHTBLUE_EX + 'which magazine do you want?')
                try:
                    magazine_31 = next(element for element in SHELF if element.title == magazine_3)
                    page_3 = int(input(Fore.LIGHTBLUE_EX+'How many pages do you read?'))
                    magazine.Magazine.read(magazine_31, page_3)
                    print(Fore.YELLOW + dash)
                except:
                    print(Fore.WHITE + " This magazine doesn't exist.")
                continue
            elif choice_3 == '3':
                podcast_3 = input(Fore.LIGHTBLUE_EX + 'which podcast do you want?')
                try:
                    podcast_31 = next(element for element in SHELF if element.title == podcast_3)
                    time_3 = int(input('\033[34m' + 'How much time do you listen?'))
                    podcast.Podcast_episode.listen(podcast_31, time_3)
                    print(Fore.YELLOW + dash)
                except:
                    print(Fore.WHITE + " This podcast doesn't exist.")
                continue
            elif choice_3 == '4':
                audio_3 = input(Fore.LIGHTBLUE_EX + 'which audiobook do you want?')
                try:
                    audio_31 = next(element for element in SHELF if element.title == audio_3)
                    time_3 = int(input('\033[34m' + 'How much time do you listen?'))
                    audiobook.Audiobook.listen(audio_31, time_3)
                    print(Fore.YELLOW + dash)
                except:
                    print(Fore.WHITE + " This audio_book doesn't exist.")
                continue
            elif choice_3 == '5':
                print(Fore.YELLOW + dash)
                break
    elif choice == '4':
        print(Fore.WHITE + dash)
        print(Fore.WHITE + '{:<10s} {:>10s} {:>10s}'.format(header[0], header[1], header[2]))
        print(Fore.WHITE + dash)
        my_sort(SHELF)
        print(Fore.YELLOW + dash)
        continue
    elif choice == '5':
        print(Fore.RED + f'---------- Good lock {NAME} -----------')
        break
