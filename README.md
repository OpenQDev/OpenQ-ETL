# OpenQ-ETL

## Initial Upload

https://docs.pingcap.com/tidb/stable/tidb-lightning-overview

tiup tidb-lightning -backend local -d 

```bash
mysql --host 127.0.0.1 --port 4000 -u root < init.sql
```

```bash
mysql --host 127.0.0.1 --port 4000 -u root < init.sql && python3 etl.py
```

```bash
mycli --host 127.0.0.1 --port 4000 -u root
```