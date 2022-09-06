def make_album(s_name, a_name, n=0):
    a = {'singer_name': s_name, 'album_name': a_name}
    if n:
        a['number'] = n
    return a


albums = []
prompt = "\nPlease tell me your favorite albums:"
prompt += "\n(Enter 'quit' to end the program)"

while True:
    print(prompt)

    singer_name = input("Singer name: ")
    if singer_name == 'quit':
        break

    album_name = input("Album name: ")
    if album_name == 'quit':
        break

    sign = input("\nDo you know how many songs in this album (yes/no): ")
    if sign == 'yes':
        number = input("Number of songs: ")
        number = int(number)
        album = make_album(singer_name, album_name, number)
        albums.append(album)
    else:
        print("Do not worry! It does not matter")
        album = make_album(singer_name, album_name)
        albums.append(album)

    print("\nLet's check the album:")
    print(album)
