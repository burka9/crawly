running = True


def quit():
	global running
	running = False
	print("Goodbye!")


def unknown_command():
	print("Unknown command!")

def fetch_new_domain():
	print("Fetching new domain...")
	# Fetch new domain here
	print("Done!")


def create_services_for_domains():
	print("Creating services for domains...")
	# Create services for domains here
	print("Done!")


maps = {
	"exit": quit,
	"fetch": fetch_new_domain,
	"create": create_services_for_domains,
}


while running:
	command = input()

	if command in maps:
		maps[command]()
	else:
		unknown_command()

