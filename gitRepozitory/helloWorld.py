def print_hello(text: str) -> str:
	result = "Hello, {}!!"
	return result.format(text)

print(print_hello("Rita"))
