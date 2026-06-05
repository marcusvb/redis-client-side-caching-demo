from redis import Redis

client = Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)

print("Type values. Each line updates key 'foo'.")
print()

while True:
    value = input("foo> ")

    client.set("foo", value)

    print(f"Updated foo = {value}")
