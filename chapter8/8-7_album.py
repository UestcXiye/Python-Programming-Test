def make_album(singer_name, album_name, number=''):
    album = {'singer_name': singer_name, 'album_name': album_name}
    if number:
        album['number'] = number
    return album


albums = []
albums.append(make_album('周杰伦', '八度空间', number=10))
albums.append(make_album('陈奕迅', 'Rice & Shine'))
# print(albums)
for album in albums:
    print(album)
