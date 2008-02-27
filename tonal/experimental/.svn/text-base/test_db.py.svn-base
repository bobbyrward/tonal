#!/usr/bin/env python

from db.db_sqlalchemy import *

rock = get_or_create_genre('Rock')
tool = get_or_create_artist('Tool')
opiate = get_or_create_album('Opiate')
tool.albums.append(opiate)

cold_and_ugly = Song()

tool.songs.append(cold_and_ugly)
opiate.songs.append(cold_and_ugly)
rock.songs.append(cold_and_ugly)

cold_and_ugly.title = 'Cold And Ugly (Live)'
cold_and_ugly.track = 4

session.save(cold_and_ugly)
session.flush()

