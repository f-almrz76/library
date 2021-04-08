import Book2
import magazine
import podcast
import audiobook
# this variable is for all of media type
SHELF = []
dash = "-"*40
header = ["Media_type", "Name" , "progress"]


def my_sort(lst):
    """
    This function sort a list of object  with special metric :progress
    """
    lst = sorted(lst, key=lambda x: x.progress, reverse=True)
    for i in lst:
        media_type = type(i).__name__
        print('\033[29m'+'{:<20s} {:>20s} {:>20f}'.format(media_type, i.title, i.progress))


NAME = input('\033[36m' + " Hi Please Enter your name : ")
print('\033[31m' + f"---------- Welcome {NAME}----------")
while True:
    print('\033[34m'+' What do you want to do ? ')
    print('\033[36m' + "1. Add a Book / Magazine / Podcast / Aoudio Book")
    print('\033[36m' + "2. Show my book shelves")
    print('\033[36m' + '3. Add read pages or time listen')
    print('\033[36m' + '4. sort my book shelf')
    print('\033[36m' + '5. Exit')

    choise = input()

    if choise == '1':
        while True:
            print('\033[34m' + 'Which media type do you want to add ?')
            print('\033[36m' + "1.Book")
            print('\033[36m' + "2.Magazine")
            print('\033[36m' + "3.Podcast")
            print('\033[36m' + "4.Audio book")
            print('\033[36m' + "5.Previous")

            choise1 = input()
            if choise1 == '1':
                num = int(input('\033[34m' + 'How many books do you want to enter ?'))
                book=Book2.Book.get_data(num)
                SHELF.append(book)
                print('\033[33m' + dash)
                continue
            elif choise1 == '2':
                num = int(input('\033[34m' + 'How many magazine do you want to enter ?'))
                magazine = magazine.Magazine.get_data(num)
                SHELF.append(magazine)
                print('\033[33m' + dash)
                continue
            elif choise1 == '3':
                num = int(input('\033[34m' + 'How many podcast do you want to enter ?'))
                podcast = podcast.Podcast_episode.get_data(num)
                SHELF.append(podcast)
                print('\033[33m' + dash)
                continue
            elif choise1 == '4':
                num = int(input('\033[34m' + 'How many audio book do you want to enter ?'))
                audio_book = audiobook.Audiobook.get_data(num)
                SHELF.append(audio_book)
                print('\033[33m' + dash)
                continue
            elif choise1 == '5':
                print('\033[33m' + dash)
                break
        continue
    elif choise == '2':
        print('\033[29m'+dash)
        print('\033[29m'+'{:<15s} {:>15s}'.format(header[0], header[1]))
        print('\033[29m'+dash)
        for i in SHELF:
            media_type = type(i).__name__
            print('\033[29m'+'{:<15s} {:>15s}'.format(media_type, i.title))
        print('\033[33m' + dash)
        continue

    elif choise == '3':
        while True :
            print('\033[34m'+'Which media_type ?')
            print('\033[36m' + "1.Book")
            print('\033[36m' + "2.Magazine")
            print('\033[36m' + "3.Podcast")
            print('\033[36m' + "4.Audio book")
            print('\033[36m' + "5.Previous")

            choise1 = input()
            if choise1 == '1':
                Name = input('\033[34m'+'which book do you want?')
                page = int(input('\033[34m'+'How many pages do you read?'))
                obj = next(element for element in SHELF if element.title == Name)
                Book2.Book.read(obj, page)
                print('\033[33m' + dash)
                continue
            elif choise1 == '2':
                Name = input('\033[34m'+'which magazine do you want?')
                page = int(input('\033[34m'+'How many pages do you read?'))
                obj = next(element for element in SHELF if element.title == Name)
                magazine.Magazine.read(obj, page)
                print('\033[33m' + dash)
                continue
            elif choise1 == '3':
                Name = input('\033[34m'+'which podcast do you want?')
                time = int(input('\033[34m'+'How much time do you listen?'))
                obj = next(element for element in SHELF if element.title == Name)
                podcast.Podcast_episode.listen(obj, time)
                print('\033[33m' + dash)
                continue
            elif choise1 == '4':
                Name = input('\033[34m'+'which audiobook do you want?')
                time = int(input('\033[34m'+'How much time do you listen?'))
                obj = next(element for element in SHELF if element.title == Name)
                audiobook.Audiobook.listen(obj, time)
                print('\033[33m' + dash)
                continue
            elif choise1 == '5':
                print('\033[33m' + dash)
                break
    elif choise == '4':
        print('\033[29m'+dash)
        print('\033[29m'+'{:<20s} {:>20s} {:>20s}'.format(header[0], header[1],header[2]))
        print('\033[29m'+dash)
        my_sort(SHELF)
        print('\033[33m' + dash)
        continue
    elif choise == '5':
        print('\033[31m'+f'---------- Good lock {NAME} -----------')
        break
