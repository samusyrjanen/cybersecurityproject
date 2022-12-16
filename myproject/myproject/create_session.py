import django.contrib.sessions.backends.db as db

import random #importing random for the creation of random sessionid


class SessionStore(db.SessionStore):
	session_counter = 0

	def _get_new_session_key(self):
		while True:
			session_key = 'session-' + str(SessionStore.session_counter)#session hijacking can be done with sessionid if sessionid is easy to guess
            #solution for session hijacking:
            #this generates a random sessionid instead of "session-<int>"
            #session_key = str(random.getrandbits(128)) + str(SessionStore.session_counter)
			SessionStore.session_counter += 1
			if not self.exists(session_key):
				return session_key
