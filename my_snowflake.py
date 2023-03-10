from snowflake.snowflake import SnowflakeGenerator
import random

seed = random.randint(1,10)
gen = SnowflakeGenerator(seed)
id = next(gen)

print("id:{}".format(id))

