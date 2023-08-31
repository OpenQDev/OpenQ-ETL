# OpenQ-ETL

## Initial Upload

https://docs.pingcap.com/tidb/stable/tidb-lightning-overview

tiup playground
tiup tidb-lightning -backend local -config tidb-lightning.toml

```bash
mysql --host 127.0.0.1 --port 4000 -u root < init.sql
```

```bash
mysql --host 127.0.0.1 --port 4000 -u root < init.sql && python3 etl.py
```

```bash
mycli --host 127.0.0.1 --port 4000 -u root
```

### Prompts

I want to build an ETL pipeline from Github Archive to TiDB.
I want to use Python to achieve this.
I want to host everything on AWS.

Here is what the input data looks like. It's many Gigabytes of JSONL data:

{"id":"31085189265","type":"PushEvent","actor":{"id":93382891,"login":"MathiasExorde","display_login":"MathiasExorde","gravatar_id":"","url":"https://api.github.com/users/MathiasExorde","avatar_url":"https://avatars.githubusercontent.com/u/93382891?"},"repo":{"id":511095846,"name":"exorde-labs/TestnetProtocol","url":"https://api.github.com/repos/exorde-labs/TestnetProtocol"},"payload":{"repository_id":511095846,"push_id":14659474706,"size":1,"distinct_size":1,"ref":"refs/heads/main","head":"576de95f0d37aae28b91e3e5a9711b7f38e45177","before":"5f44c81598d9b0fadc02da4cebb41f4028266823","commits":[{"sha":"576de95f0d37aae28b91e3e5a9711b7f38e45177","author":{"email":"93382891+MathiasExorde@users.noreply.github.com","name":"Mathias Dail"},"message":"Automated update 2023-08-13-Aug-08","distinct":true,"url":"https://api.github.com/repos/exorde-labs/TestnetProtocol/commits/576de95f0d37aae28b91e3e5a9711b7f38e45177"}]},"public":true,"created_at":"2023-08-13T15:00:00Z","org":{"id":64810085,"login":"exorde-labs","gravatar_id":"","url":"https://api.github.com/orgs/exorde-labs","avatar_url":"https://avatars.githubusercontent.com/u/64810085?"}}
{"id":"31085189250","type":"PushEvent","actor":{"id":91749401,"login":"Nicospalla","display_login":"Nicospalla","gravatar_id":"","url":"https://api.github.com/users/Nicospalla","avatar_url":"https://avatars.githubusercontent.com/u/91749401?"},"repo":{"id":678042201,"name":"Nicospalla/tp-final-nivel3-spalla-nicolas","url":"https://api.github.com/repos/Nicospalla/tp-final-nivel3-spalla-nicolas"},"payload":{"repository_id":678042201,"push_id":14659474708,"size":1,"distinct_size":1,"ref":"refs/heads/main","head":"9023af091d6df2f256773ee8b926ed3736897eee","before":"bcd53fdf9916fb814094c8859f49e55fd6a9aa30","commits":[{"sha":"9023af091d6df2f256773ee8b926ed3736897eee","author":{"email":"nicolasaspalla@gmail.com","name":"Nicolas Spalla"},"message":"v1.2 WebApp","distinct":true,"url":"https://api.github.com/repos/Nicospalla/tp-final-nivel3-spalla-nicolas/commits/9023af091d6df2f256773ee8b926ed3736897eee"}]},"public":true,"created_at":"2023-08-13T15:00:00Z"}

There are many different "type" for these events. But I ONLY want to persist the PushEvent type.

I want to convert these JSONL files into CSV files that can be imported efficiently to TiDB using TiDB Lightning.

You'll also need to create a Repository, User and Event table schema in MySQL to handle all this.