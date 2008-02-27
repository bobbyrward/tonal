
from sqlalchemy import *
from sqlalchemy.orm import *
from tonal import settings

settings.ensure_app_dirs_exists()

uri = 'sqlite:///%s/tonal-music.db' % \
        settings.get_user_app_data_dir()

engine = create_engine(uri)
metadata = MetaData(engine)
session = create_session()

artists = Table('artists', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String, unique=True)
        )

albums = Table('albums', metadata,
            Column('id', Integer, primary_key=True),
            Column('artist_id', Integer, ForeignKey('artists.id')),
            Column('name', String, unique=True),
            Column('image', Binary)
        )

genres = Table('genres', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String, unique=True)
        )

songs = Table('songs', metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String),
            Column('path', String, unique=True),
            Column('album_id', Integer, ForeignKey('albums.id')),
            Column('artist_id', Integer, ForeignKey('artists.id')),
            Column('disc_id', Integer),
            Column('genre_id', Integer, ForeignKey('genres.id')),
            Column('year', String(30)),
            Column('track', Integer),
            Column('length', Integer),
            Column('bitrate', Integer),
            Column('size', Integer),
            Column('modified', Float),
            Column('playcount', Integer),
            Column('user_rating', Float),
            Column('last_played', DateTime),
            Column('time_added', DateTime),
            Column('blacklisted', Boolean)
        )

class Artist(object):
    def __init__(self, name=None):
        self.id = None
        self.name = name

    def __repr__(self):
        return '<Artist #%s "%s">' % (self.id, self.name)

class Album(object):
    def __init__(self, name=None, image=None):
        self.id = None
        self.artist_id = None
        self.name = name
        self.image = image

    def __repr__(self):
        return '<Album #%s "%s">' % (self.id, self.name)
        
class Genre(object):
    def __init__(self, name=None, image=None):
        self.id = None
        self.name = name

    def __repr__(self):
        return '<Genre #%s "%s">' % (self.id, self.name)
        
class Song(object):
    def __init__(self, title=None):
        self.id = None
        self.title = title

    def __repr__(self):
        return '<Song #%s "%s">' % (self.id, self.name)

songs_mapper = mapper(Song, songs)

albums_mapper = mapper(Album, albums, properties={
    'songs' : relation(Song, backref='album')
    })

artists_mapper = mapper(Artist, artists, properties={
    'songs' : relation(Song, backref='artist'),
    'albums' : relation(Album, backref='artist')
    })

genres_mapper = mapper(Genre, genres, properties={
    'songs' : relation(Song, backref='genre')
    })

metadata.create_all(engine)

def enable_debug():
    engine.echo = True

def get_or_create_genre(genre_name):
    query = session.query(Genre).filter_by(name=genre_name)

    if not query.count():
        genre = Genre(genre_name)
    else:
        genre = query.one()

    return genre

def get_or_create_artist(artist_name):
    query = session.query(Artist).filter_by(name=artist_name)

    if not query.count():
        artist = Artist(artist_name)
    else:
        artist = query.one()

    return artist

def get_or_create_album(album_name):
    query = session.query(Album).filter_by(name=album_name)

    if not query.count():
        album = Album(album_name)
    else:
        album = query.one()

    return album



