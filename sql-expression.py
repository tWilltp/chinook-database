from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our local host "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create a variable for the artist table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create a variable for the album table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create a variable for "track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Miliseconds", String),
    Column("Byte", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:
    
    # Query1 select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query2 select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns(
    # [artist_table.c.Name])

    # Query3 select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # Query4 select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query5 select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query6 select all tracks where composer is 'Queen' from the "Track" table
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)