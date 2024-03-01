import threading
from fetch import fetch_new_domain
from words import init_words, list_words

running = True


def quit():
	global running
	running = False
	print("Goodbye!")


def unknown_command():
	print("Unknown command!")


maps = {
	"exit": quit,
	"quit": quit,

	"fetch": lambda *args: fetch_new_domain(),
	"fetch_new_domain": lambda *args: fetch_new_domain(),
 
  "init_words": lambda *args: init_words(filename=args[0]),
  "init": lambda *args: init_words(filename=args[0]),

  'list_words': lambda *args: list_words(),
  'list': lambda *args: list_words(),
}



while running:
	try:
		command, *args = str(input()).split()
		if command in maps:
			maps[command](*args)
		else:
			unknown_command()
	except IndexError as iex:
		print("Missing argument", iex)
	except Exception as ex:
		print("something went wrong", ex)
