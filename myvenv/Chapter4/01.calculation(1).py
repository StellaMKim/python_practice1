# 1. assignment operation
# variable = data

# 2. arithmetic operation
# - number 
x = 5
y = 2

print( x + y )
print( x - y )
print( x * y )
print( x / y )
print( x // y ) 
print( x % y )
print( x ** y )

# - string
tag1 = "#Let's meet"
tag2 = "#from today"
tag3 = "#couple"

tag = tag1 + tag2 + tag3
print(tag)

message = "We all love Python.\n" * 5
print(message)

# complex assignment operation
level = 10 # (level 1 increase)
level +=  1  # level = level +1

health = 2000 # (health 300 decrese)
health -= 300 # health = health - 300

attack = 300 # (attack mutipled 1.5 increase)
attack *= 1.5 # attack = attack * 1.5

speed = 420 # (speed mutipled 50% decrease)
speed /= 2 # speed = speed / 2
print(level, health, attack, speed)
