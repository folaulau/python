from sqlalchemy import create_engine
import os
from snowflake.sqlalchemy import URL
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa


"""
research: https://stackoverflow.com/questions/60870620/sqlalchemy-engine-connect-fails-for-snowflake-using-keypair-authentication
"""

key_location = os.path.expanduser('~/.ssh/svc_dev.p8')
snowflake_pass_phrase = str("anvilogicdev")

with open(key_location, "rb") as key:
    p_key = serialization.load_pem_private_key(
        key.read(),
        password=snowflake_pass_phrase.encode(),
        backend=default_backend()
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())

engine = create_engine(URL(
    user="SVC_DEV",
    account="anvilogic-dev",
    role='CLOUDAPP',
    warehouse='COMPUTE_WH_CLOUDAPP',
    database='ANVILOGIC',
    schema='public',
    application="Anvilogic_SOCPlatform"
    ),
    connect_args={
        'private_key': pkb,
    }
)


connection = engine.connect()

try:
    
    results = connection.execute('select current_version()').fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()